![Quantum Nox Logo](https://i.imgur.com/F7qziom.png)

### Firefox customizations for multi-row tabs, context menus, and other functions.

#### Since Firefox 69, you have to enable `toolkit.legacyUserProfileCustomizations.stylesheets` in `about:config` for userChrome and userContent to be loaded at all as per [bug #1541233](https://bugzilla.mozilla.org/show_bug.cgi?id=1541233#c35).

If you only want multirow or any other function that isn't related to the theme (like tabs below, or focus tab on hover), you can use the installers inside the [releases](https://github.com/Izheil/Quantum-Nox-Firefox-Customizations/releases) section.

For anyone looking for the old code like the dark theme or the attempt of a mod loader, you can find it in the **backup/2025-09-12** branch.

### Last update: 16/10/2026

Files updated:

- __MultiRowTab*.uc.js__: Fixed issue with tab pinning.

### Pre-last update: 30/09/2026

Files updated:
- __MultiRowTab*.uc.js__: Fixed sizing issue in Nova redesign.

### A note on people looking to replace some Tab Mix Plus features:
You can find some of the basic settings that can be simulated through `about:config`, some userscripts, and some addons [here](https://github.com/Izheil/Quantum-Nox-Firefox-Customizations/wiki/Useful-about:config-settings#some-tab-mix-plus-features).

## Multirow Tabs and other functions
You can enable multirow tabs as well as other functions using the installer in the [releases](https://github.com/Izheil/Quantum-Nox-Firefox-Customizations/releases) section, or following the methods explained inside [Multirow and other functions](https://github.com/Izheil/Quantum-Nox-Firefox-Customizations/tree/master/Multirow%20and%20other%20functions) folder.

![Multirow apng](https://i.imgur.com/2YUO9vq.png)

If you are using Linux or Mac, or want to add some more functionability (like deleting some useless context menu commands), you will have to use the methods described inside one of the 3 main folders of this repository:

#### Short review of each folder:

* [CSS tweaks](https://github.com/Izheil/Quantum-Nox-Firefox-Customizations/tree/master/CSS%20tweaks): Enables removal of context menu items, multirow bookmarks, changing tab bar position (so that it could be under the bookmarks bar for example).
* [Multirow and other functions](https://github.com/Izheil/Quantum-Nox-Firefox-Customizations/tree/master/Multirow%20and%20other%20functions): You can find the JS files that add extra functionability to Firefox that couldn't be done with CSS alone.


## General sites dark theme
You can find an all-around sites stylesheet that will paint every site you visit dark [here](https://github.com/Izheil/Dark-userstyles/tree/master/Global%20dark%20userstyle). **You need [Stylus addon](https://addons.mozilla.org/es/firefox/addon/styl-us/) to use it**.

While it's not perfect (meaning that you should still use per-site styles for the sites you visit often), it can help to darken most sites when browsing around general sites that you don't visit often, and thus don't want/can't find a specific userstyle for them.

![Global Dark theme](https://i.imgur.com/mbeHNQp.png)

### F.A.Q.
You can find the frequently asked questions in [here](https://github.com/Izheil/Quantum-Nox-Firefox-Customizations/wiki/Frequently-Asked-Questions).

## Credits
The original code for the multirow tabs (the CSS part) was written by **Andreicristianpetcu**, and you can find it [here](https://discourse.mozilla.org/t/tabs-in-two-or-more-rows-like-tabmixpro-in-quantum/21657/2), or for just the code, [here](https://github.com/andreicristianpetcu/UserChrome-Tweaks/blob/09fa38a304af88b685f4086bc8ea9997dd7db0fd/tabs/multi_row_tabs_firefox_v57.css). The fix of multi-row tabs draggability was made by **TroudhuK**, and you can find the original one [here](https://github.com/TroudhuK/userChrome.js/blob/patch-1/Firefox-57/Mehrzeilige-Tableiste/MultiRowTabLiteforFx.uc.js).

The original code for the multirow bookmarks toolbar belongs to the original creator mentioned in [this reddit thread](https://www.reddit.com/r/firefox/comments/75wya9/multiple_row_bookmark_toolbar_for_firefox_5758/), whose code was fixed by **jscher2000** to use in our current firefox version.

The fix to be able to theme unread tabs again after FF61 (see [bug #1453957](https://bugzilla.mozilla.org/show_bug.cgi?format=default&id=1453957) on bugzilla) as mentioned in [this reddit thread](https://www.reddit.com/r/FirefoxCSS/comments/8yruy8/tabbrowsertabunread_backgroundimage/), was made by **moko1960** to use in Firefox 61+.

A fix for multiple tab reordering and another fix for the new tab button to not start a row on its own without a tab on multirow was made by **Merci-chao**.

The code to be able to edit anonymous content (in our case the scrollbars and tooltips) was created thanks to the efforts of [Zeniko](http://mozilla.zeniko.ch/userchrome.js.html), [Nichu](https://github.com/nuchi/firefox-quantum-userchromejs), and [Sporif](https://github.com/Sporif/firefox-quantum-userchromejs) in the old versions, and [Xiaoxiaoflood](https://github.com/xiaoxiaoflood/firefox-scripts) for the current one.

Special thanks to **Messna** for noting the class turning into an ID on FF58, and **Snwflake** for fixing Firefox root folder location on MacOS.

Also thanks to **532910**, **BelladonnavGF**, **DallasBelt**, **Demir-delic**, **Gitut2007**, **Hakerdefo**, **Pauby**, **Tkhquang** and **YiannisNi** for noting some issues with the theme, and the requests for new features that extended this project.
