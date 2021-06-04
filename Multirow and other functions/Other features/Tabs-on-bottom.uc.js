// ==UserScript==
// @name           Tabs on bottom of window
// @namespace      https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme
// @description    Moves tabs to the bottom of the window, below the content area
// @include        main
// @compatibility  Firefox 70 to Firefox 83.0a1 (2020-09-22)
// @author         Izheil
// @version        05/10/2020 01:10 Added the option to hide tabs on fullscreen completelly until keypress
// @version        03/10/2020 05:32 Initial release
// ==/UserScript==

// Start of editable area

// You can set if the min/max/resize buttons are visible from the tabs toolbar here
var hideResButtons = true; // Set to false to show the buttons

// You can choose to always hide tabs in fullscreen here to avoid some issues
var hideFSTabs = true; // Set to false to show the tabs on fullscreen

// Choose key combination to show tabs on fullscreen (a max of 2 is allowed, and the first must be Ctrl, Alt, or Shift).
// The first letter of each key must be capital.
// This only makes sense if tabs are hidden on fullscreen (if hideFSTabs == true).
var keysForFSTabs = ["Shift", "T"]; // The default is ["Shift", "T"]

// End of editable area

// We get the tab parent element and the bottom container, among other elements
var tabsParent = document.getElementById("TabsToolbar");
var bottomBox = document.getElementById("browser-bottombox");
var menuParent = document.getElementById("titlebar");
var menuHidden = document.querySelector("#toolbar-menubar[inactive]");
var menuShown = document.querySelector("#toolbar-menubar[autohide='false']");
var menuElement = document.getElementById("toolbar-menubar");
var resizeButtons = document.querySelector("#TabsToolbar > .titlebar-buttonbox-container");
var browserContent = document.getElementById("browser");
var navToolbox = document.getElementById("navigator-toolbox");
var modKeyToggleTabs;
var keyToggleTabs;


if (keysForFSTabs.length == 2) {
	modKeyToggleTabs = keysForFSTabs[0];
	keyToggleTabs = keysForFSTabs[1];
} else {
	keyToggleTabs = keysForFSTabs[0];
}

// We move the elements here
bottomBox.appendChild(tabsParent);

// Hide the unneeded
if (hideResButtons) {
	resizeButtons.style.display = "none";
} 

if (menuHidden) {
	menuParent.setAttribute("inactiveMenu", "true")
}

var observer = new MutationObserver(function(mutations) {
  mutations.forEach(function(mutation) {
    if (mutation.type == "attributes") {
        switch(mutation.attributeName) {
			case "inactive":
				if (document.querySelector("#toolbar-menubar[inactive]")) {
					menuParent.setAttribute("inactiveMenu", "true")
					console.log("hidden")
				} else {
					menuParent.removeAttribute("inactiveMenu");
					console.log("shown")
				}
				break;
		case "autohide":
				if (document.querySelector("#toolbar-menubar[autohide='false']")) {
					menuParent.removeAttribute("inactiveMenu");
					console.log("shown")
				}
				break;
        }
    }
  });
});

observer.observe(menuElement, {
    attributeFilter: ["inactive", "autohide"],
});

// This is the element creation function for the fullscreen toggler on bottom
function addElement(elementTag, elementId) {
    // Adds an element to the document
    var p = document.body;
    var newElement = document.createElement(elementTag);
    newElement.setAttribute('id', elementId);
    p.appendChild(newElement);
}

// Creation of the toggle to show tabs on fullscreen
addElement("hbox", "fullscr-toggler-bottom")
var bottomFSTogglr = document.getElementById("fullscr-toggler-bottom");
var topFSTogglr = document.getElementById("fullscr-toggler");

topFSTogglr.onmouseover = function() {
	navToolbox.style.transition = "none";
}

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
var css = `
#main-window:not([sizemode="fullscreen"]) #titlebar[inactiveMenu] {
	margin-top: -28px !important;
}

#main-window[sizemode="fullscreen"] #fullscr-toggler-bottom {
	display: block;
	position: absolute;
	bottom: 0;
	height: 1px;
	width: 100%;
}

#main-window:not([sizemode="fullscreen"]) #fullscr-toggler-bottom {
	display: none;
}

#main-window[sizemode="fullscreen"] #TabsToolbar, 
#main-window[sizemode="fullscreen"] #navigator-toolbox {
	transition: margin 300ms;
}

#main-window:not([sizemode="fullscreen"]) #TabsToolbar {
	margin-bottom: 0 !important;
}

#TabsToolbar {
	background-image: var(--lwt-header-image), var(--lwt-additional-images);
	background-position: var(--lwt-background-alignment);
	background-repeat: var(--lwt-background-tiling);
}

`
var sss = Cc['@mozilla.org/content/style-sheet-service;1'].getService(Ci.nsIStyleSheetService);
var uri = makeURI('data:text/css;charset=UTF=8,' + encodeURIComponent(css));
sss.loadAndRegisterSheet(uri, sss.AGENT_SHEET);