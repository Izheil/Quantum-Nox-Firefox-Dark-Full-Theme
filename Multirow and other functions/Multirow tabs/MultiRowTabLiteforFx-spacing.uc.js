// ==UserScript==
// @name           MultiRowTabLiteforFx-spacing.uc.js
// @namespace      http://space.geocities.yahoo.co.jp/gl/alice0775
// @description    Multi-row tabs draggability fix, Experimental CSS version
// @include        main
// @compatibility  Firefox 69
// @author         Alice0775, Endor8, TroudhuK, Izheil
// @version        06/09/2019 23:37 Fixed issue with tabs when moving to another window
// @version        06/09/2019 11:33 Some fixes to paliate the lower row start space glitch
// @version        05/09/2019 23:22 Released the first version of the alternative multirow
// ==/UserScript==
    zzzz_MultiRowTabLite();
function zzzz_MultiRowTabLite() {
    var css =`
    /* MULTIROW TABS CSS */
    /* 
     - For tab minimum width, you have to go to about:config and modify [browser.tabs.tabMinWidth] 
       to the value you want.

     - For tab growth v 
        Value of 1 -> Tab grows. Fixed max width of 226px.
        Value of 0 -> Tab doesn't grow. Uses tab min width as fixed width. */

    :root {
        --tab-growth: 1}

    .tabbrowser-tab:not([pinned]) {
        flex-grow: var(--tab-growth);
        transition: transform 0.1s !important}
    
    .tabbrowser-tab::after {border: none !important}
    
    :root:-moz-lwtheme[lwtheme-image] {background-repeat: repeat-y !important}

    #tabbrowser-tabs .tab-background{
        max-height: var(--tab-min-height) !important;
        min-height: var(--tab-min-height) !important}

    @media (-moz-os-version: windows-win10) {
        #tabbrowser-tabs .tab-background, #tabbrowser-tabs .tabbrowser-tab {
            min-height: calc(var(--tab-min-height) + 1px) !important}
        }

    /* This fix is intended for some updates when the tab line gets chopped on top of screen 
    #main-window[sizemode="normal"] .tabbrowser-tab .tab-line,
    #main-window[sizemode="maximized"] .tabbrowser-tab .tab-line, 
    #main-window[sizemode="fullscreen"] .tabbrowser-tab .tab-line {transform: translate(0,1px) !important}
    */
    
    #tabbrowser-tabs {margin-top: 0px !important}

    .tab-stack {width: 100%}

    #tabbrowser-tabs .arrowscrollbox-scrollbox {
        display: flex;
        flex-wrap: wrap;}

    #tabbrowser-tabs .tabbrowser-arrowscrollbox {
        overflow: visible;
        display: block}

    :root[uidensity="touch"] .tabbrowser-tab,
    :root[uidensity="touch"] .tab-stack {   
        min-height: calc(var(--tab-min-height) + 3px) !important;
        max-height: calc(var(--tab-min-height) + 3px) !important;
        margin-bottom: 0 !important}

    :root[uidensity="touch"] #tabbrowser-tabs .arrowscrollbox-scrollbox {
        min-height: var(--tab-min-height) !important;}

    .arrowscrollbox-overflow-start-indicator,
    .arrowscrollbox-overflow-end-indicator {position: fixed !important}

    @media (-moz-os-version: windows-win10) {
    .titlebar-buttonbox, #titlebar-buttonbox {display: block !important; height:var(--tab-min-height) !important}}

    #tabbrowser-tabs .scrollbutton-up, #tabbrowser-tabs .scrollbutton-down, #alltabs-button, 
    :root:not([customizing]) #TabsToolbar #new-tab-button, .tabbrowser-tab::after
    {display: none}
    `;
    var sss = Cc['@mozilla.org/content/style-sheet-service;1'].getService(Ci.nsIStyleSheetService);
    var uri = makeURI('data:text/css;charset=UTF=8,' + encodeURIComponent(css));
    sss.loadAndRegisterSheet(uri, sss.AGENT_SHEET);
    gBrowser.tabContainer._getDropIndex = function(event, isLink) {
        var tabs = document.getElementsByClassName("tabbrowser-tab")
        var tab = this._getDragTargetTab(event, isLink);
        if (window.getComputedStyle(this).direction == "ltr") {
            for (let i = tab ? tab._tPos : 0; i < tabs.length; i++) {
                let rect = tabs[i].getBoundingClientRect();
                if (event.clientX < rect.x + rect.width / 2
                 && event.clientY < rect.y + rect.height) // multirow fix
                    return i;
            }
        } else {
            for (let i = tab ? tab._tPos : 0; i < tabs.length; i++) {
                let rect = tabs[i].getBoundingClientRect();
                if (event.clientX > rect.x + rect.width / 2
                 && event.clientY < rect.y + rect.height) // multirow fix
                    return i;
            }
        }
        return tabs.length;
    };

// This scrolls down to the current tab when you open a new one, or restore a session.
function scrollToView() {
    var selTab = document.querySelectorAll(".tabbrowser-tab[selected='true']")[0];
    selTab.scrollIntoView({behavior: "smooth", block: "nearest", inline: "nearest"});
}

gBrowser.tabContainer.addEventListener('TabOpen', scrollToView, false);
gBrowser.tabContainer.addEventListener("TabSelect", scrollToView, false);
document.addEventListener("SSTabRestoring", scrollToView, false);

// This sets when to apply the fix (by default a new row starts after the 23th open tab, unless you changed the min-size of tabs)
gBrowser.tabContainer.ondragstart = function(){if(gBrowser.tabContainer.clientHeight > document.getElementsByClassName("tabbrowser-tab")[0].clientHeight) {
    var tabs = document.getElementsByClassName("tabbrowser-tab");
    var selTab = document.querySelectorAll(".tabbrowser-tab[selected='true']")[0];
    var selIndex = selTab._tPos;

    gBrowser.tabContainer._getDropEffectForTabDrag = function(event){return "";}; // multirow fix: to make the default "dragover" handler do nothing
    gBrowser.tabContainer._onDragOver = function(event) {
        event.preventDefault();
        event.stopPropagation();

        var effects = orig_getDropEffectForTabDrag(event);
        if (effects == "link") {
            let tab = this._getDragTargetTab(event, true);
            if (tab) {
                if (!this._dragTime)
                    this._dragTime = Date.now();
                if (!tab.hasAttribute("pendingicon") && // annoying fix
                    Date.now() >= this._dragTime + this._dragOverDelay)
                    this.selectedItem = tab;
                return;
            }
        }

        var newIndex = this._getDropIndex(event, effects == "link");
        if (newIndex == null)
            return

        // These loops change the behaviour of the dragging to imitate firefox default one
        for (let i = 0; i < tabs.length; i++) {
            tabs[i].style.transform = "initial";
        }
        
        var newTab = document.getElementsByClassName("tabs-newtab-button")[0];

        newTab.style.display = "none";
        selTab.style.opacity = 0;

        if (selIndex > newIndex) {
            for (let i = selIndex; i < tabs.length; i++) {
                tabs[i].style.transform = "initial";
            }
            for (let i = newIndex; i < selIndex; i++) {
                let tabrect = tabs[i].getBoundingClientRect();
                tabs[i].style.transform = "translate(" + tabrect.width + "px," + 0 + ")";
                }
        } else if (selIndex == newIndex) {
            for (let i = 0; i < tabs.length; i++) {
                tabs[i].style.transform = "initial";
            }
            selTab.style.display = "block"}
          else {
            for (let i = 0; i < selIndex; i++) {
                tabs[i].style.transform = "initial";
            }
            for (let i = selIndex; i < newIndex; i++) {
                let tabrect = tabs[i].getBoundingClientRect();
                tabs[i].style.transform = "translate(" + (tabrect.width * -1) + "px," + 0 + ")";
                }
            }
        }
    }

    gBrowser.tabContainer.addEventListener("dragover", gBrowser.tabContainer._onDragOver, true);

    // This prevents the fix from leaving the tab invisible if exiting tab dragging 
    // before dropping the tab
    gBrowser.tabContainer.ondragend = function(event) {
        var tabs = document.getElementsByClassName("tabbrowser-tab");
        var newTab = document.getElementsByClassName("tabs-newtab-button")[0];

        newTab.style.display = "block";
        for (let i = 0; i < tabs.length; i++) {
            tabs[i].style.transform = "initial";
            tabs[i].style.opacity = 1;
        }
    }

    gBrowser.tabContainer.onDrop = function(event) {
        var tabs = document.getElementsByClassName("tabbrowser-tab");
        var selTab = document.querySelectorAll(".tabbrowser-tab[selected='true']")[0];
        var newTab = document.getElementsByClassName("tabs-newtab-button")[0];

        // This resets tab display to default after tab moving animation
        newTab.style.display = "block";
        for (let i = 0; i < tabs.length; i++) {
            tabs[i].style.transform = "initial";
            tabs[i].style.opacity = 1;
        }
        var newIndex;
        var dt = event.dataTransfer;
        var dropEffect = dt.dropEffect;
        var draggedTab;
        let movingTabs;
        if (dt.mozTypesAt(0)[0] == TAB_DROP_TYPE) {
            draggedTab = dt.mozGetDataAt(TAB_DROP_TYPE, 0);
            if (!draggedTab) {
              return;
            }
            movingTabs = draggedTab._dragData.movingTabs;
            draggedTab.container._finishGroupSelectedTabs(draggedTab);
        }
        if (draggedTab && dropEffect == "copy") {}
        else if (draggedTab && draggedTab.container == this) {
            newIndex = this._getDropIndex(event, false);
            if (newIndex > draggedTab._tPos)
                newIndex--;
            gBrowser.moveTabTo(draggedTab, newIndex);
        }
    };
    gBrowser.tabContainer.addEventListener("drop", function(event){this.onDrop(event);}, true);
}};

// copy of the original and overrided _getDropEffectForTabDrag method
function orig_getDropEffectForTabDrag(event) {
      var dt = event.dataTransfer;

      let isMovingTabs = dt.mozItemCount > 0;
      for (let i = 0; i < dt.mozItemCount; i++) {
        // tabs are always added as the first type
        let types = dt.mozTypesAt(0);
        if (types[0] != TAB_DROP_TYPE) {
          isMovingTabs = false;
          break;
        
        }}
      if (isMovingTabs) {
        let sourceNode = dt.mozGetDataAt(TAB_DROP_TYPE, 0);
        if (
          sourceNode instanceof XULElement &&
          sourceNode.localName == "tab" &&
          sourceNode.ownerGlobal.isChromeWindow &&
          sourceNode.ownerDocument.documentElement.getAttribute("windowtype") ==
            "navigator:browser" &&
          sourceNode.ownerGlobal.gBrowser.tabContainer == sourceNode.container
        ) {
          // Do not allow transfering a private tab to a non-private window
          // and vice versa.
          if (
            PrivateBrowsingUtils.isWindowPrivate(window) !=
            PrivateBrowsingUtils.isWindowPrivate(sourceNode.ownerGlobal)
          ) {
            return "none";}

          if (
            window.gMultiProcessBrowser !=
            sourceNode.ownerGlobal.gMultiProcessBrowser
          ) {
            return "none";}

          return dt.dropEffect == "copy" ? "copy" : "move";
        }}

      if (browserDragAndDrop.canDropLink(event)) {
        return "link";}
      return "none";}