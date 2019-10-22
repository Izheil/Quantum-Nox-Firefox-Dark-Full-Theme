<h2>Other experimental features</h2>
<p>Here go any other experimental features that aren't the main focus of the theme and their description. You shouldn't really need to install these unless you want some very specific function.</p>

<b>First make sure that you have patched Firefox with the method explained in the <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions/JS%20Loader">JS Loader</a> folder to use any of these files.</b>

<b>To avoid problems using multiple files with the tabs below fixes, I split the tabs below tweak into a standalone file. If you want to have tabs below the url bar, use the files inside the <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions/Tabs%20below">tabs below</a> folder.</b>

<p>There are probably better alternatives out there, so you should only use these if you really couldn't find it anywhere else (since, as mentioned, these are experimental)</p>

<h3>Mac-fullscreen-fix-toolbox-autohide.uc.js</h3>
<p>Forces autohide of the toolbar in fullscreen mode to fix a common issue on Mac devices where the toolbar won't do this even with the setting enabled. Windows and Linux users shouldn't need this (since it already autohides if you have it toggled in the context menu of the toolbar in fullscreen mode).</p>

<h3>Bookmarks-toggle.uc.js</h3>
<p>Toggles visibility of the bookmarks toolbar when pressing F2 (you can change which keys in the file). You need to have the "fullscreen fix" disabled on userchrome.css if using any of the "CSS tweaks" versions from this repository.</p>

<h3>Navigator-toolbox-autohide.uc.js</h3>
<p>Toggles visibility of the whole navigation toolbox as if you were on fullscreen, so that it's only visible when you have the mouse over it, or when hovering the mouse to the top of the screen when it's hidden. You can also maker bigger the hitbox to trigger the visibility of the toolbox changing the height of <code>fsToggler.style.height</code>at the bottom of the script from 10px to anything you want (just note that the bigger you make it, the more web area content will be unclickable on top).</p>

<h3>Navigator-toolbox-hide-by-keypress.uc.js</h3>
<p>Hides the navigation toolbox when pressing a key (F1 by default) when NOT in fullscreen mode. You can change the binded key through the variables inside the file..</p>

<h3>Switch-to-tab-on-hover.uc.js</h3>
<p>Lets you switch to another tab just by hovering over it.</p>

<h3>Test.as.css</h3>
<p>This is a test file to check that both external non-userchrome css files and js files are loaded through <code>userchrome.xml</code>. It draws a red border around all editable elements inside firefox UI.</p>