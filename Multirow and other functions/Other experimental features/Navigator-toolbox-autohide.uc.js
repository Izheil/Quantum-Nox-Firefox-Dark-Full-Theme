// ==UserScript==
// @name           Navigator-toolbox-autohide.uc.js
// @namespace      http://https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme
// @description    Makes the navigation toolbar autohide even when not on fullscreen.
// @include        main
// @compatibility  Firefox 65
// @author         Izheil
// @version        03/02/2019 19:40 Fixed some issue with ghost elements of the navigator box appearing when hidden
// @version        03/02/2019 19:34 Rewrote the code on Javascript only
// @version        02/02/2019 22:48 Gave a bigger toggler space for autohide on resized window
// @version        01/02/2019 22:48 Revised version to hide all content inside the navigation bar
// @version        31/01/2019 10:32 First version
// ==/UserScript==

// We define all variables first
var navBox = document.getElementById("navigator-toolbox"),
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
    fsToggler.style.height = "10px";
}
