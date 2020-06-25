// ==UserScript==
// @name           Focus-tab-on-hover.uc.js
// @namespace      https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme
// @description    Switches to the tab you hovered over.
// @include        main
// @compatibility  Firefox 73
// @author         Izheil
// @version        06/12/2019 18:27 Fixed some issue with undefined elements
// @version        23/10/2019 02:49 Fixed delay function
// @version        19/10/2019 23:37 Initial release
// ==/UserScript==

// You can set the delay you want for the hover tab to take effect before switching to another tab.
// Use miliseconds (only the number). 1 second = 1000 miliseconds.
var delayBeforeSwitch = DELAYTIME;

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
	if (EvEl != undefined) {
		if (delayBeforeSwitch > 0) {
			var delay;
			delay = setTimeout(function(){
				EvEl.closest("tabs")._selectNewTab(EvEl)
			}, delayBeforeSwitch);
			EvEl.onmouseout = function(){
				clearTimeout(delay);
			}
		} else {
			EvEl.closest("tabs")._selectNewTab(EvEl)
		}
	}
}

gBrowser.tabContainer.addEventListener('mouseover', hoverHandler, false)
