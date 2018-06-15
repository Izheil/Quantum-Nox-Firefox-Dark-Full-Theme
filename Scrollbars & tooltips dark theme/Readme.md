<h1>Custom Scrollbars and dark tooltips through UserChrome.js</h1>
<img src="https://i.imgur.com/qe6tGJW.png" title="Dark blue scrollbar">
<p>This method should be the same for all OS, and it adds CSS code with agent sheet access level through JavaScript to change the scrollbars (This means that we aren't making JavaScript scrollbars, which can be laggy sometimes. We would be actually styling the default scrollbars through Agent Sheet level CSS, which couldn't be done by default on userchrome.css because of some fix for a bug by Mozilla) as well as all the tooltips.</p>

<p>The other javascript files inside the profile folder here are used to fix other content that can't be themed through userchrome.css or usercontent.css, as well as fixing the tab draggability problem of multi-row tabs (So only copy those that you need to your chrome profile folder).</p>

<p>The only little problem with this method is that <b>you will have to delete the start up cache files for the changes to take effect every time you make a change to any of the <i>*.uc.js</i></b> files (which are the ones where the CSS rules go to change the scrollbar or tooltip colors).</p>

<p>To clear the start up cache you have to type <code>about:profiles</code> on firefox URL bar, go to that page, open the local profile directory through that page, and then delete all files inside the "startupCache" folder.</p>

<p>This is <b>NOT</b> the same profile directory where you have to place the "chrome" folder. You access that one through <code>about:support</code>, and then clicking the "open folder" button on the "profile folder" section.</p>
<p>You can edit the scrollbars appearance changing the CSS rules inside the <b>scrollbar.uc.js</b> file, just as you would change them with the old method in this repository.</p>
  
<h2>Installation</h2>
<p>To install userChrome.js you have to do a few more steps than just copying it to your <a href="https://github.com/Izheil/Firefox-57-full-dark-theme-with-scrollbars/blob/master/Scrollbars%20&%20tooltips%20dark%20theme/Readme.md#the-chrome-folder">the chrome folder</a>. The reason for this is that Firefox doesn't allow userChrome.js by default, so we have to apply certain modifications so that it allows it.</p>

<p>First, copy the contents of the "Root" folder found here to <a href="https://github.com/Izheil/Firefox-57-full-dark-theme-with-scrollbars/blob/master/Scrollbars%20&%20tooltips%20dark%20theme/Readme.md#the-root-folder">Firefox root folder</a>. These contents include the <b>config.js</b>, <b>userChromeJS.js</b> and the <b>config-prefs.js</b> file inside the "defaults/pref" folders (You have to keep this path structure when moving the files to <a href="https://github.com/Izheil/Firefox-57-full-dark-theme-with-scrollbars/blob/master/Scrollbars%20&%20tooltips%20dark%20theme/Readme.md#the-root-folder">Firefox root folder</a>).</p>
<p><strong>NOTE: When using a mac, the <a href="https://github.com/snwflake/Firefox-57-full-dark-theme-with-scrollbars/blob/master/Scrollbars%20%26%20tooltips%20dark%20theme/Root/userChromeJS.js">userChromeJS.js</a> should be placed inside
<pre>/Applications/Firefox.app/Contents/MacOS/</pre> (same folder as the binary). Otherwise it won't load on startup.</strong></p>

<p>Once you have done this, all you have to do is open the <a href="https://github.com/Izheil/Firefox-57-full-dark-theme-with-scrollbars/blob/master/Scrollbars%20&%20tooltips%20dark%20theme/Readme.md#the-chrome-folder">chrome folder</a> inside your profile folder (If you don't know where that is you can find an explanation on the section below) and place the contents that are inside the "profile" folder here in there. This is the same folder where you would place userchrome.css and usercontent.css.</p>

<h4>If you have an OS that draws checkboxes and radio buttons dark already, do NOT copy the "checkboxes.uc.js" file into your profile folder, or it will turn them white. Only place this file in your profile folder if your OS draws them whiteish (like windows when you don't use a custom theme).</h4>

<p>After that, type <code>about:profiles</code> on the URL bar of firefox, and open the local profile folder through that page. In here you will have enter the "startupcache" folder and delete all files here so that the scrollbars show properly next time you reset firefox (You will have to delete the cache every time you make a change to the scrollbars.uc.js file for it to take effect). You may have to close firefox to be able to delete all the files in the "startupcache" folder.</p>

<blockquote><b>Optional</b>: If you aren't fully convinced by the default custom scrollbar, you can try any of the other scrollbar types (only use one) using any of the scrollbar-*.uc.js files inside the "alternative scrollbars" instead of the scrollbar.uc.js inside the "profile" folder in here, or you can edit the scrollbars appearance editing only past the `s you will find inside the scrollbars.uc.js file (which is the CSS code injected by javascript to edit the scrollbars appearance).</blockquote>

<blockquote><b>Optional</b>: You may use the <b>tooltips.uc.js</b> file or any of the variants included on the "alternative tooltips" (such as the semi-transparent background ones) if you want dark tooltips (such as the url tooltip, or when you hover over a bookmark).</blockquote>

<p>If you have done everything right, you should see the custom scrollbars next time you open firefox (or after you restart it)</p>

<h4>Short version:</h4>
<ul>
  <li>Copy the contents of the "Root" folder found in this repository to <a href="https://github.com/Izheil/Firefox-57-full-dark-theme-with-scrollbars/blob/master/Scrollbars%20&%20tooltips%20dark%20theme/Readme.md#the-root-folder">Firefox root folder</a>.</li>
  <li>Copy the contents of the "Profile" folder found in this repository to the <a href="https://github.com/Izheil/Firefox-57-full-dark-theme-with-scrollbars/blob/master/Scrollbars%20&%20tooltips%20dark%20theme/Readme.md#the-chrome-folder">the chrome folder</a> inside your profile folder (except the checkboxes.uc.js file if you have an OS that already colors checkboxes dark).</li>
  <li>Open the <code>about:profiles</code> URL with firefox, and open the local profile folder there.</li>
  <li>Open the "startupcache" folder and delete everything there.</li>
  <li><b>Optional</b>: You can try the other scrollbar types inside the "alternative scrollbars" folder.</li>
  <li><b>Optional</b>: Use the <b>tooltips.uc.js</b> file to change the default color of the tooltips to fit the theme (or any of the variants on the "alternative tooltips", such as the semi-transparent background one).</li>
</ul>

<h3>The root folder:</h3>

<h4>For Windows, you can find firefox root folder here:</h4>

<pre>32bits Firefox -> C:\Program Files (x86)\Mozilla Firefox\
64bits Firefox -> C:\Program Files\Mozilla Firefox\</pre>

<p>If you have a 32-bits Windows, you will only see the 64-bits path.</p>

<h4>For Linux, you can find the root folder in this path:</h4>

<pre>/usr/lib/firefox/</pre>

<p>In some cases you might find a difference between 32 and 64 bits program installation paths in Linux, in that case you'd find the path here:</p> 

<pre>/usr/lib64/firefox/</pre>

<p>The installation directory path may also vary depending on the distribution, and if you use a package manager to install the application from their repository.</p>

<h4>For Mac, you can find the root folder in this path:</h4>

<pre>/Applications/Firefox.app/Contents/Resources</pre>

<p>To open "Firefox.app", Ctrl-click it and select Show Package Contents. If you simply click it, you will start the application.</p>

<h3>The chrome folder</h3>

<p>The fastest way to find it is to just type <code>about:support</code> on the URL bar of your firefox, and then click the <b>open folder</b> button inside the "profile folder" section.</p>
<p>After this, your profile folder will be open. You may or may not see the chrome folder. If you don't see it, just create it and place inside the usercontent.css and userchrome.css files.</p>

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
