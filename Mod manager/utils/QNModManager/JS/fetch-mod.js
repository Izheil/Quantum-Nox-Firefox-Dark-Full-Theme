// Get the source of the code from the iframe link and define some variables
let source = window.location.href
var parsedSrc = source.replace("chrome://userchromejs/content/QNModManager/html/import-mod.html?source=", "");
var srcArray;
var srcName;

// Add the CodeMirror mode to use depending on the type of script
var scriptType = document.createElement('script');
var themeUsed = document.createElement('link');
var scriptMode;
var scData;

// Get the filename of the script as a placeholder here
srcArray = parsedSrc.split("\\");
srcArray = srcArray[srcArray.length - 1].split("/");
srcName = srcArray[srcArray.length - 1];

// Load the default theme for CodeMirror here
themeUsed.rel = "stylesheet";
themeUsed.href = "../CodeMirror/theme/abcdef.css";

document.head.appendChild(themeUsed);

if (parsedSrc.slice(-3) == "css") {
	scriptMode = "css";
} else if (parsedSrc.slice(-2) == "js") {
	scriptMode = "javascript";
}

// We define the CodeMirror specs here
var codeArea = document.getElementById("scriptCode");
var scriptCont = CodeMirror.fromTextArea(codeArea, {
	lineNumbers: true,
	matchBrackets: true,
	theme: "abcdef",
	mode: scriptMode,
	readOnly: true
});

// We set the sizing of the code area
scriptCont.setSize("100%", "75vh");

// We download the actual script here and parse the main details from the header
fetch(parsedSrc)
	.then(res => res.text())
	.then(function(codeValue) {
		var scriptData = [srcName, "No description available", "Unknown", "Unknown", "Here be dragons"];
		var isCSS = /==UserStyle==/i;
		var isJS = /==UserScript==/i;
		var isHeader;
		var isContent;
		var isContentAlt;

		// We set regex to get the header content
		if (scriptMode == "css") {
			isHeader = /==UserStyle==(.*)==\/UserStyle==/is;
			isContent = /==\/UserStyle==(\s*|\t*)\*\/(.*)/is;
			isContentAlt = /==\/UserStyle==(\s*|\t*)\n\*\/(.*)/is;
		} else if (scriptMode == "javascript"){
			isHeader = /==UserScript==(.*)==\/UserScript==/is;
			isContent = /==\/UserScript==(\s*|\t*)(.*)/is;
			isContentAlt = /==\/UserScript==(\s*|\t*)\*\/(.*)/is;
		} else {
			console.log("Script type not recognized.")
			return
		}


		// We check that the script has a header
		if (isCSS.test(codeValue) || isJS.test(codeValue)) {
			var headerContent =  codeValue.match(isHeader)[1].split("\n");



			// Regex matchers to get the right metadata values
			var isName = /@name(\s+|\t+)(.+)/i;
			var isDesc = /@description(\s+|\t+)(.+)/i;
			var isVers = /@version(\s+|\t+)(.+)/i;
			var isAuth = /@author(\s+|\t+)(.+)/i;

			// We iterate over all header lines to find the metadata
			headerContent.forEach(function(value) {
				let isMetaName = isName.test(value);
				let isMetaDesc = isDesc.test(value);
				let isMetaVers = isVers.test(value);
				let isMetaAuth = isAuth.test(value);
				if (isMetaName && scriptData[0] == srcName) {
					scriptData[0] = value.match(isName)[2];
				} else if (isMetaDesc && scriptData[1] == "No description available") {
					scriptData[1] = value.match(isDesc)[2];
				} else if (isMetaVers && scriptData[2] == "Unknown") {
					scriptData[2] = value.match(isVers)[2];
				} else if (isMetaAuth && scriptData[3] == "Unknown") {
					scriptData[3] = value.match(isAuth)[2];
				}
			});
		}

		// We define the code here
		scriptData[4] = codeValue;

		var codeArea = document.getElementById("scriptCode");
		var nameLabel = document.getElementById("name");
		var descLabel = document.getElementById("description");
		var versLabel = document.getElementById("version");
		var authLabel = document.getElementById("author");

		// We add the content to the elements here
		nameLabel.innerHTML = scriptData[0];
		descLabel.innerHTML = scriptData[1];
		versLabel.innerHTML = scriptData[2];
		authLabel.innerHTML = scriptData[3];
		codeArea.value = scriptData[4];

		// Replace line breaks since they don't get registered as such in the textarea
		codeArea.innerText = codeValue.replace(/\n/g, "&#10");
		
		// We update the Codemirror value here
		scriptCont.getDoc().setValue(scriptData[4]);

		// Remove the loading animation after we are done
		document.getElementById("loader-container").style.display = "none";
	});