# Multirow and other custom functions through JS injection
You can load other CSS files or JS files that couldn't be loaded in a regular way through JS injection, which lets us modify the scrollbars further, or change the behaviour of tabs (like for multirow).

As with every other method, if some changes of your script aren't getting updated after changing it and restarting Firefox, **the first thing to try is to delete the start up cache files for the changes of any `*.uc.js` files (like the multi-row one, or the bookmarks toggler) to take effect**.

To clear the start up cache you have to type `about:profiles` on firefox URL bar, go to that page, open the local profile directory through that page, and then delete all files inside the `startupCache` folder.

This is **NOT** the same profile directory where you have to place the files from any of these folders. You access that one through `about:support`, and then clicking the "open folder" button on the "profile folder" section.

## Contents of each folder:

* [JS Loader](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions/JS%20Loader): These are the files that will enable the use of the userscripts contained in the other folders.
* [Multirow tabs](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions/Multirow%20tabs): Files to enable multiple rows of tabs instead of only having 1 row of tabs. **The javascript versions allows you to reorder tabs dragging them.** You can chose between the infinite rows or the scrollable rows versions. 
	* ![Multirow tabs preview](https://i.imgur.com/qqQn4Ky.png)
* [Other features](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions/Other%20features): You can find some additional features that can only be done through javascript here, such as autohidding the UI of Firefox, toggling visibility of bookmarks bar with a keypress, or focusing tabs on hover.

## Installation
The easiest way to install them is to use [the patcher](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/releases) created to enable JS injection, which will also let you install some of the functions automatically. All you need to do is **check that the profile folder found in the patcher is the one that you are currently using** (you can check this in `about:profiles`), and then select the functions you want to install.

You can also use the patcher to only copy the JS enabling part to your profile folder (unticking every function in the patcher so that it only applies the JS enabling part), and then copy the function files manually.

If you want to do everything manually, you will have to copy necesary files to enable the use of JS functions first following the method inside the [JS Loader](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions/JS%20Loader) folder. After that, to install any of the functions just copy the file(s) you are interested on inside any of the folders here to your [chrome folder](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/wiki/Chrome-and-Root-folders#the-chrome-folder).