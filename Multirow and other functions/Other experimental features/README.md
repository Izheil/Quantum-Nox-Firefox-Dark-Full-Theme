<h2>Other experimental features</h2>
<p>Here go any other experimental features that aren't the main focus of the theme and their description. You shouldn't really need to install these unless you want some very specific function.</p>

<p>You need to place <b>userchrome.xml</b> (If you already have one from this repository, you don't need to change it) on your <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions#the-chrome-folder">chrome folder</a> along with any of these files for them to work, along with it's binding rule on <code>userchrome.css</code>, which is already added in any of the userchrome versions of this repository.</p>
<p>For just the <code>userchrome.css</code> with the binding (and no other code), use the one inside this folder, unless you want to add it to your own custom userchrome, in which case you have to copy this rule inside it:</p>

<pre>
/* This enables the use of JS external files */
toolbarbutton#alltabs-button {
    -moz-binding: url("userChrome.xml#js")}
</pre>

<p>For the empty userchrome with just that rule, you can find it inside the <b>Multirow tabs</b> folder inside the repository.</p>

<p>There are probably better alternatives out there, so you should only use these if you really couldn't find it anywhere else (since, as mentioned, these are experimental)</p>

<h3>Mac-fullscreen-fix-toolbox-autohide.uc.js</h3>
<p>Forces autohide of the toolbar in fullscreen mode to fix a common issue on Mac devices where the toolbar won't do this even with the setting enabled. Windows and Linux users shouldn't need this (since it already autohides if you have it toggled in the context menu of the toolbar in fullscreen mode).</p>

<h3>Bookmarks-toggle.uc.js</h3>
<p>Toggles visibility of the bookmarks toolbar when pressing F2 (you can change which keys in the file). You need to have the "fullscreen fix" disabled on userchrome.css if using any of the "CSS tweaks" versions from this repository.</p>

<h3>Navigator-toolbox-autohide.uc.js</h3>
<p>Toggles visibility of the whole navigation toolbox as if you were on fullscreen, so that it's only visible when you have the mouse over it, or when hovering the mouse to the top of the screen when it's hidden. You can also maker bigger the hitbox to trigger the visibility of the toolbox changing the height of <code>fsToggler.style.height</code>at the bottom of the script from 10px to anything you want (just note that the bigger you make it, the more web area content will be unclickable on top).</p>

<h3>Navigator-toolbox-autohide-tabs-below.uc.js</h3>
<p>Same as navigator toolbox autohide, except that it shows the tabs below (you have to disable the tweak on userchrome.css if you had it enabled). You can also maker bigger the hitbox to trigger the visibility of the toolbox changing the height of <code>fsToggler.style.height</code>at the bottom of the script from 20px to anything you want (just note that the bigger you make it, the more web area content will be unclickable on top).</p>

<h3>Navigator-toolbox-hide-by-keypress.uc.js</h3>
<p>Hides the navigation toolbox when pressing a key (F1 by default) when NOT in fullscreen mode. You can change the binded key through the variables inside the file..</p>

<h3>Test.as.css</h3>
<p>This is a test file to check that both external non-userchrome css files and js files are loaded through <code>userchrome.xml</code>. It draws a red border around all editable elements inside firefox UI.</p>