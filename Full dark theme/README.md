# Full dark theme for firefox
Following the method described here, you will be able to give dark colors to firefox as shown in the following picture:

![Dark firefox UI](https://i.imgur.com/I4x1a8w.png)

![Dark addons](https://i.imgur.com/t1Nf65V.png)

## Installation

**Note: As of Firefox 69, you will need to enable the use of these files through a configuration setting.** The preference in question is `toolkit.legacyUserProfileCustomizations.stylesheets`. Here is how you change its value:

1. Load `about:config` in the Firefox address bar.
	1. Confirm that you will be careful.
	2. Search for `toolkit.legacyUserProfileCustomizations.stylesheets` using the search at the top.
2. Toggle the preference. `True` means Firefox supports the CSS files, `False` that it ignores them.

#### Step by step:
* Type `about:support` in your URL bar, then go to that page.
* Click the "open folder" button inside the "profile folder" section.
* Create a folder named "chrome" in your profile folder if it doesn't exist yet.
* [Download the repository files](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/archive/master.zip) and uncompress them anywhere you like.
* Place all files (.css files) from the "Full dark theme" folder to your "chrome" folder.
* **Optional**: If you want to use the custom dark scrollbars, or dark tooltips, you will also have to enable JS injection using the installer in [releases](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/releases) (just don't select any function to install when patching if you don't need them), or patch your firefox manually with the method described [here](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions/JS%20Loader).
* **Optional**: Edit userChrome.css to change any style you aren't fully convinced with (or to give a different style to the unread tabs, etc...).
* **Optional**: You can also edit userChrome.css to change the background of the `about:home` page.
* **Optional**: If you want a different style for the scrollbars or the tooltips, use any of the alternatives on the [Alternative scrollbars & tooltips](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Full%20dark%20theme/Alternative%20scrollbars%20%26%20tooltips) folder.
* **Optional**: If you want the default scrollbar style (userChrome still paints it dark), or white tooltips, don't copy the relevant CSS files for them.
* **Optional**: If you want a dark version of either of the addons mentioned in the [addons dark themes section](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme#addon-dark-themes) in the front page of this repository, change the UUID's of them inside `addons.css`. You can use the `Addons-UUID-replacer-*` executable to automate this (unless you are on Mac, where you will have to install python and run the python file inside `installers/Addons UUID replacer` to get the same result). If on Linux, make sure to run it as a regular user, **not as sudo**.

If you have copied everything right, the folders structure should look something like this:
Structure of [the chrome folder](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/wiki/Chrome-and-Root-folders#the-chrome-folder) files inside your profile folder:

* __utils (folder) -> Only if you want to use the `*.as.css` and `*.uc.js` files.__
* addons.css
* scrollbars.as.css
* setAttribute_unread.uc.js
* tooltips.as.css
* userChrome.css
* userContent.css

Structure of [firefox root folder](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/wiki/Chrome-and-Root-folders#firefox-root-folder) files (where your firefox is installed):

* browser (folder)
* defaults (folder)
  * pref (folder)
    * channel-prefs.js
    * **config-prefs.js**
* fonts (folder)
* uninstall (folder)
* (Other optional folders might appear here)
* firefox.exe (or other Firefox executable depending on your OS)
* **config.js**
* Other .dll files

Bolded files or folders mark the required things to enable JS injection.

## The userChrome.css file

The userChrome file turns dark all context menus, bookmarks, the url bar, the search bar, the main menu, and the toolbar. 
It will, although, not turn dark the extension popups you may have.

![Dark search menu (spanish)](https://i.imgur.com/E7iG7az.png)

![Dark context menu (spanish)](https://i.imgur.com/7zj3SSq.png)

It will also turn dark the autocomplete popups (mostly a side-effect)
userChrome.css is also the file that enables loading of external (placed in the chrome folder) .css and .js files through the use of `userChrome.xml` (such as `scrollbars.as.css` or `MultiRowTabLiteforFx.uc.js`).

## The userContent.css file

The userContent file will turn dark all the `about:about` pages.

![Dark firefox about: pages](https://i.imgur.com/mKWPUSk.png)

![Dark addons page](https://i.imgur.com/97ebC1x.png)

It will also turn dark the [Mozilla addons](https://addons.mozilla.org) page, both the old and the new, the file explorer inside firefox, and the "view source of page" page.