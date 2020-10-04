## Other features
Here go any other feature that isn't the main focus of the theme and their description.

**First make sure that you have patched Firefox with either [the patcher](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/releases) (which also lets you install any of these files automatically along with the patch), or with the method explained in the [JS Loader](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions/JS%20Loader) folder to use any of these files.**

**If using the patcher, make sure that the default profile found is the one you are currently using (you can check this in `about:profiles`).**

### Bookmarks-toggle.uc.js
Toggles visibility of the bookmarks toolbar when pressing F2 (you can change which keys in the file). You need to have the "fullscreen fix" disabled on userchrome.css if using any of the "CSS tweaks" versions from this repository.

### Focus-tab-on-hover.uc.js
Lets you switch to another tab just by hovering over it. You can specify a delay to wait before switching to the hovered tab inside the file (the variable on top of the file).

### Mac-fullscreen-fix-toolbox-autohide.uc.js
Forces autohide of the toolbar in fullscreen mode to fix a common issue on Mac devices where the toolbar won't do this even with the setting enabled. Windows and Linux users shouldn't need this (since it already autohides if you have it toggled in the context menu of the toolbar in fullscreen mode).

### Navigator-toolbox-autohide.uc.js
Toggles visibility of the whole navigation toolbox as if you were on fullscreen, so that it's only visible when you have the mouse over it, or when hovering the mouse to the top of the screen when it's hidden. You can also maker bigger the hitbox to trigger the visibility of the toolbox changing the height of `fsToggler.style.height`at the bottom of the script from 10px to anything you want (just note that the bigger you make it, the more web area content will be unclickable on top).

### Navigator-toolbox-hide-by-keypress.uc.js
Hides the navigation toolbox when pressing a key (F1 by default) when NOT in fullscreen mode. You can change the binded key through the variables inside the file.

### Tabs-on-bottom.uc.js
Changes the position of tabs to be below the web content area (at the bottom of the browser).
You can also choose if you want to hide the tabs below by default on fullscreen until pressing a shortcut (`Shift + T` by default) by changing the variables on top of the screen.

### Test.as.css
This is a test file to check that both external non-userchrome css files and js files are loaded through `userchrome.xml`. It draws a red border around all editable elements inside firefox UI.