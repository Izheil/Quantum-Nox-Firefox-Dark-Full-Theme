(function() {
    var css =`
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
	max-width: 14px !important;
	min-width: 14px !important;

	background: linear-gradient(to right, #222, #444) !important;
	background-size: 14px 14px !important;
	background-repeat: repeat-y !important;
	background-position: 50% 0% !important;
	cursor: default;
}

scrollbar[orient="horizontal"] {
	margin-top: 0px !important;
	max-height: 14px !important;
	min-height: 14px !important;
  
	background: linear-gradient(#222, #444) !important;
	background-size: 14px 14px !important;
	background-repeat: repeat-x  !important;
	background-position: 0% 50% !important;
	cursor: default;
}

scrollbar thumb[orient="vertical"] {
	min-height: 28px !important;
	width: 14px !important;
	min-width: 14px !important;
	max-width: 14px !important;
}

scrollbar thumb[orient="horizontal"] {
	min-width: 32px !important;
	height: 14px !important;
	min-height: 14px !important;
	max-height: 14px !important;
}

scrollbar thumb {
	border-radius: 6px !important;
	background: transparent !important;
	border: 2px solid rgba(0,255,255,0) !important;
	box-shadow: 0 0 0 8px #888 inset !important;
	opacity: 1 !important; 
}

scrollbar:hover thumb,
scrollbar thumb:active {
	box-shadow: 0 0 0 8px #c60 inset !important;
}

scrollbar thumb:active {
	background: #c60 !important;
}

scrollcorner {
	background-image: radial-gradient(at top left, #222, #444);
	background-color: #444 !important;
}

/* no buttons */
scrollbar scrollbarbutton{
	min-height: 0px !important;
	min-width: 0px !important;
	max-height: 14px !important;
	max-width: 14px !important;
	height: 0px !important;
	width: 0px !important;
}`;

    var sss = Cc['@mozilla.org/content/style-sheet-service;1'].getService(Ci.nsIStyleSheetService);
    var uri = makeURI('data:text/css;charset=UTF=8,' + encodeURIComponent(css));
    sss.loadAndRegisterSheet(uri, sss.AGENT_SHEET);
})();
