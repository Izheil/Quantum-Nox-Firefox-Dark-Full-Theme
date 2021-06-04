// ==UserScript==
// @name           Scrollable Multirow Tabs
// @namespace      https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme
// @description    Multi-row tabs draggability fix with scrollable rows
// @include        main
// @compatibility  Firefox 70 to Firefox 91.0a1 (2021-06-03)
// @author         Alice0775, Endor8, TroudhuK, Izheil, Merci-chao
// @version        04/06/2021 04:39 Lightweight themes bg fix, and tab height fix for Proton
// @version        07/03/2021 23:24 Compatibility fix with Simple Tab Groups addon
// @version        12/02/2021 06:23 Added the option to make the scrollbar thin and change its color
// @version        12/02/2021 02:18 The new tab button now wont start a new row by itself, and multiple tab selection fixed
// @version        04/01/2021 22:45 Added an optional tab rows resizer that you can toggle with "useResizer" var
// @version        07/12/2020 01:21 Stopped hidding tab right borders since it's not related to multirow
// @version        25/09/2020 23:26 Fixed glitch on opening tabs in the background while on fullscreen
// @version        06/09/2020 18:29 Compatibility fix for Australis and fix for pinned tabs glitch
// @version        28/07/2020 23:28 Compatibility fix for FF81 
// @version        03/07/2020 00:34 Fixed an issue with the new tab button overflowing the scrollbar
// @version        12/05/2020 13:09 Removed unnecesary selector
// @version        09/04/2020 08:14 Minor fixes for tab line when window is resized
// @version        08/04/2020 05:40 Compatibility fix for FF77
// @version        16/03/2020 05:15 Fixed some issue with tab transitions
// @version        06/03/2020 21:56 Fixed an issue with tab lines and duplicated buttons
// @version        12/02/2020 03:30 Fixed some issue with the min/resize/close buttons
// @version        18/01/2020 02:39 Added a fix for people who always spoof their useragent
// @version        13/01/2020 05:01 Fixed the tab drop indicator on FF72+
// @version        15/11/2019 15:45 Unified FF67+ and FF72 versions
// @version        11/10/2019 18:32 Compatibility fix for FF71
// @version        06/09/2019 23:37 Fixed issue with tabs when moving to another window
// @version        05/09/2019 03:24 Fixed tab draggability to work with FF69
// @version        23/03/2019 08:30 Variables to set min-width of tabs
// @version        09/03/2019 15:38 Fixed compatibility issue with Tab Session Manager addon
// @version        18/02/2019 20:46 Tab line not being fully shown on maximized or fullscreen
// @version        03/02/2019 15:15 Firefox 67
// @version        03/02/2019 04:22 Fixed issue with scrolling when selecting non-visible tab
// @version        02/02/2019 00:17 Fixed transparent line under tabs and touch density tabs issue
// @version        01/02/2019 10:32 Fixed issue window dragging while keeping scrollbar dragging
// @version        31/01/2019 10:32 Fixed issue with fullscreen
// @version        30/01/2019 02:05 Fixed issue with a pixel being above the tab bar
// @version        30/11/2018 06:12 Now only the necesary rows appear, not static number of rows
// @version        23/11/2018 00:41 Firefox 65
// ==/UserScript==
zzzz_MultiRowTabLite();
function zzzz_MultiRowTabLite() {
    // EDITABLE JAVASCRIPT VARIABLES

    // Enables the use of the rows resizer
    var useResizer = false;

    // Use thin scrollbar for tabs
    var useThinScrollbar = false;

    // CSS section
	var css =`
    /* MULTIROW TABS CSS */

    /* EDITABLE CSS VARIABLES */

    /* You can set the max number of rows before the scrollbar appears and the tab width here.

     - For tab minimum width, you have to go to about:config and modify [browser.tabs.tabMinWidth] 
       to the value you want. You shouldn't use values lower than 58 for this setting or tabs will
       start to overlap, and scrolling with the wheel will stop working.

     - For tab width growth v 
        Value of 1 -> Tab grows. Fixed max width of 226px.
        Value of 0 -> Tab doesn't grow. Uses tab min width as fixed width.
        
     - To change the color or width of the resizer, change the --resizer-* variables to any other 
       value you want. (like #666 for color or 5px for width)
       By default, the resizer uses the color of the other text elements in the toolbar that your 
       lightweight theme uses. 

     - You can change the scrollbar color using the --tabs-scrollbar-color variable if you enabled
       "useThinScrollbar" (setting it as true) JavaScript variable above. If you want to color the 
       scrollbar but keep it as normal size, use userContent.css or any of the .as.css scrollbar 
       files available.
    */

    :root {
        --max-tab-rows: TABROWS;
        --tab-growth: 1;
        --resizer-color: var(--lwt-text-color);
        --resizer-width: 10px;
        --tabs-scrollbar-color: #05a; /* Only applicable if "useThinScrollbar" JS variable is set as true */
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
    */

    #TabsToolbar {
        --tab-min-height: inherit !important;

        /* You don't need to change this last one */
        --toolbarbutton-inner-padding: inherit !important;
    }

    /*-------- Don't edit past here unless you know what you are doing --------*/
    
    #navigator-toolbox:-moz-lwtheme {
        background-repeat: repeat !important;
    }
    
    .tabbrowser-tab:not([pinned]) {
        flex-grow: var(--tab-growth)}

    #tabbrowser-tabs .tab-background, #tabbrowser-tabs .tabbrowser-tab {
        min-height: var(--tab-min-height) !important}

    #nav-bar {box-shadow: none !important}

	.tab-stack {width: 100%}

    #tab-scrollbox-resizer {
        width: var(--resizer-width);
        border-bottom: 5px double var(--resizer-color);
        cursor: n-resize;
    }

    @media (-moz-os-version: windows-win10) {
        #TabsToolbar .titlebar-buttonbox-container {display: block}
        
        #window-controls > toolbarbutton {
            max-height: calc(var(--tab-min-height) + 8px);
            display: inline;
        }

        #main-window[sizemode="fullscreen"] #window-controls {
            display: flex;
        }
    }

    @media (-moz-os-version: windows-win7), (-moz-os-version: windows-win8) {
        #tabbrowser-tabs .tabbrowser-tab {
            border-top: none !important}
    }

    /* This fixes the new tab button overflowing to the new row alone */
    #tabs-newtab-button {
        margin-left: -32px !important} 
        
    .tabbrowser-tab[last-visible-tab="true"] { 
        margin-right: 32px !important}

    /* These fix issues with pinned tabs on the overflow status */
    #tabbrowser-tabs[overflow="true"] > #tabbrowser-arrowscrollbox > #tabs-newtab-button,
    #TabsToolbar:not([customizing="true"]) #tabbrowser-tabs[hasadjacentnewtabbutton] > #tabbrowser-arrowscrollbox > #tabs-newtab-button {
        display: inline-flex !important;
    }

    #alltabs-button, #tabs-newtab-button .new-tab-popup,
    #TabsToolbar:not([customizing="true"]) #tabbrowser-tabs[hasadjacentnewtabbutton] ~ #new-tab-button
    {display: none}

    #tabbrowser-tabs .tab-background, #tabbrowser-tabs .tabbrowser-tab {
        min-height: var(--tab-min-height) !important}

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

	`;

    // We check if using australis here
    var australisElement = getComputedStyle(document.getElementsByClassName("tabbrowser-tab")[0])
                           .getPropertyValue('--svg-before-normal-density');

    if (australisElement == null) {
        australisElement = getComputedStyle(document.querySelector(":root"))
                           .getPropertyValue('--svg-selected-after');
    }

    // Here the FF71+ changes
    if (document.querySelector("#tabbrowser-tabs > arrowscrollbox").shadowRoot) {

        css +=`
        #tabbrowser-tabs > arrowscrollbox {
          overflow: visible;
          display: block;
          
        }
        
        scrollbar, #tab-scrollbox-resizer {-moz-window-dragging: no-drag !important}
        `;

        // This is a fix for the shadow elements:
        var style = document.createElement('style');
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
            max-height: calc((var(--tab-min-height) + 8px) * var(--max-tab-rows));
        }

        .arrowscrollbox-overflow-start-indicator,
        .arrowscrollbox-overflow-end-indicator {position: fixed !important}

        .scrollbutton-up, .scrollbutton-down, spacer,
        #scrollbutton-up, #scrollbutton-down {display: none !important}
        `;

        if (useThinScrollbar == true) {
            style.innerHTML += `
            scrollbox {
                scrollbar-color: var(--tabs-scrollbar-color) transparent;
                scrollbar-width: thin;
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

        document.querySelector("#tabbrowser-tabs > arrowscrollbox").shadowRoot.appendChild(style);
	} else {
        // Here the FF69-FF70 changes
		css +=`
        #tabbrowser-tabs .scrollbutton-up, #tabbrowser-tabs .scrollbutton-down {
            display: none !important}

		#tabbrowser-tabs .arrowscrollbox-scrollbox {
	        display: flex;
	        flex-wrap: wrap; 
	        overflow-x: hidden;
	        overflow-y: auto;     
	        min-height: var(--tab-min-height);
	        max-height: calc(var(--tab-min-height)*var(--max-tab-rows))}

        #tabbrowser-tabs .tabbrowser-arrowscrollbox {
            overflow: visible;
            display: block}

	    .arrowscrollbox-overflow-start-indicator,
    	.arrowscrollbox-overflow-end-indicator {position: fixed !important}

	    #main-window[tabsintitlebar] #tabbrowser-tabs scrollbar, #tab-scrollbox-resizer {
	        -moz-window-dragging: no-drag}
	    `;

        if (useThinScrollbar == true) {
            style.innerHTML += `
            #tabbrowser-tabs .arrowscrollbox-scrollbox {
                scrollbar-color: var(--tabs-scrollbar-color) transparent;
                scrollbar-width: thin;
            }
            `
        }

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
        let selTab = document.querySelectorAll(".tabbrowser-tab[selected='true']")[0];
        let wrongTab = document.querySelectorAll('.tabbrowser-tab[style^="margin-inline-start"]');
        let hiddenToolbox = document.querySelector('#navigator-toolbox[style^="margin-top"]');
        let fullScreen = document.querySelector('#main-window[sizemode="fullscreen"]');
        selTab.scrollIntoView({behavior: "smooth", block: "nearest", inline: "nearest"});
        if (wrongTab[0]) {
            for(let i = 0; i < wrongTab.length; i++) {
                wrongTab[i].removeAttribute("style");
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

    gBrowser.tabContainer.addEventListener('TabOpen', scrollToView, false);
    gBrowser.tabContainer.addEventListener("TabSelect", scrollToView, false);
    document.addEventListener("SSTabRestoring", scrollToView, false);

    // Handles resizing of rows when enabled
    if (useResizer) {
        var tabsScrollbox;
        // FF71+
        if (document.querySelector("#tabbrowser-tabs > arrowscrollbox").shadowRoot) {
            tabsScrollbox = document.querySelector("#tabbrowser-tabs > arrowscrollbox").shadowRoot.querySelector(".scrollbox-clip > scrollbox");
        // FF70-
        } else {
            tabsScrollbox = document.querySelector("#tabbrowser-tabs .arrowscrollbox-scrollbox");
        }
        
        var tabsContainer = document.getElementById("TabsToolbar-customization-target");
        var mainWindow = document.getElementById("main-window");

        // Adds the resizer element to tabsContainer
        var tabsResizer = document.createElement("div");
        tabsResizer.setAttribute('id', "tab-scrollbox-resizer");
        tabsContainer.appendChild(tabsResizer);
        console.log("Potato")

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

    // We set this to check if the listeners were added before
    var Listeners = false;

    // This sets when to apply the fix (by default a new row starts after the 23th open tab, unless you changed the min-size of tabs)
    gBrowser.tabContainer.ondragstart = function(){
        if(gBrowser.tabContainer.clientHeight > document.getElementsByClassName("tabbrowser-tab")[0].clientHeight) {

            /* fix for moving multiple selected tabs */
            gBrowser.visibleTabs.forEach(t => t.style.transform && "");
            var tab = this._getDragTargetTab(event, false);
            let selectedTabs = gBrowser.selectedTabs;
            while (selectedTabs.length) {
                let t = selectedTabs.pop();
                if (t._tPos > tab._tPos)
                    gBrowser.moveTabTo(t, tab._tPos + 1);
                else if (t == tab)
                    selectedTabs.reverse();
                else if (t._tPos < tab._tPos)
                    gBrowser.moveTabTo(t, tab._tPos - 1);
            }

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
                var movingTabs;
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

                    /* fix for moving multiple selected tabs */
                    let selectedTabs = gBrowser.selectedTabs;
                    if (newIndex > selectedTabs[selectedTabs.length - 1]._tPos + 1)
                        newIndex--;
                    else if (newIndex >= selectedTabs[0]._tPos)
                        newIndex = -1;
                    else
                        selectedTabs.reverse();
                    
                    if (newIndex > -1)
                        selectedTabs.forEach(t => gBrowser.moveTabTo(t, newIndex));
                }
            };

            // We then attach the event listeners for the new functionability to take effect
            if (Listeners == false) {
                gBrowser.tabContainer.addEventListener("dragover", gBrowser.tabContainer._onDragOver, true);
                gBrowser.tabContainer.addEventListener("drop", function(event){this.onDrop(event);}, true);
                Listeners = true;
            }
        }
    };
}

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
        
        }
    }
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
        if (PrivateBrowsingUtils.isWindowPrivate(window) !=
        PrivateBrowsingUtils.isWindowPrivate(sourceNode.ownerGlobal)) {
            return "none";
        }

        if (window.gMultiProcessBrowser !=
            sourceNode.ownerGlobal.gMultiProcessBrowser) {
        return "none";}

        return dt.dropEffect == "copy" ? "copy" : "move";
    }}

    if (browserDragAndDrop.canDropLink(event)) {
        return "link";
    }
    return "none";
}
