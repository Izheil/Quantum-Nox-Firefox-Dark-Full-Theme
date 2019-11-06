<h2>Tabs below standalones</h2>
<p>If you have the rules to change the tabs toolbar below the urlbar added to your userChrome, you don't need these. These are just a convenient way to toggle tabs below tweak by copying a single file to your <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions#the-chrome-folder">chrome folder</a>.

<b>First make sure that you have patched Firefox with the method explained in the <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions/JS%20Loader">JS Loader</a> folder to use any of these files.</b>

<p>Alternatively, if you don't want to apply the patch from above and only want the tabs below fix, you could just copy the code of the file you want to apply here to your <code>userChrome.css</code> file.</p>

<p><strong>Note: If you go the <code>userChrome.css</code> way, you will need to enable the use of these <code>userChrome.css</code> through a configuration setting.</strong> The preference in question is <code>toolkit.legacyUserProfileCustomizations.stylesheets</code>. Here is how you change its value:
<ol>
	<li>Load <code>about:config</code> in the Firefox address bar.</li>
    	<li>Confirm that you will be careful.</li>
    	<li>Search for <code>toolkit.legacyUserProfileCustomizations.stylesheets</code> using the search at the top.</li>
	<li>Toggle the preference. <code>True</code> means Firefox supports the CSS files, <code>False</code> that it ignores them.</li>
</ol>

<h3>Tabs-below.as.css</h3>
<p>Changes the order of the toolbars inside the navigation box. This one sets the position of the tab bar below the url bar, and the menu bar (the one with file, edit, etc...) to be on top of all the other bars (you need to have the menu bar toggled as always visible). <b>If you use this file, delete any code you had on userChrome.css to change the tabs position to avoid any conflict</b>.</p>