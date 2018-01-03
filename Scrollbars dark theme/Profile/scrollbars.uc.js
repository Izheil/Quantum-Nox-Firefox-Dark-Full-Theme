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

	background: linear-gradient(to right, #222, #444) !important;
	background-size: 16px 16px !important;
	background-repeat: repeat-y !important;
	background-position: 50% 0% !important;
	cursor: default;
}

scrollbar[orient="horizontal"] {
	margin-top: 0px !important;
	max-height: 16px !important;
	min-height: 16px !important;
  
	background: linear-gradient(#222, #444) !important;
	background-size: 16px 16px !important;
	background-repeat: repeat-x  !important;
	background-position: 0% 50% !important;
	cursor: default;
}

scrollbar thumb[orient="vertical"] {
	min-height: 32px !important;
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
	transition: all .4s !important; 
	opacity: 1 !important;
}

scrollbar:hover thumb[orient="horizontal"],
scrollbar thumb[orient="horizontal"]:active {
	background: linear-gradient(#46b, #249) !important;
}

scrollbar:hover thumb[orient="vertical"],
scrollbar thumb[orient="vertical"]:active {
	background: linear-gradient(to right, #46b, #249) !important;
}

scrollbar thumb[orient="vertical"]:active {
	max-width: 16px !important;
	width: 16px !important;
	transform: translate(0, 0);
}

scrollbar thumb[orient="horizontal"]:active {
	max-height: 16px !important;
	height: 16px !important;
	transform: translate(0, 0);
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
