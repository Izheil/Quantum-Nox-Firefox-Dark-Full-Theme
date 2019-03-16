// ==UserScript==
// @name           Mac-fullscreen-fix-toolbox-autohide.uc.js
// @namespace      http://https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme
// @description    Makes the navigation toolbar autohide when on fullscreen even on Mac. Windows and Linux users don't need this.
// @include        main
// @compatibility  Firefox 65
// @author         Izheil
// @version        17/03/2019 00:28 First release
// ==/UserScript==

// We define all variables first
var navBox = document.querySelectorAll("#navigator-toolbox[inFullscreen='true']")[0],
	fsToggler = document.getElementById("fullscr-toggler");

// This shows the navigation bar when hovering over the fullscr-toggler element (div on top of screen)
fsToggler.onmouseover = function() {
	navBox.style.visibility = "visible";
	navBox.style.opacity = "1";
	fsToggler.style.display = "none";
}

// This hides the navigation bar when hovering over the web area
document.getElementById("browser").onmouseover = function() {
  	navBox.style.visibility = "collapse";
  	navBox.style.opacity = "0";
    fsToggler.style.display = "block";
    fsToggler.style.height = "1px";
}
