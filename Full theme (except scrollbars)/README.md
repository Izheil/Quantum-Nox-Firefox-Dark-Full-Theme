<h1>Theme colors + added functions</h1>
<p>Following the method described here, you will be able to give dark colors to firefox as shown in the following image:</p>

<img src="https://i.imgur.com/0JYmgPo.png" title="Dark firefox overall UI" />

<img src="https://i.imgur.com/m7TGyqz.png" title="Dark addons" />

<p>You will also be able to give certain new functions (or delete some useless ones) to firefox:</p>
<ul>
  <li>Allow the sidebar be completelly closed by just resizing it.</li>
  <li>Change the font used on the ULR box to prevent URL spoofing with a more differentiable font (<b>Disabled by default</b>).</li>
  <li>Tabs bar below bookmarks or URL box (<b>Disabled by default</b>).</li>
  <li>Give tabs a rounded corners appearance (<b>Disabled by default</b>). </li>
  <li>Tab close button always visible .</li>
  <li>Multirow tabs. There is currently a problem with tab draggability when having more than 1 row of tabs open, so you won't be able to reorder them.</li>
  <li>Multirow bookmarks (<b>Disabled by default</b>).</li>
  <li>Delete the following commands from context menus:
  	<ul>
  	  <li>Reload tab (<b>Not deleted by default</b>).</li>
  	  <li>Pin tab (<b>Not deleted by default</b>).</li>
  	  <li>Duplicate tab (<b>Not deleted by default</b>).</li>
  	  <li>Open tab in new window (<b>Not deleted by default</b>).</li>
  	  <li>Reload all tabs (Would be terrible if you had many tabs open and misclicked).</li>
  	  <li>Bookmark all tabs.</li>
  	  <li>Close all tabs to the right (<b>Not deleted by default</b>).</li>
  	  <li>Close all other tabs.</li>
  	  <li>Close tab (You can close them using the close button)</li>
  	  <li>Navigation buttons (Back, forward and reload buttons) & it's separator (Since you can do the same with the keyboard or other buttons).</li>
  	  <li>Send image... (Misclicking this when saving an image can happen easily, and waiting for outlook to open to close it gets annoying).</li>
  	  <li>Set image as desktop background...</li>
  	  <li>Bookmark this page (You can do the same with the star icon on the URL bar, or creating the bookmark manually with more control of where it's going to be placed).</li>
  	  <li>Send page...(Same as with send image, if you wanted to send something, you'd open your prefered mail yourself).</li>
  	  <li>Bookmark this link (Same as bookmark this page).</li>
  	  <li>Send link... (Same as send page).</li>
  	  <li>Open link in new tab (<b>Not deleted by default</b>, but you can the same middle mouse clicking, or holding ctrl while clicking a link).</li>
  	  <li>Open link in a new window.</li>
  	  <li>Open link in a private window.</li>
  	  <li>Take a screenshot and its separator (Since you can already access it through the 3 dots button on the URL bar).</li>
  	  <li>Send tab to device and its separators.</li>
  	  <li>Send page to device and its seaparator.</li>
  	  <li>Send link to device and its separator.</li>
  	</ul></li>
</ul>

<h4>You can turn the features you want on or off changing the commented lines on the CSS file (To change them you just have to open the userchrome.css with notepad or any code editor, and encase between "/*" and "*/" (without the quotation marks) the lines you don't want to take effect). Of course, if you think that you are NEVER going to use certain feature, you can always delete the specific lines you don't want without any other side-effect.</h4>

<h2>Installation</h2>

<p>Most of the job is already done with the userContent.css and userChrome.css files that you have to place in the 
<a href="https://github.com/Izheil/Firefox-57-full-dark-theme-with-scrollbars/tree/master/Full%20theme%20(except%20scrollbars)#the-chrome-folder">the chrome folder</a> of your firefox profile. For this to work as intended, you should be using a persona (aka lightweight theme) or the default dark theme (The persona used on the screenshot is "<a href="https://addons.mozilla.org/en-US/firefox/addon/deep-dark-blue-forest/">Deek Dark Blue forest</a>" by <b>Sondergaard</b>).</p>
<p>The only remaining part that won't be dark themed will be the synced tabs sidebar, the tooltips, and the scrollbars (since they can't be styled through userChrome nor usercontent). This can be themed using the method described in the <a href="https://github.com/Izheil/Firefox-57-full-dark-theme-with-scrollbars/tree/master/Scrollbars%20%26%20tooltips%20dark%20theme">Scrollbars & tooltips dark theme</a> folder.</p>
<p>If you would also like a dark version of either <a href="https://addons.mozilla.org/es/firefox/addon/ublock-origin/">Ublock Origin</a>, <a href="https://addons.mozilla.org/es/firefox/addon/video-downloadhelper/">Video Download Helper</a>, <a href="https://addons.mozilla.org/es/firefox/addon/flash-video-downloader/">Flash Video Downloader</a>, <a href="https://addons.mozilla.org/es/firefox/addon/tab-session-manager/">Tab session manager</a>, or <a href="https://addons.mozilla.org/es/firefox/addon/undo-closed-tabs-revived/">Undo closed tabs button</a> extensions, copy the "addons.css" file in your <a href="https://github.com/Izheil/Firefox-57-full-dark-theme-with-scrollbars/tree/master/Full%20theme%20(except%20scrollbars)#the-chrome-folder">the chrome folder</a> as well, and make sure to delete the comment start slash (/*) at the end of the coloring part inside userchrome.css to change the color of the popup arrows on those extensions that may need it.</p>
<p>In case that you just want to change the default scrollbars, you can apply just that without the need of using the usercontent or userchrome files provided here.</p>

<h4>Step by step:</h4>
<ul>
  <li>Type <code>about:support</code> in your URL bar, then go to that page.</li>
  <li>Click the "open folder" button inside the "profile folder" section.</li>
  <li>Create a folder named "chrome" in your profile folder if it doesn't exist yet.</li>
  <li>Place "usercontent.css" and "userchrome.css" inside the "chrome" folder.</li>
  <li><b>Optional</b>: Follow the method described to change the scrollbars to change the tooltip using the "tooltip.uc.js" file inside the "Scrollbars & tooltips dark theme/profile/" folder in this repository.</li>
  <li><b>Optional</b>: Edit userchrome.css to change any style you aren't fully convinced with (or to give a different style to the unread tabs, etc...).</li>
  <li><b>Optional</b>: Edit userchrome.css to delete (or comment out) any function you aren't going to use or don't want.</li>
  <li><b>Optional</b>: If you want a dark version of either of <a href="https://addons.mozilla.org/es/firefox/addon/ublock-origin/">Ublock Origin</a>, <a href="https://addons.mozilla.org/es/firefox/addon/video-downloadhelper/">Video Download Helper</a>, <a href="https://addons.mozilla.org/es/firefox/addon/flash-video-downloader/">Flash Video Downloader</a>, <a href="https://addons.mozilla.org/es/firefox/addon/tab-session-manager/">Tab session manager</a>, <a href="https://addons.mozilla.org/es/firefox/addon/undo-closed-tabs-revived/">Undo closed tabs button</a>, <a href="https://addons.mozilla.org/es/firefox/addon/s3download-statusbar/">Download Manager (S3)</a>, <a href="https://addons.mozilla.org/es/firefox/addon/privacy-badger17/">Privacy badger</a>, <a href="https://addons.mozilla.org/es/firefox/addon/noscript/">Noscript</a> or <a href="https://addons.mozilla.org/es/firefox/addon/s3google-translator/">S3 Translator</a> extensions, you can also edit the "addons.css" file to update the dynamic URLs of the addons you want to theme (further explanations inside the "addons.css" file). Also make sure to delete the comment start slash (/*) at the end of the coloring part inside userchrome.css (the rules under the line that says ADDON POPUPS) to change the color of the popup arrows on those extensions that may need it.</li>
</ul>

<h3>The chrome folder</h3>

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
<br /><p>This will also cause any file icons to take on a hazy, 50% alpha look. To restore the old settings (hide the files and make the icons look normal) issue the same commands again, but enter FALSE instead of TRUE.<p>

<h2>The userChrome.css file</h2>

<p>The userchrome file turns dark all context menus, bookmarks, the url bar, the search bar, the main menu, and the toolbar. 
It will, although, not turn dark the extension popups you may have. <p>
<img src="https://i.imgur.com/wWjBcqz.png" title="Dark search menu (spanish)" />
<img src="https://i.imgur.com/7zj3SSq.png" title="Dark context menu (spanish)" />
<p>It will also turn dark the autocomplete popups (mostly a side-effect)</p>
<br />
<p>Userchrome.css is also where the added functions (such as multirow tabs) is contained, so if you are looking to delete some function you don't want or reenable one context menu command deleted by default here, you have to edit this file.</p>

<h2>The userContent.css file</h2>

<p>The usercontent file will turn dark all the <code>about:about</code> pages.</p>
<img src="https://i.imgur.com/a41WkP8.png" title="Dark preferences page" />
<img src="https://i.imgur.com/WbhhkKa.png" title="Dark addons page" />

<p>It will also turn dark the <a href="https://addons.mozilla.org">Mozilla addons page</a>, both the old and the new, the file explorer inside firefox, and the "view source of page" page.</p>
