// ==UserScript==
// @name           Navigator-toolbox-hide-by-keypress.uc.js
// @namespace      http://https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme
// @description    Makes the navigation toolbar to hide even when not on fullscreen when pressing a key.
// @include        main
// @compatibility  Firefox 69
// @author         Izheil
// @version        27/05/2019 03:43 Gave variable a more unique name
// @version        26/05/2019 10:19 First version
// ==/UserScript==

// You can edit which key to press below. Make sure to encase the name between "" or '', and end the variable with a comma (,)
// You can't use ctrl, shift, alt, or CMD.
var keyToPress = "F1",

	// We define the non editable variables below
	navBox = document.getElementById("navigator-toolbox"),
	navBoxVisible = true;

// Event listener for keypresses
window.addEventListener("keydown", navBoxHideToggle, false);

function navBoxHideToggle(evt) {
if (!window.fullScreen) {
    if (evt.key == keyToPress && navBoxVisible == true) {
	 navBox.style.visibility = "collapse";
	 navBox.style.opacity = "0";
	 navBoxVisible = false}

	else if (evt.key == keyToPress && navBoxVisible == false) {
     navBox.style.visibility = "visible";
     navBox.style.opacity = "1";

     var bookmarkItems = document.querySelectorAll("#PlacesToolbarItems .bookmark-item");
		  for (var i = 0; i < bookmarkItems.length; i++) {
		  	bookmarkItems[i].style.visibility = "visible";
		  }

	 navBoxVisible = true}
	}
}