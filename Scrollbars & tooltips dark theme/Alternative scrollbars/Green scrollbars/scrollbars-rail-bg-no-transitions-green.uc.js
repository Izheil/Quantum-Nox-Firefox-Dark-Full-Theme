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
	background: linear-gradient(to right, transparent 0, transparent 1px, #999 1px, #444 15px, transparent 15px, transparent 16px) !important;
}

scrollbar thumb[orient="horizontal"] {
	min-width: 32px !important;
	height: 16px !important;
	min-height: 16px !important;
	max-height: 16px !important;
	background: linear-gradient(transparent 0, transparent 1px, #999 1px, #444 15px, transparent 15px, transparent 16px) !important;
}

scrollbar thumb {
	border-radius: 15px !important;
}

scrollbar:hover thumb[orient="horizontal"],
scrollbar thumb[orient="horizontal"]:hover {
	background: linear-gradient(transparent 0, transparent 1px, #2f832f 1px, #1b4b1b 15px, transparent 15px, transparent 16px) !important;
}

scrollbar:hover thumb[orient="vertical"],
scrollbar thumb[orient="vertical"]:hover {
	background: linear-gradient(to right, transparent 0, transparent 1px, #2f832f 1px, #1b4b1b 15px, transparent 15px, transparent 16px) !important;
}

scrollbar thumb[orient="vertical"]:active {
	background: linear-gradient(to right, #2f832f, #143814) !important;
	border-radius: 6px !important;
}

scrollbar thumb[orient="horizontal"]:active {
	background: linear-gradient(#2f832f, #143814) !important;
	border-radius: 6px !important;
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
