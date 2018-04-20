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
	background-color: #888 !important;
	background-image: linear-gradient(to right, rgba(0,0,0,0), rgba(0,0,0,0.7)) !important;
	transform: scale(0.857, 1) translate(0.5px, 0);

}

scrollbar thumb[orient="horizontal"] {
	min-width: 28px !important;
	height: 14px !important;
	min-height: 14px !important;
	max-height: 14px !important;
	background-color: #888 !important;
	background-image: linear-gradient(rgba(0,0,0,0), rgba(0,0,0,0.7)) !important;
	transform: scale(1, 0.857) translate(0, 0.5px);

}

scrollbar thumb {
	border-radius: 15px !important;
	transition: all 0.4s !important;
}

scrollbar:hover thumb[orient="vertical"],
scrollbar:hover thumb[orient="horizontal"] {
	background-color: #46b !important;
}

scrollbar thumb[orient="vertical"]:active,
scrollbar thumb[orient="horizontal"]:active {
	background-color: #46b !important;
	border-radius: 6px !important;
	transform: scale(1, 1) translate(0, 0);
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
