(function() {
    var css =`
/* Fix for OS's (like default windows) that draws checkboxes and radio buttons whiteish */
select, checkbox .checkbox-check, radio .radio-check {
  filter: invert(81%) hue-rotate(170deg) !important}

@-moz-document url-prefix(http), url-prefix(moz-extension://), url-prefix(about:) {
select, input[type="checkbox"], input[type="radio"], input[type="number"], .checkbox-check, 
.radio-check {
  filter: invert(81%) hue-rotate(170deg) !important}
}
`;

    var sss = Cc['@mozilla.org/content/style-sheet-service;1'].getService(Ci.nsIStyleSheetService);
    var uri = makeURI('data:text/css;charset=UTF=8,' + encodeURIComponent(css));
    sss.loadAndRegisterSheet(uri, sss.AGENT_SHEET);
})();
