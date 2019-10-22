// ==UserScript==
// @name           Switch-to-tab-on-hover.uc.js
// @namespace      https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme
// @description    Switches to the tab you hovered over.
// @include        main
// @compatibility  Firefox 69
// @author         Izheil
// @version        19/10/2019 23:37 Initial release
// ==/UserScript==

function getParentByClass(el, className) {
  do {
    if (el.classList.contains(className)) {
      return el;
    } else {
      el = el.parentNode;
    }
  } while (el && el.parentNode)
}

function hoverHandler(e){
	var EvEl = getParentByClass(e.target, "tabbrowser-tab");
	EvEl.addEventListener('mouseover', switchToTab, false);
	setTimeout(function(){EvEl.removeEventListener('mouseover', switchToTab, false);}, 500);
}

function switchToTab(event) {
	  if (event.button != 0 || this.disabled) {
	    return;
	  }
	  
	  this.parentNode.ariaFocusedItem = null;

	  if (this == this.parentNode.selectedItem) {
	    // This tab is already selected and we will fall
	    // through to mousedown behavior which sets focus on the current tab,
	    // Only a click on an already selected tab should focus the tab itself.
	    return;
	  }

	  // Call this before setting the 'ignorefocus' attribute because this
	  // will pass on focus if the formerly selected tab was focused as well.
	  this.closest("tabs")._selectNewTab(this)
	  

	  var isTabFocused = false;
	  try {
	    isTabFocused = document.commandDispatcher.focusedElement == this;
	  } catch (e) {}

	  // Set '-moz-user-focus' to 'ignore' so that PostHandleEvent() can't
	  // focus the tab; we only want tabs to be focusable by the mouse if
	  // they are already focused. After a short timeout we'll reset
	  // '-moz-user-focus' so that tabs can be focused by keyboard again.
	  if (!isTabFocused) {
	    this.setAttribute("ignorefocus", "true");
	    setTimeout(tab => tab.removeAttribute("ignorefocus"), 0, this);
	  }
}

gBrowser.tabContainer.addEventListener('mouseover', hoverHandler, false)
