// ==UserScript==
// @name           Tabs on bottom of window
// @namespace      https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme
// @description    Moves tabs to the bottom of the window, below the content area
// @include        main
// @compatibility  Firefox 134
// @author         Izheil
// @version        11/01/2025 02:45 Fixed tabs not showing at bottom after proton
// @version        05/10/2020 01:10 Added the option to hide tabs on fullscreen completelly until keypress
// @version        03/10/2020 05:32 Initial release
// ==/UserScript==

// Start of editable area

// You can set if the min/max/resize buttons are visible from the tabs toolbar here
let hideResButtons = true; // Set to false to show the buttons

// You can choose to always hide tabs in fullscreen here to avoid some issues
let hideFSTabs = false; // Set to true to show the tabs only when pressing the key combination

// Choose key combination to show tabs on fullscreen (a max of 2 is allowed, and the first must be Ctrl, Alt, or Shift).
// The first letter of each key must be capital.
// This only makes sense if tabs are hidden on fullscreen (if hideFSTabs == true).
let keysForFSTabs = ["Shift", "T"]; // The default is ["Shift", "T"]

// End of editable area

// We get the tab parent element and the bottom container, among other elements
let tabsParent = document.getElementById("TabsToolbar");

let menuHidden = document.querySelector("#toolbar-menubar[inactive]");
let menuShown = document.querySelector("#toolbar-menubar[autohide='false']");
let menuElement = document.getElementById("toolbar-menubar");
let resizeButtons = document.querySelector("#TabsToolbar > .titlebar-buttonbox-container");
let browserContent = document.getElementById("browser");
let navToolbox = document.getElementById("navigator-toolbox");
let modKeyToggleTabs;
let keyToggleTabs;

// Create bottom box
let bottomBox = createNewElement("div", "browser-bottombox");

if (keysForFSTabs.length == 2) {
	modKeyToggleTabs = keysForFSTabs[0];
	keyToggleTabs = keysForFSTabs[1];
} else {
	keyToggleTabs = keysForFSTabs[0];
}

// Hide the unneeded
if (hideResButtons) {
	resizeButtons.style.display = "none";
} 

// This is the element creation function for the fullscreen toggler on bottom
function createNewElement(elementTag, elementId) {
    // Adds an element to the document
    let newElement = document.createElement(elementTag);
    newElement.setAttribute('id', elementId);
	return newElement;
}

// Creation of the toggle to show tabs on fullscreen
let bottomFSTogglr = createNewElement("div", "fullscr-toggler-bottom");
let topFSTogglr = document.getElementById("fullscr-toggler");

// Function to show tabs when they are hidden
function showTabs() {
	tabsParent.style.marginBottom = "0";
	tabsParent.style.transition = "none";
}

// Function to hide tabs when they are shown
function hideTabs() {
	tabsParent.style.marginBottom = tabsParent.getBoundingClientRect().height * -1 + "px";
	tabsParent.style.transition = "margin 300ms";
}

// We choose to show tabs on fullscreen if the user enabled that option
if (hideFSTabs) {
	// Event listener for keypresses
	window.addEventListener("keydown", tabsToggle, false);

	// Key shortcut toggler
	function tabsToggle(e) {
		// We define the modifiers here
		if (keysForFSTabs.length == 2) {
			switch(keysForFSTabs[0]) {
				case "Shift":
					modKeyToggleTabs = e.shiftKey;
					break;
				case "Ctrl":
					modKeyToggleTabs = e.ctrlKey;
					break;
				case "Alt":
					modKeyToggleTabs = e.altKey;
					break;
				case "Cmd":
					modKeyToggleTabs = e.metaKey;
					break;
			}
		}

		if (window.fullScreen && modKeyToggleTabs && e.key == keyToggleTabs) {
			console.log(tabsParent.style.marginBottom)
			if (tabsParent.style.marginBottom == "0px") {
				hideTabs();
			} else {
				showTabs();
			}
		}
	}

// If we don't hide tabs completelly by default
} else {
	// Event listener for tabs area
	bottomFSTogglr.addEventListener("mouseover", showTabs, false);
}

browserContent.onmouseover = function() {
	hideTabs();
	navToolbox.style.transition = "margin 300ms";
}

// We hide the titlebar when not shown as well as the tabs when in fullscreen
let css = `
#main-window[inFullscreen]) #toolbar-menubar:not([inactive]) {
	margin-top: 28px !important;
}

#main-window[inFullscreen] #fullscr-toggler-bottom {
	display: block;
	height: 1px;
	width: 100%;
}

#main-window:not([inFullscreen]) #fullscr-toggler-bottom {
	display: none;
}

#main-window[inFullscreen] #TabsToolbar, 
#main-window[inFullscreen] #navigator-toolbox {
	transition: margin 300ms;
}

#main-window:not([inFullscreen]) #TabsToolbar {
	margin-bottom: 0 !important;
}

#TabsToolbar {
	background-image: var(--lwt-header-image), var(--lwt-additional-images);
	background-position: var(--lwt-background-alignment);
	background-repeat: var(--lwt-background-tiling);
}

`
let sss = Cc['@mozilla.org/content/style-sheet-service;1'].getService(Ci.nsIStyleSheetService);
let uri = makeURI('data:text/css;charset=UTF=8,' + encodeURIComponent(css));
sss.loadAndRegisterSheet(uri, sss.AGENT_SHEET);

// We move the elements here
bottomBox.appendChild(tabsParent);
document.body.appendChild(bottomFSTogglr);
document.body.appendChild(bottomBox);