// ==UserScript==
// @name           Navigator-toolbox-autohide-tabs-below.uc.js
// @namespace      http://https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme
// @description    Makes the navigation toolbar autohide even when not on fullscreen.
// @include        main
// @compatibility  Firefox 65
// @author         Izheil
// @version        02/02/2019 03:34 Included a fix for tabs-below to be compatible with autohide
// @version        02/02/2019 22:48 Gave a bigger toggler space for autohide on resized window
// @version        01/02/2019 22:48 Revised version to hide all content inside the navigation bar
// @version        31/01/2019 10:32 First version
// ==/UserScript==
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

document.getElementById("fullscr-toggler").onmouseover = function() {
    var css =`
      #navigator-toolbox > *:not(#nav-bar), #toolbar-menubar {visibility: visible !important}
      #main-window[sizemode="maximized"] #nav-bar,
      #main-window[sizemode="fullscreen"] #nav-bar,
      #main-window[sizemode="normal"] #nav-bar {margin-top: 0 !important}

      #toolbar-menubar {display: block !important}
      #fullscr-toggler {display: none !important}`;
    var sss = Cc['@mozilla.org/content/style-sheet-service;1'].getService(Ci.nsIStyleSheetService);
    var uri = makeURI('data:text/css;charset=UTF=8,' + encodeURIComponent(css));
    sss.loadAndRegisterSheet(uri, sss.AGENT_SHEET);
}

// You may need to change these margins if you are using an older windows version.
document.getElementById("browser").onmouseover = function() {
    var css =`
      #navigator-toolbox > *:not(#nav-bar), #toolbar-menubar {visibility: collapse !important}
      #main-window[sizemode="maximized"] #nav-bar {margin-top: -73px !important}
      #main-window[sizemode="fullscreen"] #nav-bar {margin-top: -81px !important}
      #main-window[sizemode="normal"] #nav-bar {margin-top: -78px !important}

      #toolbar-menubar {display: none !important}

      #main-window:not([sizemode="normal"]) #fullscr-toggler {
        display: block !important; 
        height: 1px !important}
        
      #main-window[sizemode="normal"] #fullscr-toggler {
        display:block !important; 
        height: 5px !important}`;
    var sss = Cc['@mozilla.org/content/style-sheet-service;1'].getService(Ci.nsIStyleSheetService);
    var uri = makeURI('data:text/css;charset=UTF=8,' + encodeURIComponent(css));
    sss.loadAndRegisterSheet(uri, sss.AGENT_SHEET);
}