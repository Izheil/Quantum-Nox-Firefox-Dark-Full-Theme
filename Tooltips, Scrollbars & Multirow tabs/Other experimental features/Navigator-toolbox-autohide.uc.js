// ==UserScript==
// @name           Navigator-toolbox-autohide.uc.js
// @namespace      http://https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme
// @description    Makes the navigation toolbar autohide even when not on fullscreen.
// @include        main
// @compatibility  Firefox 65
// @author         Izheil
// @version        01/31/2019 10:32 First version
// ==/UserScript==
document.getElementById("fullscr-toggler").onmouseover = function() {
    var css =`
      #PersonalToolbar, #titlebar {visibility: visible !important}
      #nav-bar {margin-top: 0 !important}
      #fullscr-toggler {display: none !important}`;
    var sss = Cc['@mozilla.org/content/style-sheet-service;1'].getService(Ci.nsIStyleSheetService);
    var uri = makeURI('data:text/css;charset=UTF=8,' + encodeURIComponent(css));
    sss.loadAndRegisterSheet(uri, sss.AGENT_SHEET);
}

document.getElementById("browser").onmouseover = function() {
    var css =`
      #PersonalToolbar, #titlebar {visibility: collapse !important}
      #nav-bar {margin-top: -33px !important}
      #fullscr-toggler {display: block !important}`;
    var sss = Cc['@mozilla.org/content/style-sheet-service;1'].getService(Ci.nsIStyleSheetService);
    var uri = makeURI('data:text/css;charset=UTF=8,' + encodeURIComponent(css));
    sss.loadAndRegisterSheet(uri, sss.AGENT_SHEET);
}