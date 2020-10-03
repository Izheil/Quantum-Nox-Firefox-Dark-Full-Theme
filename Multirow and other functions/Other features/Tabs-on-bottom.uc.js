// ==UserScript==
// @name           Tabs on bottom of window
// @namespace      https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme
// @description    Moves tabs to the bottom of the window, below the content area
// @include        main
// @compatibility  Firefox 70 to Firefox 83.0a1 (2020-09-22)
// @author         Izheil
// @version        03/10/2020 05:32 Initial release
// ==/UserScript==

// Start of editable area

// You can set if the min/max/resize buttons are visible from the tabs toolbar here
var hideResButtons = true; // Set to false to show the buttons

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
    	};
    };
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

bottomFSTogglr.onmouseover = function() {
	tabsParent.style.marginBottom = "0";
	tabsParent.style.transition = "none";
}

browserContent.onmouseover = function() {
	tabsParent.style.marginBottom = tabsParent.getBoundingClientRect().height * -1 + "px";
	tabsParent.style.transition = "margin 300ms";
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