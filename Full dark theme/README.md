<h1>Full dark theme for firefox</h1>
<p>Following the method described here, you will be able to give dark colors to firefox as shown in the following picture:</p>

<img src="https://i.imgur.com/zNKhEV6.png" title="Dark firefox UI with custom background" />

<img src="https://i.imgur.com/QEOrYbx.png" title="Dark addons" />

<h2>Installation</h2>
<p>You can check a video guide <a href="https://youtu.be/kNHe6XDgUN4">here</a>.</p>

<h4>Step by step:</h4>
<ul>
  <li>Type <code>about:support</code> in your URL bar, then go to that page.</li>
  <li>Click the "open folder" button inside the "profile folder" section.</li>
  <li>Create a folder named "chrome" in your profile folder if it doesn't exist yet.</li>
  <li>Place all files from this folder inside the "chrome" folder.</li>
  <li><b>Optional</b>: Edit userchrome.css to change any style you aren't fully convinced with (or to give a different style to the unread tabs, etc...).</li>
  <li><b>Optional</b>: You can also edit userchrome.css to change the background of the <code>about:home</code> page.</li>
  <li><b>Optional</b>: If you want a different style for the scrollbars or the tooltips, use any of the alternatives on the <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Full%20dark%20theme/Alternative%20scrollbars%20%26%20tooltips">Alternative scrollbars & tooltips</a> folder.</li>
  <li><b>Optional</b>: If you want the default scrollbar style (userchrome still paints it dark), or white tooltips, don't copy the relevant CSS files for them.</li>
  <li><b>Optional</b>: If you want a dark version of either of the addons mentioned in the <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme#addon-dark-themes">addons dark themes section</a> in the front page of this repository, change the UUID's of them inside <code>addons.css</code>. An explanation on how to do so is given inside the file.</li>
</ul>

<h4>Long explanation:</h4>
<p>Most of the job is already done with the <code>userContent.css</code> and <code>userChrome.css</code>  files that you have to place in the 
<a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Full%20dark%20theme#the-chrome-folder">the chrome folder</a> of your firefox profile. For this to work as intended, you should be using a persona (aka lightweight theme) or the default dark theme (The persona used on the screenshot is "<a href="https://addons.mozilla.org/es/firefox/addon/polygon-dark-by-madonna/">Dark Polygon</a>" by <b>MaDonna</b>.</p>
<p>You can also change the tab line color to Windows current theme color (You have to change the commented line that is described in line 19 inside userChrome.css), and the background image of your lightweight theme to one of your choice.</p>
<p>On line 15 inside usercontent.css you can change the default text color of input boxes for those using a dark OS theme that affects the background of these.</p>
<p>You can also change the background of the <code>about:home</code> and <code>about:newtab</code> pages editting line 19 on userContent.css, and deleting the final "/*", and specifying the route of the image you want to use as background (if it's a link, place it where the "file:///" part is, otherwise, place the path of the file after the "file:///".</p>
<img src="https://i.imgur.com/OhKiBCI.png"></li>
<p>The files <code>scrollbars.as.css</code> and <code>tooltips.as.css</code> give a custom style to the scrollbars, the tooltips to look dark, so if you don't want these to have a custom style, don't copy the files you don't want.</p>
<p>If you would also like a dark version of either <a href="https://addons.mozilla.org/es/firefox/addon/ublock-origin/">Ublock Origin</a>, <a href="https://addons.mozilla.org/es/firefox/addon/video-downloadhelper/">Video Download Helper</a>, <a href="https://addons.mozilla.org/es/firefox/addon/flash-video-downloader/">Flash Video Downloader</a>, <a href="https://addons.mozilla.org/es/firefox/addon/tab-session-manager/">Tab session manager</a>, <a href="https://addons.mozilla.org/es/firefox/addon/undo-closed-tabs-revived/">Undo closed tabs button</a>, <a href="https://addons.mozilla.org/es/firefox/addon/s3download-statusbar/">Download Manager (S3)</a>, <a href="https://addons.mozilla.org/es/firefox/addon/privacy-badger17/">Privacy badger</a>, <a href="https://addons.mozilla.org/es/firefox/addon/noscript/">Noscript</a>, <a href="https://addons.mozilla.org/es/firefox/addon/lastpass-password-manager/">LastPass password manager</a>, <a href="https://addons.mozilla.org/en-US/firefox/addon/window-resize/">Windows resize</a> or <a href="https://addons.mozilla.org/es/firefox/addon/s3google-translator/">S3 Translator</a>, copy the "addons.css" file in your <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Theme%20colors#the-chrome-folder">the chrome folder</a> as well. You will also need to edit the "addons.css" file to update the dynamic URLs of the addons you want to theme (further explanations inside the "addons.css" file). Also make sure to delete the comment start slash (/*) from the ending rules (the rules under the line that says ADDON POPUPS) in userchrome.css to change the color of the popup arrows on those extensions that may need it.</p>
<p>In case that you just want to change the default scrollbars, you can apply just that without the need
of using the usercontent or userchrome files provided here.</p>

<h2>The userChrome.css file</h2>

<p>The userchrome file turns dark all context menus, bookmarks, the url bar, the search bar, the main menu, and the toolbar. 
It will, although, not turn dark the extension popups you may have. <p>
<img src="https://i.imgur.com/wWjBcqz.png" title="Dark search menu (spanish)" />
<img src="https://i.imgur.com/7zj3SSq.png" title="Dark context menu (spanish)" />
<p>It will also turn dark the autocomplete popups (mostly a side-effect)</p>
<p>Userchrome.css is also the file that enables loading of external (placed in the chrome folder) .css and .js files through the use of <code>userchrome.xml</code> (such as <code>scrollbars.as.css</code> or <code>MultiRowTabLiteforFx.uc.js</code>).</p>

<h2>The userContent.css file</h2>

<p>The usercontent file will turn dark all the <code>about:about</code> pages.</p>
<img src="https://i.imgur.com/mKWPUSk.png" title="Dark firefox about: pages" />
<img src="https://i.imgur.com/97ebC1x.png" title="Dark addons page" />

<h2>The chrome folder</h2>
<p>The fastest way to find it is to just type <code>about:support</code> on the URL bar of your firefox, and then click the <b>open folder</b> button inside the "profile folder" section. After this, your profile folder will be open.</p>

<p><i>You may or may not see the chrome folder. If you don't see it, just create it and place inside the usercontent.css and userchrome.css files.</i></p>

<p>If you want to know the exact location for profile folders (information taken from <a href="http://kb.mozillazine.org/Profile_folder_-_Firefox">here</a>):</p>

<h4>On Windows 7 and above, profile folders are in this location, by default:</h4>

<pre>C:\Users\(Windows login/user name)\AppData\Roaming\Mozilla\Firefox\Profiles\(profile folder)</pre>

<p><i>If you have never used userchrome.css or usercontent.css before, you will have to create a folder named "chrome" inside the profile folder, which is where you will have to place these files.</i></p>

<p>This is where you would have to place the files once you have created the chrome folder:</p>

<pre>C:\Users\(Windows login/user name)\AppData\Roaming\Mozilla\Firefox\Profiles\(profile folder)\chrome\</pre>
  
<p>The AppData folder is a hidden folder; to show hidden folders, open a Windows Explorer window and choose "Tools → Folder Options → View (tab) → Show hidden files and folders".</p>

<p>You can also use this path to find the profile folder, even when it is hidden:</p>

<pre>%APPDATA%\Mozilla\Firefox\Profiles\(profile folder)</pre>

<h4>On Linux, profile folders are located in this other location:</h4>

<pre>/home/(Your-username)/.mozilla/firefox/(profile folder)</pre>

<p><i>If you have never used userchrome.css or usercontent.css before, you will have to create a folder named "chrome" inside the profile folder, which is where you will have to place these files.</i></p>

<p>This is where you would have to place the files once you have created the chrome folder:</p>

<pre>/home/(Your-username)/.mozilla/firefox/(profile folder)/chrome/</pre>

<p>The ".mozilla" folder is a hidden folder. To show hidden files in Nautilus (Gnome desktop's default file browser), choose "View -> Show Hidden Files". On others such as Dolphin (Kubuntu's default file browser), you'd have to choose "Control -> Hidden files"</p>

<h4>On Mac, profile folders are in one of these locations:</h4>

<pre>~/Library/Application Support/Firefox/Profiles/(profile folder)
~/Library/Mozilla/Firefox/Profiles/(profile folder)</pre>

<p><i>If you have never used userchrome.css or usercontent.css before, you will have to create a folder named "chrome" inside the profile folder, which is where you will have to place these files.</i></p>

<p>This is where you would have to place the files once you have created the chrome folder:</p>

<pre>~/Library/Application Support/Firefox/Profiles/(profile folder)/chrome
~/Library/Mozilla/Firefox/Profiles/(profile folder)/chrome/</pre>

<p>The tilde character (~) refers to the current user's Home folder, so ~/Library is the /Macintosh HD/Users/(username)/Library folder. For OS X 10.7 Lion and above, the ~/Library folder is hidden by default.</p>

<p>You can make them visible by typing the following in a terminal window.</p>
<pre>defaults write com.apple.finder AppleShowAllFiles TRUE
killall Finder</pre>
<p>This will also cause any file icons to take on a hazy, 50% alpha look. To restore the old settings (hide the files and make the icons look normal) issue the same commands again, but enter FALSE instead of TRUE.<p>

<p>It will also turn dark the <a href="https://addons.mozilla.org">Mozilla addons page</a>, both the old and the new, the file explorer inside firefox, and the "view source of page" page.</p>
