## Multi-row tabs
You can have multi-row tabs using any of these javascript files.
There are 2 versions, one that creates infinite rows of bars as you keep opening tabs, and another that shows a max number of rows that you can specify before showing a scrollbar to show the rest of rows.

These versions have been tested with FF70+ up to FF80.0a1 (2020-07-01)

**First make sure that you have patched Firefox with either [the patcher](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/releases) (which also lets you install any of these files automatically along with the patch), or with the method explained in the [JS Loader](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions/JS%20Loader) folder to use any of these files.**

**If using the patcher, make sure that the default profile found is the one you are currently using (you can check this in `about:profiles`).**

To avoid problems using multiple files with the tabs below fixes, I split the tabs below tweak into a standalone file. If you want to have tabs below the url bar, use the files inside the [tabs below](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions/Tabs%20below) folder.

### MultiRowTabLiteforFx.uc.js
Shows all tabs you currently have open splitting them on rows, without any limit to the amount of rows to show. Choose this option if you want to always see all the tabs you have open without limits to the number of rows. When dragging tabs around, an arrow will show where the dragged tab will be placed.

![Multirow unlimited](https://i.imgur.com/GWSgqD9.png)

### MultiRowTab-scrollable.uc.js
Shows all tabs you currently have open splitting them on rows up to a max of 3 rows by default (can be changed using the variable inside the file). After the max number of rows has been reached, a scrollbar will be shown to be able to scroll around the extra tabs. When dragging tabs around, an arrow will show where the dragged tab will be placed.

![Multirow scrollable animation](https://i.imgur.com/2YUO9vq.png)

### MultiRowTab-scrollable-autohide.uc.js
This version is the same as scrollable multirow, except the scrollbars are only shown when you hover over the tabs area. It fixes some very specific issue when loading a session restore and loading a long page with a lot of content, which sometimes would make some webarea scrollbars get "stuck".

## Tab sizing
The size of tabs in the last row is by default resizable, (like in the pictures above, which is the default Firefox behaviour) which will make them shrink as more tabs are fit inside the row. If you want to make all the tabs have a fixed width (so that tabs in the last row won't resize depending on how many tabs are open in that row), you will have to edit the file and change the variable `--tab-growth` to 0 (which will use the value of `browser.tabs.tabMinWidth` in **about:config** as their fixed width).

![Tab sizing example](https://i.imgur.com/twzsQ6V.png)

It's also possible to keep tab resizability but change the min-width of tabs through `browser.tabs.tabMinWidth` as well.

As for tab max size, it can't be changed without causing issues with tab session managers (The issue made tab session managers to save the last 3 closed tabs when they were not suposed to), which is the reason why there isn't an option to change this inside here anymore.