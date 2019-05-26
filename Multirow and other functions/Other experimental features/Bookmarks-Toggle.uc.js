// ==UserScript==
// @name           Bookmarks-toggle.uc.js
// @namespace      http://https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme
// @description    Bookmarks toolbar toggle on keydown
// @include        main
// @compatibility  Firefox 69
// @author         Izheil
// @version        26/05/2019 10:19 Added a variable to change the key to press
// @version        25/05/2019 08:14 Added a compatibility fix for Firefox 67+
// @version        27/12/2018 15:05 Simplified the code
// @version        27/12/2018 15:05 Firefox 64
// ==/UserScript==
window.addEventListener("keydown", bookmarkToggle, false);

// If you want them to be visible by default, change this to true instead.
var toggled = false,
// You can edit which key to press below. Make sure to encase the name between "" or '', and end the variable with a semicolon (;)
// You can't use ctrl, shift, alt, or CMD.
	keyPress = "F2";

if (toggled == false) {
	document.getElementById("PersonalToolbar").style.visibility = "collapse";
}

function bookmarkToggle(evt) {
	// Input the key you want to use here
    if (evt.key == keyPress && toggled == true) {
	 document.getElementById("PersonalToolbar").style.visibility = "collapse";
	 toggled = false}
	// Input the key you want to use here
	else if (evt.key == keyPress && toggled == false) {
     document.getElementById("PersonalToolbar").style.visibility = "visible";

     var bookmarkItems = document.querySelectorAll("#PlacesToolbarItems .bookmark-item");
		  for (var i = 0; i < bookmarkItems.length; i++) {
		  	bookmarkItems[i].style.visibility = "visible";
		  }

	 toggled = true}
}


