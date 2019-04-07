<img src="https://i.imgur.com/F7qziom.png" title="Quantum Nox"/>

<h3>Previously known as "Firefox 57+ full dark theme with scrollbars and multirow tabs", I decided to give it an actual name instead of leaving it as just a description.</h3>
<p>This theme is mainly intended for the stable release of Firefox (<b>This means that while it will most probably work with nightly and ESR for the most part, it may have less support for those versions</b>).</p>
<p>You can use it to fully change the colors of most of firefox UI to dark-gray colors (with #222-#444 colors mostly), including scrollbars, tooltips, sidebar, as well as dialogs. With the files here you can also as remove some context menu options, enable multirow tabs, change the font of the url bar...</p>
<p><b>Of course... you could as well use these files to color your firefox any way you wanted</b>, the only thing you'd have to do is change the correct values (what each class or id does is commented above each) in the .css files (as far as you know some 
basic css or <a href="https://www.w3schools.com/colors/colors_picker.asp">color coding</a>, it shouldn't be too hard) using notepad, or some code editing program (such as notepad++ on Windows).</p>
<p>To change these you will have to use the right hex codes. You can find a color picker to hex code in <a href="https://www.w3schools.com/colors/colors_picker.asp">this page</a>.</p>
<h4>If you want to edit a file and you want to use notepad (windows), you may see that all code is a wall of text without any line break (the files get compressed like that when uploaded, so there isn't much to do there), in which case you can always drag & drop the file you want to modify into any internet browser window (like firefox) to see the actual code with line breaks, and then copy & paste it back to the open file with notepad, making it regain the line breaks on notepad again.<br />
<br />
This problem doesn't happen if you use a code editor such as notepad++, atom, sublime text...</h4>

<h3>Last update: <b>02/04/2019</b></h3>
<p>Files updated:</p>
<ul>
  <li><b>Quantum Nox - Global dark style.user.css</b>: Fixed issue with the checkboxes not showing the checked state.</li>
</ul>
<h3>Pre-Last update: <b>29/03/2019</b></h3>
<p>Files updated:</p>
<ul>
  <li><b>Quantum Nox - Global dark style.user.css</b>: You can change the brightness % of images via the context menu of stylus now. Also added the option to invert the color of images.</li>
</ul>

<code>
<h3>A note on people looking to replace some Tab Mix Plus features</h3>
<p>As for using this theme to replace some functions of <b>Tab Mix Plus</b>, I'll keep the functions that can be done through CSS here until TMP gets back on track on webextensions (since these fixes are a bit more annoying to toggle for people that don't know CSS), but as of right now, it covers multi-row tabs, keep the close button on tabs always visible, and color-coding tabs when they are loaded, unloaded, etc...</p>
<p>Most other functions of Tab Mix Plus can already be "simulated" changing some <code>about:config</code> settings:</p>
 <ul>
 	<li>To keep FF open even after closing the last tab -> <code>browser.tabs.closeWindowWithLastTab</code> to <i>false</i>.</li>
 	<li>To open a search result typed on the URL bar on a new tab -> <code>browser.urlbar.openintab</code> to <i>true</i>.</li>
 	<li>To open a search result typed on the search bar on a new tab -> <code>browser.search.openintab</code> to <i>true</i>.</li>
 	<li>To open bookmarks on a new tab instead of the current tab -> <code>browser.tabs.loadBookmarksInTabs</code> to <i>true</i>.</li>
 	<li>To force popups on new tabs instead of windows -> <code>browser.link.open_newwindow.restriction</code> to <i>0</i> (should be 2 by default).</li>
 	<li>Open related tabs (the ones you open) as the last tab in the tab bar -> <code>browser.tabs.insertRelatedAfterCurrent</code> to <i>false</i>.</li>
</ul>
<p>... or through extensions (not a comprehensive list, only the ones themed here are mentioned), like <a href="https://addons.mozilla.org/es/firefox/addon/tab-session-manager/">Tab session manager</a>, <a href="https://addons.mozilla.org/es/firefox/addon/undo-closed-tabs-revived/">Undo closed tabs button</a>.</p>
</code></br>

<h2>Installation</h2>

<h3>Main browser UI</h3>
<img src="https://i.imgur.com/zNKhEV6.png" title="Dark firefox UI with custom background" />
<img src="https://i.imgur.com/q8MhDSX.png" title="Dark firefox Dialog" />

<p>If you are on windows and only want the theme or multirow, you can use the batch file installers inside the <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Installers">installers</a> folder.</p> 

<p>If you are using Linux or Mac, or want to add some more functionability (like deleting some useless context menu commands), you will have to use the methods described inside one of the 3 main folders of this repository:</p>

<h4>Short review of each folder:</h4>
<ul>
  <li><a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/CSS%20tweaks">CSS tweaks</a>: Enables removal of context menu items, multirow bookmarks, changing tab bar position (so that it could be under the bookmarks bar for example)</li>
  <li><a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Full%20dark%20theme">Full dark theme</a>: Gives dark colors to firefox UI, including the scrollbars and the tooltips. Can also change the background image of <code>about:home</code> and the header image used as a persona.</li>
  <li><a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions">Multirow and other functions</a>: You can find the JS files that add extra functionability to Firefox that couldn't be done with CSS alone.</li>
</ul>

<img src="https://i.imgur.com/OhKiBCI.png">

<h4>You can turn the features you want on or off changing the commented lines on <code>userchrome.css</code> (To change them you just have to open it with notepad or any code editor, and encase between "/*" and "*/" (without the quotation marks) the lines you don't want to take effect). Of course, if you think that you are NEVER going to use certain feature, you can always delete the specific lines you don't want without any other side-effect.</h4>

<p>You can find a video tutorial on how to install the theme without installers <a href="https://youtu.be/kNHe6XDgUN4">here</a>.</p>

<h2>General sites dark theme</h2>
<p>You can apply the global dark userstyle found inside the <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Global%20dark%20userstyle">Global dark userstyle</a> folder to theme general sites with an all-around CSS stylesheet. <b>You need stylus addon to use it</b>.</p>

<p>While it's not perfect (meaning that you should still use per-site styles for the sites you visit often), it can help to darken most sites when browsing around general sites that you don't visit often, and thus don't want/can't find a specific userstyle for them.</p>
<img src="https://i.imgur.com/S34ylDn.png">

[![Install directly with Stylus](https://img.shields.io/badge/Install%20directly%20with-Stylus-00adad.svg)](https://raw.githubusercontent.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/master/Global%20dark%20userstyle/Quantum%20Nox%20-%20Global%20dark%20style.user.css)

<p>It is recommended that you check the <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Global%20dark%20userstyle">Global dark userstyle</a> readme to know how to add site exclusions to the global userstyle.</p>

<h2>Addon dark themes</h2>
<p>You can apply a dark theme to certain addons changing the UUID's of them inside the <code>addons.css</code> file inside the "Full dark theme" folder (more instructions on how to do that inside the addons file).</p>
<img src="https://i.imgur.com/m7TGyqz.png" title="Dark addons" />
<p>Here is a list of the themed addons:</p>
<ul>
	<li><a href="https://addons.mozilla.org/es/firefox/addon/cookie-autodelete/">Cookie autodelete</a></li>
	<li><a href="https://addons.mozilla.org/es/firefox/addon/s3download-statusbar/">Download Manager (S3)</a></li>
	<li><a href="https://addons.mozilla.org/es/firefox/addon/flash-video-downloader/">Flash Video Downloader</a></li>
	<li><a href="https://addons.mozilla.org/es/firefox/addon/history-autodelete/">History autodelete</a></li>
	<li><a href="https://addons.mozilla.org/es/firefox/addon/https-everywhere/">HTTPS Everywhere</a></li>
	<li><a href="https://addons.mozilla.org/es/firefox/addon/noscript/">Noscript</a></li>
	<li><a href="https://addons.mozilla.org/en-US/firefox/addon/gmail-notifier-restartless/">Notifier for Gmail (restartless)</a></li>
	<li><a href="https://addons.mozilla.org/es/firefox/addon/multi-account-containers/">Multi-accounts containers</a></li>
	<li><a href="https://addons.mozilla.org/es/firefox/addon/onetab/">OneTab</a></li>
	<li><a href="https://addons.mozilla.org/en-US/firefox/addon/popup-blocker-ultimate/">Popup Blocker Ultimate</a></li>
	<li><a href="https://addons.mozilla.org/es/firefox/addon/privacy-badger17/">Privacy badger</a></li>
	<li><a href="https://addons.mozilla.org/es/firefox/addon/tab-session-manager/">Tab session manager</a></li>
	<li><a href="https://addons.mozilla.org/es/firefox/addon/temporary-containers/">Temporary containers</a></li>
	<li><a href="https://addons.mozilla.org/es/firefox/addon/ublock-origin/">Ublock Origin</a></li>
	<li><a href="https://addons.mozilla.org/es/firefox/addon/undo-closed-tabs-revived/">Undo closed tabs button</a></li>
	<li><a href="https://addons.mozilla.org/es/firefox/addon/video-downloadhelper/">Video Download Helper</a></li> 
	<li><a href="https://addons.mozilla.org/es/firefox/addon/viewhance/">Viewhance</a></li>
</ul>

<p>You might have noticed that we no longer have <a href="https://gist.github.com/Izheil/49db523ee66d88995401bb6844605763">Lastpass dark theme</a> inside <code>addons.css</code> anymore. This is because at the time that addon was themed, I didn't know much about it. After some research it seems like Lastpass has had a history of security issues (in 2011, 2015, 2016, and 2017), as well as there being other open source alternatives out there that seem to be more reliable, like <b>Bitwarden</b> (it also has a built-in dark mode) which is available for all major browsers.</p>

<h3>The scrollbars</h3>

<p>This theme colors scrollbars using <code>usercontent.css</code> to give them a basic re-color.</p> 
<img src="https://i.imgur.com/hqwoq9n.png" title="Re-colored dark scrollbar" />

<p>If you <b>want a different style on the scrollbars</b>, you can try using the <code>scrollbars.as.css</code> file inside the <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Full%20dark%20theme/Alternative%20scrollbars%20%26%20tooltips/Alternative%20scrollbars">Alternative scrollbars</a> folder, which will make the scrollbars look more rounded and will have some sort of "puffy" effect when clicking them.</p>
<img src="https://i.imgur.com/sOHN1ds.gif" title="Custom dark blue scrollbar" />

<p>If instead you just <b>don't want scrollbars to show at all but keep scrollability</b>, you can do this through <code>usercontent.css</code> setting the variable <code>--scrollbars-width</code> to none (should be the first rule on the <code>:root</code> section (almost at the start)), and deleting <code>scrollbars.as.css</code>.</p>
<p>If you aren't using the usercontent provided here for some reason, you can always just add this code to your self-created <code>usercontent.css</code>:</p><code>*|* {scrollbar-width: none !important}</code>
<br /><br />

<h2>FAQ:</h2>
<h3>How do I submit an issue?</h3>
<p>As of 26/03/2019 I stopped offering active support for new features or issues. This doesn't mean that I won't be mantaining the project, it just means I won't be taking feature requests nor unrelated issues to the functionability offered by the files inside this repository anymore.</p>

<p>If you find some problem that is <b>directly related</b> with any of the functions offered by any of the files in this repository, you can comment it inside the relevant commit that you think may have affected the function that is giving you trouble. If you can't tell which, comment in the last one. Comments about new functionability or things that aren't related to the actual functionability of the files will be ignored (You can already ask about problems you may have with firefox on <a href="https://www.reddit.com/r/firefox/">r/firefox</a> or <a href="https://www.reddit.com/r/firefoxcss/">r/firefoxCSS</a> subreddits, or on <a href="https://support.mozilla.org/">Firefox support</a> pages).</p>

<h3>The pre-loading screen of websites is still white, how can I change this?</h3>
<p>The fastest way to solve the "blinking" white screen is to change the default web background color on Firefox settings > General > "Colors..." button > Background, which will make the blinking dissapear and be changed to the color you set up. This, although, can cause some issues on some very few and specific pages like BBC, where they don't set a background color to override the one set here (the number of sites with this problem is very small, most sites override the background color set by this setting).</p>

<h3>The synced tabs sidebar isn't themed.</h3>
<p>Since it's anonymous content of the browser we can't theme it through userChrome or userContent, which is why you will have to apply the fix inside <code>Sync-tabs-sidebar.as.css</code>. It requires the use of external CSS files loading, which is enabled thorugh <code>userchrome.css</code> and <code>userchrome.xml</code>.</p>

<h3>Some context menu commands dissapear after installing userchrome.</h3>
<p>If you only want the dark theme, use the default <code>userchrome.css</code> file inside "Full dark theme", which won't make the context menu commands dissapear. In case you want to use the features part of the theme, just delete everything after the line that says <code>/* CONTEXT MENU COMMANDS */</code> (you can find it using the search option on notepad, or the code editor you are using).</p>
<p>In case you still want to delete some commands but not all, just comment out the ones that you want to appear, and leave as active the ones that you want to dissapear.</p>
<p>For example, this is active, so the command is hidden:</p>
<pre>/* Send image... */
#context-sendimage,</pre>
<p>...But this is commented out, so the command will show on the context menu:</p>
<pre>/* Send image... *//*
#context-sendimage,*/</pre>
<p>You will see that the ones that I have commented out by default only have the starting "/*" of the comment after the description of what they are, since the closing "*/" would come from the next description comment below them.</p>


<h3>The bookmarks toolbar text/tabs text color is black and I can't see the letters over the dark background.</h3>
<p>This is caused by your persona (lightweight theme), and while you could change these settings inside userchrome, I thought it was better to just change the settings on the persona directly (since not all personas will look the same). To do so you'd have to open <code>about:config</code>, and search for <b>lightweightThemes.usedThemes</b>. Once there, find the "textcolor" setting and type any color you'd want to use instead of black or the color being used by the theme (use #fff for white). The persona you are currently using should be in the first place in the list.</p>

<h3>The bookmarks multirow shows an empty scrollbar when enabled.</h3>
<p>If you are using an old version of the scrollbars, or you are just plain not using the scrollbars here, you will have to add some code to delete the empty scrollbars that show on the bookmark toolbars. You have to use this code on a "*.ac.css" file (so you would need to have firefox patched with the method explained on the <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions">Multirow and other functions</a> folder), since otherwise it won't work:

<pre>
/* This deletes the scrollbar from bookmarks toolbar when using multirow bookmarks */
#PlacesToolbarItems scrollbar {display: none !important}
</pre>

<h3>I only want to use the multirow/(Any other) feature, but not the other ones!</h3>
<p>You only need to modify <b>userChrome.css</b>, deleting the lines that you don't want to apply (Every function has a comment above it saying what each ruleset does), or if you think you may want them later, just encase the feature parts that you don't want to apply between /* and */:</p>

<code>/* This is an example of a comment that wouldn't be read on a .css file */</code>

<h3>I'm opening web files locally (as in opening html pages that you have created or downloaded) and the background is not the color it should be.</h3>
<p>To change the directory browsing page and change how .css or some .txt files appear when opened with Firefox, I had to specify it to affect urls that start with "file:///", meaning that any file opened with Firefox will get overriden with those rules as well. To prevent this, go to userContent.css, and comment out the lines that affect this url (This rule should be exactly under the color variables at the start of the file).</p>

<h3>I placed userchrome.css inside my chrome folder and I still don't have multi-row tabs!</h3>
<p>While we only needed to use CSS to enable multi-row tabs, this breaks tabs draggability, making reordering tabs when it was enabled a bit erratic, so to fix this, I decided to put all multi-row tabs code inside the <b>MultiRowTabLiteforFx.uc.js</b> file. This means that now Multi-row tabs can be enabled following the method described inside the <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions/Multirow%20tabs">Multirow tabs</a> folder. If you were using CSS code on your <code>userchrome.css</code> to enable multirow tabs, delete (or comment it out) for the js file to take effect.</p>

<h3>Why use this method instead of using <a href="https://addons.mozilla.org/es/firefox/addon/styl-us/">Stylus</a>?</h3>
<p>The main reason is that you can't style firefox about: pages nor dialog windows with just stylus.</p>

<h3>The theme is making the text of some addon popups unreadable, how do I fix this?</h3>
<p>The theme is made so that it changes most background colors, including the one of the popups that don't have any background color specified by their original creator. Sadly it doesn't change the text of these by default, so you may have to do it manually, or report the addon you want themed here, or just use the fix inside userchrome.css (at around lines 326-329) to turn the addons back to their white background color.</p>

<h2>Credits</h2>
<p>The original code for the custom scrollbars which we modified here belongs to <b>Arty2</b>, and you can find it <a href="https://gist.github.com/Arty2/fdf19aea2c601032410516f059d58eb1">here</a>.
<p>The original code for the multirow tabs (the CSS part) was written by <b>Andreicristianpetcu</b>, and you can find it <a href="https://discourse.mozilla.org/t/tabs-in-two-or-more-rows-like-tabmixpro-in-quantum/21657/2">here</a>, or for just the code, <a href="https://github.com/andreicristianpetcu/UserChrome-Tweaks/blob/09fa38a304af88b685f4086bc8ea9997dd7db0fd/tabs/multi_row_tabs_firefox_v57.css">here</a>. The fix of multi-row tabs draggability was made by <b>TroudhuK</b>, and you can find the original one <a href="https://github.com/TroudhuK/userChrome.js/blob/patch-1/Firefox-57/Mehrzeilige-Tableiste/MultiRowTabLiteforFx.uc.js">here</a>.</p>
<p>The original code for the multirow bookmarks toolbar belongs to the original creator mentioned in <a href="https://www.reddit.com/r/firefox/comments/75wya9/multiple_row_bookmark_toolbar_for_firefox_5758/">this reddit thread</a>, whose code was fixed by <b>jscher2000</b> to use in our current firefox version.</p>
<p>The original version of the global dark style for general websties which we modified here belongs to <b>Stormi</b>, and you can find it <a href="https://userstyles.org/styles/31267/global-dark-style-changes-everything-to-dark">here</a>.
<p>The code to be able to edit anonymous content (in our case the scrollbars and tooltips) was created thanks to the efforts of <a href="http://mozilla.zeniko.ch/userchrome.js.html">Zeniko</a>, <a href="https://github.com/nuchi/firefox-quantum-userchromejs">Nichu</a>, and <a href="https://github.com/Sporif/firefox-quantum-userchromejs">Sporif</a>.
<p>Special thanks to <b>Messna</b> for noting the class turning into an ID on FF58, and <b>Snwflake</b> for fixing Firefox root folder location on MacOS.</p>
<p>Also thanks to <b>BelladonnavGF</b>, <b>Demir-delic</b>, <b>DallasBelt</b>, <b>Gitut2007</b>, <b>Hakerdefo</b>, <b>Tkhquang</b> and <b>YiannisNi</b> for noting some issues with the theme, and the requests for new features that extended this project.</p>

<h2>Donations</h2>
<p>If you want to support this project, consider donating any amount through paypal to motivate me keep this repository up and updated.</p>
​
<a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=BMUFYBSRA7ENL&source=url" title="Paypal donations button" onclick="javascript:window.open('https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=BMUFYBSRA7ENL&source=url','WIPaypal','toolbar=no, location=no, directories=no, status=no, menubar=no, scrollbars=yes, resizable=yes, width=1060, height=700'); return false;"><img src="https://www.paypalobjects.com/webstatic/mktg/logo/pp_cc_mark_74x46.jpg" border="0" alt="PayPal Logo" /></a>