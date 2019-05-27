<h2>Tabs below standalones</h2>
<p>If you have the rules to change the tabs toolbar below the urlbar added to your userchrome, you don't need these. These are just a convenient way to toggle tabs below tweak by copying a single file to your <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions#the-chrome-folder">chrome folder</a>. Alternatively, if you don't want to apply the <b>userchrome.xml</b> fix and only want the tabs below fix, you could just copy the code of the file you want to apply, and copy it to your <code>userchrome.css</code> file.</p>

<p>If you want to use these files as is, you need to place <b>userchrome.xml</b> (If you already have one from this repository, you don't need to change it) on your <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions#the-chrome-folder">chrome folder</a> along with any of these files for them to work, along with it's binding rule on <code>userchrome.css</code>, which is already added in any of the userchrome versions of this repository.</p>
<p>For just the <code>userchrome.css</code> with the binding (and no other code), use the one inside this folder, unless you want to add it to your own custom userchrome, in which case you have to copy this rule inside it:</p>

<pre>
/* This enables the use of JS external files */
toolbarbutton#alltabs-button {
    -moz-binding: url("userChrome.xml#js")}
</pre>

<p>For the empty userchrome with just that rule, you can find it inside this folder in the repository.</p>

<h3>Tabs-below-Menu-onTop.as.css</h3>
<p>Changes the order of the toolbars inside the navigation box. This one sets the position of the tab bar below the url bar, and the menu bar (the one with file, edit, etc...) to be on top of all the other bars (you need to have the menu bar toggled as always visible). <b>If you use this file, delete any code you had on userchrome.css to change the tabs position to avoid any conflict</b>.</p>

<h3>Tabs-below-Menu-overTabs.as.css</h3>
<p>Changes the order of the toolbars inside the navigation box. This one sets the position of the tab bar below the url bar, and the menu bar (the one with file, edit, etc...) to be right above the tabs bar, but below the url bar. <b>If you use this file, delete any code you had on userchrome.css to change the tabs position to avoid any conflict</b>.</p>