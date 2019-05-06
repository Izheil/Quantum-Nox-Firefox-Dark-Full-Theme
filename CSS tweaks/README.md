<h1>Only functionability CSS tweaks</h1>

<p>The files contained here contain fixes that will let you alter the default behaviour of Firefox. They are intended to be used as a template of the functions that you can use on your own custom <code>userchrome.css</code> for this goal. This means that you shouldn't just copy everything in every file to your userchrome, but instead select the features you are interested on to customize your Firefox in the way that you want.</p> 

<p>With this goal in mind, a base empty <code>userchrome.css</code> is included (with the javascript fix included if you want to use it later, which won't work unless you have <code>userchrome.xml</code> as well), in case you don't have one already, so that you can use any of the tweaks included here without the need to know much CSS (you will just need to copy the things you want, which have a comment above them with a description of what each does).</p>

<p>If you are using the dark theme <code>userchrome.css</code> file, add the fixes from the files here in that one instead.</p>

<p>To make it work, it's as simple as copying the function you want to apply at the bottom of <code>userchrome.css</code>, place it inside <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/CSS%20tweaks#the-chrome-folder">the chrome folder</a> if you hadn't yet, and restart Firefox.</p>
<p>I describe what tweaks does each file contain below.</p>

<h4>You can also keep some tweak inside your <code>userchrome.css</code> without it being enabled by encasing the lines you don't want to apply between "/*" and "*/" (without the quotation marks).</h4>

<h3>Bookmarks+URLbar+Sidebar.css</h3>

<p>This file contains changes that affect the behaviour of the bookmarks bar (such as enabling <b>multirow bookmarks</b> that you can also make auto-hide), the URL bar, and the sidebar.</p>

<ul>
  <li>Allow the sidebar be completelly closed by just resizing it.</li>
  <li>Change the font used on the ULR box to prevent URL spoofing with a more differentiable font.</li>
  <li>Bookmark toolbar auto-hide.</li>
  <li>Fix for an issue with fullscreen not showing bookmark bar nor menu bar.</li>
</ul>

<h3>Context-menu-commands.css</h3>

<p>This file contains selectors that target most commands contained in context menus (like send image, reload tab, etc..), so that you can hide them to make your context menus look less cluttered with commands that you may never or rarely use.</p>

<ul>
  <li>You can hide the following commands from context menus:
  	<ul>
  	  <li>Reload tab.</li>
      <li>Mute tab.</li>
      <li>Mute selected tabs.</li>
      <li>Select all tabs (only the active tab context menu, not the title context menu one).</li>
  	  <li>Pin tab.</li>
      <li>Pin selected tabs.</li>
  	  <li>Duplicate tab.</li>
  	  <li>Open tab in new window.</li>
      <li>Send tab to device.</li>
      <li>Separators left by send tab to device on tabs context menu.</li>
  	  <li>Reload selected tabs (only the active tab context menu, not the title context menu one).</li>
      <li>Bookmark tab.</li>
  	  <li>Bookmark selected tabs.</li>
      <li>Reopen tab in container.</li>
      <li>Move tab.</li>
  	  <li>Close all tabs to the right.</li>
  	  <li>Close all other tabs.</li>
  	  <li>Close tab.</li>
      <li>Open bookmarked page in a new window.</li>
      <li>Open bookmarked page in a new private window.</li>
      <li>Open all bookmarked pages in the bookmark folder.</li>
  	  <li>Navigation buttons (Back, forward and reload buttons) & it's separator (since you can do the same with the keyboard or other buttons).</li>
  	  <li>Send image... (misclicking this when saving an image can happen easily, and waiting for outlook to open to close it gets annoying).</li>
  	  <li>Set image as desktop background...</li>
  	  <li>Bookmark this page (you can do the same with the star icon on the URL bar, or creating the bookmark manually with more control of where it's going to be placed).</li>
  	  <li>Send page...(same as with send image, if you wanted to send something, you'd open your prefered mail yourself).</li>
      <li>Send video... (same as with send page).</li>
      <li>Save video capture.</li>
      <li>Frame selector separator (You can hide it to avoid double separators).</li>
  	  <li>Bookmark this link (same as bookmark this page).</li>
  	  <li>Send link... (same as send image).</li>
      <li>Search highlighted word on your default search engine.</li>
  	  <li>Open link in new tab (You can do the same middle mouse clicking, or holding ctrl while clicking a link).</li>
  	  <li>Open link in a new window.</li>
  	  <li>Open link in a private window.</li>
  	  <li>Take a screenshot and its separator.</li>
  	  <li>Send tab to device and its separators.</li>
  	  <li>Send page to device and its separator.</li>
  	  <li>Send link to device and its separator.</li>
  	</ul></li>
</ul>

<h3>Tab-related-Tweaks.css</h3>

<p>These will let you change the look and position of the tabs and the tab box.</p>

<ul>
  <li><b>Tabs bar below</b> bookmarks or URL box.</li>
  <li>Give tabs rounded corners.</li>
  <li>Tab close button always visible.</li>
</ul>

<p>Rounded tabs:</p>
  <img src="https://i.imgur.com/qoG4Iiy.png">

<h2>Installation</h2>

<p>All you need to do is place the userChrome.css file inside <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/CSS%20tweaks#the-chrome-folder">the chrome folder</a> of your firefox profile.</p>

<h4>Step by step:</h4>
<ul>
  <li>Type <code>about:support</code> in your URL bar, then go to that page.</li>
  <li>Click the "open folder" button inside the "profile folder" section.</li>
  <li>Create a folder named "chrome" in your profile folder if it doesn't exist yet.</li>
  <li>Place "userchrome.css" inside the "chrome" folder.</li>
  <li><b>Optional</b>: Edit userchrome.css to delete (or comment out) any function you aren't going to use or don't want.</li>
</ul>

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
