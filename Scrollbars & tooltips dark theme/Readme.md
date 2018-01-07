<h1>Custom Scrollbars and dark tooltips through UserChrome.js</h1>
<img src="https://i.imgur.com/qe6tGJW.png">
<p>This method should be the same for all OS, and it adds CSS code with agent sheet access level through JavaScript to change the scrollbars (This means that we aren't making JavaScript scrollbars, which can be laggy sometimes. We would be actually styling the default scrollbars through Agent Sheet level CSS, which couldn't be done by default on userchrome.css because of some fix for a bug by Mozilla) as well as all the tooltips.</p>

<p>The only little problem with this method is that you will have to delete the start up cache files for the changes to take effect every time you make a change to any of the <b>*.uc.js</b> files (which are the ones where the CSS rules go to change the scrollbar or tooltip colors).</p>

<p>To clear the start up cache you have to type <code>about:profiles</code> on firefox URL bar, go to that page, open the local profile directory through that page, and then delete all files inside the "startupCache" folder.</p>

<p>This is <b>NOT</b> the same profile directory where you have to place the "chrome" folder. You access that one through <code>about:support</code>, and then clicking the "open folder" button on the "profile folder" section.</p>
<p>You can edit the scrollbars appearance changing the CSS rules inside the <b>scrollbar.uc.js</b> file, just as you would change them with the old method in this repository.</p>
  
<h2>Installation</h2>
<p>To install userChrome.js you have to do a few more steps than just copying it to your chrome folder. The reason for this is that Firefox doesn't allow userChrome.js by default, so we have to apply certain modifications so that it allows it.</p>

<p>First, copy the contents of the "Root" folder found here to Firefox's root folder. These contents include the <b>config.js</b>, <b>userChromeJS.js</b> and the <b>config-prefs.js</b> file inside the "defaults/pref" folders (You have to keep this path structure when moving the files to Firefox root folder). If you don't know where that is, you can find an explanation on how to find it in the last section of this page.<p>
  
<p>Once you have done this, all you have to do is open the chrome folder inside your profile folder (If you don't know where that is you can find an explanation on the section below) and place the contents that are inside the "profile" folder here in there. This is the same folder where you would place userchrome.css and usercontent.css.<p>

<p>After that, type <code>about:profiles</code> on the URL bar of firefox, and open the local profile folder through that page. In here you will have enter the "startupcache" folder and delete all files here so that the scrollbars show properly next time you reset firefox (You will have to delete the cache every time you make a change to the scrollbars.uc.js file for it to take effect). You may have to close firefox to be able to delete all the files in the "startupcache" folder.</p>

<p><b>Optional</b>: If you aren't fully convinced by the default custom scrollbar, you can try any of the other scrollbar types (only use one) using any of the scrollbar-*.uc.js files inside the "alternative scrollbars" instead of the scrollbar.uc.js inside the "profile" folder in here.</p>

<p><b>Optional</b>: You may use the <b>tooltips.uc.js</b> file or any of the variants included on the "alternative tooltips" (such as the semi-transparent background ones) if you want dark tooltips (such as the url tooltip, or when you hover over a bookmark).</p>

<p>If you have done everything right, you should see the custom scrollbars next time you open firefox (or after you restart it)</p>

<h4>Short version:</h4>
<ul>
  <li>Copy the contents of the "Root" folder found in this repository to Firefox root folder.</li>
  <li>Copy the contents of the "Profile" folder found in this repository to the chrome folder inside your profile folder.</li>
  <li>Open the <code>about:profiles</code> URL with firefox, and open the local profile folder there.</li>
  <li>Open the "startupcache" folder and delete everything there.</li>
  <li><b>Optional</b>: You can try the other scrollbar types inside the "alternative scrollbars" folder.</li>
  <li><b>Optional</b>: Use the <b>tooltips.uc.js</b> file to change the default color of the tooltips to fit the theme (or any of the variants on the "alternative tooltips", such as the semi-transparent background one).</li>
</ul>

<h3>The chrome folder</h3>
<p>If you don't know where that is, just type <code>about:support</code> on the URL bar of your firefox, and in the page
you will be redirected to, on the section labed as "profile folder" click the <b>open folder</b> button.</p>
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

<p>You can make them visible by typing the following in a terminal window.</p>
<pre>defaults write com.apple.finder AppleShowAllFiles TRUE
killall Finder</pre>
<br /><p>This will also cause any file icons to take on a hazy, 50% alpha look. To restore the old settings (hide the files and make the icons look normal) issue the same commands again, but enter FALSE instead of TRUE.<p>  
  
<h3>Firefox root folder depending on your OS</h3>

<p>Depending on your OS, the root folder will be in a different location (information taken from <a href="http://kb.mozillazine.org/Installation_directory">here</a>):</p>

<h4>For Windows, you can find firefox root folder here:</h4>

<pre>32bits Firefox -> C:\Program Files (x86)\Mozilla Firefox\
64bits Firefox -> C:\Program Files\Mozilla Firefox\</pre>

<p>If you have a 32-bits Windows, you will only see the 64-bits path.</p>

<h4>For Linux, you can find the root folder in this path by default:</h4>

<pre>/usr/lib/firefox</pre>

<p>In some cases you might find a difference between 32 and 64 bits program installation paths in Linux, in that case you'd find the path here:</p> 

<pre>/usr/lib64/firefox</pre>

<p>The installation directory path may also vary depending on the distribution, and if you use a package manager to install the application from their repository.</p>

<h4>For Mac, you can find the firefox root folder in this path:</h4>

<pre>/Applications/Firefox.app/</pre>

<p>To open "Firefox.app", Ctrl-click it and select Show Package Contents. If you simply click it, you will start the application.</p>
