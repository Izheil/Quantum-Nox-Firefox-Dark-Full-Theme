(function() {
    var css =`
/* TOOLTIPS */
tooltip, .statuspanel-label {
  -moz-appearance: none !important;
  background: rgba(50,50,50,0.8) !important;
  color: #eee !important;
  border: 1px solid #111 !important;
}`;

    var sss = Cc['@mozilla.org/content/style-sheet-service;1'].getService(Ci.nsIStyleSheetService);
    var uri = makeURI('data:text/css;charset=UTF=8,' + encodeURIComponent(css));
    sss.loadAndRegisterSheet(uri, sss.AGENT_SHEET);
})();
