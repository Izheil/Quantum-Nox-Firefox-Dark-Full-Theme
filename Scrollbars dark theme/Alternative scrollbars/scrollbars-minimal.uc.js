(function() {
    var css =`
scrollbar {
	z-index: 2147483647 !important;
	position: relative !important;
	transition: all 0s !important; 
}

scrollbar,
scrollbar * {
	-moz-appearance: none !important;
	margin: 0px !important;
	padding: 0px !important;
	border: 0px !important;
	box-shadow: none !important;
}

scrollbar[orient="vertical"] {
	-moz-margin-start: 0px !important;
	max-width: 12px !important;
	min-width: 12px !important;

	background: transparent !important;
	background-size: 12px 12px !important;
	background-repeat: repeat-y !important;
	background-position: 50% 0% !important;
	cursor: default;
}

scrollbar[orient="horizontal"] {
	margin-top: 0px !important;
	max-height: 12px !important;
	min-height: 12px !important;
  
	background: transparent !important;
	background-size: 12px 12px !important;
	background-repeat: repeat-x  !important;
	background-position: 0% 50% !important;
	cursor: default;
}

scrollbar thumb[orient="vertical"] {
	min-height: 24px !important;
	width: 12px !important;
	min-width: 12px !important;
	max-width: 12px !important;
}

scrollbar thumb[orient="horizontal"] {
	min-width: 24px !important;
	height: 12px !important;
	min-height: 12px !important;
	max-height: 12px !important;
}

scrollbar thumb {
	border-radius: 6px !important;
	background: transparent !important;
	border: 2px solid rgba(0,255,255,0) !important;
	box-shadow: 0 0 0 8px rgba(100,100,100,0.3) inset !important;
	transition: all 0s !important; 
	opacity: 1 !important; 
}

scrollbar:hover thumb,
scrollbar thumb:active {
	box-shadow: 0 0 0 8px rgba(100,100,100,0.7) inset !important;
	transition: all .3s !important; 
}

scrollbar thumb:active {
	background: rgba(100,100,100,0.7) !important;
}

/* no buttons */
scrollbar scrollbarbutton{
	min-height: 0px !important;
	min-width: 0px !important;
	max-height: 12px !important;
	max-width: 12px !important;
	height: 0px !important;
	width: 0px !important;
}`;

    var sss = Cc['@mozilla.org/content/style-sheet-service;1'].getService(Ci.nsIStyleSheetService);
    var uri = makeURI('data:text/css;charset=UTF=8,' + encodeURIComponent(css));
    sss.loadAndRegisterSheet(uri, sss.AGENT_SHEET);
})();