// ==UserScript==
// @name           MultiRowTabLiteforFx.uc.js
// @namespace      http://space.geocities.yahoo.co.jp/gl/alice0775
// @description    Multi-row tabs draggability fix, Experimental CSS version
// @include        main
// @compatibility  Firefox 78.0a1 (2020-05-04)
// @author         Alice0775, Endor8, TroudhuK, Izheil
// @version        12/05/2020 13:09 Removed unnecesary selector
// @version        09/04/2020 08:14 Minor fixes for tab line when window is resized
// @version        08/04/2020 04:30 Compatibility fix for FF77
// @version        16/03/2020 05:15 Fixed some issue with tab transitions
// @version        06/03/2020 21:56 Fixed an issue with tab lines and duplicated buttons
// @version        12/02/2020 03:30 Fixed some issue with the min/resize/close buttons
// @version        18/01/2020 02:39 Added a fix for people who always spoof their useragent
// @version        13/01/2020 05:01 Fixed the tab drop indicator on FF72+
// @version        15/11/2019 15:45 Unified FF67+ and FF72 versions
// @version        11/10/2019 18:32 Compatibility fix for FF71
// @version        06/09/2019 23:37 Fixed issue with tabs when moving to another window
// @version        05/09/2019 03:24 Fixed tab draggability to work with FF69
// @version        22/07/2019 19:21 Compatibility fix with Windows 7
// @version        23/03/2019 22:25 Comments on tab width
// @version        09/03/2019 15:38 Fixed compatibility issue with Tab Session Manager addon
// @version        18/02/2019 20:46 Tab line not being fully shown on maximized or fullscreen
// @version        03/02/2019 15:15 Firefox 67
// @version        01/02/2019 23:48 Fixed empty pixel line below tabs
// @version        31/01/2019 10:32 Fixed issue with fullscreen
// @version        30/01/2019 02:05 Fixed issue with a pixel being above the tab bar
// @version        23/11/2018 00:41 Firefox 65
// @version        19/10/2018 07:34 Firefox 62
// @version        11/05/2018 15:05 Firefox 60
// ==/UserScript==
zzzz_MultiRowTabLite();
function zzzz_MultiRowTabLite() {
	var css =`
    /* MULTIROW TABS CSS */
    /* You can set the max number of rows before the scrollbar appears here.

     - For tab minimum width, you have to go to about:config and modify [browser.tabs.tabMinWidth] 
       to the value you want.

     - For tab growth v 
        Value of 1 -> Tab grows. Fixed max width of 226px.
        Value of 0 -> Tab doesn't grow. Uses tab min width as fixed width. */

    :root {
        --tab-growth: 1}

    .tabbrowser-tab:not([pinned]) {
        flex-grow: var(--tab-growth)}
        
    .tabbrowser-tab::after {border: none !important}

    :root:-moz-lwtheme[lwtheme-image] {background-repeat: repeat-y !important}

    #tabbrowser-tabs .tab-background, #tabbrowser-tabs .tabbrowser-tab {
        min-height: var(--tab-min-height) !important}

    #main-window[sizemode="normal"] #TabsToolbar {margin-top: 1px !important}

    #nav-bar {box-shadow: none !important}
    
	.tab-stack {width: 100%}

    #tabbrowser-tabs > arrowscrollbox{
        overflow: visible;
        display: block}

    @media (-moz-os-version: windows-win10) {
        #TabsToolbar .titlebar-buttonbox-container {display: block}
    }

    #alltabs-button, .tabbrowser-tab::after
    {display: none}

	`;

    // Here the FF71+ changes
	if (document.querySelector("#tabbrowser-tabs > arrowscrollbox").shadowRoot) {
	    css +=`
		scrollbar {-moz-window-dragging: no-drag !important}
	    `;

	    // This is a fix for the shadow elements:
	    var style = document.createElement('style');
	    style.innerHTML = `
        scrollbox {
            display: flex;
            flex-wrap: wrap}

	    .arrowscrollbox-overflow-start-indicator,
	    .arrowscrollbox-overflow-end-indicator {position: fixed !important}

	    .scrollbutton-up, .scrollbutton-down, spacer,
        #scrollbutton-up, #scrollbutton-down {display: none !important}
	    `
	    document.querySelector("#tabbrowser-tabs > arrowscrollbox").shadowRoot.appendChild(style);
	} else {
        // Here the FF66-FF70 changes
		css +=`

        #tabbrowser-tabs .scrollbutton-up, #tabbrowser-tabs .scrollbutton-down {
            display: none !important}

		#tabbrowser-tabs .arrowscrollbox-scrollbox {
            display: flex;
            flex-wrap: wrap;}

	    .arrowscrollbox-overflow-start-indicator,
    	.arrowscrollbox-overflow-end-indicator {position: fixed !important}

	    #main-window[tabsintitlebar] #tabbrowser-tabs scrollbar {
	        -moz-window-dragging: no-drag}
	    `;
	}

	var sss = Cc['@mozilla.org/content/style-sheet-service;1'].getService(Ci.nsIStyleSheetService);
	var uri = makeURI('data:text/css;charset=UTF=8,' + encodeURIComponent(css));
	sss.loadAndRegisterSheet(uri, sss.AGENT_SHEET);

    gBrowser.tabContainer._getDropIndex = function(event, isLink) {
        var tabs = document.getElementsByClassName("tabbrowser-tab");
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

// We set this to check if the listeners were added before
var Listeners = false;

// This sets when to apply the fix (by default a new row starts after the 23th open tab, unless you changed the min-size of tabs)
gBrowser.tabContainer.ondragstart = function(){
    if(gBrowser.tabContainer.clientHeight > document.getElementsByClassName("tabbrowser-tab")[0].clientHeight) {

    gBrowser.tabContainer._getDropEffectForTabDrag = function(event){return "";}; // multirow fix: to make the default "dragover" handler do nothing
    gBrowser.tabContainer._onDragOver = function(event) {
        event.preventDefault();
        event.stopPropagation();

        var ind = this._tabDropIndicator;

        var effects = orig_getDropEffectForTabDrag(event);
        if (effects == "link") {
            let tab = this._getDragTargetTab(event, true);
            if (tab) {
                if (!this._dragTime)
                    this._dragTime = Date.now();
                if (!tab.hasAttribute("pendingicon") && // annoying fix
                    Date.now() >= this._dragTime + this._dragOverDelay);
                    this.selectedItem = tab;
                ind.hidden = true;
                return;
            }
        }

        var newIndex = this._getDropIndex(event, effects == "link");
        if (newIndex == null)
            return;

        var tabs = document.getElementsByClassName("tabbrowser-tab");
        var ltr = (window.getComputedStyle(this).direction == "ltr");
        var rect = this.arrowScrollbox.getBoundingClientRect();
        var newMarginX, newMarginY;
        if (newIndex == tabs.length) {
            let tabRect = tabs[newIndex - 1].getBoundingClientRect();
            if (ltr)
                newMarginX = tabRect.right - rect.left;
            else
                newMarginX = rect.right - tabRect.left;
            newMarginY = tabRect.top + tabRect.height - rect.top - rect.height; // multirow fix

            if (CSS.supports("offset-anchor", "left bottom")) // Compatibility fix for FF72+
                newMarginY += rect.height / 2 - tabRect.height / 2;
            
        } else if (newIndex != null || newIndex != 0) {
            let tabRect = tabs[newIndex].getBoundingClientRect();
            if (ltr)
                newMarginX = tabRect.left - rect.left;
            else
                newMarginX = rect.right - tabRect.right;
            newMarginY = tabRect.top + tabRect.height - rect.top - rect.height; // multirow fix

            if (CSS.supports("offset-anchor", "left bottom")) // Compatibility fix for FF72+
                newMarginY += rect.height / 2 - tabRect.height / 2;
        }

        newMarginX += ind.clientWidth / 2;
        if (!ltr)
            newMarginX *= -1;

        ind.hidden = false;

        ind.style.transform = "translate(" + Math.round(newMarginX) + "px," + Math.round(newMarginY) + "px)"; // multirow fix
        ind.style.marginInlineStart = (-ind.clientWidth) + "px";
        };

    gBrowser.tabContainer.onDrop = function(event) {
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

    // We then attach the event listeners for the new functionability to take effect
    if (Listeners == false) {
        gBrowser.tabContainer.addEventListener("dragover", gBrowser.tabContainer._onDragOver, true);
        gBrowser.tabContainer.addEventListener("drop", function(event){this.onDrop(event);}, true);
        Listeners = true;
        }
    }
};}

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
