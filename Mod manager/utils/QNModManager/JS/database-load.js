// These create the database to store the mods 
var db;
var DBrequest = indexedDB.open("FirefoxMods", 1);

// In case of database creation or upgrade
DBrequest.onupgradeneeded = function(event) {
	console.log("Updating database...");
	var db = event.target.result;

	// Create an objectStore to hold the settings of the script
	var settingStore = db.createObjectStore("Settings", { keyPath: "name" });
	settingStore.createIndex("SettingName", "name", { unique: true });

	// Create an objectStore to hold the JS scripts data
	var jsModStore = db.createObjectStore("JSMods", { keyPath: "id", autoIncrement: true });
	jsModStore.createIndex("JSModURL", "updateURL", { unique: true });

	// Create an objectStore to hold the CSS scripts data
	var cssModStore = db.createObjectStore("CSSMods", { keyPath: "id", autoIncrement: true });
	cssModStore.createIndex("CSSModURL", "updateURL", { unique: true });
};

// If things go right, we start doing things
DBrequest.onsuccess = function() {
	db = this.result;

	db.onerror = function(event) {
		// Generic error handler for all errors targeted at this database's
		// requests!
		console.error("Database error: " + event.target.errorCode);
	};

	// This is the element creation function:
    function addElement(parentEl, elementTag, elementClass, html="") {
        var newElement = document.createElement(elementTag);
        if (Array.isArray(elementClass)) {
			for (var x = 0; x < elementClass.length; x++)
				newElement.classList.add(elementClass[x]);
        } else if (elementClass) {
			newElement.classList.add(elementClass);
        }
        if (html != "") {newElement.innerHTML = html}

        parentEl.appendChild(newElement);
		return newElement;
    }

	// Checks header metadata of mods and returns an array with the information
	// Returns an array with the values [script name, script description, version, author, 
	// update url, preferences array, [default name, default description, default update url]]
	function checkMetadata(store, defaultName, codeValue, sourcePath="") {
		
		// function to add preferences
		function addPreference(regArray, defValue=null, userVal=null) {
			if (!defValue) {
				defValue = regArray[8];
			}
			if (!userVal) {
				userVal = regArray[8];
			}

			var preference = {
				type: regArray[2],
				name: regArray[4],
				description: regArray[6],
				value: defValue,
				userValue: userVal,
			};

			return preference;
		}

		var isCSS = /==UserStyle==/i;
		var isJS = /==UserScript==/i;
		var prefs = [];
		// Name, Description, Version, Author, Update URL, preferences, default values
		var headerMeta = [defaultName, "No description provided", "Pending", "Unknown", sourcePath, [], 
							[defaultName, "No description provided", ""]];
		var isHeader;

		// We first set the appropiate regex for the kind of script that we are adding
		if (store == "CSSMods") {
			isHeader = /==UserStyle==(.*)==\/UserStyle==/is;
		} else if (store == "JSMods"){
			isHeader = /==UserScript==(.*)==\/UserScript==/is;
		} else {
			console.log("Script type not recognized.")
			return
		}

		// If the script has a metadata header we get it's data
		if (isCSS.test(codeValue) || isJS.test(codeValue)) {
			var headerContent =  codeValue.match(isHeader)[1].split("\n");

			// Regex matchers to get the right metadata values
			var isName = /@name(\s+|\t+)(.+)/i;
			var isDesc = /@description(\s+|\t+)(.+)/i;
			var isVers = /@version(\s+|\t+)(.+)/i;
			var isAuth = /@author(\s+|\t+)(.+)/i;
			var isUpd = /@updateURL(\s+|\t+)(.+)/i;
			var isVar = /@var(\s+|\t+)(\S+)(\s+|\t+)(\S+)(\s+|\t+)"(.+)"(\s+|\t+)(.+)/i;
			var isSel = false;
			var totalSel = "";
			var fixValue = "";
			var storedMeta;

			// We iterate over all header lines to find the metadata
			headerContent.forEach(function(value) {
				let isMetaName = isName.test(value);
				let isMetaDesc = isDesc.test(value);
				let isMetaVers = isVers.test(value);
				let isMetaAuth = isAuth.test(value);
				let isMetaUpd = isUpd.test(value);
				let isPref = isVar.test(value);
				let preference = null;
				let prefKeys;

				// Check for type of element in the header

				// Name of the script
				if (isMetaName && headerMeta[0] == defaultName) {
					headerMeta[0] = value.match(isName)[2];
					headerMeta[6][0] = headerMeta[0];

				// Description of the script
				} else if (isMetaDesc && headerMeta[1] == "No description provided") {
					headerMeta[1] = value.match(isDesc)[2];
					headerMeta[6][1] = headerMeta[1];

				// Version of the script
				} else if (isMetaVers && headerMeta[2] == "Pending") {
					headerMeta[2] = value.match(isVers)[2];

				// Author of the script
				} else if (isMetaAuth && headerMeta[3] == "Unknown") {
					headerMeta[3] = value.match(isAuth)[2];

				// Update URL of the script (if any)
				} else if (isMetaUpd && headerMeta[4] == "") {
					headerMeta[4] = value.match(isUpd)[2];
					headerMeta[6][2] = headerMeta[4];

				// Variables of the script
				} else if (isPref || isSel) {
					// Check if multi-line select is active
					if (!isSel) {
						let prefType = value.match(isVar)[2];
						var prefValue = value.match(isVar)[8];
						if (prefType == "select" && prefValue[0] == "{") {
							fixValue = prefValue.trim()
							if (fixValue.length > 2 && fixValue.includes("}", -2)) {
								try {
									prefValue = JSON.parse(fixValue);
									prefKeys = Object.entries(prefValue);

									// Variable objects for select variables are created here
									preference = addPreference(value.match(isVar), prefKeys, prefKeys[0][1]);
									prefs.push(preference);
								} catch {
									console.log('The select variable was not well constructed. Check for missing "s or brackets.');
								}
							} else {
								storedMeta = value.match(isVar);
								totalSel = prefValue;
								isSel = true;
							}

						// Parse the number arrays to add them first
						} else if (prefType == "number" && prefValue[0] == "[" && prefValue.includes("]", -2)) {
							prefValue = prefValue.trim();
							prefValue = prefValue.replace("[", "");
							prefValue = prefValue.replace("]", "");
							prefValue = prefValue.split(",");

							var hasNumType = false;
							var i = 1;

							if ((prefValue[0].trim())[0] == "'") {
								prefValue[0] = (prefValue[0].trim()).replaceAll("'", "");
								hasNumType = true;
							} else if ((prefValue[0].trim())[0] == '"') {
								prefValue[0] = (prefValue[0].trim()).replaceAll('"', "");
								hasNumType = true;
							}

							if (!hasNumType) {
								i = 0;
							}

							// Convert non-type elements of the number array to numbers
							for (var e = i; e < prefValue.length; e++) {
								try {
									prefValue[i] = parseInt(prefValue[i]);
								} catch(err) {
									console.log("The number value for " + prefValue[i] + " was not a valid number")
								}
							}

							// Variable objects for number variables are created here
							if (hasNumType) {
								preference = addPreference(value.match(isVar), prefValue, prefValue[1]);
							} else {
								preference = addPreference(value.match(isVar), prefValue, prefValue[0]);
							}

							prefs.push(preference);
						} else {
							// Variable objects for any other variable are created here
							preference = addPreference(value.match(isVar));
							prefs.push(preference);
						}
					// Multi-line select parsing here
					} else {
						value = value.trim();
						if (value.startsWith("//")) {
							value = value.replace("//", "");
							value = value.trim();
						}
						if (value.startsWith("}") || value.endsWith("}") || value.startsWith("@val") || value.startsWith("==/")) {
							if (totalSel != "" && totalSel != "{") {
								if (value.endsWith("}") || value.startsWith("}") || value.endsWith("};")) {
									totalSel += value;
									try {
										prefValue = JSON.parse(totalSel);
										prefKeys = Object.entries(prefValue);

										preference = addPreference(storedMeta, prefKeys, prefKeys[0][1]);
										prefs.push(preference);

									} catch {
										console.log('The select variable was not well constructed. Check for missing "s or brackets.');
									}
								}

							}
						} else {
							totalSel += value;
						}
					}
				}
			});
			headerMeta[5] = prefs;
		}
		return headerMeta;
	}

	function getReadableDate(date = new Date()) {
		let timeArray = [date.getHours(), date.getMinutes(), date.getSeconds()];

		for (let q = 0; q < timeArray.length; q++) {
			if (timeArray[q] < 10) {
				timeArray[q] = "0" + timeArray[q]
			}
		}
		return date.getFullYear() + "/" + (date.getMonth() + 1) + "/" + date.getDate() + 
				" - " + timeArray[0] + ":" + timeArray[1] + ":" + timeArray[2];
	}

	// Adds an existing mod to the store
	async function importMod(store, modObj) {
		const transaction = db.transaction(store, "readwrite");
		const modStore =  transaction.objectStore(store);
		let indexName = "JSModURL"

		// Define the store to import the mod to the mod
		if (store == "CSSMods") {
			indexName = "CSSModURL";
		} else if (store != "JSMods") {
			console.log("Wrong database passed as parameter of import mod function.")
			return
		}

		const index =  modStore.index(indexName);

		return new Promise(function(resolve, reject) {
			// Check if the mod with the same source exists
			index.get(modObj.updateURL).onsuccess = function(event) {
				console.log("Importing mods...")
				if (event.target.result) {
					console.warn("A mod with that update URL already exists, aborting import of mod " + modObj.name);
					reject(modObj.name);
					return
				} else {
					modStore.put({
						name: modObj.name,
						description: modObj.description,
						version: modObj.version,
						author: modObj.author,
						updateURL: modObj.updateURL,
						defaults: modObj.defaults,
						code: modObj.code,
						preferences: modObj.preferences,
						enabledState: false,
						updateInterval: modObj.updateInterval,
						lastUpdate: modObj.lastUpdate,
						lastVersionCheck: modObj.lastVersionCheck,
					});
				}
				resolve();
			};
		})
	}

	// Checks for existing mods in the database and updates them
	async function addOrUpdateMod(store, modMeta, codeValue, modId=-1, updInt="default") {
		var transaction = db.transaction(store, "readwrite");
		var modStore =  transaction.objectStore(store);
		var modExists = modStore.get(modId);
		var isOn = false;
		var prefs;

		// Get current human-readable date
		let lastUpd = getReadableDate();

		// Update the default values by the code of the script
		var defaultMeta = [modMeta[0], modMeta[1], modMeta[4]];

		if (modId > 0) {
			return new Promise(function(resolve, reject) {
				modExists.onsuccess = function(event) {
					// Check if the mod exists to update instead of add
					if (event.target.result) {
						console.log("Updating mod...");
						prefs = event.target.result.preferences;
						isOn = event.target.result.enabledState;
						if (modMeta[4] == "") {
							defaultMeta[2] = event.target.result.defaults[2];
							modMeta[4] = event.target.result.updateURL;
						}
						for (let i = 0; i < prefs.length; i++) {
							for (let x = 0; x < modMeta[5].length; x++) {
								if (prefs[i].name == modMeta[5][x].name) {
									modMeta[5][x].userValue = prefs[i].userValue;
								}
							}
						}

						// We update the mod here
						var request = modStore.put({
							id: modId,
							name: modMeta[0],
							description: modMeta[1],
							version: modMeta[2],
							author: modMeta[3],
							updateURL: modMeta[4],
							defaults: defaultMeta,
							code: codeValue,
							preferences: modMeta[5],
							enabledState: isOn,
							updateInterval: updInt,
							lastUpdate: lastUpd,
							lastVersionCheck: new Date(),
						});

						// In case there is some null value on a unique entry or some other issue, this happens
						request.onerror = function() {
							alert("There was a problem while updating the mod '" + modMeta[0] + "'.");
						};

						// If the operation was successful
						request.onsuccess = function() {
							console.log("Mod '" + modMeta[0] + "' updated successfully!");
							resolve(true);
						};
					}
				}

				modExists.onerror = function() {
					resolve(false);
				}
			});
		} else {
			console.log("Creating mod...");
			
			// We add the mod here
			var request = modStore.put({
				name: modMeta[0],
				description: modMeta[1],
				version: modMeta[2],
				author: modMeta[3],
				updateURL: modMeta[4],
				defaults: defaultMeta,
				code: codeValue,
				preferences: modMeta[5],
				enabledState: isOn,
				updateInterval: updInt,
				lastUpdate: lastUpd,
				lastVersionCheck: new Date(),
			});

			// In case the object already exists this happens
			request.onerror = function() {
				alert("There was a problem while adding the mod '" + modMeta[0] + "' to the database. "
				+ "\nMake sure that a mod with the same ID or update URL doesn't already exist.");
			};

			// If the operation was successful
			request.onsuccess = function() {
				console.log("Mod '" + modMeta[0] + "' added to the database successfully!");
			};
		}

		// Alert when there was a problem with the transaction
		transaction.onerror = function() {
			alert("Error with the transaction when updating the database entry.");
		};
	}

	// Updates a mod with the given url
	async function getModUpdate(modId, store) {
		var defaultName;
		var modUpdateInt;
		var modVer;
		var path2Script;

		// Updates the date of the last check of the mod version
		function updateLastVersionCheck(store, modId) {
			modId = parseInt(modId);
			var transaction = db.transaction(store, "readwrite").objectStore(store);
			var request = transaction.get(modId);

			request.onsuccess = function(event) {
				// Get the data of the mod
				var data = event.target.result;

					if (data != null) {
						data.lastVersionCheck = new Date();

						// Put the updated object back into the database.
						var requestUpdate = transaction.put(data);

						requestUpdate.onerror = function() {
							console.log("Couldn't update the following mod last version check: " + data.name);
						};
			
						requestUpdate.onsuccess = function() {
							console.log("Mod setting updated succesfully");

							// This line is only used for debugging purposes
							// printModData(store, modId); 
						};
					}
			};

			request.onerror = function(event) {
				console.log("There was an error when checking the last version check for mod with id " + modId);
			}
		}

		// Gets the value in seconds of a date version in format of either "dd/mm/yy HH:MM" or "yy/mm/dd HH:MM"
		function getVersionTime(modVersion) {
			var dateDay = 0;
			var dateMonth = 0;
			var dateYear = 0;
			var dateHour = 0;
			var dateMin = 0;
			var dateVersion = modVersion.split(" ");
			dateVersion = dateVersion.filter(e => e);
			var splitterChar = "/";

			if (dateVersion[0].includes("-"))
				splitterChar = "-";

			var versionDate = dateVersion[0].split(splitterChar);
			var versionTime = dateVersion[1].split(":");

			if (versionDate.length == 3) {
				try {
					if (parseInt(versionDate[0]) > 31) {
						dateYear = parseInt(versionDate[0]);
						dateMonth = parseInt(versionDate[1]);
						dateDay = parseInt(versionDate[2]);
					} else {
						dateYear = parseInt(versionDate[2]);
						dateMonth = parseInt(versionDate[1]);
						dateDay = parseInt(versionDate[0]);
					}
				} catch (err) {
					console.log("The mod with id " + modId + " doesn't have a valid @version string.");
					return 0;
				}
				
			} else {
				console.log("The mod with id " + modId + " doesn't have a valid @version string.");
				return 0;
			}

			if (versionTime.length >= 2) {
				try {
					dateHour = parseInt(versionTime[0]);
					dateMin = parseInt(versionTime[1]);
				} catch (err) {
					console.log("The mod with id " + modId + " doesn't have a valid @version string.");
					dateHour = 0;
					dateMin = 0;
				}
			}

			var totalSeconds = dateMin * 60 + dateHour * 3600 + dateDay * 86400 + dateMonth * 2592000 + dateYear * 31104000;
			return totalSeconds;
		}

		// Return if the new mod version number is higher than the old
		function isNewerNumberVersion(newVersion, oldVersion) {
			var newNumVersion = newVersion.replaceAll(" ", "");
			var oldNumVersion = oldVersion.replaceAll(" ", "");
			var newVersionNum = newNumVersion.split(".");
			var oldVersionNum = oldNumVersion.split(".");

			// Put number versions of the new mod in an array
			if (newVersionNum.length <= 3) {
				try {
					newVersionNum[0] = parseInt(newVersionNum[0]);
					if (newVersionNum.length >= 2) 
						newVersionNum[1] = parseInt(newVersionNum[1]);
					if (newVersionNum.length == 3) 
						newVersionNum[2] = parseInt(newVersionNum[2]);
				} catch (err) {
					newVersionNum = [0, 0, 0];
				}
			} else {
				newVersionNum = [0, 0, 0];
			}
			
			// Put number versions of the old mod in an array
			if (oldVersionNum.length <= 3) {
				try {
					oldVersionNum[0] = parseInt(oldVersionNum[0]);
					if (oldVersionNum.length >= 2) 
						oldVersionNum[1] = parseInt(oldVersionNum[1]);
					if (oldVersionNum.length == 3) 
						oldVersionNum[2] = parseInt(oldVersionNum[2]);
				} catch (err) {
					oldVersionNum = [0, 0, 0];
				}
			} else {
				oldVersionNum = [0, 0, 0];
			}

			// Compare the versions of the new vs old
			if (newVersionNum[0] > oldVersionNum[0]) {
				return true;
			} else if (newVersionNum[0] == oldVersionNum[0]) {
				if (newVersionNum[1] > oldVersionNum[1]) {
					return true;
				} else if (newVersionNum[1] == oldVersionNum[1]) {
					if (newVersionNum[2] > oldVersionNum[2]) {
						return true;
					}
				}
			}

			// If the version is the same or lower or all checks fail
			return false;
		}

		// Return the given mod data first

		var transaction = db.transaction(store);
		var modStore =  transaction.objectStore(store);
		var request =  modStore.get(modId);

		if (modId > 0) {

			return new Promise(function(resolve, reject) {
				request.onsuccess = function(e){ 

					// Check if the mod exists to update it
					if (e.target.result) {
						defaultName = e.target.result.defaults[0];
						modUpdateInt = e.target.result.updateInterval;
						modVer = e.target.result.version;
						path2Script = e.target.result.updateURL;
						
						// Fetch the actual mod
						fetch(path2Script)
						.then(res => res.text())
						.then(function(obj) {
							// We get the metadata of the mod here and then pass it to the other functions
							var modMeta = checkMetadata(store, defaultName, obj, path2Script);

							// We check if the version of the mod we have installed is different than the lastest available version
							if (modVer != modMeta[2] && modMeta[2] != "Pending") {

								// Control variable
								var isBiggerVersion = false;
	
								// If version uses a date
								if (modMeta[2].includes("/") || modMeta[2].includes("-")) {
	
									if (modVer != "Pending" && (modVer.includes("/") || modVer.includes("-"))) {
										
										// Get the version array from the old mod version
										var oldVersion = getVersionTime(modVer);
										var newVersion = getVersionTime(modMeta[2]);
	
										if (newVersion > oldVersion)
											isBiggerVersion = true;
	
									} else {
										isBiggerVersion = true;
									}
	
								// If version uses a number (as it hopefully should)
								} else if (modMeta[2].substring(0, modMeta[2].length - 1).includes(".")) {
									
									if (modVer != "Pending" && modVer.includes(".")) {
										
										// Get the version array from the old mod version
										if (isNewerNumberVersion(modMeta[2], modVer)) {
											isBiggerVersion = true;
										}
											
									// If the old version used a date or didn't have a number version
									} else {
										isBiggerVersion = true;
									}
								}
	
								// Mod update handling here
								if (isBiggerVersion) {
									resolve(addOrUpdateMod(store, modMeta, obj, modId, modUpdateInt));
								} else {
									updateLastVersionCheck(store, modId);
									resolve(false);
								}
							} else resolve(false);
						});
					} else resolve(false);
				};
	
				request.onerror = function() {
					console.log("There was a problem updating the mod with index " + modId);
					reject();
				};
			});
			

		} else return false;
	}

	// Changes the setting of a mod
	function changeModSetting(store, modId, setting, settingVal) {
		modId = parseInt(modId);
		var transaction = db.transaction(store, "readwrite").objectStore(store);
		var request = transaction.get(modId);
		var index;
		if (store == "CSSMods") {
			index = transaction.index("CSSModID");
		} else if (store == "JSMods") {
			index = transaction.index("JSModID");
		}

		request.onsuccess = function(event) {
			// Get the data of the mod
			var data = event.target.result;
			var settingName = setting;
			var settingValue = settingVal;
			var settingLen = 1;

			if (Array.isArray(setting)) {
				settingLen = setting.length;
			}

			// We update the mod here
			for (var w = 0; w < settingLen; w++) {
				if (settingLen > 1) {
					settingName = setting[w];
					settingValue = settingVal[w];
				}

				switch(settingName) {
					case "name":
						data.name = settingValue;
						break;
					case "description":
						data.description = settingValue;
						break;
					case "updateURL":
						data.updateURL = settingValue;
						break;
					case "updateInterval":
						data.updateInterval = settingValue;
						break;
					case "code":
						data.code = settingValue;
						break;
					case "enabledState":
						data.enabledState = settingValue;
						break;
					case "lastVersionCheck":
						data.lastVersionCheck = settingValue;
						break;
					default:
						for (var x = 0; x < data.preferences.length; x++) {
							if (settingName == data.preferences[x].name) {
								data.preferences[x].userValue = settingValue;
							}
						}
						break;
				}
			}

			// Put the updated object back into the database.
			var requestUpdate = transaction.put(data);

			requestUpdate.onerror = function() {
				alert("Couldn't update the following mod setting: " + setting);
			};

			requestUpdate.onsuccess = function() {
				console.log("Mod setting updated succesfully");
				//printModData(store, modId); // This line is only used for debugging purposes
			};
		};
	}


	// Removes mods from databases
	function removeMod(store, modId) {

		// Convert string identifier to actual identifier
		modId = parseInt(modId);

		// Delete the mod
		var request = db.transaction([store], "readwrite")
					.objectStore(store)
					.delete(modId);

		request.onsuccess = function() {
			console.log("Deleted mod!");
		};

		request.onerror = function() {
			console.log("There was an error while trying to delete the registry.");
		};
	}

	// Loads mods into Firefox
	function fetchMod(store, modId) {
		modId = parseInt(modId);
		var transaction = db.transaction(store);
		var modStore = transaction.objectStore(store);
		var request = modStore.get(modId);

		request.onerror = function() {
			console.log("Couldn't fetch the data of the mod with ID " + modId);
		};

		request.onsuccess = function() {
			var modCode = request.result.code;
			var modPrefs = request.result.preferences;
			var isContent;
			var isContentAlt;
			var uri;

			// We get the actual script after changing the variables for the user defined ones here
			function getScript() {
				var sc2Run;
				if (store == "CSSMods") {
					isContent = /==\/UserStyle==(\s*|\t*)\*\/(.*)/is;
					isContentAlt = /==\/UserStyle==(\s*|\t*)\n\*\/(.*)/is;
				} else if (store == "JSMods") {
					isContent = /==\/UserScript==(\s*|\t*)(.*)/is;
					isContentAlt = /==\/UserScript==(\s*|\t*)\*\/(.*)/is;
				}

				// We check if the mod had a header and get rid of it 
				if (modCode.match(isContent)) {
					sc2Run = modCode.match(isContent)[2];
				} else if (modCode.match(isContentAlt)) {
					sc2Run = modCode.match(isContentAlt)[2];
				} else {
					sc2Run = modCode;
				}

				// We replace the preferences if they existed with the keywords on the code
				if (modPrefs != []) {
					modPrefs.forEach(function(obj) {
						sc2Run = sc2Run.replace(obj.name, obj.userValue);
					});
				}
				return sc2Run;
			}

			var parsedCode = getScript();

			// These register the mods to Firefox stylesheets or scriptloaders
			if (store == "CSSMods") {
				var sss = Cc['@mozilla.org/content/style-sheet-service;1'].getService(Ci.nsIStyleSheetService);
				uri = makeURI('data:text/css;charset=UTF=8,' + encodeURIComponent(parsedCode));
				sss.loadAndRegisterSheet(uri, sss.AGENT_SHEET);
			} else if (store == "JSMods") {
				uri = makeURI('data:application/javascript;charset=UTF=8,' + encodeURIComponent(parsedCode));
				Services.scriptloader.loadSubScriptWithOptions(uri.spec, {target: window, ignoreCache: true});
			}
		};
	}

	// Downloads a new mod directly into the database.
	// (Only used for debugging purposes)
	function downloadMod(path2Script) {
		var defaultName;
		var modType;
		fetch(path2Script)
		.then(res => res.text())
		.then(function(obj) {
			var storeName;
			var modMeta;
			defaultName = path2Script.split("/");
			defaultName = defaultName[defaultName.length - 1];
			modType = defaultName.split(".");
			modType = modType[modType.length - 1];
			
			if (modType == "css") {
				storeName = "CSSMods";
			} else if (modType == "js") {
				storeName = "JSMods";
			}

			// We get the metadata of the mod here and then pass it to the other functions
			modMeta = checkMetadata(storeName, defaultName, obj, path2Script);

			// Mod handling here
			addOrUpdateMod(storeName, modMeta, obj);
			
		});
	}

	// We add the mod cards to the CSS and JS pages with this function
	function addModToList(store, modId, name) {
		modId = parseInt(modId);
		var transaction = db.transaction(store).objectStore(store);
		var request = transaction.get(modId);

		request.onerror = function() {
			console.log("Couldn't fetch the data of the mod " + name);
		};

		request.onsuccess = function() {

			// We get the mod values here
			var modDesc = request.result.description,
				modVer = request.result.version,
				modState = request.result.enabledState,
				modUpd = request.result.lastUpdate;

			// We get the dialogs for the button actions here
			var dialogOverlay = window.parent.document.getElementById("dialogOverlay");
			var remDialog = window.parent.document.getElementById("remMod");
			var diagModName = window.parent.document.getElementById("remModName");
			var diagModID = window.parent.document.getElementById("remModID");

			// We create the cards here
			var scriptsArea = document.getElementById("userScripts");

			var newMod = addElement(scriptsArea, "div", "mod");

			// We add the mod identifier as a hidden object to use it to select the mod later
			var modIdentifier = addElement(newMod, "p", "modID", modId);
			modIdentifier.style.display = "none";

			// Then we create the disable button
			var disableBtn = addElement(newMod, "label", ["switch", "disableButton"]);
			var checkBtn = addElement(disableBtn, "input", "modState");
			addElement(disableBtn, "span", "slider");

			// Title and description
			var modNameLabel = addElement(newMod, "h2", "modName", name);
			var modDescLabel = addElement(newMod, "p", "modDesc", modDesc);

			// Card containers for buttons and update elements
			var modFooter = addElement(newMod, "div", "modFooter");
			var otherSpan = addElement(modFooter, "span", "otherData");

			// Other mod information
			addElement(otherSpan, "label", null, "Version: ");
			var modVersionLabel = addElement(otherSpan, "label", "version", modVer);
			addElement(otherSpan, "br", null);

			// Update information
			addElement(otherSpan, "label", null, "Last updated: ");
			var lastUpdValue = addElement(otherSpan, "label", "lastUpdate", modUpd);
			var updateModBtn = addElement(otherSpan, "label", "updateSingle");
			var updateModSpin = addElement(updateModBtn, "label", "updateSingleSpin", "&#8634");
			var updateModBtnLabel = addElement(updateModBtn, "label", null, " update now");

			// Button area 
			var btnAreaSpan = addElement(modFooter, "span", "buttonSet");

			// Buttons inside button area
			addElement(btnAreaSpan, "button", "editMod", "&#128393 Edit");
			addElement(btnAreaSpan, "button", "customMod", "&#9881 Customize");
			addElement(btnAreaSpan, "button", "deleteMod", "&#128465 Remove");

			// ...And then add the missing attributes here
			checkBtn.setAttribute("type", "checkbox");
			updateModBtn.setAttribute("title", "Update now");

			if (modState == true) {
				var stateCheck = document.getElementsByClassName("modState");
				stateCheck[stateCheck.length - 1].checked = true;
			} else {
				newMod.classList.add("disabled");
			}

			// Mod card buttons
			var editBtn = document.getElementsByClassName("editMod");
			var customizeBtn = document.getElementsByClassName("customMod");
			var deleteBtn = document.getElementsByClassName("deleteMod");
			var enableBtn = document.getElementsByClassName("slider");

			// Button event listeners
			editBtn[editBtn.length -1].addEventListener("click", editMod, false);
			customizeBtn[customizeBtn.length -1].addEventListener("click", customizeMod, false);
			enableBtn[enableBtn.length -1].addEventListener("click", disableMod, false);
			deleteBtn[deleteBtn.length -1].addEventListener("click", delPopup, false);
			updateModBtn.addEventListener("click", updateMod, false);

			// Mod identifier fetching
			function getModId(evt) {
				let modInFocus = evt.target.closest(".mod");
				let modToChange = encodeURI(modInFocus.querySelector(".modID").innerHTML);
				let mod2CName = encodeURI(modInFocus.querySelector(".modName").innerHTML);

				try {
					modToChange = parseInt(modToChange);
				} catch {
					modToChange = 0;
				}
				
				var modArray = [modToChange, mod2CName];
				return modArray;
			}

			// Edit mod code page
			function editMod(event) {
				let modId = getModId(event);
				window.location.href = "chrome://userchromejs/content/QNModManager/html/edit-mod.html?id=" + modId[0] 
										+ ";name=" + modId[1];
			}

			// Customize mod page
			function customizeMod(event) {
				let modId = getModId(event);
				window.location.href = "chrome://userchromejs/content/QNModManager/html/customize-mod.html?id=" + modId[0] 
										+ ";name=" + modId[1];
				
			}

			// Disable mod function
			function disableMod(event) {
				let modToDisable = event.target.parentNode.parentNode.getElementsByClassName("modID")[0].innerHTML;
				let stateCheck = event.target.parentNode.parentNode.getElementsByClassName("modState")[0];
				if (stateCheck.checked) {
					changeModSetting(modStore, modToDisable, "enabledState", false);
					event.target.parentNode.parentNode.classList.add("disabled");
				} else {
					changeModSetting(modStore, modToDisable, "enabledState", true);
					event.target.parentNode.parentNode.classList.remove("disabled");
				}
			}

			// Remove mod dialog here
			function delPopup(event) {
				let modData = getModId(event)
				diagModName.innerHTML = modData[1];
				diagModID.innerHTML = modData[0];
				dialogOverlay.style.display = "block";
				remDialog.style.display = "block";
			}

			// Update mod and its labels here
			function updateMod(event) {
				let modId = getModId(event)[0];
				
				updateModBtnLabel.innerHTML = " updating...";
				updateModSpin.innerHTML = "⏳";
				

				getModUpdate(modId, store).then(function(wasModUpdated) {
					console.log("Mod was updated: " + wasModUpdated);
					if (wasModUpdated) {
						var transaction = db.transaction(store).objectStore(store);
						var newRequest = transaction.get(modId);

						newRequest.onerror = function() {
							console.log("Couldn't fetch the data of the mod " + name);
						};
	
						newRequest.onsuccess = function() {
							modNameLabel.innerHTML = newRequest.result.name;
							modDescLabel.innerHTML = newRequest.result.description;
							modVersionLabel.innerHTML = newRequest.result.version;
							lastUpdValue.innerHTML = newRequest.result.lastUpdate;
						};
					}
					updateModBtnLabel.innerHTML = " update now";
					updateModSpin.innerHTML = "↺";
					updateModSpin.classList.remove("rotating");

					if (wasModUpdated) return true;
					else return false;
				});
			}
		};
	}

	// We add the mod settings to the customize-mod page here
	function fillModSettings(store, modId) {
		modId = parseInt(modId);
		var transaction = db.transaction(store).objectStore(store);
		var request = transaction.get(modId);

		request.onsuccess = function() {

			//printModData(store, modId); //For debugging purposes

			// We get the mod values here
			var modName = request.result.name,
				modDesc = request.result.description,
				modURL = request.result.updateURL,
				modPrefs = request.result.preferences,
				modDefs = request.result.defaults,
				modUpdInt = request.result.updateInterval;

			// The parent element
			var settingsArea = document.getElementById("advancedSettings");

			// Fill in the common settings
			document.getElementById("namePlaceholder").innerHTML = modName;
			document.getElementById("inputModName").value = modName;
			document.getElementById("inputModDesc").value = modDesc;
			document.getElementById("inputModURL").value = modURL;

			let updateOptions = document.querySelectorAll("#inputUpdInterval > option");
			for (var x = 0; x < updateOptions.length; x++) {
				if (updateOptions[x].value == modUpdInt) {
					updateOptions[x].setAttribute("selected", true);
				}
			}

			// Switch buttons function
			function flipSwitch(evt) {
				var swButton;

				// Check if clicked item is switch
				if (evt.target.className == "slider") {
					swButton = evt.target.parentNode;
				} else {
					swButton = evt.target;
				}

				// Turn switch on or off depending on state
				var isOn = swButton.getAttribute("checked");
				if (isOn) {
					swButton.removeAttribute("checked");
				} else {
					swButton.setAttribute("checked", true);
				}
			}

			// Add the advanced settings
			for (var x = 0; x < modPrefs.length; x++) {
				addElement(settingsArea, "label", "modSettingName", modPrefs[x].description);
				var varEl;

				if (modPrefs[x].type != "select") {

					// Insert input
					varEl = addElement(settingsArea, "input", "modSetting");

					switch(modPrefs[x].type) {
						case "color":
							varEl.setAttribute("type", "color");
							varEl.value = modPrefs[x].userValue;
							break;
						case "text":
							varEl.setAttribute("type", "text");
							varEl.value = modPrefs[x].userValue;
							break;
						case "number":
							varEl.setAttribute("type", "number");
							varEl.value = modPrefs[x].userValue;
							let numLen = modPrefs[x].value.length;
							if (numLen < 4 && numLen > 1) {
								varEl.setAttribute("min", modPrefs[x].value[1].trim());
								varEl.setAttribute("max", modPrefs[x].value[2].trim());
							} else if (numLen == 4) {
								varEl.setAttribute("min", modPrefs[x].value[2].trim());
								varEl.setAttribute("max", modPrefs[x].value[3].trim());
							}
							
							break;
						case "checkbox":
							varEl.remove();
							varEl = addElement(settingsArea, "label", "modSetting");
							addElement(varEl, "span", "slider");
							varEl.classList.add("switch");
							if (modPrefs[x].userValue == "true" || modPrefs[x].userValue == true) {
								varEl.setAttribute("checked", true);
							}
							varEl.addEventListener("click", flipSwitch, false);
							break;
					}
					
				} else {

					// If select-type variable
					varEl = addElement(settingsArea, "select", "modSetting");
					let selVals = modPrefs[x].value;
					let userVal = modPrefs[x].userValue;
					for (var y = 0; y < selVals.length; y++) {
						let optVal = addElement(varEl, "option", "varOption");
						optVal.innerHTML = selVals[y][0];
						optVal.setAttribute("value", selVals[y][1]);
						if (selVals[y][1] == userVal) {
							optVal.setAttribute("selected", true);
						}
					}
				}

				// Add the name of the variable last to avoid repeating the code
				if (varEl) {
					varEl.setAttribute("name", modPrefs[x].name);
					var resetEl = addElement(settingsArea, "button", "resetInputBtn");
					resetEl.innerHTML = "&#10799";
					resetEl.title = "Reset to default value";
					settingsArea.appendChild(document.createElement("br"));
				}
			}

			// Add the listeners to the reset buttons.
			// We don't do this inside the advanced area creation because there are other ones
			// in the basic area.
			var resetBtns = document.getElementsByClassName("resetInputBtn");

			function resetInput(evt) {
				var inputEl = evt.target.previousElementSibling;
				var inputName = inputEl.getAttribute("name");
				var inputVal = "";
				switch(inputName) {
					case "name":
						inputEl.value = modDefs[0];
						break;
					case "description":
						inputEl.value = modDefs[1];
						break;
					case "updateURL":
						inputEl.value = modDefs[2];
						break;
					default:
						// Get the default value of the preference
						for (var y = 0; y < modPrefs.length; y++) {
							if (modPrefs[y].name == inputName) {
								inputVal = modPrefs[y].value;
								break;
							}
						}

						// Check if it's an input
						if (inputEl.hasAttribute("type")) {

							switch(inputEl.getAttribute("type")) {
								case "text":
									inputEl.value = inputVal;
									break;
								case "color":
									inputEl.value = inputVal;
									break;
								case "number":
									if (typeof inputVal === 'number'){
										inputEl.value = inputVal;
									} else if (Array.isArray(inputVal)) {
										if (typeof inputVal[0] === 'number') {
											inputEl.value = inputVal[0];
										} else {
											inputEl.value = inputVal[1];
										}
									}
									break;
								default:
									inputEl.innerHTML = inputVal;
									break;
							}

						// Check if its a switch or select
						} else {
							if (inputEl.tagName == "LABEL"){
								if ((inputVal == "false" || inputVal == "False") && inputEl.hasAttribute("checked")) {
									inputEl.removeAttribute("checked");
								} else if ((inputVal == "true" || inputVal == "True") && !inputEl.hasAttribute("checked")) {
									inputEl.setAttribute("checked", true);
								}
							} else if (inputEl.tagName == "SELECT") {
								var firstOption = inputEl.getElementsByTagName("option")[0];
								firstOption.selected = true;
							}
						}
						break;
				}
			}

			for (var i = 0; i < resetBtns.length; i++) {
				resetBtns[i].addEventListener("click", resetInput, false);
			}
		};
	}

	function iterateMods(modAction, Stores=["CSSMods", "JSMods"]) {
		if (!Array.isArray(Stores) && Stores.length > 2) 
			Stores = [Stores];
		for (var x = 0; x < Stores.length; x++) {
			const transaction = db.transaction(Stores[x]);
			const modStore =  transaction.objectStore(Stores[x]);
			
			modStore.openCursor().onsuccess = function(event) {
				var cursor = event.target.result;
				if (cursor) {
					switch(modAction) {
						case "start":
							fetchMod(event.composedTarget.source.name, cursor.value.id);
							break;
						case "list":
							addModToList(event.composedTarget.source.name, cursor.value.id, cursor.value.name);
							break;
						case "delete":
							removeMod(event.composedTarget.source.name, cursor.value.id);
							break;
					}
					cursor.continue();
				}
				else {
					switch(modAction) {
						case "start":
							console.log("All mods on " + event.composedTarget.source.name + " store were loaded.");
							break;
						case "list":
							console.log("All mods on " + event.composedTarget.source.name + " store were added to the list.");
							break;
						case "delete":
							console.log("All mods on " + event.composedTarget.source.name + " store were removed.");
							break;
					}
				}
			};
		}
	}

	function addOrUpdateSettings(settingName, settingValue) {
		var transaction = db.transaction("Settings", "readwrite");
		var modStore = transaction.objectStore("Settings");

		if (Array.isArray(settingName)) {
			for (let i = 0; i < settingName.length; i++) {
				addSetting(settingName[i], settingValue[i]);
			}
		} else {
			addSetting(settingName, settingValue);
		}

		function addSetting(settingInUse, settingValueUsed) {
			// We change the setting here
			modStore.put({
				name: settingInUse,
				value: settingValueUsed,
			});

			transaction.onerror = function() {
				alert("Error when updating the settings!");
			};
		}
	}

	function iterateSettings() {
		var transaction = db.transaction("Settings");
		var modStore =  transaction.objectStore("Settings");
		var request = modStore.openCursor();
			
		request.onsuccess = function(event) {
			var cursor = event.target.result;
			if (cursor) {
				let settingName = cursor.value.name;
				let settingValue = cursor.value.value;
				let checkItem;
				let modSection;

				// We handle the setting actions here
				if (settingName == "updateInterval") {
					if (currentPage == "settings.html") {
						checkItem = document.querySelector('#updateInterval option[value="' + settingValue + '"]');
						checkItem.setAttribute("selected", true);
					}
				} else if (settingName == "lightMode") {
					if (settingValue == true) {
						let parentBody = window.parent.document.body;
						let frameBody = document.body;
						if (currentPage == "settings.html") {
							checkItem = document.querySelector("#lightOn input");
							checkItem.setAttribute("checked", true);
						}
						parentBody.setAttribute("class", "light");
						frameBody.setAttribute("class", "light");
					}
				// } else if (settingName == "recomendMode") {
				// 	if (settingValue == false) {
				// 		if (currentPage == "settings.html") {
				// 			checkItem = document.querySelector("#recomendOn input");
				// 			checkItem.removeAttribute("checked");
				// 		} else if (currentPage == "css.html" || currentPage == "javascript.html") {
				// 			modSection = document.getElementById("recScripts");
				// 			modSection.style.display = "none";
				// 		}
				// 	}
				}
				cursor.continue(); 
			}
		};

		request.onerror = function() {
			console.log("Couldn't obtain the value of the settings.");
		};
	}

	// Prints the values of the mod on console. Useful for debugging.
	function printModData(store, modId) {
		if (store != "Settings") {
			modId = parseInt(modId);
		}
		var transaction = db.transaction(store);
		var modStore = transaction.objectStore(store);
		var request = modStore.get(modId);

		request.onerror = function() {
			console.log("Couldn't fetch the data of the mod with ID '" + modId + "'.");
		};

		request.onsuccess = function() {
			if (store == "Settings") {
				var settingValue = request.result.value;
				console.log("[Name = " + modId + ";Value = " + settingValue + "]");
			} else {
				var modName = request.result.name;
				var modCode = request.result.code;
				var modDesc = request.result.description;
				var modVers = request.result.version;
				var modAuth = request.result.author;
				var modURL = request.result.updateURL;
				var modUpdInt = request.result.updateInterval;
				var modDefs = request.result.defaults;
				var modPrefs = request.result.preferences;
				var modState = request.result.enabledState;
				var modLastUp = request.result.lastUpdate;
				var modLastVersCh = request.result.lastVersionCheck;

				// Basic data
				console.log("Id = " + modId + "\nName = " + modName + "\nDescription = " + modDesc + "\nVersion = " + modVers + "\nAuthor = " 
					+ modAuth + "\nUpdateURL = " + modURL + "\nUpdate Interval = " + modUpdInt + "\nEnabledState = " + modState + "\nLastUpdated = " + modLastUp
					+ "\nLast check for updates = " + modLastVersCh + ","
					+ "\nDefaults {\nName: '" + modDefs[0] + "',"
					+ "\nDescription: '" + modDefs[1] + "'," + "\nUpdate URL: '" + modDefs[2] + "'}," + "\nCode = {" + modCode
					+ "},\n");

				// Preferences data
				console.log("Mod preferences = {\n");
				for (var x = 0; x < modPrefs.length; x++) {
					console.log(modPrefs[x]);
				}
				console.log("}");
			}
		};
	}

	// Function to start CodeMirror instances
	function loadCodeMirror(codeArea, scriptMode, cmTheme="abcdef") {
		// Load Codemirror instance
		let scriptCont = CodeMirror.fromTextArea(codeArea, {
			lineNumbers: true,
			matchBrackets: true,
			theme: cmTheme,
			mode: scriptMode,
			readOnly: false
		});

		// We set the sizing of the code area
		scriptCont.setSize("100%", "90vh");
		return scriptCont;
	}

	// We get the raw html link here
	let rawPage = window.location.href;
	console.log("Navigating to " + rawPage);
	
	let noSrcPage = (rawPage.split("?")[0]).split("#")[0];
	let currentPage = noSrcPage.split("/")[noSrcPage.split("/").length - 1];
	let parentCategory = (window.top.location.href).split("#")[1];
	let store;

	// Fetch the store we are on here
	if (parentCategory == "css.html") {
		store = "CSSMods";
	} else if (parentCategory == "javascript.html") {
		store = "JSMods";
	}

	// We get the ID and Name of the mod to be loaded here
	function parseModURL(modStaticUrl) {
		var URLMeta = rawPage.replace(modStaticUrl, "")
		URLMeta = URLMeta.split(";");
		var modToChange = parseInt(decodeURI(URLMeta[0]));
		var mod2CName = decodeURI(URLMeta[1].split("=")[1]);
		return [modToChange, mod2CName];
	}

	// We change the settings here
	iterateSettings();
	switch(currentPage) {
		case "settings.html":

			const exportModsBtn = document.getElementById("exportAllScriptsBtn");
			const importModsBtn = document.getElementById("importAllScriptsBtn");

			// We update the settings on page leave
			window.addEventListener('beforeunload', function() {
				let uISel = document.getElementById("updateInterval");
				let updateInterval = uISel.options[uISel.selectedIndex].value;

				const lightMode = document.querySelector("#lightOn input");
				//const recomMode = document.querySelector("#recomendOn input");

				addOrUpdateSettings(["updateInterval", "lightMode"],
									[updateInterval, lightMode.checked]);
			}, false);


			// Function to export all installed scripts and styles
			async function exportAllMods() {
				console.info("Fetching all scripts to export...");
				function getDBEntries(dbStore) {
					let transaction = db.transaction(dbStore);
					let modStore =  transaction.objectStore(dbStore);
					let request = modStore.openCursor();
						
					return new Promise((resolve, reject) => {
						request.onsuccess = function(e) {
							const cursor = e.target.result;
							let modArray = [];
							if (cursor) {
								modArray.push(cursor.value);
								cursor.continue();
							}
							resolve(modArray);
						}

						request.onerror = function(e) {
							resolve([]);
						}
					});
				}
				const JSEntries = await getDBEntries("JSMods");
				const CSSEntries = await getDBEntries("CSSMods");

				const exportedJSON = JSON.stringify({
					"JS": JSEntries, 
					"CSS": CSSEntries
				});

				console.info("Exporting scripts to JSON file...");
				let element = document.createElement('a');
				const scriptBlob = new Blob([exportedJSON], {type: "text/plain"});
				element.href = URL.createObjectURL(scriptBlob);
				element.download = "QNModsExport.json";
				document.body.appendChild(element);

				element.click();

				document.body.removeChild(element);
			}

			// Function to import all installed scripts and styles from an exported json file
			function importAllMods() {
				console.log("Entered import function");	
				const fileImportInput = document.getElementById("file-import");
				let fileToImport;
				
				fileImportInput.click();

				fileImportInput.onchange = function(){
					if (fileImportInput.files.length > 0) {
						const fr = new FileReader();
						fileToImport = fileImportInput.files[0];
						fr.readAsText(fileToImport);
						fr.onload = function(e) {
							const content = e.target.result;
							const modsObject = JSON.parse(content);
							let importPromises = []
							
							modsObject.CSS.forEach(item => {
								importPromises.push(importMod("CSSMods", item));
							});

							modsObject.JS.forEach(item => {
								importPromises.push(importMod("JSMods", item));
							});
							
							if (importPromises.length > 0) {
								
								Promise.allSettled(importPromises).then(result => {
									let importError = []
									result.forEach(promise => {
										if (Object.prototype.hasOwnProperty.call(promise, "reason")) {
											importError.push(promise.reason);
										}
									})

									// In case some mod couldn't be imported
									if (importError.length > 0) {
										let message = "The following mods couldn't be imported due to already being part of your database: "

										for (let i = 0; i < importError.length; i++) {
											message += "\n" + importError[i];
										}
	
										alert(message)
									}
								});

							}

							console.log("Mods imported!");
						};
						
					} else {
						console.log("User canceled the operation");
					}
				}
			}

			// Add export and import button listeners
			exportModsBtn.onclick = exportAllMods;
			importModsBtn.onclick = importAllMods;
			
			break;
		case "css.html":
		case "javascript.html":
			var modStore;

			if (currentPage == "css.html") {
				modStore = "CSSMods";
			} else if (currentPage == "javascript.html") {
				modStore = "JSMods";
			}
			
			iterateMods("list", [modStore]);
			
			// We get the dialog elements of the parent window here
			var remButton = window.parent.document.querySelector("#remMod .actBtn");
			var remDiag = window.parent.document.getElementById("remMod");
			var addDialog = window.parent.document.getElementById("addMod");
			var dialogOverlay = window.parent.document.getElementById("dialogOverlay");

			// Along with all the static buttons
			var addButton = document.getElementById("addModBtn");
			var importButton = document.getElementById("importModBtn");
			var updateAllButton = document.getElementById("updateAllBtn");

			// Action for the remove mod button
			function removeModBtn() {
				let remID = window.parent.document.getElementById("remModID").innerHTML;
				removeMod(modStore, remID);
				location.reload();
				dialogOverlay.style.display = "none";
				remDiag.style.display = "none";
			}

			// We show the import mod dialog here
			function importPopup() {
				dialogOverlay.style.display = "block";
				addDialog.style.display = "block";
			}

			// We show the code editor when adding a new mod here
			function addNewMod() {
				window.location.href = "chrome://userchromejs/content/QNModManager/html/edit-mod.html?id=-1;name=New%20mod";
			}

			// We simulate the clicking of the update now label to update each mod in the page
			function updateAllMods() {
				var updateLabels = document.getElementsByClassName("updateSingle");
				for(var x = 0; x < updateLabels.length; x++) {
					updateLabels[x].click();
				}
			}

			// We add the button click events here
			addButton.addEventListener("click", addNewMod, false);
			importButton.addEventListener("click", importPopup, false);
			remButton.addEventListener("click", removeModBtn, false);
			updateAllButton.addEventListener("click", updateAllMods, false);
			break;
		case "customize-mod.html":
			// We get the name of the mod to customize here
			var URLMeta = parseModURL("chrome://userchromejs/content/QNModManager/html/customize-mod.html?id=")
			var modToChange = URLMeta[0];
			var mod2CName = URLMeta[1];
			document.getElementById("namePlaceholder").innerHTML = mod2CName;
			document.getElementById("inputModName").value = mod2CName;

			// Get the button elements here
			var saveBtn = document.getElementById("saveChangesBtn");
			var cancelBtn = document.getElementById("cancelChangesBtn");

			// Add the advanced settings of the mod
			fillModSettings(store, modToChange);

			// Set the save button action
			saveBtn.onclick = function() {
				var modSettings = document.querySelectorAll("#modSettings *[name]");
				var modName = document.getElementById("namePlaceholder");
				var notifTooltip = document.getElementById("bottom-notice");
				var settingNames = [];
				var settingValues = [];
			
				for (var x = 0; x < modSettings.length; x++) {
					settingNames.push(modSettings[x].getAttribute("name"));

					// If the element is an input or a select, we get the values directly
					if (modSettings[x].nodeName == "INPUT" || modSettings[x].nodeName == "SELECT" ||
						modSettings[x].nodeName == "TEXTAREA") {
						settingValues.push(modSettings[x].value)
						continue;
					
					// If a switch, we transform the "checked" state into true or false
					} else if (modSettings[x].nodeName == "LABEL") {
						if (modSettings[x].hasAttribute("checked")) {
							settingValues.push(true);
						} else {
							settingValues.push(false);
						}
					}
				}
				changeModSetting(store, modToChange, settingNames, settingValues)
				modName.innerHTML = modSettings[0].value;
				notifTooltip.innerHTML = "Settings saved!";
				notifTooltip.style.transform = "translateY(-40px)";
				setTimeout(function(){
					notifTooltip.style.transform = "translateY(40px)";}, 3000);
			};

			// Set the cancel button action
			cancelBtn.onclick = function() {
				window.location.href = "./" + parentCategory;
			};
			
			break;
		case "edit-mod.html":
			// Get the button identifiers and other initial vars
			var codeBtn = document.getElementById("codeBtn");
			var configBtn = document.getElementById("configBtn");
			var helpBtn = document.getElementById("helpBtn");
			var exportModBtn = document.getElementById("exportModBtn");
			var saveModBtn = document.getElementById("saveModBtn");
			var closeEditBtn = document.getElementById("closeEditBtn");
			var inputModName = document.getElementById("inputModName");
			var inputModDesc = document.getElementById("inputModDesc");
			var inputModURL = document.getElementById("inputModURL");
			var selectModUpdate = document.getElementById("updateInterval");
			var modTitle = document.getElementById("editModTitle");
			var codeArea = document.getElementById("editModFrame");
			var scriptMode = "css";
			var scriptExt = ".as.css";
			store = "CSSMods";

			// Add the CodeMirror mode to use depending on the type of script
			var themeUsed = document.createElement('link');

			// Load the default theme for CodeMirror here
			themeUsed.rel = "stylesheet";
			themeUsed.href = "../CodeMirror/theme/abcdef.css";

			document.head.appendChild(themeUsed);

			if (parentCategory == "javascript.html") {
				scriptMode = "javascript";
				scriptExt = ".uc.js"
				store = "JSMods";
			}

			// Connect the first 3 buttons to their frames
			function switchFrame(event) {

				var activeFrameId;

				if (event.target == helpBtn) {
					activeFrameId = document.getElementById("helpModFrame");
					document.getElementsByClassName("CodeMirror")[0].setAttribute("hidden", true);
				} else if (event.target == configBtn) {
					activeFrameId = document.getElementById("configModFrame");
					document.getElementsByClassName("CodeMirror")[0].setAttribute("hidden", true);
				} else {
					activeFrameId = document.getElementById("editModFrame");
					document.getElementsByClassName("CodeMirror")[0].removeAttribute("hidden");
				}

				// Update the active tab status
				document.getElementById("codeModHeader").getElementsByClassName("active")[0].removeAttribute("class");
				event.target.classList.add("active");

				// Show the corresponding frame only
				document.getElementsByClassName("activeFrame")[0].setAttribute("hidden", true);
				document.getElementsByClassName("activeFrame")[0].removeAttribute("class");
				activeFrameId.classList.add("activeFrame");
				activeFrameId.removeAttribute("hidden");
			}

			// Function to export script to a file
			function exportScript() {
				console.info("Exporting script...");
				let element = document.createElement('a');
				const scriptCont = document.querySelector('.CodeMirror').CodeMirror.getValue();
				const scriptBlob = new Blob([scriptCont], {type: "text/plain"});
				element.href = URL.createObjectURL(scriptBlob);
				element.download = document.getElementById("editModTitle").innerHTML + scriptExt;
				document.body.appendChild(element);

				element.click();

				document.body.removeChild(element);
			}

			// Function to save script to the database
			function saveScript() {
				console.info("Saving script...");
				var scriptCont = document.querySelector('.CodeMirror').CodeMirror;
				var codeValue = scriptCont.getDoc().getValue();
				var modMeta = checkMetadata(store, mod2CName, codeValue);

				// Update the values with the ones inserted by the user on the "config" section of the mod
				if (inputModName.innerHTML != "" && inputModName.innerHTML != null) {
					modMeta[0] = inputModName.innerHTML;
				}

				if (inputModDesc.innerHTML != "" && inputModDesc.innerHTML != null) {
					modMeta[1] = inputModDesc.innerHTML;
				}

				if (inputModURL.innerHTML != "" && inputModURL.innerHTML != null) {
					modMeta[4] = inputModURL.innerHTML;
				}

				addOrUpdateMod(store, modMeta, codeValue, modToChange, selectModUpdate.value);

				modTitle.innerHTML = modMeta[0];

				var notifTooltip = document.getElementById("bottom-notice");
				notifTooltip.innerHTML = "Mod saved!";
				notifTooltip.style.transform = "translateY(-40px)";
				setTimeout(function(){
					notifTooltip.style.transform = "translateY(40px)";}, 3000);
			}

			// Connect first 3 buttons to the frame switching function
			codeBtn.onclick = switchFrame;
			configBtn.onclick = switchFrame;
			helpBtn.onclick = switchFrame;

			// Connect last 3 buttons to their functions
			exportModBtn.onclick = exportScript;
			saveModBtn.onclick = saveScript;
			closeEditBtn.onclick = function() {
				window.location.href = "./" + parentCategory;
			}

			// We get the name of the mod to edit here
			var URLMeta = parseModURL("chrome://userchromejs/content/QNModManager/html/edit-mod.html?id=")
			var modToChange = URLMeta[0];
			var mod2CName = URLMeta[1];

			// If not a new mod, we try to load it
			if (modToChange != -1) {
				modTitle.innerHTML = mod2CName;

				// Access the mod store to find the script by ID
				let modId = parseInt(modToChange);
				var transaction = db.transaction(store);
				var modStore = transaction.objectStore(store);
				var request = modStore.get(modId);

				request.onerror = function() {
					console.log("Couldn't fetch the data of the mod with name " + mod2CName);
				};

				request.onsuccess = function() {
					var modCode = request.result.code;
					var modDefs = request.result.defaults;
					var modName = request.result.name;
					var modDesc = request.result.description;
					var modURL = request.result.updateURL;
					var modUpInt = request.result.updateInterval;

					// Fill in custom name if different from the code one
					if (modName != modDefs[0]) 
						inputModName.innerHTML = modName;
					
					// Fill in custom description if different from the code one
					if (modDesc != modDefs[1]) 
						inputModDesc.innerHTML = modDesc;
					
					// Fill in custom description if different from the code one
					if (modURL != modDefs[2]) 
						inputModURL.innerHTML = modURL;
					
					selectModUpdate.value = modUpInt;

					codeArea.value = modCode;

					// Replace line breaks since they don't get registered as such in the textarea
					codeArea.innerText = modCode.replace(/\n/g, "&#10");

					// Load codemirror instance
					loadCodeMirror(codeArea, scriptMode);
				}
			} else {
				// Add the templates for each type of script in case of new mod creation
				if (scriptMode == "css") {
					var modCode = `// ==UserStyle==
// @name           New UserStyle
// @description    This is the description of the new userstyle
// @author         Me
// @version        0.0.1
// ==/UserStyle==

/* Code goes here */`;
					
				} else {
					var modCode = `// ==UserScript==
// @name           New Script
// @description    This is the description of the new script
// @author         Me
// @version        0.0.1
// ==/UserScript==

(function(){
	// Code goes here
})()`;
				}

				codeArea.value = modCode;

				// Replace line breaks since they don't get registered as such in the textarea
				codeArea.innerText = modCode.replace(/\n/g, "&#10");

				// Load codemirror instance
				loadCodeMirror(codeArea, scriptMode);
			}
			break;
		case "import-mod.html":
			// We get the action button selectors here
			var installBtn = document.getElementById("installModBtn");
			var cancelBtn = document.getElementById("cancelModBtn");
			var reloadBtn = document.getElementById("reloadModBtn");
			var indexName;

			// We check the extension of the file just in case
			var parsedSrc = rawPage.replace("chrome://userchromejs/content/QNModManager/html/import-mod.html?source=", "");
			var srcArray = parsedSrc.split(".");
			var srcExt = srcArray[srcArray.length - 1];

			// Define the store to add the mod
			if (parentCategory == "css.html" || srcExt == "css") {
				store = "CSSMods";
				indexName = "CSSModURL";
			} else if (parentCategory == "javascript.html" || srcExt == "js") {
				store = "JSMods";
				indexName = "JSModURL";
			}

			// Button actions
			reloadBtn.onclick = function() {
				location.reload();
			}

			cancelBtn.onclick = function() {
				window.location.href = "./" + parentCategory;
			}

			installBtn.onclick = function() {
				// First check the metadata to see if there is another mod with the same name
				var defaultName = document.getElementById("name").innerHTML;
				var codeValue = document.querySelector(".CodeMirror").CodeMirror.getValue();
				var modMeta = checkMetadata(store, defaultName, codeValue);

				if (modMeta[4] == "") {
					modMeta[4] = parsedSrc;
				}

				var transaction = db.transaction(store);
				var modStore =  transaction.objectStore(store);
				var index =  modStore.index(indexName);

				// Check if the mod with the same source exists
				index.get(modMeta[4]).onsuccess = function(event) {
					if (event.target.result) {
						alert("A mod from the same source already exists.\nChange the update url of the old one if you want a duplicate.");
					} else {
						console.log("No duplicates found, adding mod to the database...");
						addOrUpdateMod(store, modMeta, codeValue);
					}
				}

				index.get(modMeta[4]).onerror = function() {
					alert("There was an error while trying to access the mods index");
				};

				// Do something when all the data is added to the database.
				transaction.oncomplete = function() {
					console.log("Finished the import process.");
					window.location.href = "./" + parentCategory;
				};

				transaction.onerror = function() {
					alert("Error when adding the mod to the database!");
					window.location.href = "./" + parentCategory;
				};
			}
			break;
		}
};

DBrequest.onerror = function() {
	console.log("Failed to open IndexedDB.");
};