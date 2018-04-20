<h1>Only functionability CSS tweaks</h1>

<p>The userChrome.css file in this folder contains a series of CSS tweaks that can change your firefox in the following ways:</p>
<ul>
  <li>Allow the sidebar be completelly closed by just resizing it (lines 7-15).</li>
  <li>Change the font used on the ULR box to prevent URL spoofing with a more differentiable font (lines 17-24, <b>disabled by default</b>).</li>
  <li>Tabs bar below bookmarks or URL box (lines 26-40, <b>disabled by default</b>).</li>
  <li>Give tabs a rounded corners appearance (lines 42-51, <b>disabled by default</b>). </li>
  <li>Tab close button always visible (lines 53-60).</li>
  <li>Multirow tabs (lines 62-103). There is currently a problem with tab draggability when having more than 1 row of tabs open, so you won't be able to reorder them.</li>
  <li>Multirow bookmarks (lines 105-113, <b>disabled by default</b>).</li>
  <li>Delete the following commands from context menus:
  	<ul>
  	  <li>Reload tab (line 122, <b>not deleted by default</b>).</li>
  	  <li>Pin tab (line 125, <b>not deleted by default</b>).</li>
  	  <li>Duplicate tab (line 128, <b>not deleted by default</b>).</li>
  	  <li>Open tab in new window (line 131, <b>not deleted by default</b>).</li>
      <li>Separators left by send tab to device on tabs context menu (line 134 and 137, <b>not deleted by default</b>).</li>
  	  <li>Reload all tabs (line 134, would be terrible if you had many tabs open and misclicked).</li>
  	  <li>Bookmark all tabs (line 137).</li>
  	  <li>Close all tabs to the right (line 146, <b>not deleted by default</b>).</li>
  	  <li>Close all other tabs (line 149).</li>
  	  <li>Close tab (line 152, you can close them using the close button)</li>
  	  <li>Navigation buttons (Back, forward and reload buttons) & it's separator (line 156, since you can do the same with the keyboard or other buttons).</li>
  	  <li>Send image... (line 159, misclicking this when saving an image can happen easily, and waiting for outlook to open to close it gets annoying).</li>
  	  <li>Set image as desktop background... (line 162).</li>
  	  <li>Bookmark this page (line 165, you can do the same with the star icon on the URL bar, or creating the bookmark manually with more control of where it's going to be placed).</li>
  	  <li>Send page...(line 168, same as with send image, if you wanted to send something, you'd open your prefered mail yourself).</li>
  	  <li>Bookmark this link (line 171, same as bookmark this page).</li>
  	  <li>Send link... (line 174, same as send page).</li>
      <li>Search highlighted word on your default search engine (line 178, same as send page).</li>
  	  <li>Open link in new tab (181, <b>not deleted by default</b>, but you can the same middle mouse clicking, or holding ctrl while clicking a link).</li>
  	  <li>Open link in a new window (line 183).</li>
  	  <li>Open link in a private window (line 185).</li>
  	  <li>Take a screenshot and its separator (line 190, since you can already access it through the 3 dots button on the URL bar).</li>
  	  <li>Send tab to device and its separators (line 193).</li>
  	  <li>Send page to device and its separator (line 196).</li>
  	  <li>Send link to device and its separator (lines 199).</li>
  	</ul></li>
</ul>

<p>Rounded tabs:</p>
  <img src="https://i.imgur.com/qoG4Iiy.png">
  
<p>Multirow tabs:</p>
  <img src="https://i.imgur.com/3LbvuMU.png">

<h4>You can turn the features you want on or off changing the commented lines on the CSS file (To change them you just have to open the userchrome.css with notepad or any code editor, and encase between "/*" and "*/" (without the quotation marks) the lines you don't want to take effect). Of course, if you think that you are NEVER going to use certain feature, you can always delete the specific lines you don't want without any other side-effect.</h4>

<h2>Installation</h2>

<p>All you need to do is place the userChrome.css file inside <a href="https://github.com/Izheil/Firefox-57-full-dark-theme-with-scrollbars/tree/master/Theme%20features#the-chrome-folder">the chrome folder</a> of your firefox profile.</p>

<h4>Step by step:</h4>
<ul>
  <li>Type <code>about:support</code> in your URL bar, then go to that page.</li>
  <li>Click the "open folder" button inside the "profile folder" section.</li>
  <li>Create a folder named "chrome" in your profile folder if it doesn't exist yet.</li>
  <li>Place "userchrome.css" inside the "chrome" folder.</li>
  <li><b>Optional</b>: Edit userchrome.css to delete (or comment out) any function you aren't going to use or don't want.</li>
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
<p>This will also cause any file icons to take on a hazy, 50% alpha look. To restore the old settings (hide the files and make the icons look normal) issue the same commands again, but enter FALSE instead of TRUE.<p>
