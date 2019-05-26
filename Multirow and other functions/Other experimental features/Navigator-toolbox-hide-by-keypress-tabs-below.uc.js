// ==UserScript==
// @name           Navigator-toolbox-hide-by-keypress-tabs-below.uc.js
// @namespace      http://https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme
// @description    Makes the navigation toolbar to hide even when not on fullscreen when pressing a key (tabs below urlbar).
// @include        main
// @compatibility  Firefox 69
// @author         Izheil
// @version        26/05/2019 10:51 First version
// ==/UserScript==

// You can edit which key to press below. Make sure to encase the name between "" or '', and end the variable with a comma (,)
// You can't use ctrl, shift, alt, or CMD.
var keyToPress = "F1",

	// We define the non editable variables below
	navBox = document.getElementById("navigator-toolbox"),
	toggled = true;

var css =`
  #nav-bar {-moz-box-ordinal-group: 2 !important}
  #PersonalToolbar {-moz-box-ordinal-group: 1 !important}
  #titlebar {-moz-box-ordinal-group: 3 !important}

  #navigator-toolbox {margin-top: 40px !important}
  /* ^ Change the margin to 10px if you don't want to use the menu bar on top ^ */

  /* This changes the menu bar on top of the screen intead of over the tab bar */
  #toolbar-menubar{
    position: fixed !important; 
    width: 100% !important;
    top: 0 !important;
    margin-top: 7px !important}

  #toolbar-menubar .titlebar-buttonbox-container {
    float: right !important}

  #window-controls {
    position: fixed !important;
    top: 0 !important; 
    right: 0 !important}
    `;
var sss = Cc['@mozilla.org/content/style-sheet-service;1'].getService(Ci.nsIStyleSheetService);
var uri = makeURI('data:text/css;charset=UTF=8,' + encodeURIComponent(css));
sss.loadAndRegisterSheet(uri, sss.AGENT_SHEET);

// Event listener for keypresses
window.addEventListener("keydown", navBoxHideToggle, false);

function navBoxHideToggle(evt) {
if (!window.fullScreen) {
    if (evt.key == keyToPress && toggled == true) {
	 navBox.style.visibility = "collapse";
	 navBox.style.opacity = "0";
	 toggled = false}

	else if (evt.key == keyToPress && toggled == false) {
     navBox.style.visibility = "visible";
     navBox.style.opacity = "1";

     var bookmarkItems = document.querySelectorAll("#PlacesToolbarItems .bookmark-item");
		  for (var i = 0; i < bookmarkItems.length; i++) {
		  	bookmarkItems[i].style.visibility = "visible";
		  }

	 toggled = true}
	}
}