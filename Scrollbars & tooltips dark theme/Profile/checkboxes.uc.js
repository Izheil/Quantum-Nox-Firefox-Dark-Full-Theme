(function() {
    var css =`
/* Fix for OS's (like default windows) that draws checkboxes and radio buttons whiteish */
dialog select, dialog checkbox .checkbox-check, dialog radio .radio-check {
  filter: invert(81%) hue-rotate(170deg) !important}

@-moz-document url-prefix(moz-extension://), url-prefix(about:) {
select:not(#excludedDomainsBox):not(.form-control), input[type="checkbox"], input[type="radio"], input[type="number"], checkbox .checkbox-check, 
radio .radio-check {filter: invert(81%) hue-rotate(170deg) !important}}

@-moz-document url-prefix(https://addons.mozilla.org) {
input[type="checkbox"], input[type="radio"], input[type="number"], checkbox .checkbox-check, 
radio .radio-check {filter: invert(81%) hue-rotate(170deg) !important}

#lang-picker {
	filter: invert(75%) !important;
	border: 1px solid #ddd !important;
	fill: #000 !important}
}
`;

    var sss = Cc['@mozilla.org/content/style-sheet-service;1'].getService(Ci.nsIStyleSheetService);
    var uri = makeURI('data:text/css;charset=UTF=8,' + encodeURIComponent(css));
    sss.loadAndRegisterSheet(uri, sss.AGENT_SHEET);
})();
