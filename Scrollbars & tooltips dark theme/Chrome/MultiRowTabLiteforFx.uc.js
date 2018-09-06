// ==UserScript==
// @name           zzzz-MultiRowTabLiteforFx.uc.js
// @namespace      http://space.geocities.yahoo.co.jp/gl/alice0775
// @description    Multi-row tabs draggability fix, Experimental CSS version
// @include        main
// @compatibility  Firefox 61
// @author         Alice0775, Endor8, TroudhuK, Izheil
// @version        2018/20/08 03:05 Fixed some issue with min-width
// @version        2018/11/05 15:05 Firefox 60
// @version        2016/08/05 00:00 Firefox 48
// @version        2016/05/01 00:01 hide favicon if busy
// @version        2016/03/09 00:01 Bug 1222490 - Actually remove panorama for Fx45+
// @version        2016/02/09 00:01 workaround css for lwt
// @version        2016/02/09 00:00
// ==/UserScript==
    zzzz_MultiRowTabLite();
function zzzz_MultiRowTabLite() {
    var css =`
    /* MULTIROW TABS CSS */
    .tabbrowser-tab:not([pinned]) {
        flex-grow:1;
        min-width:100px !important}

    .tabbrowser-tab, .tab-background {height:var(--tab-min-height) !important}

    .tab-stack {width: 100%}

    #tabbrowser-tabs .scrollbox-innerbox {
        display: flex;
        flex-wrap: wrap;}

    #tabbrowser-tabs .arrowscrollbox-scrollbox {
        overflow: visible;
        display: block}

    @media (-moz-os-version: windows-win10) {
    #titlebar-buttonbox {height:var(--tab-min-height) !important}}

    #titlebar {height:var(--tab-min-height) !important}

    #titlebar {margin-bottom:calc(1px + var(--tab-min-height)*-1) !important}

    #main-window[sizemode="maximized"] #titlebar
    {margin-bottom: calc(8px + var(--tab-min-height)*-1)!important}

    #main-window[sizemode="maximized"][uidensity=compact] #titlebar
    {margin-bottom: calc(6px + var(--tab-min-height)*-1)!important}

    .tab-line {height: 2px !important}

    #main-window[sizemode="maximized"] .tab-line {height: 2px !important}

    #titlebar:active {margin-bottom: 0 !important}

    #titlebar:active #titlebar-content {margin-bottom:var(--tab-min-height) !important}

    #tabbrowser-tabs .scrollbutton-up, #tabbrowser-tabs .scrollbutton-down, #alltabs-button, .tabbrowser-tab:not([fadein])
    {display: none}
    `;
    var sss = Cc['@mozilla.org/content/style-sheet-service;1'].getService(Ci.nsIStyleSheetService);
    var uri = makeURI('data:text/css;charset=UTF=8,' + encodeURIComponent(css));
    sss.loadAndRegisterSheet(uri, sss.AGENT_SHEET);
    gBrowser.tabContainer._getDropIndex = function(event, isLink) {
        var tabs = this.childNodes;
        var tab = this._getDragTargetTab(event, isLink);
        if (window.getComputedStyle(this).direction == "ltr") {
        	for (let i = tab ? tab._tPos : 0; i < tabs.length; i++) {
                let boxObject = tabs[i].boxObject;
        		if (event.screenX < boxObject.screenX + boxObject.width / 2
                 && event.screenY < boxObject.screenY + boxObject.height) // multirow fix
        			return i;
            }
        } else {
        	for (let i = tab ? tab._tPos : 0; i < tabs.length; i++) {
                let boxObject = tabs[i].boxObject;
        		if (event.screenX > boxObject.screenX + boxObject.width / 2
                 && event.screenY < boxObject.screenY + boxObject.height) // multirow fix
        			return i;
            }
        }
        return tabs.length;
    };
    // This sets when to apply the fix (by default a new row starts after the 23th open tab, unless you changed the min-size of tabs)
    gBrowser.tabContainer.ondragstart = function(){if(gBrowser.tabContainer.childNodes.length >= (window.innerWidth - 200) / 75) {

    gBrowser.tabContainer._getDropEffectForTabDrag = function(event){return "";}; // multirow fix: to make the default "dragover" handler does nothing
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
        		if (!tab.hasAttribute("pending") && // annoying fix
                    Date.now() >= this._dragTime + this._dragOverDelay)
        			this.selectedItem = tab;
        		ind.collapsed = true;
        		return;
        	}
        }

        var newIndex = this._getDropIndex(event, effects == "link");
        if (newIndex == null)
            return;

        var ltr = (window.getComputedStyle(this).direction == "ltr");
        var rect = this.arrowScrollbox.getBoundingClientRect();
        var newMarginX, newMarginY;
        if (newIndex == this.childNodes.length) {
            let tabRect = this.childNodes[newIndex - 1].getBoundingClientRect();
            if (ltr)
                newMarginX = tabRect.right - rect.left;
            else
                newMarginX = rect.right - tabRect.left;
            newMarginY = tabRect.top + tabRect.height - rect.top - rect.height; // multirow fix
        } else {
            let tabRect = this.childNodes[newIndex].getBoundingClientRect();
            if (ltr)
                newMarginX = tabRect.left - rect.left;
            else
                newMarginX = rect.right - tabRect.right;
            newMarginY = tabRect.top + tabRect.height - rect.top - rect.height; // multirow fix
        }

        ind.collapsed = false;

        newMarginX += ind.clientWidth / 2;
        if (!ltr)
            newMarginX *= -1;

        ind.style.transform = "translate(" + Math.round(newMarginX) + "px," + Math.round(newMarginY) + "px)"; // multirow fix
        ind.style.marginInlineStart = (-ind.clientWidth) + "px";
    };
    gBrowser.tabContainer.addEventListener("dragover", gBrowser.tabContainer._onDragOver, true);

    gBrowser.tabContainer.onDrop = function(event) {
        var newIndex;
        var dt = event.dataTransfer;
        var draggedTab;
        if (dt.mozTypesAt(0)[0] == TAB_DROP_TYPE) {
            draggedTab = dt.mozGetDataAt(TAB_DROP_TYPE, 0);
            if (!draggedTab)
                return;
        }
        var dropEffect = dt.dropEffect;
        if (draggedTab && dropEffect == "copy") {}
        else if (draggedTab && draggedTab.parentNode == this) {
            newIndex = this._getDropIndex(event, false);
            if (newIndex > draggedTab._tPos)
                newIndex--;
            gBrowser.moveTabTo(draggedTab, newIndex);
        }
    };
    gBrowser.tabContainer.addEventListener("drop", function(event){this.onDrop(event);}, true);
}}}

// copy of the original and overrided _getDropEffectForTabDrag method
function orig_getDropEffectForTabDrag(event) {
    var dt = event.dataTransfer;
    if (dt.mozItemCount == 1) {
        var types = dt.mozTypesAt(0);
        // tabs are always added as the first type
        if (types[0] == TAB_DROP_TYPE) {
            let sourceNode = dt.mozGetDataAt(TAB_DROP_TYPE, 0);
            if (sourceNode instanceof XULElement &&
                sourceNode.localName == "tab" &&
                sourceNode.ownerGlobal.isChromeWindow &&
                sourceNode.ownerDocument.documentElement.getAttribute("windowtype") == "navigator:browser" &&
                sourceNode.ownerGlobal.gBrowser.tabContainer == sourceNode.parentNode) {
                // Do not allow transfering a private tab to a non-private window
                // and vice versa.
                if (PrivateBrowsingUtils.isWindowPrivate(window) !=
                    PrivateBrowsingUtils.isWindowPrivate(sourceNode.ownerGlobal))
                    return "none";

                if (window.gMultiProcessBrowser !=
                    sourceNode.ownerGlobal.gMultiProcessBrowser)
                    return "none";

                return dt.dropEffect == "copy" ? "copy" : "move";
            }
        }
    }

    if (browserDragAndDrop.canDropLink(event)) {
        return "link";
    }
    return "none";
}
