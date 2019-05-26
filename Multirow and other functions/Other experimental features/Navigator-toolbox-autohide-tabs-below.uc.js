// ==UserScript==
// @name           Navigator-toolbox-autohide-tabs-below.uc.js
// @namespace      http://https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme
// @description    Makes the navigation toolbar autohide even when not on fullscreen (tabs positioned below urlbar).
// @include        main
// @compatibility  Firefox 69
// @author         Izheil
// @version        25/05/2019 08:23 Fixed a compatibility issue with Firefox 67+
// @version        04/02/2019 19:40 Fixed some issue with ghost elements of the navigator box appearing when hidden
// @version        03/02/2019 19:35 Rewrote the code to use more javascript instead of pure CSS
// @version        02/02/2019 03:34 Included a fix for tabs-below to be compatible with autohide
// @version        02/02/2019 22:48 Gave a bigger toggler space for autohide on resized window
// @version        01/02/2019 22:48 Revised version to hide all content inside the navigation bar
// @version        31/01/2019 10:32 First version
// ==/UserScript==
// We define all variables first
var navBox = document.getElementById("navigator-toolbox"),
  fsToggler = document.getElementById("fullscr-toggler");

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

// This shows the navigation bar when hovering over the fullscr-toggler element (div on top of screen)
fsToggler.onmouseover = function() {
  navBox.style.visibility = "visible";
  navBox.style.opacity = "1";
  fsToggler.style.display = "none";

  var bookmarkItems = document.querySelectorAll("#PlacesToolbarItems .bookmark-item");
      for (var i = 0; i < bookmarkItems.length; i++) {
        bookmarkItems[i].style.visibility = "visible";
      }
}

// This hides the navigation bar when hovering over the web area
document.getElementById("browser").onmouseover = function() {
    navBox.style.visibility = "collapse";
    navBox.style.opacity = "0";
    fsToggler.style.display = "block";
    fsToggler.style.height = "20px";
}