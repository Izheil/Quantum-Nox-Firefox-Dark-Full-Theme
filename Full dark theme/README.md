<h1>Full dark theme for firefox</h1>
<p>Following the method described here, you will be able to give dark colors to firefox as shown in the following picture:</p>

<img src="https://i.imgur.com/zNKhEV6.png" title="Dark firefox UI with custom background" />

<img src="https://i.imgur.com/bEleqP7.png" title="Dark addons" />

<h2>Installation</h2>

<p><strong>Note: As of Firefox 69, you will need to enable the use of these files through a configuration setting.</strong> The preference in question is <code>toolkit.legacyUserProfileCustomizations.stylesheets</code>. Here is how you change its value:
<ol>
	<li>Load <code>about:config</code> in the Firefox address bar.</li>
    	<li>Confirm that you will be careful.</li>
    	<li>Search for <code>toolkit.legacyUserProfileCustomizations.stylesheets</code> using the search at the top.</li>
	<li>Toggle the preference. <code>True</code> means Firefox supports the CSS files, <code>False</code> that it ignores them.</li>
</ol>

<h4>Step by step:</h4>
<ul>
  <li>Type <code>about:support</code> in your URL bar, then go to that page.</li>
  <li>Click the "open folder" button inside the "profile folder" section.</li>
  <li>Create a folder named "chrome" in your profile folder if it doesn't exist yet.</li>
  <li>Place all files (.css files) from this folder to the "chrome" folder.</li>
  <li><b>Optional</b>: If you want to use the custom dark scrollbars, or dark tooltips, you will also have to enable JS injection using the installer in <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/releases">releases</a> (just don't select any function to install when patching if you don't need them), or patch your firefox manually with the method described <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions/JS%20Loader">here</a>.</li>
  <li><b>Optional</b>: Edit userChrome.css to change any style you aren't fully convinced with (or to give a different style to the unread tabs, etc...).</li>
  <li><b>Optional</b>: You can also edit userChrome.css to change the background of the <code>about:home</code> page.</li>
  <li><b>Optional</b>: If you want a different style for the scrollbars or the tooltips, use any of the alternatives on the <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Full%20dark%20theme/Alternative%20scrollbars%20%26%20tooltips">Alternative scrollbars & tooltips</a> folder.</li>
  <li><b>Optional</b>: If you want the default scrollbar style (userChrome still paints it dark), or white tooltips, don't copy the relevant CSS files for them.</li>
  <li><b>Optional</b>: If you want a dark version of either of the addons mentioned in the <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme#addon-dark-themes">addons dark themes section</a> in the front page of this repository, change the UUID's of them inside <code>addons.css</code>. An explanation on how to do so is given inside the file.</li>
</ul>

<p>If you have copied everything right, the folders structure should look something like this:</p>
<p>Structure of <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/wiki/Chrome-and-Root-folders#the-chrome-folder">the chrome folder</a> files inside your profile folder:</p>
<ul>
  <li><b>utils (folder) -> Only if you want to use the *.as.css and *.uc.js files.</b></li>
  <li>addons.css</li>
  <li>scrollbars.as.css</li>
  <li>setAttribute_unread.uc.js</li>
  <li>tooltips.as.css</li>
  <li>userChrome.css</li>
  <li>userContent.css</li>
</ul>

<p>Structure of <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/wiki/Chrome-and-Root-folders#firefox-root-folder">firefox root folder</a> files (where your firefox is installed):</p>
<ul>
  <li>browser (folder)</li>
  <li>defaults (folder)</li>
  <ul>
    <li>pref (folder)</li>
    <ul>
      <li>channel-prefs.js</li>
      <li><b>config-prefs.js</b></li>
    </ul>
  </ul>
  <li>fonts (folder)</li>
  <li>uninstall (folder)</li>
  <li>(Other optional folders might appear here)</li>
  <li>firefox.exe (or other Firefox executable depending on your OS)</li>
  <li><b>config.js</b></li>
  <li>Other .dll files</li>
</ul>

<p>Bolded files or folders mark the required things to enable JS injection.</p>

<h2>The userChrome.css file</h2>

<p>The userChrome file turns dark all context menus, bookmarks, the url bar, the search bar, the main menu, and the toolbar. 
It will, although, not turn dark the extension popups you may have. <p>
<img src="https://i.imgur.com/wWjBcqz.png" title="Dark search menu (spanish)" />
<img src="https://i.imgur.com/7zj3SSq.png" title="Dark context menu (spanish)" />
<p>It will also turn dark the autocomplete popups (mostly a side-effect)</p>
<p>userChrome.css is also the file that enables loading of external (placed in the chrome folder) .css and .js files through the use of <code>userChrome.xml</code> (such as <code>scrollbars.as.css</code> or <code>MultiRowTabLiteforFx.uc.js</code>).</p>

<h2>The userContent.css file</h2>

<p>The userContent file will turn dark all the <code>about:about</code> pages.</p>
<img src="https://i.imgur.com/mKWPUSk.png" title="Dark firefox about: pages" />
<img src="https://i.imgur.com/97ebC1x.png" title="Dark addons page" />

<p>It will also turn dark the <a href="https://addons.mozilla.org">Mozilla addons page</a>, both the old and the new, the file explorer inside firefox, and the "view source of page" page.</p>