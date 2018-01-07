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
	max-width: 0px !important;
	min-width: 0px !important;
}

scrollbar[orient="horizontal"] {
	margin-top: 0px !important;
	max-height: 0px !important;
	min-height: 0px !important;
}

scrollbar thumb[orient="vertical"] {
	min-height: 0px !important;
	width: 0px !important;
	min-width: 0px !important;
	max-width: 0px !important;
}

scrollbar thumb[orient="horizontal"] {
	min-width: 0px !important;
	height: 0px !important;
	min-height: 0px !important;
	max-height: 0px !important;
}

scrollbar thumb {
	opacity: 0 !important; 
}


/* no buttons */
scrollbar scrollbarbutton{
	min-height: 0px !important;
	min-width: 0px !important;
	max-height: 0px !important;
	max-width: 0px !important;
	height: 0px !important;
	width: 0px !important;
}`;

    var sss = Cc['@mozilla.org/content/style-sheet-service;1'].getService(Ci.nsIStyleSheetService);
    var uri = makeURI('data:text/css;charset=UTF=8,' + encodeURIComponent(css));
    sss.loadAndRegisterSheet(uri, sss.AGENT_SHEET);
})();