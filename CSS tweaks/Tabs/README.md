# Tab fixes

### Always-show-sound-icon-when-playing.as.css
Makes the sound icon to be always visible on normal and touch density (since otherwise it is only visible on hover), while also showing the favicon.

![Sound icon always shown preview](https://i.imgur.com/NfkFqZR.png)

### Post-tabs-space-resizing.as
This makes the space that comes before the min/max/close button (space where you can place addons), but
after the tabs section thinner. You will still be able to place addons here, this only modifies the unused space before those addons in that space.

### Tab-close-button-always-visible.as.css
The close button at the right side of each tab will always be visible.

### Tabs-below.as.css
If using Mac, use the `Tabs-below-Menu-onTop.as.css` version instead, since this will display an empty margin that is not usable for Mac users.

Changes the order of the toolbars inside the navigation box. This one sets the position of the tab bar below the url bar, and the menu bar (the one with file, edit, etc...) to be on top of all the other bars (you need to have the menu bar toggled as always visible, which can be toggled in the context menu that opens right clicking a blank space in the tabs bar). If you don't know which one to use, use this one.

### Tabs-below-Menu-onTop.as.css
This is the only version of tabs below that Mac users should use.

Changes the order of the toolbars inside the navigation box. This one sets the position of the tab bar below the url bar, and the menu bar (the one with file, edit, etc...) to be below the Url bar, but above the Tabs bar. You won't need to toggle the menu bar as always visible.

As with the `Tabs-below.as.css` file, the code is optimized for `1920x1080` resolutions, so see above for fixes if you have issues with the tabs overlapping the bookmarks toolbar.

### Tab-separators.as.css
Adds subtle separators between tabs.
![Tab separators preview](https://i.imgur.com/BkOtU5b.png)

### Tab-state-coloring.as.css
This will change the tabs text color when the state of tabs is unread, loading, loaded but unread...
**You can also change the background color of tabs for each state with it**, just make sure to change the `background-color` rules for the tab background color, and the `color` one for text color.

By default it's not possible to change the unread state of tabs since they are not labeled as unread (Firefox removed the unread state of tabs a few versions ago), so if you want to change that state read below, otherwise, you can just use the code without patching your firefox.

You can patch your Firefox using the [patcher](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/releases) by choosing your Firefox version, and the "Enable unread state on tabs" option.
This will add a "utils" folder and a "setAttribute_unread.uc.js" file to your chrome folder, which are required to customize unread tabs with userChrome.

Alternatively, if you use MacOS or something goes wrong with the patcher, you can always do the manual patching with the method explained in [JS Loader](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions/JS%20Loader) folder from this repository, and then copying the [setAttribute_unread.uc.js](https://raw.githubusercontent.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/master/CSS%20tweaks/Tabs/setAttribute_unread.uc.js) file to your [chrome folder](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/wiki/Chrome-and-Root-folders#the-chrome-folder).

### Rounded-contected-tabs.as.css
Adds rounded tabs similar to those of chromium browsers.
You can change the tab line to be any color you want (by default uses your lightweight theme color).

![Rounded tabs preview](https://i.imgur.com/0K2E48w.png)
