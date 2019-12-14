<h1>Patching Firefox to enable JS injection (userchromeJS)</h1>
<p>The files here are a fork of the work of <a href="https://github.com/xiaoxiaoflood/firefox-scripts">xiaoxiaoflood</a>, fixed to work with FF69+, and only loading the necessary things to load external JS and CSS files.</p>

<h2>Installation</h2>
<p>You can patch your Firefox using the installer in the <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/releases">releases</a> section. The patcher will choose the default profile folder, so if you have more than 1 profile you should go to <code>about:profiles</code> and make sure that the path the patcher selects is the same as the one of the profile that you are currently using.</p>

<p>Alternatively you can follow the explanations below for the manual installation.</p>

<h3>Manual installation</h3>
<p>To patch firefox with this method, you will have to locate both <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions/JS%20Loader#Firefox-root-folder">firefox root folder</a>, and your profile <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions/JS%20Loader#the-chrome-folder">chrome folder</a>.</p>

<h4>Step by step:</h4>
<ol>
  <li>Copy <code>defaults</code> folder and <code>config.js</code> files inside <code>root</code> to <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions/JS%20Loader#Firefox-root-folder">firefox root folder</a>.</li>
  <li>Copy <code>utils</code> folder to your <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions/JS%20Loader#the-chrome-folder">chrome folder</a>.</li>
</ol>

<p>Next time you start up firefox, changes should take effect.</p>

<p>If you did it right, the structure of firefox root folder should look like this:</p>
<ul>
  <li>browser (folder)</li>
  <li>defaults (folder)</li>
  <ul>
    <li>pref (folder)</li>
    <ul>
      <li>channel-prefs.js</li>
      <li>config-prefs.js</li>
    </ul>
  </ul>
  <li>fonts (folder)</li>
  <li>gmp-clearkey (folder)</li>
  <li>uninstall (folder)</li>
  <li>firefox.exe/firefox</li>
  <li>config.js</li>
  <li>Other .dll files</li>
</ul>

<p>And the structure of the chrome folder should look like:</p>
<ul>
  <li>utils (folder)</li>
  <li>Any other optional file like userChrome.css, userContent.css, MultiRowTabLiteforFx.uc.js, etc...</li>
</ul>

<p>The files inside the "utils" folder will enable both <code>*.uc.js</code> and <code>*.as.css</code> files inside your chrome folder.</p>
<p>To override CSS styles that can't be changed in any other way (like for scrollbars, or certain tooltips), you must give the CSS files you want to use the extension <code>.as.css</code>, since they won't be read at all if you don't (unless you import them directly through <code>userChrome.css</code> with an <b>@import</b> rule, but they will be read with the same privileges as userChrome.css).</p>

<h2>Firefox root folder</h2>
<p>The root folder is where both the executable and the "defaults" folder of your current installed firefox are located</p>
<h4>For Windows, you can find firefox root folder here:</h4>

<pre>32bits Firefox -> C:\Program Files (x86)\Mozilla Firefox\
64bits Firefox -> C:\Program Files\Mozilla Firefox\</pre>

<p>If you have a 32-bits Windows, you will only see the 64-bits path.</p>

<h4>For Linux, you can find the root folder by default in this path:</h4>

<pre>/usr/lib/firefox/browser</pre>

<p>In some cases you might find a difference between 32 and 64 bits program installation paths in Linux, in that case you'd find the path here:</p> 

<pre>/usr/lib64/firefox/browser</pre>

<p>The installation directory path may also vary depending on the distribution, and if you use a package manager to install the application from their repository.</p>

<h4>For Mac, you can find the root folder in this path:</h4>

<pre>/Applications/Firefox.app/content/resources</pre>

<p>To open "Firefox.app", Ctrl-click it and select Show Package Contents. If you simply click it, you will start the application.</p>

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
