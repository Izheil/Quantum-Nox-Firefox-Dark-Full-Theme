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
    
	background: linear-gradient(#222, #444) !important;
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
	background: linear-gradient(to right, transparent 0, transparent 1px, #999 1px, #333 11px, transparent 11px, transparent 12px) !important;
}

scrollbar thumb[orient="horizontal"] {
	min-width: 24px !important;
	height: 12px !important;
	min-height: 12px !important;
	max-height: 12px !important;
	background: linear-gradient(transparent 0, transparent 1px, #999 1px, #333 11px, transparent 11px, transparent 12px) !important;
}

scrollbar thumb {
	border-radius: 15px !important;
	opacity: 1 !important;
}

scrollbar:hover thumb[orient="horizontal"],
scrollbar thumb[orient="horizontal"]:active {
	background: linear-gradient(transparent 0, transparent 1px, #46b 1px, #1e2d53 11px, transparent 11px, transparent 12px) !important;
}

scrollbar:hover thumb[orient="vertical"],
scrollbar thumb[orient="vertical"]:active {
	background: linear-gradient(to right, transparent 0, transparent 1px, #46b 1px, #1e2d53 11px, transparent 11px, transparent 12px) !important;
}

scrollbar thumb[orient="vertical"]:active {
	background: linear-gradient(to right, #46b, #172342) !important;
	border-radius: 6px !important;
}

scrollbar thumb[orient="horizontal"]:active {
	background: linear-gradient(#46b, #172342) !important;
	border-radius: 6px !important;
}

/* no buttons */
scrollbar scrollbarbutton{
	min-height: 0px !important;
	min-width: 0px !important;
	max-height: 12px !important;
	max-width: 12px !important;
	height: 0px !important;
	width: 0px !important;
	background: radial-gradient (circle, #888, #555);
}`;

    var sss = Cc['@mozilla.org/content/style-sheet-service;1'].getService(Ci.nsIStyleSheetService);
    var uri = makeURI('data:text/css;charset=UTF=8,' + encodeURIComponent(css));
    sss.loadAndRegisterSheet(uri, sss.AGENT_SHEET);
})();
