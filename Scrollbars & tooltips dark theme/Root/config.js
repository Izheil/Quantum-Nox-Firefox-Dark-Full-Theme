//
/* ***** BEGIN LICENSE BLOCK *****
 * Version: MPL 1.1/GPL 2.0/LGPL 2.1
 *
 * The contents of this file are subject to the Mozilla Public License Version
 * 1.1 (the "License"); you may not use this file except in compliance with
 * the License. You may obtain a copy of the License at
 * http://www.mozilla.org/MPL/
 *
 * Software distributed under the License is distributed on an "AS IS" basis,
 * WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
 * for the specific language governing rights and limitations under the
 * License.
 *
 * The Original Code is the userChrome.js component.
 *
 * The Initial Developer of the Original Code is
 * Simon Bünzli <zeniko@gmail.com>
 *
 * Portions created by the Initial Developer are Copyright (C) 2007
 * the Initial Developer. All Rights Reserved.
 *
 * Contributor(s):
 * alta88 <alta88@gmail.com>
 *
 * Alternatively, the contents of this file may be used under the terms of
 * either the GNU General Public License Version 2 or later (the "GPL"), or
 * the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
 * in which case the provisions of the GPL or the LGPL are applicable instead
 * of those above. If you wish to allow use of your version of this file only
 * under the terms of either the GPL or the LGPL, and not to allow others to
 * use your version of this file under the terms of the MPL, indicate your
 * decision by deleting the provisions above and replace them with the notice
 * and other provisions required by the GPL or the LGPL. If you do not delete
 * the provisions above, a recipient may use your version of this file under
 * the terms of any one of the MPL, the GPL or the LGPL.
 *
 * ***** END LICENSE BLOCK ***** */

try {

/*Components.utils.import("resource://gre/modules/XPCOMUtils.jsm");
*/
Components.utils.import("resource://gre/modules/osfile.jsm");

function UserChrome_js() {
  var os = Components.classes["@mozilla.org/observer-service;1"]
                     .getService(Components.interfaces.nsIObserverService);
  os.addObserver(this, "final-ui-startup", false);
};

UserChrome_js.prototype = {
/*// Properties required for XPCOM registration:
  classDescription: "userChromeJS Loading Component",
  classID         : Components.ID("{8DEB3B5E-7585-4029-B6D0-4733CE8DED50}"),
  contractID      : "@userChromeJS;1",

  _xpcom_categories: [{
    category: "app-startup",
    service: true
  }],
*/
/* ........ QueryInterface .................................................. */
/*
  QueryInterface: XPCOMUtils.generateQI([Components.interfaces.nsISupports,
                                         Components.interfaces.nsIObserver,
                                         Components.interfaces.nsIModule,
                                         Components.interfaces.nsIFactory,
                                         Components.interfaces.nsIDOMEventListener]),
*/
/* ........ nsIObserver ..................................................... */

  observe: function(aSubject, aTopic, aData) {
    var os = Components.classes["@mozilla.org/observer-service;1"]
                       .getService(Components.interfaces.nsIObserverService);

    switch (aTopic) {
/*  case "app-startup":
    case "profile-after-change":
      os.addObserver(this, "final-ui-startup", false);
      break;
*/  case "final-ui-startup":
      var file = Components.classes["@mozilla.org/file/directory_service;1"]
                           .getService(Components.interfaces.nsIProperties)
                           .get("UChrm", Components.interfaces.nsIFile);
      file.append("userChrome.js");
/*
      if (!file.exists()) {
        var componentFile = __LOCATION__;
        var componentsDir = componentFile.parent;
        var extensionDir = componentsDir.parent;
        extensionDir.append("README.txt");
        if (extensionDir.exists())
          extensionDir.copyTo(file.parent, "userChrome.js");
      }
*/
      if (file.exists() && file.isFile() &&
          !Components.classes["@mozilla.org/xre/app-info;1"]
                     .getService(Components.interfaces.nsIXULRuntime)
                     .inSafeMode) {
        this.mFileURL = Components.classes["@mozilla.org/network/io-service;1"]
                                  .getService(Components.interfaces.nsIIOService)
                                  .getProtocolHandler("file")
                                  .QueryInterface(Components.interfaces.nsIFileProtocolHandler)
                                  .getURLSpecFromFile(file);
        var path = OS.Constants.Path.libDir;
        path = OS.Path.join(path, "userChromeJS.js");
        this.uCFileURI = OS.Path.toFileURI(path);

        os.addObserver(this, "domwindowopened", false);
      }
      break;
    case "domwindowopened":
      aSubject.addEventListener("load", this, true);
      break;
    }
  },

/* ........ nsIDOMEventListener ............................................. */

  handleEvent: function(aEvent) {
    var document = aEvent.originalTarget;
    if (document.location && document.location.protocol == "chrome:") {
      try {
        let loader = Components.classes["@mozilla.org/moz/jssubscript-loader;1"]
                               .getService(Components.interfaces.mozIJSSubScriptLoader);
/*
        loader.loadSubScript("chrome://userChromeJS/content/userChromeJS.js",
                             document.defaultView,
                             "UTF-8");
*/
        loader.loadSubScript(this.uCFileURI,
                             document.defaultView,
                             "UTF-8");

        loader.loadSubScript(this.mFileURL,
                             document.defaultView,
                             "UTF-8");
      }
      catch (ex) {
        // script execution can be stopped with |throw "stop";|
        if (ex !== "stop") {
          Components.utils.reportError(ex);
        }
      }
    }
  }

};

/**
 * The following line is what XPCOM uses to create components. Each component
 * prototype must have a .classID which is used to create it.
 *
 * XPCOMUtils.generateNSGetFactory was introduced in Mozilla 2 (Firefox 4).
 */
/*var NSGetFactory = XPCOMUtils.generateNSGetFactory([UserChrome_js]);
*/
new UserChrome_js();

} catch(ex) {
  Components.utils.reportError(ex);
};

