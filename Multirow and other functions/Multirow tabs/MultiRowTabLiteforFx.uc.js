// ==UserScript==
// @name           Unlimited rows of tabs
// @namespace      https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme
// @description    Multi-row tabs draggability fix with unlimited rows
// @include        main
// @compatibility  Firefox 70 to Firefox 141
// @author         Alice0775, Endor8, TroudhuK, Izheil, Merci-chao
// @version        11/01/2025 01:59 Fixed pinned tabs with Firefox 142.0a1 (2025-06-29)+
// @version        30/04/2025 05:30 Fixed arrowscrollbox selector on FF137+
// @version        04/04/2025 06:56 Fixed issue with Firefox 139.0a1 (2025-04-02)+
// @version        11/01/2025 01:59 Fixed gBrowser issue with Firefox 134+
// @version        13/11/2024 23:13 Fixed issue with Firefox 133+
// @version        07/09/2024 13:25 Compatibility fix for FF131a (Nightly)
// @version        10/05/2023 18:42 Fix tab-growth variable from not applying
// @version        14/01/2023 22:36 Fixed new tab button getting overlapped with last tab
// @version        15/12/2022 22:17 Fixed min/max/close button duplication when having menu bar always visible
// @version        14/12/2022 19:11 Fixed issue with Firefox 108 (Stable)
// @version        21/11/2022 18:38 Fixed issue with Firefox 108a (Nightly)
// @version        15/04/2022 17:58 Fix for duplicated buttons when having titlebar enabled
// @version        12/04/2022 05:40 Min/Max/Close buttons resizing fix
// @version        22/01/2022 16:50 Tab sizing fixes
// @version        02/11/2021 03:15 Made pinned tabs to not have forced Proton sizing
// @version        15/09/2021 11:39 Added experimental support for tab sizing below 20px
// @version        10/09/2021 09:49 Fixed regression of pinned tabs icon showing unaligned
// @version        08/07/2021 07:31 Fixed some issue when having only pinned tabs
// @version        05/06/2021 03:11 Lightweight themes fix
// @version        04/06/2021 04:39 Tab height fix for Proton
// @version        07/03/2021 23:24 Compatibility fix with Simple Tab Groups addon
// @version        12/02/2021 02:18 The new tab button now wont start a new row by itself, and multiple tab selection fixed
// @version        07/12/2020 01:21 Stopped hidding tab right borders since it's not related to multirow
// @version        25/09/2020 23:26 Fixed glitch on opening tabs in the background while on fullscreen
// @version        06/09/2020 18:29 Compatibility fix for Australis and fix for pinned tabs glitch
// @version        28/07/2020 23:28 Compatibility fix for FF81
// @version        04/07/2020 18:20 Added the option to change tab height
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
window.addEventListener("load", () => zzzz_MultiRowTabLite(), false);

// Don't change these
let lastKnownIndex = null;
let lastGroupStart = null;
let lastGroupEnd = null;
let draggedTabIndex = null;

function zzzz_MultiRowTabLite() {
	let css =`
    /* MULTIROW TABS CSS */

    /* EDITABLE CSS VARIABLES */

    /* You can change the tab width here.

     - For tab minimum width, you have to go to about:config and modify [browser.tabs.tabMinWidth] 
       to the value you want. You shouldn't use values lower than 58 for this setting or tabs will
       start to overlap, and scrolling with the wheel will stop working.

     - For tab width growth v 
        Value of 1 -> Tab grows. Fixed max width of 226px.
        Value of 0 -> Tab doesn't grow. Uses tab min width as fixed width.
    */

    :root {
        --tab-growth: 1;
    }

    /* You can change the height of tabs here.

       If you want a more compact view, you can toggle compact mode by setting [browser.compactmode.show] as 
       "true" on about:config, and then turn on compact density on the customize page (right click empty space
       on tab bar -> Customize/personalize toolbar (should be the last option) -> Density select box). 

       Using compact view will make your tabs smaller in height in a more supported way than the variables 
       here can.  
    
       If you want a custom tab height smaller than the default but different than compact view, change the 
       "inherit" value in #TabsToolbar --tab-min-height variable to the value you want. 

       For reference, in Proton, the default heights by density are as follows:
       - Compact mode: 29px
       - Regular mode: 36px
       - Touch mode: 41px
       
       Note that with Proton, when there is media playing, the tab text will appear in 2 lines, and unlike
       with compact mode this won't be changed to fit with a custom height set by this variable, so anything 
       lower than 30px might make the text to go outside the tab area.

       With compact mode enabled on Proton, the min value you should be using for --tab-min-height below is 20px.
       Anything below that will cause issues.
    */

    #TabsToolbar {
        --tab-min-height: inherit !important;
    }

    /*  These below control the padding of the new tab button and min/max/close buttons respectively.
        YOU DON'T NEED TO CHANGE THESE unless you want to use values of --tab-min-height lower than 20px. 
        Before changing them, you need to UNCOMMENT the 2 rules below for them TO TAKE EFFECT. 

        The first rule (#TabsToolbar) controls the padding around the "new tab" button. Make sure to always use "px" 
        as unit for it to work, even on 0 value. Reducing it will allow a lower limit on the tabs height. 
        
        The second rule (.titlebar-buttonbox) has paddings control the padding of the min/max/close buttons. 
        Changing these are required if you want the tab bar to be smaller when having 1 row. */

    #TabsToolbar {
        --toolbarbutton-inner-padding: inherit !important;
    }

    /* Sizing of the titlebar buttons */
    .titlebar-buttonbox {
        height: var(--tab-min-height) !important;
    }

    /*-------- Don't edit past here unless you know what you are doing --------*/
    
    /* These 2 rules are a fix to make sure that tabs become smaller on smaller --tab-min-height values */
    .tabbrowser-tab {
        max-height: calc(var(--tab-min-height) + var(--toolbarbutton-inner-padding)) !important;
    }

    .toolbar-items {-moz-box-align: start !important}

    /* Common multirow code */
    #navigator-toolbox:-moz-lwtheme {
        background-color: var(--toolbar-bgcolor) !important;
    }

    :root[lwtheme-image] #navigator-toolbox {background-repeat: repeat-y !important}

    .tabbrowser-tab:not([pinned]) {
        flex-grow: var(--tab-growth) !important}

    #tabbrowser-tabs .tab-background, #tabbrowser-tabs .tabbrowser-tab {
        min-height: var(--tab-min-height) !important}

    #nav-bar {box-shadow: none !important}
    
	.tab-stack {width: 100%}

    @media (-moz-platform: windows-win10), (-moz-platform: windows-win11) {
        #TabsToolbar .titlebar-buttonbox-container {display: block}
        
        #window-controls > toolbarbutton {
            max-height: calc(var(--tab-min-height) + 8px);
            display: inline;
        }

        #main-window[sizemode="fullscreen"] #window-controls {
            display: flex;
        }
    }

    @media (-moz-platform: windows-win7), (-moz-platform: windows-win8) {
        #tabbrowser-tabs .tabbrowser-tab {
            border-top: none !important}
    }

    /* A fix for pinned tabs triggering another row when only pinned tabs are shown in a row */
    .tabbrowser-tab[pinned] {
        height: calc(var(--tab-min-height) + 8px) !important;
    }

    /* Disable duplicated min/max/close buttons */
    #toolbar-menubar:not([inactive])~#TabsToolbar .titlebar-buttonbox-container {
        width: 0 !important;
    }

    /* This fixes the new tab button overflowing to the new row alone */
    #tabs-newtab-button {
        margin-left: -32px !important} 
        
    .tabbrowser-tab:last-of-type { 
        margin-right: 32px !important}

    /* This fixes issues with tab dragging */
    .tabbrowser-tab[dragtarget] {
        z-index: 1 !important;
        position: initial !important;
    }

    .tabbrowser-tab {
        left: 0 !important;
    }

    #tabbrowser-arrowscrollbox-periphery {
        transform: none !important}

    /* These fix issues with pinned tabs on the overflow status */
    #tabbrowser-tabs[overflow="true"] > #tabbrowser-arrowscrollbox > #tabs-newtab-button,
    #TabsToolbar:not([customizing="true"]) #tabbrowser-tabs[hasadjacentnewtabbutton] > #tabbrowser-arrowscrollbox > #tabs-newtab-button {
        display: inline-flex !important;
    }

    #alltabs-button, #tabs-newtab-button .new-tab-popup, 
    #TabsToolbar:not([customizing="true"]) #tabbrowser-tabs[hasadjacentnewtabbutton] ~ #new-tab-button 
    {display: none}

    #tabbrowser-tabs, #tabbrowser-arrowscrollbox, .tabbrowser-tab[style^="margin-inline-start"], 
    #tabbrowser-tabs[positionpinnedtabs] > #tabbrowser-arrowscrollbox > .tabbrowser-tab[pinned] {
        margin-inline-start: 0 !important;
    }

    #tabbrowser-tabs[positionpinnedtabs] > #tabbrowser-arrowscrollbox > .tabbrowser-tab[pinned] {
        position: initial !important;
    }

    #tabbrowser-tabs[positionpinnedtabs] {
        padding-inline-start: 0 !important;
    }

    /* Remove duplicated min/max/close buttons */
    #nav-bar > .titlebar-buttonbox-container {
        display: none !important;
    }

    #TabsToolbar .titlebar-buttonbox-container {
        display: block !important;
    }

	`;

    // We check if using australis here
    let australisElement = getComputedStyle(document.getElementsByClassName("tabbrowser-tab")[0])
                           .getPropertyValue('--svg-before-normal-density');

    if (australisElement == null) {
        australisElement = getComputedStyle(document.querySelector(":root"))
                           .getPropertyValue('--svg-selected-after');
    }

    // Here the FF71+ changes
    let style = document.createElement('style');
    let arrowScrollbox = resolveTabsContainer();

    // Fix pinned tabs past FF141+
    const pinnedTabsContainer = document.getElementById("pinned-tabs-container");
    if (pinnedTabsContainer) {
        const pinnedObserver = new MutationObserver((mutationList) => {
            for (const mutation of mutationList) {
                migratePinnedTabs(arrowScrollbox, mutation.addedNodes);
            }
        });
        pinnedObserver.observe(pinnedTabsContainer, { childList: true });

        document.getElementById("context_unpinTab").addEventListener("click", moveUnpinnedTabsAfterPinned, false);
        document.getElementById("context_unpinSelectedTabs").addEventListener("click", moveUnpinnedTabsAfterPinned, false);
    }

	if (arrowScrollbox.shadowRoot) {
        css +=
        `scrollbar, #tab-scrollbox-resizer {-moz-window-dragging: no-drag !important}

        #tabbrowser-tabs > arrowscrollbox {
            overflow: visible;
            display: block;
        `

        // This is a fix for the shadow elements:
        style.innerHTML = `
        .scrollbox-clip {
            overflow: visible;
            display: block}

        scrollbox {
            display: flex;
            flex-wrap: wrap;
            min-height: var(--tab-min-height);
        }

        /* Firefox 131+ fix */
        scrollbox > slot {
            flex-wrap: wrap;
        }

	    .arrowscrollbox-overflow-start-indicator,
	    .arrowscrollbox-overflow-end-indicator {position: fixed !important}

	    .scrollbutton-up, .scrollbutton-down, spacer,
        #scrollbutton-up, #scrollbutton-down {display: none !important}
	    `

        if (australisElement) {
            css += `
            .tabbrowser-tab[first-visible-tab="true"] {
              padding-left: 0 !important;
            }
            `;

            style.innerHTML += `
            scrollbox {
                padding: 0 30px;
            }
            `;
        }

        arrowScrollbox.shadowRoot.appendChild(style);
	} else {
        // Here the FF69-FF70 changes
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

        if (australisElement) {
            css += `
            .tabbrowser-tab[first-visible-tab="true"] {
                padding-left: 0 !important;
            }

            #tabbrowser-tabs .arrowscrollbox-scrollbox {
                padding: 0 30px;
            }
            `;
        }
	}

	let sss = Cc['@mozilla.org/content/style-sheet-service;1'].getService(Ci.nsIStyleSheetService);
	let uri = makeURI('data:text/css;charset=UTF=8,' + encodeURIComponent(css));
	sss.loadAndRegisterSheet(uri, sss.AGENT_SHEET);

    gBrowser.tabContainer._getDropIndex = function(event) {
        let tabToDropAt = getTabFromEventTarget(event, false);
        const tabPos = findIndexOfTab(arrowScrollbox, tabToDropAt);

        if (window.getComputedStyle(this).direction == "ltr") {
            let rect = tabToDropAt.getBoundingClientRect();
            if (event.clientX < rect.x + rect.width / 2)
                return tabPos;
            else 
                return tabPos + 1;
            
        } else {
            let rect = tabToDropAt.getBoundingClientRect();
            if (event.clientX > rect.x + rect.width / 2)
                return tabPos;
            else
                return tabPos + 1;
        }
    };

    // We set this to check if the listeners were added before
    let listenersActive = false;

    // This sets when to apply the fix (by default a new row starts after the 23th open tab, unless you changed the min-size of tabs)
    gBrowser.tabContainer.ondragstart = (event) => {
        const pinnedTabsCount = arrowScrollbox.querySelectorAll(".tabbrowser-tab[newPin]").length;
        draggedTabIndex = findIndexOfTab(arrowScrollbox, getTabFromEventTarget(event, false));
        if(gBrowser.tabContainer.arrowScrollbox.clientHeight > document.getElementsByClassName("tabbrowser-tab")[0].clientHeight || pinnedTabsCount > 0) {

            // Multiple tab select fix
            gBrowser.visibleTabs.forEach(t => t.style.transform = "");
            
            // Event handling
            if (!listenersActive) {
                gBrowser.tabContainer.getDropEffectForTabDrag = (event) => orig_getDropEffectForTabDrag(event);
                gBrowser.tabContainer._getDropEffectForTabDrag = (event) => orig_getDropEffectForTabDrag(event);
                gBrowser.tabContainer.on_dragover = (dragoverEvent) => performTabDragOver(dragoverEvent);
                gBrowser.tabContainer._onDragOver = (dragoverEvent) => performTabDragOver(dragoverEvent);
                gBrowser.tabContainer.ondrop = (dropEvent) => performTabDropEvent(dropEvent);
                listenersActive = true;
            }
        }
    };
}

/**
 * Gets the tab from the event target.
 * @param {*} event The event.
 * @returns The tab if it was part of the target or its parents, otherwise null
 */
function getTabFromEventTarget(event, { ignoreTabSides = false } = {}) {
    let { target } = event;
    if (target.nodeType != Node.ELEMENT_NODE) {
        target = target.parentElement;
    }
    let tab = target?.closest("tab") || target?.closest("tab-group");
    const selectedTab = gBrowser.selectedTab;
    if (tab && ignoreTabSides) {
        let { width, height } = tab.getBoundingClientRect();
        if (
            event.screenX < tab.screenX + width * 0.25 ||
            event.screenX > tab.screenX + width * 0.75 ||
            ((event.screenY < tab.screenY + height * 0.25 ||
                event.screenY > tab.screenY + height * 0.75) &&
                gBrowser.tabContainer.verticalMode)
        ) {
            return selectedTab;
        }
    }
    if (!tab) {
        return selectedTab;
    }
    return tab;
}

/**
 * Performs the tab drag over event.
 * @param {*} event The drag over event.
 */
function performTabDragOver(event) {
    event.preventDefault();
    event.stopPropagation();

    let ind = gBrowser.tabContainer._tabDropIndicator;

    let effects = orig_getDropEffectForTabDrag(event);
    let tab;
    if (effects == "link") {
        tab = getTabFromEventTarget(event, true);
        if (tab) {
            if (!gBrowser.tabContainer._dragTime)
                gBrowser.tabContainer._dragTime = Date.now();
            if (!tab.hasAttribute("pendingicon") && // annoying fix
                Date.now() >= gBrowser.tabContainer._dragTime + gBrowser.tabContainer._dragOverDelay)
                gBrowser.tabContainer.selectedItem = tab;
            ind.hidden = true;
            return;
        }
    }

    if (!tab) {
        tab = getTabFromEventTarget(event, false);
    }
    
    let newIndex = gBrowser.tabContainer._getDropIndex(event);
    if (newIndex == null)
        return;

    // Update the last known index and group position
    lastKnownIndex = newIndex;
    
    if (tab.nodeName == "tab-group" && !lastGroupStart) {
        lastGroupStart = tab.querySelector("tab:first-of-type")._tPos;
        lastGroupEnd = tab.querySelector("tab:last-of-type")._tPos;
    }

    let tabs = document.querySelectorAll("tab");
    let ltr = (window.getComputedStyle(gBrowser.tabContainer).direction == "ltr");
    let rect = gBrowser.tabContainer.arrowScrollbox.getBoundingClientRect();
    let newMarginX, newMarginY;
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
}

/**
 * Performs the tab drop event.
 * @param {*} event The drop event.
 */
function performTabDropEvent(event) {
    let newIndex;
    let dt = event.dataTransfer;
    let dropEffect = dt.dropEffect;
    let draggedTab;
    if (dt.mozTypesAt(0)[0] == TAB_DROP_TYPE) {
        draggedTab = dt.mozGetDataAt(TAB_DROP_TYPE, 0);
        if (!draggedTab) {
            return;
        }
    }

    if (draggedTab && dropEffect != "copy" && draggedTab.container == gBrowser.tabContainer) {
        newIndex = lastKnownIndex;

        /* fix for moving multiple selected tabs and tab groups */
        let selectedTabs = gBrowser.selectedTabs;
        const tabsContainer = resolveTabsContainer();
        let pinnedTabsCount = tabsContainer.querySelectorAll(".tabbrowser-tab[newPin]").length;
        
        if (lastGroupStart) {
            selectedTabs = [draggedTab?.closest("tab-group")];
            if (lastKnownIndex >= lastGroupStart && lastKnownIndex <= lastGroupEnd) {
                newIndex = lastGroupStart;
            } else if (lastKnownIndex == lastGroupEnd + 1) {
                newIndex = lastGroupStart + 1;
            }
        }

        if (selectedTabs[selectedTabs.length - 1] == null)
            newIndex = lastKnownIndex;
        
        if (newIndex > gBrowser.tabContainer.itemCount)
            newIndex = gBrowser.tabContainer.itemCount;
        
        
        // Pin the tab if it wasn't pinned
        if (newIndex < pinnedTabsCount) {
            selectedTabs.forEach(t => {
                if (newIndex > draggedTabIndex) {
                    newIndex--;
                }

                if (t.pinned) {
                    gBrowser.unpinTab(t);
                }

                gBrowser.pinTab(t);
                migratePinnedTabs(tabsContainer, document.querySelectorAll("#pinned-tabs-container .tabbrowser-tab"));
                setTimeout(() => {
                    const tab = tabsContainer.querySelector(`.tabbrowser-tab[newPin]:nth-child(${tabsContainer.querySelectorAll("tab[newPin]").length})`);
                    const tabToMoveAt = tabsContainer.childNodes[newIndex];
                    if (tabToMoveAt == null)
                        tabsContainer.insertBefore(tab, document.getElementById("tabbrowser-arrowscrollbox-periphery"));
                    else
                        tabsContainer.insertBefore(tab, tabToMoveAt);
                }, 10);
            });
        } else {
            selectedTabs.forEach(t => {
                if (t.hasAttribute("newPin")) {
                    t.removeAttribute("newPin");
                }
                gBrowser.moveTabBefore(t, tabsContainer.childNodes[newIndex])
            });
        }

        // Restart global vars
        lastKnownIndex = null;
        lastGroupStart = null;
        lastGroupEnd = null;
    }
}

// copy of the original and overrided _getDropEffectForTabDrag method
function orig_getDropEffectForTabDrag(event) {
    let dt = event.dataTransfer;

    let isMovingTabs = dt.mozItemCount > 0;
    for (let i = 0; i < dt.mozItemCount; i++) {
        // tabs are always added as the first type
        let types = dt.mozTypesAt(0);
        if (types[0] != TAB_DROP_TYPE) {
            isMovingTabs = false;
            break;
        }
    }

    if (isMovingTabs) {
        let sourceNode = dt.mozGetDataAt(TAB_DROP_TYPE, 0);
        if (XULElement.isInstance(sourceNode) &&
            sourceNode.localName == "tab" &&
            sourceNode.ownerGlobal.isChromeWindow &&
            sourceNode.ownerDocument.documentElement.getAttribute("windowtype") ==
            "navigator:browser" &&
            sourceNode.ownerGlobal.gBrowser.tabContainer == sourceNode.container) {
            // Do not allow transfering a private tab to a non-private window
            // and vice versa.
            if (PrivateBrowsingUtils.isWindowPrivate(window) !=
                PrivateBrowsingUtils.isWindowPrivate(sourceNode.ownerGlobal))
                return "none";
        

            if (window.gMultiProcessBrowser !=
                sourceNode.ownerGlobal.gMultiProcessBrowser)
                return "none";
        

            if (window.gFissionBrowser != sourceNode.ownerGlobal.gFissionBrowser)
                return "none";
        

            return dt.dropEffect == "copy" ? "copy" : "move";
        }
    }

    if (Services.droppedLinkHandler.canDropLink(event, true)) 
        return "link";

    return "none";
}

/**
 * The pinned tabs to migrate to the main container.
 * @param {Tab} pinnedTabs 
 */
function migratePinnedTabs(newContainer, pinnedTabs) {
    if (!pinnedTabs || pinnedTabs.length == 0)
        return;
    pinnedTabs.forEach((tab) => {
        tab.setAttribute("newPin", "true");
        let firstUnpinnedTab = newContainer.querySelector(".tabbrowser-tab:not([pinned])");
        if (firstUnpinnedTab)
            newContainer.insertBefore(tab, firstUnpinnedTab);
        else
            newContainer.insertBefore(tab, document.getElementById("tabbrowser-arrowscrollbox-periphery"));
    });
}

/**
 * Returns the current tabs container.
 * @returns {Arrowscrollbox} The arrow scrollbox that contains tabs.
 */
function resolveTabsContainer() {
    let arrowScrollbox = document.querySelector("#tabbrowser-tabs > arrowscrollbox");
    const newScrollbox = document.getElementById("tabbrowser-arrowscrollbox");
    if (newScrollbox) {
        arrowScrollbox = newScrollbox;
    }

    return arrowScrollbox;
}

/**
 * Finds the index of a tab in a parent container.
 * @param {*} tabsContainer The parent container with all tabs.
 * @param {*} tab The tab to calculate the position of.
 * @returns The index of the tab inside the parent container.
 */
function findIndexOfTab(tabsContainer, tab) {
    return Array.prototype.indexOf.call(tabsContainer.childNodes, tab)
}

/**
 * Moves unpinned tabs after pinned tabs.
 */
function moveUnpinnedTabsAfterPinned() {
    const tabsContainer = resolveTabsContainer();
    setTimeout(() => {
        const pinnedTabs = tabsContainer.querySelectorAll(".tabbrowser-tab[pinned]");
        const lastPinnedTab = pinnedTabs[pinnedTabs.length - 1];
        const lastPinnedTabIndex = findIndexOfTab(tabsContainer, lastPinnedTab);

        for (let i = lastPinnedTabIndex; i >= 0; i--) {
            const tab = tabsContainer.childNodes[i];
            tab.style.display = "flex";
            if (!tab.hasAttribute("pinned")) {
                tab.removeAttribute("newPin");
                const lastPinnedIndex = findIndexOfTab(tabsContainer, lastPinnedTab) + 1;
                tabsContainer.insertBefore(tab, tabsContainer.childNodes[lastPinnedIndex]);
            }
        }
    }, 50);
}