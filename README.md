<h1>Firefox 57+ full dark theme with dark scrollbars and multirow tabs</h1>

<p>This repository includes the files requires to (almost) fully dark theme firefox quantum to dark-gray colors 
(with #222-#444 colors mostly). </p>
<p><b>Of course... you could as well use these files to color your firefox any way you wanted</b>, the only thing you'd have to do
is change the correct values (what each class or id does is commented above each) in the .css files (as far as you know some 
basic css or color coding, it shouldn't be too hard)</p>
<p>What this "theme" will not affect will be your persona, the text color used by it, and the accent color (line above active tab). To change those settings, you can change them manually through the <code>about:config</code> page, searching 
<b>lightweightThemes.usedThemes</b> there, and changing the textcolor or accentcolor codes of your used persona respectively.</p><br />
<p><b>Why use this method instead of using stylus?</b></p>
<p>The main reason is that you can't style firefox about pages nor the scrollbar with just stylus.</p>

<h2>Installation</h2>

<h3>Main browser UI</h3>

<img src="https://i.imgur.com/a2HnUxz.png" title="Dark firefox overall UI" />

<p>Most of the job is already done with the userContent.css and userChrome.css files that you have to place in the 
chrome folder of your firefox profile (Look below for "the chrome folder" section if you don't know where that is). For this to work as intended, you should be using a persona (aka lightweight theme) or the default dark theme (The persona used on the screenshot is "<a href="https://addons.mozilla.org/en-US/firefox/addon/deep-dark-blue-forest/">Deek Dark Blue forest</a>" by <b>Sondergaard</b>).</p>
<p>If you are only looking for how to change the default scrollbars, you can apply just that without the need
of using the usercontent or userchrome files provided here.</p>

<h3>The scrollbars</h3>
<p>The scrollbars file isn't as easy to install as userchrome or usercontent (but still pretty simple). 
The reason for this is that to style the scrollbars we can't use external styles through the stylus extension or userchrome.</p>
<p>To install the scrollbars, you will have to edit a file (<code>chrome.manifest</code>) yourself (Don't worry, it's just 1 line), 
as well as <b>placing the scrollbars.css file inside firefox's root folder</b>.</p> 
<p>Firefox root folder is where the <code>firefox.exe</code> file is located inside the mozilla firefox folder inside program 
files (or the x86 program files if you have a 32-bits firefox).</p>
<p>Once you have located the <code>chrome.manifest</code> file on firefox root folder (there is another one inside the "browser" folder that you don't have to edit), edit it with notepad (or any code editor program you see fit for the
job). You will see a blank file (it was 0kb heavy after all), where you should add the line:</p>

<code>override chrome://global/skin/scrollbars.css scrollbars.css</code>

<p>...Or you could be lazy and just copy the chrome.manifest uploaded here directly to firefox root folder.</p>
<p>If you have done everything correctly, firefox should have the custom-made scrollbars now (or after you restart firefox if
you had it open).</p>
<h3>The chrome folder</h3>
<p>If you don't know where that is, just type <code>about:support</code> on the URL bar of your firefox, and in the page
you will be redirected to, on the section labed as "profile folder" click the <b>open folder</b> button.</p>
<p>After this, your profile folder will be open, it should be located somewhere like: 
<code>C:/Users/(your-username)/AppData/Roaming/Mozilla/Firefox/Profiles/(random-letters-and-numbers.default)/</code><p>
<p>You may or may not see the chrome folder. If you don't see it, just create it and place inside the 
usercontent.css and userchrome.css files.<p>


<h2>The userChrome.css file</h2>

<p>The userchrome file turns dark all context menus, bookmarks, the url bar, the search bar, the main menu, and the toolbar. 
It will, although, not turn dark the extension popups you may have. <p>
<img src="https://i.imgur.com/wWjBcqz.png" title="Dark search menu (spanish)" /></a>
<p>You can also opt to only change the layout of certain context menus, but not all of them, using the commented lines
in the file.</p>
<img src="https://i.imgur.com/7zj3SSq.png" title="Dark context menu (spanish)" /></a>
<p>It will also turn dark the autocomplete popups (mostly a side-effect)</p>
<br />

<p>This userchrome will also make the close button on tabs always show, as well as adding multiple row tabs support thanks to <a href="https://github.com/andreicristianpetcu/UserChrome-Tweaks/blob/09fa38a304af88b685f4086bc8ea9997dd7db0fd/tabs/multi_row_tabs_firefox_v57.css">the code</a> of <b>Andreicristianpetcu</b>. It will also hide some (at least to me) useless options of the main context menu, such as "send image", 
"set as desktop background", "bookmark page", "send page", "bookmark this link", "send link" and "send tab/page/link to device".</p>
<p>If for some reason you wanted to keep any of those, you can still recover them deleting the css entries for the ones you are 
interested on (or commenting them between /* and */)</p>


<h2>The userContent.css file</h2>

<p>The usercontent file will turn dark the most commonly used <code>about</code> pages.</p>
<img src="https://i.imgur.com/e4zVTC7.png" title="Dark preferences page" /></a>
<p>These include:</p>
<ul>
  <li>Home</li>
  <li>Preferences</li>
  <li>Addons*</li>
  <li>About</li>
  <li>Error</li>
  <li>Cache</li>
  <li>Config</li>
  <li>Plugins</li>
  <li>Memory</li>
  <li>Downloads</li>
  <li>Support</li>
</ul>

<p>*The addons page has a popup (the one that appears when you right click an addon and choose "about...") that couldn't be
styled.</p>
<p>As of 24/11/2017, a dark theme for the Mozilla addons page was also added.</p>

<h2>The scrollbars.css file</h2>
<img src="https://i.imgur.com/2WBVmxY.png?1" title="Dark blue scrollbar" /></a>

<p>Same as with the other files, you can edit the scrollbars appearance using the scrollbars.css, editing only past the 
"New Scrollbar starts here" line. The reason for this is that to change the scrollbars we had to override the actual scrollbars
default file of the program, so you have to keep the original lines above your changes to prevent firefox from crashing (as
well as having a default scrollbar in case you wanted to play around with the new scrollbar attributes).</p> <br />
<h2>Credits</h2>
<p>The original code for the custom scrollbars belongs to <b>Arty2</b>, and you can find it <a href="https://gist.github.com/Arty2/fdf19aea2c601032410516f059d58eb1">here</a>.
<p>The original code for the multirow tabs was written by <b>Andreicristianpetcu</b>, and you can find it <a href="https://discourse.mozilla.org/t/tabs-in-two-or-more-rows-like-tabmixpro-in-quantum/21657/2">here</a>, or for just the code, <a href="https://github.com/andreicristianpetcu/UserChrome-Tweaks/blob/09fa38a304af88b685f4086bc8ea9997dd7db0fd/tabs/multi_row_tabs_firefox_v57.css">here</a>.
