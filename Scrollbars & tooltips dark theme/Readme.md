<h1>Custom Scrollbars and dark tooltips through UserChrome.js</h1>
<img src="https://i.imgur.com/qe6tGJW.png">
<p>This method should be the same for all OS, and it adds CSS code with agent sheet access level through JavaScript to change the scrollbars (This means that we aren't making JavaScript scrollbars, which can be laggy sometimes. We would be actually styling the default scrollbars through Agent Sheet level CSS, which couldn't be done by default on userchrome.css because of some fix for a bug by Mozilla) as well as all the tooltips.</p>

<p>The only little problem with this method is that <b>you will have to delete the start up cache files for the changes to take effect every time you make a change to any of the <i>*.uc.js</i></b> files (which are the ones where the CSS rules go to change the scrollbar or tooltip colors).</p>

<p>To clear the start up cache you have to type <code>about:profiles</code> on firefox URL bar, go to that page, open the local profile directory through that page, and then delete all files inside the "startupCache" folder.</p>

<p>This is <b>NOT</b> the same profile directory where you have to place the "chrome" folder. You access that one through <code>about:support</code>, and then clicking the "open folder" button on the "profile folder" section.</p>
<p>You can edit the scrollbars appearance changing the CSS rules inside the <b>scrollbar.uc.js</b> file, just as you would change them with the old method in this repository.</p>
  
<h2>Installation</h2>
<p>To install userChrome.js you have to do a few more steps than just copying it to your <a href="https://github.com/Izheil/Firefox-57-full-dark-theme-with-scrollbars#the-chrome-folder">the chrome folder</a>. The reason for this is that Firefox doesn't allow userChrome.js by default, so we have to apply certain modifications so that it allows it.</p>

<p>First, copy the contents of the "Root" folder found here to <a href="https://github.com/Izheil/Firefox-57-full-dark-theme-with-scrollbars/blob/master/Scrollbars%20&%20tooltips%20dark%20theme/Readme.md#the-root-folder">Firefox root folder</a>. These contents include the <b>config.js</b>, <b>userChromeJS.js</b> and the <b>config-prefs.js</b> file inside the "defaults/pref" folders (You have to keep this path structure when moving the files to <a href="https://github.com/Izheil/Firefox-57-full-dark-theme-with-scrollbars/blob/master/Scrollbars%20&%20tooltips%20dark%20theme/Readme.md#the-root-folder">Firefox root folder</a>).<p>
  
<p>Once you have done this, all you have to do is open the <a href="https://github.com/Izheil/Firefox-57-full-dark-theme-with-scrollbars#the-chrome-folder">the chrome folder</a> inside your profile folder (If you don't know where that is you can find an explanation on the section below) and place the contents that are inside the "profile" folder here in there. This is the same folder where you would place userchrome.css and usercontent.css.<p>

<p>After that, type <code>about:profiles</code> on the URL bar of firefox, and open the local profile folder through that page. In here you will have enter the "startupcache" folder and delete all files here so that the scrollbars show properly next time you reset firefox (You will have to delete the cache every time you make a change to the scrollbars.uc.js file for it to take effect). You may have to close firefox to be able to delete all the files in the "startupcache" folder.</p>

<blockquote><b>Optional</b>: If you aren't fully convinced by the default custom scrollbar, you can try any of the other scrollbar types (only use one) using any of the scrollbar-*.uc.js files inside the "alternative scrollbars" instead of the scrollbar.uc.js inside the "profile" folder in here.</blockquote>

<blockquote><b>Optional</b>: You may use the <b>tooltips.uc.js</b> file or any of the variants included on the "alternative tooltips" (such as the semi-transparent background ones) if you want dark tooltips (such as the url tooltip, or when you hover over a bookmark).</blockquote>

<p>If you have done everything right, you should see the custom scrollbars next time you open firefox (or after you restart it)</p>

<h4>Short version:</h4>
<ul>
  <li>Copy the contents of the "Root" folder found in this repository to <a href="https://github.com/Izheil/Firefox-57-full-dark-theme-with-scrollbars/blob/master/Scrollbars%20&%20tooltips%20dark%20theme/Readme.md#the-root-folder">Firefox root folder</a>.</li>
  <li>Copy the contents of the "Profile" folder found in this repository to the <a href="https://github.com/Izheil/Firefox-57-full-dark-theme-with-scrollbars#the-chrome-folder">the chrome folder</a> inside your profile folder.</li>
  <li>Open the <code>about:profiles</code> URL with firefox, and open the local profile folder there.</li>
  <li>Open the "startupcache" folder and delete everything there.</li>
  <li><b>Optional</b>: You can try the other scrollbar types inside the "alternative scrollbars" folder.</li>
  <li><b>Optional</b>: Use the <b>tooltips.uc.js</b> file to change the default color of the tooltips to fit the theme (or any of the variants on the "alternative tooltips", such as the semi-transparent background one).</li>
</ul>

<h3>The root folder:</h3>

<h4>For Windows, you can find firefox root folder here:</h4>
​
<pre>32bits Firefox -> C:\Program Files (x86)\Mozilla Firefox\
64bits Firefox -> C:\Program Files\Mozilla Firefox\</pre>
​
<p>If you have a 32-bits Windows, you will only see the 64-bits path.</p>
​
<h4>For Linux, you can find the manifest file by default in this path:</h4>
​
<pre>/usr/lib/firefox/browser</pre>
​
<p>In some cases you might find a difference between 32 and 64 bits program installation paths in Linux, in that case you'd find the path here:</p> 
​
<pre>/usr/lib64/firefox/browser</pre>
​
<p>The installation directory path may also vary depending on the distribution, and if you use a package manager to install the application from their repository.</p>
​
<h4>For Mac, you can find the chrome manifest in this path:</h4>
​
<pre>/Applications/Firefox.app/content/resources</pre>
​
<p>To open "Firefox.app", Ctrl-click it and select Show Package Contents. If you simply click it, you will start the application.</p>

