// ==UserScript==
// @name           Bookmarks-toolbar-autohide.uc.js
// @namespace      http://https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme
// @description    Autohides Bookmarks toolbar, and only shows it when hovering over the navigation toolbox.
// @include        main
// @compatibility  Firefox 69
// @author         Izheil
// @version        25/05/2019 08:36 First version
// ==/UserScript==

// We define toolbar variables first
var navBox = document.getElementById("navigator-toolbox"),
	BookBox = document.getElementById("PersonalToolbar");

// We set this so that it starts hidden by default.
BookBox.style.visibility = "collapse";

// This shows the bookmarks bar when hovering over the navigation toolbox.
navBox.onmouseover = function() {
	BookBox.style.visibility = "visible";
	bookmarkItems = document.querySelectorAll("#PlacesToolbarItems .bookmark-item");
	  for (var i = 0; i < bookmarkItems.length; i++) {
	  	bookmarkItems[i].style.visibility = "visible";
	  }
}

// This hides the bookmarks bar when hovering over the web area
document.getElementById("browser").onmouseover = function() {
  	BookBox.style.visibility = "collapse";
}
