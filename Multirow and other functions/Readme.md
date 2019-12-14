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

<p>If you want to do everything manually, you will have to copy necesary files to enable the use of JS functions first following the method inside the <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions/JS%20Loader">JS Loader</a> folder. After that, to install any of the functions just copy the file(s) you are interested on inside any of the folders here to your <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions#the-chrome-folder">chrome folder</a>.</p>

<h2>The chrome folder</h2>
<p>This is where you have to place the files of this repository.</p>
<p>The fastest way to find it is to just type <code>about:support</code> on the URL bar of your firefox, and then click the <b>open folder</b> button inside the "profile folder" section.</p>
<p>After this, your profile folder will be open. You may or may not see the chrome folder. If you don't see it, just create it and place inside the <code>userContent.css</code> and <code>userChrome.css</code> files.</p>

<p>If you want to know the exact location for profile folders (information taken from <a href="http://kb.mozillazine.org/Profile_folder_-_Firefox">here</a>):</p>

<h4>On Windows 7 and above, profile folders are in this location, by default:</h4>

<pre>C:\Users\(Windows login/user name)\AppData\Roaming\Mozilla\Firefox\Profiles\(profile folder)</pre>
  
<p>The AppData folder is a hidden folder; to show hidden folders, open a Windows Explorer window and choose "Tools → Folder Options → View (tab) → Show hidden files and folders".</p>

<p>You can also use this path to find the profile folder, even when it is hidden:</p>

<pre>%APPDATA%\Mozilla\Firefox\Profiles\(profile folder)</pre>

<h4>On Linux, profile folders are located in this other location:</h4>

<pre>/home/(Your-username)/.mozilla/firefox/(profile folder)</pre>

<p>The ".mozilla" folder is a hidden folder. To show hidden files in Nautilus (Gnome desktop's default file browser), choose "View -> Show Hidden Files". On others such as Dolphin (Kubuntu's default file browser), you'd have to choose "Control -> Hidden files"</p>

<h4>On Mac, profile folders are in one of these locations:</h4>

<pre>~/Library/Application Support/Firefox/Profiles/(profile folder)
~/Library/Mozilla/Firefox/Profiles/(profile folder)</pre>

<p>The tilde character (~) refers to the current user's Home folder, so ~/Library is the /Macintosh HD/Users/(username)/Library folder. For OS X 10.7 Lion and above, the ~/Library folder is hidden by default.</p>

<p>You can make them visible by hitting the following key combination inside Finder:</p>
<pre>CMD + SHIFT + .</pre>
<p>This will also cause any file icons to take on a hazy, 50% alpha look. To restore the old settings (hide the files and make the icons look normal) hit the same combination again.<p>