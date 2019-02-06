// ==UserScript==
// @name           Bookmarks-toggle.uc.js
// @namespace      http://https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme
// @description    Bookmarks toolbar toggle on keydown
// @include        main
// @compatibility  Firefox 65
// @author         Izheil
// @version        27/12/2018 15:05 Simplified the code
// @version        27/12/2018 15:05 Firefox 64
// ==/UserScript==
window.addEventListener("keydown", bookmarkToggle, false);

// This assumes you have added the "visibility: collapse !important" rule on your userchrome.css for #PersonalToolbar
// If you want them to be toggled by default, change this to true instead.
var toggled = false;

document.getElementById("PersonalToolbar").style.visibility = "collapse";

// If you want to use a combination of keys instead than one, include evt.key == "your key here" with
// a && inclusion (for example evt.key == "F2" && evt.key =="a" would trigger the toggling when both
// F2 and a buttons are pressed). For ctrl, shift, or alt keys, just use evt.ctrlKey, evt.shiftKey, and evt.altKey instead.
function bookmarkToggle(evt) {
	// Input the key you want to use here
    if (evt.key == "F2" && toggled == true) {
	 document.getElementById("PersonalToolbar").style.visibility = "collapse";
	 toggled = false}
	// Input the key you want to use here
	else if (evt.key == "F2" && toggled == false) {
     document.getElementById("PersonalToolbar").style.visibility = "visible";
	 toggled = true}
}


