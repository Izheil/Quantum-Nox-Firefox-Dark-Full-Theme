// ==UserScript==
// @name           Scrollable Multirow Tabs
// @namespace      https://github.com/Izheil/Quantum-Nox-Firefox-Customizations
// @description    Multi-row tabs draggability fix with scrollable rows
// @include        main
// @compatibility  Firefox 157 to Firefox 160.0a1 (2026-10-16)
// @author         Alice0775, Endor8, TroudhuK, Izheil, Merci-chao
// @version        16/10/2026 17:40 Fix issue with tab pinning of the last pinned tab.
// @version        30/09/2026 03:03 Fix tab sizing calculation for Nova design.
// @version        22/08/2026 04:20 Fix tab sizing calculation.
// @version        21/08/2026 16:15 Fix issue with group before pinned tabs on session restore.
// @version        29/03/2026 03:58 Fix issue with new button and split view
// @version        15/03/2026 22:05 Add toggle for resizing or not tabs when they have icons
// @version        17/02/2026 23:38 Fix issue with dragging tabs to the end
// @version        12/02/2026 18:40 Fix dragging tabs from a tab group
// @version        03/10/2025 02:59 Fix tab group label showing on move
// @version        01/10/2025 06:15 Fix issues with tab group moving
// @version        27/09/2025 06:40 Fix issues with tab groups
// @version        12/07/2025 00:28 Fix spacing with tab groups and new tab button
// ==/UserScript==
function zzzz_MultiRowTabLite() {
    // EDITABLE JAVASCRIPT VARIABLES

    // Enables the use of the rows resizer
    const useResizer = false;

    // Size of the scrollbar
    // auto = default OS size | thin = half the width | none = always hidden scrollbar
    const scrollbarSize = "auto";

    // Allow tabs resizing when there is an icon (like the sound icon)
    // Only change this if you don't want the tabs to resize when having an icon.
    const allowResizeWithIcon = true;

    // If the new tab button should be hidden
    const hideNewTabBtn = false;

    // CSS section
	let css =`
    /* MULTIROW TABS CSS */

    /* EDITABLE CSS VARIABLES */

    /* You can set the max number of rows before the scrollbar appears and the tab width here.

     - For tab minimum width, you have to go to about:config and modify [browser.tabs.tabMinWidth] 
       to the value you want. You shouldn't use values lower than 58 for this setting or tabs will
       start to overlap, and scrolling with the wheel will stop working.

     - For tab width growth v 
        Value of 1 -> Tab grows. Fixed max width of 226px.
        Value of 0 -> Tab doesn't grow. Uses tab min width as fixed width. 
        (Set the JS variable allowResizeWithIcon to false if you don't want tabs to resize when 
        having icons as well).
        
     - To change the color or width of the resizer, change the --resizer-* variables to any other 
       value you want. (like #666 for color or 5px for width)
       By default, the resizer uses the color of the other text elements in the toolbar that your 
       lightweight theme uses. 

     - You can change the scrollbar color using the --tabs-scrollbar-color variable. The first value
       is the thumb color, the second is the track.
    */

    :root {
        --max-tab-rows: 3;
        --tab-growth: 1;
        --resizer-color: var(--lwt-text-color);
        --resizer-width: 10px;
        --tabs-scrollbar-color: inherit; /* An example of using a custom color would be "#05a #252525" */
    }

    /* You can change the height of tabs here.

       If you want a more compact view, you can toggle compact mode by setting [browser.compactmode.show] as 
       "true" on about:config, and then turn on compact density on the customize page (right click empty space
       on tab bar -> Customize/personalize toolbar (should be the last option) -> Density select box). 

       Using compact view will make your tabs smaller in height in a more supported way than the variables 
       here can.  
    
       If you want a custom tab height smaller than the default but different than compact view, change the 
       "inherit" value in #TabsToolbar --tab-min-height variable to the value you want. 

       For reference, in Nova, the default heights by density are as follows:
       - Compact mode: 25px
       - Regular mode: 32px
       - Touch mode: 37px
       
       Note that with Nova, when there is media playing, the tab text will appear in 2 lines, and unlike
       with compact mode this won't be changed to fit with a custom height set by this variable, so anything 
       lower than 30px might make the text to go outside the tab area.

       With compact mode enabled on Nova, the min value to not cause issues you should be using 
       for --tab-min-height is 20px.
    */

    #TabsToolbar {
        --tab-min-height: inherit !important;
    }

    /*  These below control the padding of the new tab button and min/max/close buttons respectively.
        YOU DON'T NEED TO CHANGE THESE unless you want to use values of --tab-min-height lower than 20px. 
        Before changing them, you need to UNCOMMENT the 2 rules below for them TO TAKE EFFECT. */

    #TabsToolbar {
        --toolbarbutton-inner-padding: inherit !important;
    }

    /* Sizing of the titlebar buttons */
    .titlebar-buttonbox {
        height: var(--tab-min-height) !important;
    }

    /*-------- Don't edit past here unless you know what you are doing --------*/
    #tab-rows-resizer {
        -moz-window-dragging: no-drag !important;
        height: unset !important;
        cursor: n-resize !important;
        border-bottom: 5px double var(--resizer-color);
        min-width: var(--resizer-width);
    }

    /* Common multirow code */
    #navigator-toolbox:-moz-lwtheme {
        background-color: var(--toolbar-bgcolor) !important;
    }

    :root[lwtheme-image] #navigator-toolbox {background-repeat: repeat-y !important}
    
    .tabbrowser-tab:not([pinned]) {
        flex-grow: var(--tab-growth) !important;
    }

    #tabbrowser-tabs .tab-background, #tabbrowser-tabs .tabbrowser-tab {
        min-height: var(--tab-min-height) !important}

    #nav-bar {box-shadow: none !important}

	.tab-stack {width: 100%}

    @media (-moz-platform: windows-win10), (-moz-platform: windows-win11) {
        #TabsToolbar .titlebar-buttonbox-container {display: block}
        
        #window-controls > toolbarbutton {
            max-height: calc(var(--tab-min-height) + 12px);
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
        height: calc(var(--tab-min-height) + 12px) !important;
    }

    /* Make tab split view container not be bigger in height than the size of a tab */
    tab-split-view-wrapper {
        max-height: var(--tab-min-height) !important;
        padding: 0px !important;
    }

    /* Disable duplicated min/max/close buttons */
    #toolbar-menubar:not([inactive])~#TabsToolbar .titlebar-buttonbox-container {
        width: 0 !important;
    }

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

    #tabs-newtab-button .new-tab-popup,
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

    /* Fix issues with group tabs */
    .tab-group-label-container {
        margin-inline-start: 0 !important;
    }
	`;

    // We check if using australis here
    let australisElement = getComputedStyle(document.getElementsByClassName("tabbrowser-tab")[0])
                           .getPropertyValue('--svg-before-normal-density');

    if (australisElement == null) {
        australisElement = getComputedStyle(document.querySelector(":root"))
                           .getPropertyValue('--svg-selected-after');
    }

    // Check if it's proton past FF91
    let tabsHavePadding = false;
    const tabBackground = document.getElementsByClassName("tab-background")[0];
    if (parseInt(getComputedStyle(tabBackground).getPropertyValue('--tab-margin-block').substring(0,1)) > 0) {
        tabsHavePadding = true;
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
    }
    
    css +=
    `scrollbar {-moz-window-dragging: no-drag !important}

    #tabbrowser-tabs > arrowscrollbox {
        overflow: visible;
        display: block;
    `

    // This is a fix for the shadow elements:
    style.innerHTML = `
    .scrollbox-clip {
        overflow: visible;
        display: block;
    }

    scrollbox {
        display: flex;
        flex-wrap: wrap; 
        overflow-x: hidden;
        overflow-y: auto;
        min-height: var(--tab-min-height);
        max-height: calc(var(--tab-min-height) * var(--max-tab-rows));
    }

    /* Firefox 131+ fix */
    scrollbox > slot {
        flex-wrap: wrap;
    }

    .arrowscrollbox-overflow-start-indicator,
    .arrowscrollbox-overflow-end-indicator {position: fixed !important}

    .scrollbutton-up, .scrollbutton-down, spacer,
    #scrollbutton-up, #scrollbutton-down {display: none !important}
    `;

    // This is a fix for the tabs with icons
    if (!allowResizeWithIcon) {
        css += `
        .tabbrowser-tab:not([pinned]) {
            --tab-min-width-extra-icons: 0px !important;
        }
        `
    }

    // If the new tab button is hidden we don't apply the overflowing fix
    if (hideNewTabBtn) {
        css += `
        #tabbrowser-arrowscrollbox-periphery {
            display: none !important}
        `
    } else {
        css += `
        /* This fixes the new tab button overflowing to the new row alone */
        #tabbrowser-arrowscrollbox-periphery {
            margin-left: -36px !important}
        
        .tabbrowser-tab:has(+#tabbrowser-arrowscrollbox-periphery), tab-group:has(+#tabbrowser-arrowscrollbox-periphery),
        .tab-group:has(+#tabbrowser-arrowscrollbox-periphery) > tab:last-of-type, 
        tab-split-view-wrapper:has(+#tabbrowser-arrowscrollbox-periphery) {
            margin-right: 36px !important}
        `
    }

    // This is a fix for FF89+ (Proton)
    if (tabsHavePadding) {
        style.innerHTML += `
        scrollbox {
            max-height: calc((var(--tab-min-height) + 12px) * var(--max-tab-rows));
        }
        `;
    }

    // Possible sizes of the scrollbar
    if (scrollbarSize == "thin") {
        style.innerHTML += `
        scrollbox {
            scrollbar-color: var(--tabs-scrollbar-color);
            scrollbar-width: thin;
        }
        `
    } else if (scrollbarSize == "none") {
        style.innerHTML += `
        scrollbox {
            scrollbar-width: none;
        }
        `
    } else {
        style.innerHTML += `
        scrollbox {
            scrollbar-color: var(--tabs-scrollbar-color);
            scrollbar-width: auto;
        }
        `
    }

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

	let sss = Cc['@mozilla.org/content/style-sheet-service;1'].getService(Ci.nsIStyleSheetService);
	let uri = makeURI('data:text/css;charset=UTF=8,' + encodeURIComponent(css));
	sss.loadAndRegisterSheet(uri, sss.AGENT_SHEET);

    gBrowser.tabContainer._getDropIndex = function(event) {
        let tabToDropAt = getTabFromEventTarget(event, false);
        const tabPos = findDropIndexOfTab(arrowScrollbox, tabToDropAt);

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

    // Detects if exiting fullscreen for fullscreenchange event
    function checkFullScreenScrolling() {
        if (!document.fullscreenElement) {
            let selTab = document.querySelector(".tabbrowser-tab[selected]");
            selTab.scrollIntoView();
        }
    }

    gBrowser.tabContainer.addEventListener("TabSelect", scrollToView, false);
    gBrowser.tabContainer.addEventListener("SSTabRestoring", scrollToView, false);

    // Fix for some linux issue when going out of fullscreen
    document.addEventListener("fullscreenchange", checkFullScreenScrolling, false);

    // Handles resizing of rows when enabled
    if (useResizer) {
        let tabsScrollbox;
        // FF153+
        if (document.getElementById("tabbrowser-arrowscrollbox").shadowRoot) {
            tabsScrollbox = document.getElementById("tabbrowser-arrowscrollbox").shadowRoot.querySelector("scrollbox");
        // FF71+
        } else if (document.querySelector("#tabbrowser-tabs > arrowscrollbox").shadowRoot) {
            tabsScrollbox = document.querySelector("#tabbrowser-tabs > arrowscrollbox").shadowRoot.querySelector("scrollbox");
        } 
        
        const tabsContainer = document.getElementById("TabsToolbar-customization-target");
        const mainWindow = document.getElementById("main-window");

        // Adds the resizer element to tabsContainer
        let tabsResizer = document.createElement("resizer");
        tabsResizer.setAttribute('id', "tab-rows-resizer");
        tabsContainer.appendChild(tabsResizer);

        // Removes the listeners for tab rows resizing
        function finishRowsResizing(event) {
            tabsScrollbox.style.maxHeight = event.clientY + "px";
            mainWindow.style.cursor = "default";
            document.removeEventListener("mouseup", finishRowsResizing, false);
            document.removeEventListener("mousemove", updateRowsSize, false);
        }

        // Updates the max-height of the tabs when the mouse moves
        function updateRowsSize(event) {
            tabsScrollbox.style.maxHeight = event.clientY + "px";
        }

        // Starts changing the tab max-height when you click the resizer element
        tabsResizer.onmousedown = function() {
            mainWindow.style.cursor = "n-resize";
            document.addEventListener("mouseup", finishRowsResizing, false);
            document.addEventListener("mousemove", updateRowsSize, false);
        }
    }

    let listenersActive = false;

    // This sets when to apply the fix (by default a new row starts after the 23th open tab, unless you changed the min-size of tabs)
    gBrowser.tabContainer.ondragstart = (event) => {
        const pinnedTabsCount = arrowScrollbox.querySelectorAll(".tabbrowser-tab[newPin]").length;
        draggedTabIndex = findDropIndexOfTab(arrowScrollbox, getTabFromEventTarget(event, false));
        if(gBrowser.tabContainer.arrowScrollbox.clientHeight > document.getElementsByClassName("tabbrowser-tab")[0].clientHeight || pinnedTabsCount > 0) {

            // Multiple tab select fix
            gBrowser.visibleTabs.forEach(t => t.style.transform = "");
            
            // Event handling
            if (!listenersActive) {
                gBrowser.tabContainer.on_dragover = (dragoverEvent) => performTabDragOver(dragoverEvent);
                gBrowser.tabContainer._onDragOver = (dragoverEvent) => performTabDragOver(dragoverEvent);
                gBrowser.tabContainer.ondrop = (dropEvent) => performTabDropEvent(dropEvent);
                listenersActive = true;
            }
        }
    };
}

const TAB_SELECTOR = "tab";
const TAB_GROUP_SELECTOR = "tab-group";

// Don't change these
let lastKnownIndex = null;
let groupToInsertTo = null;
let positionInGroup = null;
let draggedTabIndex = null;

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
    let tab = target?.closest(TAB_SELECTOR) || target?.closest(TAB_GROUP_SELECTOR);
    let selectedTab = getDraggedTab(event);
    if (selectedTab.nodeName === "label") {
        selectedTab = findParentOfType(selectedTab, TAB_GROUP_SELECTOR, 3)?.querySelector("tab:first-of-type") || gBrowser.selectedTab;
    }
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

    let ind = gBrowser.tabContainer.getElementsByClassName("tab-drop-indicator")[0];

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
    
    let dropIndex = gBrowser.tabContainer._getDropIndex(event);
    if (dropIndex == null)
        return;

    let tabs = gBrowser.tabContainer.querySelectorAll(TAB_SELECTOR);
    let draggedTab = getDraggedTab(event);
    let draggedGroup = findParentOfType(draggedTab, TAB_GROUP_SELECTOR, 3);
    
    if (!tab)
        tab = getTabFromEventTarget(event, false);
    
    // Handle drop index on tab label
    if (tab.nodeName === TAB_GROUP_SELECTOR) {
        groupToInsertTo = tab;
        positionInGroup = 0;

        // Make the dragged tab go to the end of the group if it's a regular tab
        if (draggedTab?.nodeName === TAB_SELECTOR) {
            let groupEnd = Array.prototype.indexOf.call(tabs, tab.querySelector("tab:last-of-type")) + 1;
            // We can't rely on dropIndex here, so we gotta calculate the index using the group absolute positions
            positionInGroup = -1;
            dropIndex = groupEnd;
        }
    }
    // Update the last known group position
    else if (tab.parentNode.nodeName === TAB_GROUP_SELECTOR) {
        groupToInsertTo = tab.parentNode;
        let groupStart = tab.parentNode.querySelector("tab:first-of-type");
        positionInGroup = dropIndex - Array.prototype.indexOf.call(tabs, groupStart);
    } else {
        groupToInsertTo = null;
        positionInGroup = null;
    }

    // Move the tab to the last position if it's moved to an empty area of the tab box
    if (event.target === gBrowser.tabContainer.arrowScrollbox || event.target == gBrowser.tabContainer.newTabButton)
        dropIndex = gBrowser.tabs.length;

    let ltr = (window.getComputedStyle(gBrowser.tabContainer).direction == "ltr");
    let rect = gBrowser.tabContainer.arrowScrollbox.getBoundingClientRect();
    let newMarginX, newMarginY;

    // Update the tab drop position (different from the drop indicator due to tab groups)
    lastKnownIndex = dropIndex;

    if (dropIndex == tabs.length) {
        let tabRect = tabs[dropIndex - 1].getBoundingClientRect();
        if (ltr)
            newMarginX = tabRect.right - rect.left;
        else
            newMarginX = rect.right - tabRect.left;
        newMarginY = tabRect.top + tabRect.height - rect.top - rect.height; // multirow fix

        if (CSS.supports("offset-anchor", "left bottom")) // Compatibility fix for FF72+
            newMarginY += rect.height / 2 - tabRect.height / 2;
    } else if (dropIndex != null || dropIndex != 0) {
        let tabRect = tabs[dropIndex].getBoundingClientRect();
        let tabLeft = tabRect.left;
        let tabRight = tabRect.right;
        let tabHeight = tabRect.height;
        let tabTop = tabRect.top;

        // Handle drop index position when hovering over a group label
        let tabGroup = tab.nodeName === TAB_GROUP_SELECTOR ? tab : tab.parentNode;
        if (draggedTab?.nodeName === "label" && tabGroup?.nodeName === TAB_GROUP_SELECTOR) {
            let tabRect;
            let draggedIndex = Array.prototype.indexOf.call(tabs, draggedGroup.querySelector("tab:first-of-type"));
            let groupStart = Array.prototype.indexOf.call(tabs, tabGroup.querySelector("tab:first-of-type"));
            let groupEnd = Array.prototype.indexOf.call(tabs, tabGroup.querySelector("tab:last-of-type")) + 1;
            let groupSize = groupEnd - groupStart;

            if (positionInGroup < groupSize / 2 && draggedIndex !== groupStart) {
                tabRect = tabGroup.childNodes[0].getBoundingClientRect();
                tabLeft = tabRect.left;
            } else {
                tabRect = tabGroup.querySelector("tab:last-of-type").getBoundingClientRect();
                tabLeft = tabRect.right;
            }
            
            tabTop = tabRect.top;
            tabRight = tabRect.right;
            tabHeight = tabRect.height;
        } else {
            let draggingGroupToAnotherGroup = groupToInsertTo === tab && draggedTab?.nodeName === "label";
            let draggingBeforeGroup = tab.nodeName === TAB_SELECTOR && tab.parentNode.nodeName !== TAB_GROUP_SELECTOR 
                && tabs[dropIndex].parentNode.nodeName === TAB_GROUP_SELECTOR 
                && tabs[dropIndex].parentNode !== draggedGroup;
            let groupToCheck = groupToInsertTo
            if (tabs[dropIndex].parentNode.nodeName === TAB_GROUP_SELECTOR)
                groupToCheck = tabs[dropIndex].parentNode;
            let draggingAfterConsecutiveGroup = groupToInsertTo !== groupToCheck && tabGroup == groupToInsertTo;
            if (draggingGroupToAnotherGroup || draggingBeforeGroup || draggingAfterConsecutiveGroup) {
                
                let tabRect = groupToCheck.childNodes[0].getBoundingClientRect();
                tabLeft = tabRect.left;
                tabTop = tabRect.top;
                tabRight = tabRect.right;
                tabHeight = tabRect.height;
            }
        }

        if (ltr)
            newMarginX = tabLeft - rect.left;
        else
            newMarginX = rect.right - tabRight;
        newMarginY = tabTop + tabHeight - rect.top - rect.height; // multirow fix

        if (CSS.supports("offset-anchor", "left bottom")) // Compatibility fix for FF72+
            newMarginY += rect.height / 2 - tabHeight / 2;
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
    let draggedTab = getDraggedTab(event);
    const tabsContainer = resolveTabsContainer();
    const allTabs = tabsContainer.querySelectorAll(TAB_SELECTOR);

    // Handle moving tab groups
    let tabGroup = findParentOfType(draggedTab, TAB_GROUP_SELECTOR, 3);
    if (draggedTab.nodeName === "label" && tabGroup) {
        let tabToMoveTo = allTabs[lastKnownIndex];
        let draggedIndex = Array.prototype.indexOf.call(allTabs, tabGroup.querySelector("tab:first-of-type"));
        if (draggedIndex === lastKnownIndex)
            return;
        if (groupToInsertTo) {
            let groupStart = Array.prototype.indexOf.call(allTabs, groupToInsertTo.querySelector("tab:first-of-type"));
            let groupEnd = Array.prototype.indexOf.call(allTabs, groupToInsertTo.querySelector("tab:last-of-type"));
            let groupSize = groupEnd - groupStart;
            if (positionInGroup < groupSize / 2)
                gBrowser.moveTabBefore(tabGroup, groupToInsertTo);
            else
                gBrowser.moveTabAfter(tabGroup, groupToInsertTo);
        } else if (lastKnownIndex !== allTabs.length)
            gBrowser.moveTabBefore(tabGroup, tabToMoveTo);
        else
            gBrowser.moveTabAfter(tabGroup, allTabs[lastKnownIndex - 1]);
    }
    // Handle moving regular tabs
    else if (draggedTab && dropEffect != "copy" && draggedTab.container == gBrowser.tabContainer) {
        if (lastKnownIndex > allTabs.length) 
            lastKnownIndex = allTabs.length;
        newIndex = lastKnownIndex;

        // Perform the actual moving of tabs
        moveSelectedTabs(newIndex, tabsContainer, event);

        // Scroll to view since the scroll goes up when moving a tab down
        scrollToView(false);

        // Restart global vars
        lastKnownIndex = null;
        groupToInsertTo = null;
        positionInGroup = null;
    }
}

/**
 * Moves the selected tabs to a new index.
 * @param {*} newIndex The new index to move tabs to.
 * @param {*} tabsContainer The tabs container where tabs are.
 * @param {*} event The drop event.
 */
function moveSelectedTabs(newIndex, tabsContainer, event) {
    /* fix for moving multiple selected tabs and tab groups */
    let selectedTabs = gBrowser.selectedTabs.filter(t => t != null);
    
    let pinnedTabsCount = tabsContainer.querySelectorAll(".tabbrowser-tab[newPin]").length;

    // Pin the tab if it wasn't pinned
    if (newIndex >= 0 && newIndex < pinnedTabsCount) {
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
    // Handle moving tabs to a group
    } else if (groupToInsertTo) {
        moveTabsToGroup(selectedTabs, event);

    // Handle regular tab moving
    } else {
        let allTabs = tabsContainer.querySelectorAll(TAB_SELECTOR);
        let tabToMoveTo = allTabs[newIndex];
        let shouldMoveAfter = tabToMoveTo?.parentNode.nodeName === TAB_GROUP_SELECTOR;
        let shouldUngroup = false;
        if (!tabToMoveTo && allTabs[newIndex - 1]) {
            tabToMoveTo = allTabs[newIndex - 1];
            shouldMoveAfter = true;
            shouldUngroup = true;
        }
        if (shouldMoveAfter)
            tabToMoveTo = allTabs[newIndex - 1];
        
        selectedTabs.forEach(t => {
            let tabWasPinned = t.hasAttribute("newPin");

            if (t.hasAttribute("newPin")) {
                if (t.pinned) {
                    gBrowser.unpinTab(t)
                }
                t.removeAttribute("newPin");
            }

            if ((tabWasPinned && newIndex == pinnedTabsCount) || (!tabWasPinned && newIndex < pinnedTabsCount)) {
                gBrowser.pinTab(t)
                migratePinnedTabs(tabsContainer, document.querySelectorAll("#pinned-tabs-container .tabbrowser-tab"));
            }
            
            if (!shouldMoveAfter)
                gBrowser.moveTabBefore(t, tabToMoveTo);
            else
                gBrowser.moveTabAfter(t, tabToMoveTo);

            if (shouldUngroup)
                gBrowser.ungroupTab(t);
        });
    }
}

// This scrolls down to the current tab when you open a new one, or restore a session.
function scrollToView(smooth = true) {
    let selTab = document.querySelector(".tabbrowser-tab[selected]");
    let wrongTab = document.querySelectorAll('.tabbrowser-tab[style^="margin-inline-start"]');
    let hiddenToolbox = document.querySelector('#navigator-toolbox[style^="margin-top"]');
    let fullScreen = document.querySelector('#main-window[sizemode="fullscreen"]');
    if (smooth)
        selTab.scrollIntoView({behavior: "smooth", block: "nearest", inline: "nearest"});
    else
        selTab.scrollIntoView({behavior: "instant", block: "nearest", inline: "nearest"});
    if (wrongTab[0]) {
        for(const element of wrongTab) {
            element.removeAttribute("style");
        }
    }

    // If in fullscreen we also make sure to keep the toolbar hidden when a new row is created
    // when opening a new tab in the background
    if (fullScreen && hiddenToolbox) {
        let toolboxHeight = hiddenToolbox.getBoundingClientRect().height;
        let tabsHeight = selTab.getBoundingClientRect().height;
        hiddenToolbox.style.marginTop = ((toolboxHeight + tabsHeight) * -1) + "px";
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

        try {
            // Assume we are using firefox above 160
            const { isTab, isTabGroupLabel, isSplitViewWrapper } = Tabbrowser;
            usingNewerVersion = false;
            if (
                (isTab(sourceNode) ||
                isTabGroupLabel(sourceNode) ||
                isSplitViewWrapper(sourceNode)) &&
                sourceNode.documentGlobal.isChromeWindow &&
                sourceNode.ownerDocument.documentElement.getAttribute("windowtype") ==
                "navigator:browser"
            ) {
                // Do not allow transfering a private tab to a non-private window
                // and vice versa.
                if (PrivateBrowsingUtils.isWindowPrivate(window) !=
                PrivateBrowsingUtils.isWindowPrivate(sourceNode.documentGlobal)) {
                    return "none";
                }

                if (window.gMultiProcessBrowser !=
                sourceNode.documentGlobal.gMultiProcessBrowser) {
                    return "none";
                }

                if (window.gFissionBrowser != sourceNode.documentGlobal.gFissionBrowser) {
                    return "none";
                }

                return dt.dropEffect == "copy" ? "copy" : "move";
            }
        } catch (ReferenceError) {
            // Assume we are using FF159 or older
            let nodeOwnerGlobal = sourceNode.ownerGlobal;
            if (!nodeOwnerGlobal)
                nodeOwnerGlobal = sourceNode.documentGlobal;
            if ((gBrowser.isTab(sourceNode) || gBrowser.isTabGroupLabel(sourceNode)) &&
                nodeOwnerGlobal.isChromeWindow &&
                sourceNode.ownerDocument.documentElement.getAttribute("windowtype") ==
                "navigator:browser") {
                // Do not allow transfering a private tab to a non-private window
                // and vice versa.
                if (PrivateBrowsingUtils.isWindowPrivate(window) !=
                    PrivateBrowsingUtils.isWindowPrivate(nodeOwnerGlobal))
                    return "none";
            

                if (window.gMultiProcessBrowser !=
                    nodeOwnerGlobal.gMultiProcessBrowser)
                    return "none";
            

                if (window.gFissionBrowser != nodeOwnerGlobal.gFissionBrowser)
                    return "none";
            

                return dt.dropEffect == "copy" ? "copy" : "move";
            }
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
        if (firstUnpinnedTab) {
            let tabGroup = findParentOfType(firstUnpinnedTab, TAB_GROUP_SELECTOR);
            if (tabGroup)
                firstUnpinnedTab = tabGroup
            newContainer.insertBefore(tab, firstUnpinnedTab);
        } else
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
 * Moves a set of tabs to a group.
 * @param {*} selectedTabs The tabs to move to the group.
 * @param {*} event The drop event.
 */
function moveTabsToGroup(selectedTabs, event) {
    let tabInGroupToMoveTo = groupToInsertTo.querySelector(`tab:nth-of-type(${positionInGroup + 1})`);
    
    selectedTabs.forEach(t => {
        if (t.hasAttribute("newPin")) {
            t.removeAttribute("newPin");
        }
        gBrowser.moveTabToExistingGroup(t, groupToInsertTo);
        
        if (event.target === gBrowser.tabContainer.arrowScrollbox || event.target == gBrowser.tabContainer.newTabButton) {
            gBrowser.moveTabAfter(t, groupToInsertTo);
            gBrowser.ungroupTab(t);
        } else if (tabInGroupToMoveTo)
            gBrowser.moveTabBefore(t, tabInGroupToMoveTo);
        else
            gBrowser.moveTabAfter(t, groupToInsertTo.querySelector("tab:last-of-type"));
        
    });
}

/**
 * Finds the index of a tab in a parent container.
 * @param {*} tabsContainer The parent container with all tabs.
 * @param {*} tab The tab to calculate the position of.
 * @returns The index of the tab inside the parent container.
 */
function findDropIndexOfTab(tabsContainer, tab) {
    return Array.prototype.indexOf.call(tabsContainer.querySelectorAll(TAB_SELECTOR), tab)
}

/**
 * Checks if the element is a child of the specified node type.
 * @param {*} element The element to check the parents.
 * @param {*} nodeName The node type to check.
 * @param {number} maxDepth The max depth of the parents to check of the element.
 * @returns The parent node of the given type if it exists.
 */
function findParentOfType(element, nodeName, maxDepth = 5) {
    let depth = 0;
    while (depth < maxDepth) {
        depth++;
        element = element.parentNode;
        if (element.nodeName === nodeName)
            return element;
    }
    return null;
}

/**
 * Gets the currently dragged tab.
 * @param {Event} event The drag event.
 * @returns The dragged tab.
 */
function getDraggedTab(event) {
    let draggedTab;
    let dt = event.dataTransfer;
    if (dt.mozTypesAt(0)[0] == TAB_DROP_TYPE) {
        draggedTab = dt.mozGetDataAt(TAB_DROP_TYPE, 0);
        if (!draggedTab) {
            return null;
        }
    }
    return draggedTab;
}

// Don't remove the event listener for the main method
window.addEventListener("load", () => zzzz_MultiRowTabLite(), false);