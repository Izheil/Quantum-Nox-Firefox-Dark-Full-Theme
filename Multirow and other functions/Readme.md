<h1>Multirow and other custom functions through JS injection</h1>
<p>You can load other CSS files or JS files that couldn't be loaded in a regular way through JS injection, which lets us modify the scrollbars further, or change the behaviour of tabs (like for multirow)</p>
<p>Mozilla finally removed all XBL bindings from firefox, so in advance of the removal of the posibility to inject JS scripts through <b>userchrome.xml</b>, I decided to update the patching method to another one that doesn't rely on this.</p>
<p>If you are still using the old userchrome.xml method, you can keep using it until Mozilla decides to deprecate XUL completelly, in which case it will stop working and you will have to use the new one explained below.</p>

<p>As with every other method, if some changes of your script aren't getting updated after changing it and restarting Firefox, <b>the first thing to try is to delete the start up cache files for the changes of any <i>*.uc.js</i> files (like the multi-row one, or the bookmarks toggler) to take effect</b>.</p>

<p>To clear the start up cache you have to type <code>about:profiles</code> on firefox URL bar, go to that page, open the local profile directory through that page, and then delete all files inside the "startupCache" folder.</p>

<p>This is <b>NOT</b> the same profile directory where you have to place the files from any of these folders. You access that one through <code>about:support</code>, and then clicking the "open folder" button on the "profile folder" section.</p>

<h2>Contents of each folder:</h2>
<ul>
	<li><a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions/JS%20Loader">JS Loader</a>: These are the files that will enable the use of the userscripts contained in the other folders.</li>
	<li><a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions/Multirow%20tabs">Multirow tabs</a>: Files to enable multiple rows of tabs instead of mono-row. You can chose between infinite rows and scrollable rows version. <ul><li><img src="https://i.imgur.com/qqQn4Ky.png"></li></ul></li>
	<li><a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions/Other%20features">Other features</a>: You can find some additional features that can only be done through javascript here, such as autohidding the UI of Firefox, toggling visibility of bookmarks bar with a keypress, or focusing tabs on hover.</li>
	<li><a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions/Tabs%20below">Tabs below</a>: These files will change the position of the Tabs bar to be below the URL bar. You can edit the rules within them to change the order to your liking.</li>
</ul>

<h2>Installation</h2>
<p>The easiest way to install them is to use <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/releases">the patcher</a> created to enable JS injection, which will also let you install some of the functions automatically. All you need to do is <b>check that the profile folder found in the patcher is the one that you are currently using</b> (you can check this in <code>about:profiles</code>), and then select the functions you want to install.</p>

<p>You can also use the patcher to only copy the JS enabling part to your profile folder (unticking every function in the patcher so that it only applies the JS enabling part), and then copy the function files manually.</p>

<p>If you want to do everything manually, you will have to copy necesary files to enable the use of JS functions first following the method inside the <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions/JS%20Loader">JS Loader</a> folder. After that, to install any of the functions just copy the file(s) you are interested on inside any of the folders here to your <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/wiki/Chrome-and-Root-folders#the-chrome-folder">chrome folder</a>.</p>