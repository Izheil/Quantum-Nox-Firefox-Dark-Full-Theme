<h1>Multirow and other custom functions through JS injection</h1>
<p>You can load other CSS files or JS files that couldn't be loaded in a regular way through JS injection, which lets us modify the scrollbars further, or change the behaviour of tabs (like for multirow)</p>
<p>It should be the same for all OS, and it works by binding to a random DOM element some JS code, letting us run other JS files, or AGENT_SHEET level CSS.</p>

<p>For this method, we use <code>userchrome.css</code> and <code>userchrome.xml</code> to enable the previously mentioned files (for further details on what is needed check the folders inside this one).</p>

<p>You could make your own files, as far as you follow this naming convention:</p>
<ul>
	<li><code>*.uc.js</code> for javascript files.</li>
	<li><code>*.as.css</code> for AGENT_SHEET level CSS files.</li>
</ul>

<p>The only little problem with this method is that <b>you will have to delete the start up cache files for the changes to take effect every time you make a change to any of the <i>*.uc.js</i></b> files (like the multi-row one, or the bookmarks toggler).</p>

<p>To clear the start up cache you have to type <code>about:profiles</code> on firefox URL bar, go to that page, open the local profile directory through that page, and then delete all files inside the "startupCache" folder.</p>

<p>This is <b>NOT</b> the same profile directory where you have to place the files from any of these folders. You access that one through <code>about:support</code>, and then clicking the "open folder" button on the "profile folder" section.</p>

<h2>Contents of each folder:</h2>
<ul>
	<li><a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions/Multirow%20tabs">Multirow tabs</a>: Files to enable multiple rows of tabs instead of mono-row. You can chose between infinite rows and scrollable rows version. <ul><li><img src="https://i.imgur.com/qqQn4Ky.png"></li></ul></li>
	<li><a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions/Other%20experimental%20features">Other experimental features</a>: You can find some additional features that can only be done through javascript here, such as autohidding the UI of Firefox, or toggling visibility of bookmarks bar with a keypress.</li>
	<li><a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions/Tabs%20below">Tabs below</a>: These files will change the position of the Tabs bar to be below the URL bar. You can edit the rules within them to change the order to your liking.</li>
</ul>

<h3>Installation</h3>
<p>To install any of the files, just copy the file(s) you are interested on inside any of the folders here along with <code>userchrome.xml</code>, and copy them to your chrome folder. You also will need to have enabled the use of <code>userchrome.xml</code> through <code>userchrome.css</code> (you can learn how to do it inside any of the folders).</p>

<h3>The chrome folder</h3>
<p>This is where you have to place the files of this repository.</p>
<p>The fastest way to find it is to just type <code>about:support</code> on the URL bar of your firefox, and then click the <b>open folder</b> button inside the "profile folder" section.</p>
<p>After this, your profile folder will be open. You may or may not see the chrome folder. If you don't see it, just create it and place inside the <code>usercontent.css</code> and <code>userchrome.css</code> files.</p>

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