(function() {
    var css =`
/* TOOLTIPS */
tooltip, .statuspanel-label {
  -moz-appearance: none !important;
  background-color: #333 !important;
  color: #ddd !important;
  border: 1px solid #111 !important;
}`;

    var sss = Cc['@mozilla.org/content/style-sheet-service;1'].getService(Ci.nsIStyleSheetService);
    var uri = makeURI('data:text/css;charset=UTF=8,' + encodeURIComponent(css));
    sss.loadAndRegisterSheet(uri, sss.AGENT_SHEET);
})();
