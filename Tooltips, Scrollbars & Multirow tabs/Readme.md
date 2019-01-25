<h1>Custom Scrollbars and dark tooltips through UserChrome.js</h1>
<img src="https://i.imgur.com/qe6tGJW.png" title="Dark blue scrollbar">
<p>This method should be the same for all OS, and it works by binding to a random DOM element some JS code, letting us run other JS files, or AGENT_SHEET level CSS.</p>

<p>You could make your own files, as far as you follow this naming convention:</p>
<ul>
	<li><code>*.uc.js</code> for javascript files.</li>
	<li><code>*.as.css</code> for AGENT_SHEET level CSS files.</li>
</ul>

<h3>If you only want multirow, scrollbars, or the tooltips, you DON'T need any of the files from the theme folders.</h3>
<p>All you need is to create your own empty userchrome.css, with only this content:</p>

<pre>
/* DO NOT DELETE THIS LINE */
@namespace url("http://www.mozilla.org/keymaster/gatekeeper/there.is.only.xul");

/* This enables the use of JS external files */
toolbarbutton#alltabs-button {
    -moz-binding: url("userChrome.xml#js")}
</pre>

<p>The only little problem with this method is that <b>you will have to delete the start up cache files for the changes to take effect every time you make a change to any of the <i>*.uc.js</i></b> files (which are the ones where the CSS rules go to change the scrollbar or tooltip colors).</p>

<p>To clear the start up cache you have to type <code>about:profiles</code> on firefox URL bar, go to that page, open the local profile directory through that page, and then delete all files inside the "startupCache" folder.</p>

<p>This is <b>NOT</b> the same profile directory where you have to place the "chrome" folder. You access that one through <code>about:support</code>, and then clicking the "open folder" button on the "profile folder" section.</p>
<p>You can edit the scrollbars appearance changing the CSS rules inside the <b>scrollbar.as.css</b> file.</p>
  
<h2>Installation</h2>
<p>You can find a video tutorial <a href="https://youtu.be/FHV1-LbX_Vo">here</a>. The folder names will be a bit different, but it should be understable.</p>

<h4>Short version:</h4>
<ul>
  <li>Copy the contents of the "Chrome" folder found in this repository to the <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Tooltips%20%26%20Scrollbar%20customizations#the-chrome-folder">the chrome folder</a> inside your profile folder (except the <code>checkboxes.as.css</code> file if you have an OS that already colors checkboxes dark).</li>
  <li>Open the <code>about:profiles</code> URL with firefox, and open the local profile folder there.</li>
  <li>Open the "startupcache" folder and delete everything there.</li>
  <li><b>Optional</b>: You can try the other scrollbar types inside the "alternative scrollbars" folder.</li>
  <li><b>Optional</b>: Use the <code>tooltips.as.css</code> file to change the default color of the tooltips to fit the theme (or any of the variants on the "alternative tooltips", such as the semi-transparent background one).</li>
  <li><b>Optional</b>: If you prefer scrollable multi-rows, change the multirows file (<b>MultiRowTabLiteforFx.uc.js</b>) for the scrollable version (<b><code>MultiRowTab-scrollable.uc.js</code></b>) inside the "Multirow scrollable versions" folder.</li>
</ul>

<h4>Detailed explanation</h4>
<p>First you need to enable the use of javascript files from your profile folder. All you need to do is to copy <code>userChrome.css</code> and <code>userChrome.xml</code> to your <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Tooltips%20%26%20Scrollbar%20customizations#the-chrome-folder">chrome folder</a>.This is the same folder where you would place <code>userchrome.css</code> and <code>usercontent.css</code>.</p>

<blockquote><b>For those that are only interested on the scrollbars or multirow tabs but not the dark background, or want to use their own <code>userChrome.css</code>, this is the only rule you need to add to it (which you have to place in the <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Tooltips%20%26%20Scrollbar%20customizations#the-chrome-folder">chrome folder</a>, like you would even if you used the userchrome from this repository):</b>
<pre>/* This enables the use of JS external files */
toolbarbutton#alltabs-button {
    -moz-binding: url("userChrome.xml#js")}</pre>
If you are <a href="http://kb.mozillazine.org/index.php?title=UserChrome.css&printable=yes">creating a new <code>userChrome.css</code></a> file only for this, make sure to also add these lines on top of the file:
<pre>/* DO NOT DELETE THIS LINE */
@namespace url("http://www.mozilla.org/keymaster/gatekeeper/there.is.only.xul");</pre>
In either case, remember to also place <code>userchrome.xml</code> into your <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Tooltips%20%26%20Scrollbar%20customizations#the-chrome-folder">chrome folder</a> as well.
</blockquote>

<h4>If you have an OS that draws checkboxes and radio buttons dark already, do NOT copy the <code>checkboxes.as.css</code> file into the chrome folder, or it will turn them white. Only place this file in your profile folder if your OS draws them whiteish (like windows when you don't use a custom theme).</h4>

<p>After that, type <code>about:profiles</code> on the URL bar of firefox, and open the local profile folder through that page. In here you will have enter the "startupcache" folder and delete all files here so that the scrollbars show properly next time you reset firefox (You will have to delete the cache every time you make a change to the <code>scrollbars.as.css</code> file for it to take effect). You may have to close firefox to be able to delete all the files in the "startupcache" folder.</p>

<blockquote><b>Optional</b>: If you aren't fully convinced by the default custom scrollbar, you can try any of the other scrollbar types (only use one) using any of the <code>scrollbar-*.as.css</code> files inside the "alternative scrollbars" instead of the <code>scrollbar.as.css</code> inside the "Chrome" folder in here, or you can edit the scrollbars appearance editing only past the `s you will find inside the <code>scrollbars.as.css</code> file (which is the CSS code injected by javascript to edit the scrollbars appearance).</blockquote>

<blockquote><b>Optional</b>: You may use the <b>tooltips.as.css</b> file or any of the variants included on the "alternative tooltips" (such as the semi-transparent background ones) if you want dark tooltips (such as the url tooltip, or when you hover over a bookmark).</blockquote>

<blockquote><b>Optional</b>: If you are going to use multi-row tabs, you can choose the scrollable version inside the "Multirow scrollable versions" folder. The non-scrollable (the default) one will have the height of 1 row of tabs at first, and will keep growing to adapt to how many rows of tabs you have open (since it won't scroll, the height of the tabs box will keep growing as you open more rows of tabs, and will decrease as you close them), while the scrollable one will grow up to a max of the set number of rows (3 by default), and then will show a scrollbar to scroll around them. To use the scrollable version, you will have to delete the other multirow file and move the scrollable version to your <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Tooltips%20%26%20Scrollbar%20customizations#the-chrome-folder">chrome folder</a> (only one file of each kind should be used at a time).</blockquote>

<p>If you have done everything right, you should see the custom scrollbars next time you open firefox (or after you restart it)</p>

<h3>The chrome folder</h3>

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
