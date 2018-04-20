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
	max-width: 16px !important;
	min-width: 16px !important;

	background: linear-gradient(rgba(175,175,175,0.2), rgba(175,175,175,0.2)) !important;
	background-size: 1px 1px !important;
	background-repeat: repeat-y !important;
	background-position: 50% 0% !important;
	cursor: default;
}

scrollbar[orient="horizontal"] {
	margin-top: 0px !important;
	max-height: 16px !important;
	min-height: 16px !important;
  
	background: linear-gradient(rgba(175,175,175,0.2), rgba(175,175,175,0.2)) !important;
	background-size: 1px 1px !important;
	background-repeat: repeat-x  !important;
	background-position: 0% 50% !important;
	cursor: default;
}

scrollbar thumb[orient="vertical"] {
	min-height: 32px !important;
	width: 16px !important;
	min-width: 16px !important;
	max-width: 16px !important;
}

scrollbar thumb[orient="horizontal"] {
	min-width: 32px !important;
	height: 16px !important;
	min-height: 16px !important;
	max-height: 16px !important;
}

scrollbar thumb {
	border-radius: 6px !important;
	background: transparent !important;
	border: 2px solid rgba(0,255,255,0) !important;
	box-shadow: 0 0 0 8px #888 inset !important;
	transition: all 0.4s !important; 
	opacity: 1 !important; 
}

scrollbar:hover thumb,
scrollbar thumb:active {
	box-shadow: 0 0 0 8px #2f832f inset !important;
}

scrollbar thumb:active {
	background: #2f832f !important;
}

scrollcorner {
	background-color: transparent !important;
	border-top: 1px solid rgba(175,175,175,0.2);
	border-left: 1px solid rgba(175,175,175,0.2);
}

/* no buttons */
scrollbar scrollbarbutton{
	min-height: 0px !important;
	min-width: 0px !important;
	max-height: 16px !important;
	max-width: 16px !important;
	height: 0px !important;
	width: 0px !important;
}`;

    var sss = Cc['@mozilla.org/content/style-sheet-service;1'].getService(Ci.nsIStyleSheetService);
    var uri = makeURI('data:text/css;charset=UTF=8,' + encodeURIComponent(css));
    sss.loadAndRegisterSheet(uri, sss.AGENT_SHEET);
})();
