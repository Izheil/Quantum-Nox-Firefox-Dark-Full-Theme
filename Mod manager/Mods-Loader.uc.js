// ==UserScript==
// @name           Mods manager
// @namespace      https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme
// @description    Firefox Mods manager
// @compatibility  Firefox 91.0a1
// @author         Izheil
// @version        27/06/2020 13:09 First release
// ==/UserScript==

// This section deletes the whole database (for debugging purposes)
// var dbDel = indexedDB.deleteDatabase("FirefoxMods");

// dbDel.onsuccess = function () {
// 	console.log("Deleted database successfully");
// };

// dbDel.onerror = function () {
// 	console.log("Couldn't delete database");
// };

// dbDel.onblocked = function () {
// 	console.log("Couldn't delete database due to the operation being blocked");
// };

var db;
var DBrequest = window.indexedDB.open("FirefoxMods", 1);

DBrequest.onupgradeneeded = function(event) {
	console.log("Updating database...");
	var db = event.target.result;

	// Create an objectStore to hold the settings of the script
	var settingStore = db.createObjectStore("Settings", { keyPath: "name" });
	settingStore.createIndex("SettingName", "name", { unique: true });

	// Create an objectStore to hold the JS scripts data
	var jsModStore = db.createObjectStore("JSMods", { keyPath: "id", autoIncrement: true });
	jsModStore.createIndex("JSModID", "id", { unique: true });
	jsModStore.createIndex("JSModURL", "updateURL", { unique: true });

	// Create an objectStore to hold the CSS scripts data
	var cssModStore = db.createObjectStore("CSSMods", { keyPath: "id", autoIncrement: true });
	cssModStore.createIndex("CSSModID", "id", { unique: true });
	cssModStore.createIndex("CSSModURL", "updateURL", { unique: true });
};

DBrequest.onsuccess = function() {
	db = this.result;

    db.onerror = function(event) {
		// Generic error handler for all errors targeted at this database's
		// requests!
		console.error("Database error: " + event.target.errorCode);
	};

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
		// Name, Description, Version, Author, Update URL
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

	// Checks for existing mods in the database and updates them
	function updateMod(store, modMeta, codeValue, modId=-1, updInt="default", updURL="") {
		var indexName;
		if (store == "CSSMods") {
			indexName = "CSSModID";
		} else if (store == "JSMods") {
			indexName = "JSModID";
		}
		var transaction = db.transaction(store, "readwrite");
		var modStore =  transaction.objectStore(store);
		var index =  modStore.index(indexName);
		var isOn = false;
		var prefs;

		// Get current date
		let d = new Date();
		let timeArray = [d.getHours(), d.getMinutes(), d.getSeconds()]

		for (let q = 0; q < 3; q++) {
			if (timeArray[q] < 10) {
				timeArray[q] = "0" + timeArray[q]
			}
		}

		// Set human-readable form for date
		var lastUpd = String(d.getFullYear() + "/" + (d.getMonth() + 1) + "/" + d.getDate() + 
							" - " + timeArray[0] + ":" + timeArray[1] + ":" + timeArray[2]);

		if (modMeta[4] == "")
			modMeta[4] = updURL;

		// Update the default values by the code of the script
		var defaultMeta = [modMeta[0], modMeta[1], modMeta[4]];

		if (modId > 0) {

			index.get(modId).onsuccess = function(event) {
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
						lastVersionCheck: d,
					});
				}

				// In case there is some null value on a unique entry or some other issue, this happens
				request.onerror = function() {
					console.log("There was a problem while adding the mod '" + modMeta[0] + "' to the database. "
							+ "\nMake sure that a mod with the same ID or update URL doesn't already exist.");
				};
	
				// If the operation was successful
				request.onsuccess = function() {
					console.log("Mod '" + modMeta[0] + "' updated successfully!");
				};
			};
		}

		// Alert when the index couldn't be accessed to update a mod
		index.get(modMeta[0]).onerror = function() {
			console.log("There was an error while trying to access the mods database index.");
		};

		// Alert when there was a problem with the transaction
		transaction.onerror = function() {
			console.log("Error with the transaction when updating the database entry.");
		};
	}

	// Loads mods into Firefox
	function fetchMod(store, modId) {
		var transaction = db.transaction(store);
		var modStore = transaction.objectStore(store);
		var request = modStore.get(modId);

		request.onerror = function() {
			console.log("Couldn't fetch the data of the mod " + modId);
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

	// Updates a mod with the given url
	function getModUpdate(modId, modUpdateInt, defaultName, modVer, storeName, path2Script) {
		var defaultName;


		// Updates the date of the last check of the mod version
		function updateLastVersionCheck(store, modId) {
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
					if (parseInt(versionDate[0]) >= 2000) {
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
			var newVersionNum = newNumVersion[0].split(".");
			var oldVersionNum = oldNumVersion[0].split(".");

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
					if (newVersionNum[2] > newVersionNum[2]) {
						return true;
					}
				}
			}

			// If the version is the same or lower or all checks fail
			return false;
		}

		// Fetch the actual mod
		fetch(path2Script)
		.then(res => res.text())
		.then(function(obj) {

			// We get the metadata of the mod here and then pass it to the other functions
			var modMeta = checkMetadata(storeName, defaultName, obj, path2Script);

			// We check if the version of the mod we have installed is older than the lastest available version
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
						if (isNewerNumberVersion(modMeta[2], modVer))
							isBiggerVersion = true;

					// If the old version used a date or didn't have a number version
					} else {
						isBiggerVersion = true;
					}
				}

				// Mod update handling here
				if (isBiggerVersion) 
					updateMod(storeName, modMeta, obj, modId, modUpdateInt);
				else 
					updateLastVersionCheck(storeName, modId)
			} 
		});
	}

	function iterateMods(modAction) {
		
		// Common function to iterate through the mods
		function iterateModStores(generalUpdateInterval="startup") {
			var Stores = ["CSSMods", "JSMods"];
			for (var x = 0; x < Stores.length; x++) {
				var transaction = db.transaction(Stores[x]);
				var modStore =  transaction.objectStore(Stores[x]);
				
				modStore.openCursor().onsuccess = function(event) {
					var cursor = event.target.result;
					if (cursor) {
						if (modAction == "start") {
							fetchMod(event.composedTarget.source.name, cursor.value.id);
						} else if (modAction == "update") {
	
							if (cursor.value.updateURL != "") {

								var updInterval = cursor.value.updateInterval;
								var versCheckDate = cursor.value.lastVersionCheck;
								var versionCheckTime = -1;

								if (updInterval == "default") 
									updInterval = generalUpdateInterval;

								switch(cursor.value.updateInterval) {

									case "never" || "startup":
										// Don't check for the last version check
										break;
									case "daily":
										versionCheckTime = 86400000
										break;
									case "weekly":
										versionCheckTime = 604800000
										break;
									case "monthly":
										versionCheckTime = 2592000000
										break;
									default:
										updInterval = "startup";
										break;
									
								}

								// We check if the time between the last check and now is below the time frame
								// of the update interval
								if (updInterval != "never" && updInterval != "startup" &&
									Math.abs(new Date() - versCheckDate) < versionCheckTime) {
										updInterval = "never";
									}

								// If the mod isn't set to never update, we update the mod
								if (updInterval != "never")
									getModUpdate(cursor.value.id, cursor.value.updateInterval, cursor.value.defaults[0],
												cursor.value.version, event.composedTarget.source.name, cursor.value.updateURL);
							}

							// TODO - Test the update script
						}
						cursor.continue();
					}
					else {
						if (modAction == "start") {
							console.log("All mods on " + event.composedTarget.source.name + " store were loaded.");
						} else if (modAction == "update") {
							console.log("All mods on " + event.composedTarget.source.name + " store were updated.");
						}
					}
				};
			}
		}

		// Possible actions of the function 
		if (modAction == "update") {
			var transaction = db.transaction("Settings");
			var modStore =  transaction.objectStore("Settings");
			var index =  modStore.index("SettingName");

			index.get("updateInterval").onsuccess = function(event) {
				if (event.target.result && event.target.result.value != "startup") 
					iterateModStores(event.target.result.value);
				else 
					iterateModStores();
			}

			// Alert when the index couldn't be accessed to update a mod
			index.get("updateInterval").onerror = function() {
				console.log("Couldn't find the default value of the mods update interval. " +
							"Either the settings haven't been created yet, or it's the first run.");
			};
		} else 
			iterateModStores();
	}

	// Prints the values of the mod on console. Useful for debugging.
	function printModData(store, modId) {
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
				var modDefs = request.result.defaults;
				var modPrefs = request.result.preferences;
				var modState = request.result.enabledState;
				var modLastUp = request.result.lastUpdate;
				var modLastVersCh = request.result.lastVersionCheck;

				// Basic data
				console.log("Name = " + modName + "\nDescription = " + modDesc + "\nVersion = " + modVers + "\nAuthor = " 
					+ modAuth + "\nUpdateURL = " + modURL + "\nEnabledState = " + modState + "\nLastUpdated = " + modLastUp
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

	// We handle mod updates here
	iterateMods("update");
	// Debugging tests here
	// printModData("Settings", "advancedMode");
};

DBrequest.onerror = function() {
	console.log("Failed to open IndexedDB.");
};