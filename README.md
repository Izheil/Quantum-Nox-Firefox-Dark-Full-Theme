![Quantum Nox Logo](https://i.imgur.com/F7qziom.png)

### Firefox customizations for a full dark theme, multi-row tabs, custom scrollbar, and other functions.

#### Since Firefox 69, you have to enable `toolkit.legacyUserProfileCustomizations.stylesheets` in `about:config` for userChrome and userContent to be loaded at all as per [bug #1541233](https://bugzilla.mozilla.org/show_bug.cgi?id=1541233#c35).

If you are on Windows or Linux and only want multirow or any other function that isn't related to the theme (like tabs below, or focus tab on hover), you can use the installers inside the [releases](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/releases) section.

This theme is mainly **intended to be used alongside a lightweight theme**, and for the stable release of Firefox (**This means that while it will most probably work with nightly and ESR for the most part, it may have less support for those versions**).
You can use it to fully change the colors of most of firefox UI to dark-gray colors (with #222-#444 colors mostly), including scrollbars, tooltips, sidebar, as well as dialogs. With the files here you can also as remove some context menu options, enable multirow tabs, change the font of the url bar...

If you want to know how to change some colors of the theme, check the [wiki](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/wiki/Editting-CSS-files).

### Last update: 28/06/2020

Files updated:
* **userChrome.css**: Fixed some issues on nightly. Also changed context menu borders and separators to gray.

### Pre-Last update: 24/06/2019

Files updated:
* **Addons.css**: Removed Popup Ultimate Blocker theme from addons.css, since the same functionability is already available on [Ublock Origin](https://addons.mozilla.org/en-US/firefox/addon/ublock-origin/), as well as undo closed tab (revived) button, since a better alternative ([Undo close tab](https://addons.mozilla.org/en-US/firefox/addon/undoclosetabbutton/)) already exists.
* __Addons-UUID-replacer-*__ Added a UUID automatic replacer for the `addons.css` file. You can find it inside the `Full dark theme` folder.


### A note on people looking to replace some Tab Mix Plus features:
You can find some of the basic settings that can be simulated through `about:config`, some userscripts, and some addons [here](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/wiki/Useful-about:config-settings#some-tab-mix-plus-features).

## Multirow Tabs and other functions
You can enable multirow tabs as well as other functions using the installer in the [releases](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/releases) section, or following the methods explained inside [Multirow and other functions](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions) folder.

![Multirow apng](https://i.imgur.com/2YUO9vq.png)

## Main browser UI
![Dark firefox UI](https://i.imgur.com/I4x1a8w.png)

![Dark firefox Dialog](https://i.imgur.com/q8MhDSX.png)

If you are using Linux or Mac, or want to add some more functionability (like deleting some useless context menu commands), you will have to use the methods described inside one of the 3 main folders of this repository:

#### Short review of each folder:

* [CSS tweaks](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/CSS%20tweaks): Enables removal of context menu items, multirow bookmarks, changing tab bar position (so that it could be under the bookmarks bar for example).
* [Full dark theme](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Full%20dark%20theme): Gives dark colors to firefox UI, including the scrollbars and the tooltips. Can also change the background image of `about:home` and the header image used as a persona.
* [Multirow and other functions](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions): You can find the JS files that add extra functionability to Firefox that couldn't be done with CSS alone.

![Custom Firefox home page](https://i.imgur.com/OhKiBCI.png)

## General sites dark theme
You can find an all-around sites stylesheet that will paint every site you visit dark [here](https://github.com/Izheil/Dark-userstyles/tree/master/Global%20dark%20userstyle). **You need [Stylus addon](https://addons.mozilla.org/es/firefox/addon/styl-us/) to use it**.

While it's not perfect (meaning that you should still use per-site styles for the sites you visit often), it can help to darken most sites when browsing around general sites that you don't visit often, and thus don't want/can't find a specific userstyle for them.

![Global Dark theme](https://i.imgur.com/mbeHNQp.png)

## Addon dark themes
You can apply a dark theme to certain addons changing the UUID's of them inside the `addons.css` file inside the "Full dark theme" folder (more instructions on how to do that inside the addons file).

![Dark addons](https://i.imgur.com/t1Nf65V.png)

Here is a list of the themed addons:
* [Ant Video Downloader](https://addons.mozilla.org/en-US/firefox/addon/video-downloader-player/)
* [Cookie autodelete](https://addons.mozilla.org/en-US/firefox/addon/cookie-autodelete/)
* [Download Manager (S3)](https://addons.mozilla.org/en-US/firefox/addon/s3download-statusbar/)
* [Forget Me Not](https://addons.mozilla.org/en-US/firefox/addon/forget_me_not/)
* [History autodelete](https://addons.mozilla.org/en-US/firefox/addon/history-autodelete/)
* [HTTPS Everywhere](https://addons.mozilla.org/en-US/firefox/addon/https-everywhere/)
* [Noscript](https://addons.mozilla.org/en-US/firefox/addon/noscript/)
* [Notifier for Gmail (restartless)](https://addons.mozilla.org/en-US/firefox/addon/gmail-notifier-restartless/)
* [Multi-accounts containers](https://addons.mozilla.org/en-US/firefox/addon/multi-account-containers/)
* [OneTab](https://addons.mozilla.org/en-US/firefox/addon/onetab/)
* [Privacy badger](https://addons.mozilla.org/en-US/firefox/addon/privacy-badger17/)
* [Tab session manager](https://addons.mozilla.org/en-US/firefox/addon/tab-session-manager/)
* [Temporary containers](https://addons.mozilla.org/en-US/firefox/addon/temporary-containers/)
* [Ublock Origin](https://addons.mozilla.org/en-US/firefox/addon/ublock-origin/)
* [uMatrix](https://addons.mozilla.org/en-US/firefox/addon/umatrix/)
* ~~Undo closed tabs button~~ -> Use [Undo close tab](https://addons.mozilla.org/en-US/firefox/addon/undoclosetabbutton/) instead (which is more updated and requires no theming).
* [Video Download Helper](https://addons.mozilla.org/en-US/firefox/addon/video-downloadhelper/)
* [Viewhance](https://addons.mozilla.org/en-US/firefox/addon/viewhance/)


You might have noticed that we no longer have [Lastpass dark theme](https://gist.github.com/Izheil/49db523ee66d88995401bb6844605763) inside `addons.css` anymore. This is because at the time that addon was themed, I didn't know much about it. After some research it seems like Lastpass has had a history of security issues (in 2011, 2015, 2016, and 2017), as well as there being other open source alternatives out there that seem to be more reliable, like **Bitwarden** (it also has a built-in dark mode) which is available for all major browsers.

## The scrollbars

This theme colors scrollbars using `userContent.css` to give them a basic re-color.

![Re-colored dark scrollbar](https://i.imgur.com/hqwoq9n.png)

If you **want a different style on the scrollbars**, you can try using the `scrollbars.as.css` file inside the [Alternative scrollbars](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Full%20dark%20theme/Alternative%20scrollbars%20%26%20tooltips/Alternative%20scrollbars) folder, which will make the scrollbars look more rounded and will have some sort of "puffy" effect when clicking them.

![Custom dark blue scrollbar](https://i.imgur.com/sOHN1ds.gif)

If instead you just **don't want scrollbars to show at all but keep scrollability**, you can do this through `userContent.css` setting the variable `--scrollbars-width` to none (should be the first rule on the `:root` section (almost at the start)), and deleting `scrollbars.as.css`.

If you aren't using the userContent provided here for some reason, you can always just add this code to your self-created `userContent.css`:
`*|* {scrollbar-width: none !important}`

### F.A.Q.
You can find the frequently asked questions in [here](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/wiki/Frequently-Asked-Questions).

## Credits
The original code for the custom scrollbars which we modified here belongs to **Arty2**, and you can find it [here](https://gist.github.com/Arty2/fdf19aea2c601032410516f059d58eb1).

The original code for the multirow tabs (the CSS part) was written by **Andreicristianpetcu**, and you can find it [here](https://discourse.mozilla.org/t/tabs-in-two-or-more-rows-like-tabmixpro-in-quantum/21657/2), or for just the code, [here](https://github.com/andreicristianpetcu/UserChrome-Tweaks/blob/09fa38a304af88b685f4086bc8ea9997dd7db0fd/tabs/multi_row_tabs_firefox_v57.css). The fix of multi-row tabs draggability was made by **TroudhuK**, and you can find the original one [here](https://github.com/TroudhuK/userChrome.js/blob/patch-1/Firefox-57/Mehrzeilige-Tableiste/MultiRowTabLiteforFx.uc.js).

The original code for the multirow bookmarks toolbar belongs to the original creator mentioned in [this reddit thread](https://www.reddit.com/r/firefox/comments/75wya9/multiple_row_bookmark_toolbar_for_firefox_5758/), whose code was fixed by **jscher2000** to use in our current firefox version.

The fix to be able to theme unread tabs again after FF61 (see [bug #1453957](https://bugzilla.mozilla.org/show_bug.cgi?format=default&id=1453957) on bugzilla) as mentioned in [this reddit thread](https://www.reddit.com/r/FirefoxCSS/comments/8yruy8/tabbrowsertabunread_backgroundimage/), was made by **moko1960** to use in Firefox 61+.

The code to be able to edit anonymous content (in our case the scrollbars and tooltips) was created thanks to the efforts of [Zeniko](http://mozilla.zeniko.ch/userchrome.js.html), [Nichu](https://github.com/nuchi/firefox-quantum-userchromejs), and [Sporif](https://github.com/Sporif/firefox-quantum-userchromejs) in the old versions, and [Xiaoxiaoflood](https://github.com/xiaoxiaoflood/firefox-scripts) for the current one.

Special thanks to **Messna** for noting the class turning into an ID on FF58, and **Snwflake** for fixing Firefox root folder location on MacOS.

Also thanks to **532910**, **BelladonnavGF**, **DallasBelt**, **Demir-delic**, **Gitut2007**, **Hakerdefo**, **Tkhquang** and **YiannisNi** for noting some issues with the theme, and the requests for new features that extended this project.

## Donations
If you want to support this project, consider buying me a coffee to motivate me keep this repository up and running.
​<br><br>
<a href="https://ko-fi.com/K3K4TQ97" target="_blank"><img height="36" style="border:0px;height:36px;" src="https://az743702.vo.msecnd.net/cdn/kofi2.png?v=2" border="0" alt="Buy Me a Coffee at ko-fi.com" /></a>

...or any other amount you see fit on paypal.

<a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=BMUFYBSRA7ENL&source=url"><img alt="" border="0" src="https://www.paypalobjects.com/webstatic/mktg/logo/pp_cc_mark_74x46.jpg"/></a>
