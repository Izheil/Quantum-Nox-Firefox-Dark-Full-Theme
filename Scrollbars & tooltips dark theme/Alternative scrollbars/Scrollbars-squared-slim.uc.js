(function() {
    var css =`
scrollbar {
	z-index: 2147483647 !important;
	position: relative !important;
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

	background: linear-gradient(to right, #222, #444) !important;
	background-size: 12px 12px !important;
	background-repeat: repeat-y !important;
	background-position: 50% 0% !important;
	cursor: default;
}

scrollbar[orient="horizontal"] {
	margin-top: 0px !important;
	max-height: 12px !important;
	min-height: 12px !important;
  
	background: linear-gradient(to right, #222, #444) !important;
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
	background: transparent !important;
	box-shadow: 0 0 0 8px #666 inset !important;
	opacity: 1 !important;
	transition: 0.5s !important;  
}

scrollbar:hover thumb {
	box-shadow: 0 0 0 8px #888 inset !important;
}

scrollbar thumb:active {
	box-shadow: 0 0 0 8px #444 inset !important;
	transition: 0s !important; 
}

scrollcorner {
	background-image: radial-gradient(at top left, #222, #444);
	background-color: #444 !important;
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
