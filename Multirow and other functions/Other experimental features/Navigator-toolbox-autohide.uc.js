// ==UserScript==
// @name           Navigator-toolbox-autohide.uc.js
// @namespace      http://https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme
// @description    Makes the navigation toolbar autohide even when not on fullscreen.
// @include        main
// @compatibility  Firefox 65
// @author         Izheil
// @version        02/02/2019 22:48 Gave a bigger toggler space for autohide on resized window
// @version        01/02/2019 22:48 Revised version to hide all content inside the navigation bar
// @version        31/01/2019 10:32 First version
// ==/UserScript==
document.getElementById("fullscr-toggler").onmouseover = function() {
    var css =`
      #navigator-toolbox > *:not(#nav-bar) {visibility: visible !important}
      #main-window[sizemode="maximized"] #nav-bar,
      #main-window[sizemode="fullscreen"] #nav-bar,
      #main-window[sizemode="normal"] #nav-bar {margin-top: 0 !important}
      #fullscr-toggler {display: none !important}`;
    var sss = Cc['@mozilla.org/content/style-sheet-service;1'].getService(Ci.nsIStyleSheetService);
    var uri = makeURI('data:text/css;charset=UTF=8,' + encodeURIComponent(css));
    sss.loadAndRegisterSheet(uri, sss.AGENT_SHEET);
}

// You may need to change these margins if you are using an older windows version.
document.getElementById("browser").onmouseover = function() {
    var css =`
      #navigator-toolbox > *:not(#nav-bar) {visibility: collapse !important}
      #main-window[sizemode="maximized"] #nav-bar {margin-top: -33px !important}
      #main-window[sizemode="fullscreen"] #nav-bar {margin-top: -41px !important}
      #main-window[sizemode="normal"] #nav-bar {margin-top: -38px !important}

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