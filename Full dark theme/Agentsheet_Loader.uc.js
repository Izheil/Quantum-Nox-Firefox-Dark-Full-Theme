// ==UserScript==
// @name            AS.CSS files loader
// @include         main
// @author          Haggai Nuchi, ported by Izheil
// @onlyonce
// ==/UserScript==

(function () {
  var chromeFiles = FileUtils.getDir("UChrm", []).directoryEntries;
  var sss = Cc['@mozilla.org/content/style-sheet-service;1'].getService(Ci.nsIStyleSheetService);

  while(chromeFiles.hasMoreElements()) {
      var file = chromeFiles.getNext().QueryInterface(Ci.nsIFile);
      var fileURI = Services.io.newFileURI(file);

      if(file.isFile()) {
          type = "none";
          if(/\.as\.css$/i.test(file.leafName)) {
              type = "agentsheet";
          }
          if(type != "none") {
              console.log("----------\\ " + file.leafName + " (" + type + ")");
              try {
                  if(type == "agentsheet") {
                      if(!sss.sheetRegistered(fileURI, sss.AGENT_SHEET))
                          sss.loadAndRegisterSheet(fileURI, sss.AGENT_SHEET);
                  }
              } catch(e) {
                  console.log("########## ERROR: " + e + " at " + e.lineNumber + ":" + e.columnNumber);
              }
              console.log("----------/ " + file.leafName);
          }
      }
  }
})()
