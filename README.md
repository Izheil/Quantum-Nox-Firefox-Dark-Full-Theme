<img src="https://i.imgur.com/F7qziom.png" title="Quantum Nox"/>

<code>
<h3>Thank you to everyone who took some of their time to answer the survey questions about the theme!</h3> 
<p>Looks like what most people like about the theme is the look, that it covers a bit more than other themes, and the scrollbars (since the default ones are too low-contrast on windows). Multirow (by itself alone) was also voted (which I guess is no surprise), as well as the complete set of theme+features.</p>
<p>I'm glad to know that the theme is at least useful to a few. I started it back when FF57 rolled out, since I hated the default scrollbar contrast that Firefox had on Windows, as well as <b>Tab Mix Plus</b> getting deprecated because of webextensions, meaning no more multi-row, or color coded tabs (which might just be an aesthetic thing, but I got used to it).</p>
<p>There was also the issue of Firefox being white by default on the <code>about:</code> pages, without any means of changing it through normal means nor any extension (since the full themes had also been deprecated with FF57), and the "dark" firefox theme being... a bit lacking at most.</p>
<p>I then decided to start my own theme, since there were no other around back then, to fix all these little issues that had piled up with the release of FF57, and release it to the public just in case other people like me had the same problems.</p>
<p>I'm happy to know that people is using it as a solution to these problems, so <b>thanks to everyone using this theme</b>!</p>
</br>
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

<h3>Previously known as "Firefox 57+ full dark theme with scrollbars and multirow tabs", I decided to give it an actual name instead of leaving it as just a description.</h3>
<p>This theme is mainly intended for the stable release of Firefox (<b>This means that while it will most probably work with nightly and ESR for the most part, it may have less support for those versions</b>).</p>
<p>You can use it to fully change the colors of most of firefox UI to dark-gray colors (with #222-#444 colors mostly), including scrollbars, tooltips, sidebar, as well as some other things, such as removing some context menu options, enabling multirow tabs, changing the font of the url bar...</p>
<p><b>Of course... you could as well use these files to color your firefox any way you wanted</b>, the only thing you'd have to do is change the correct values (what each class or id does is commented above each) in the .css files (as far as you know some 
basic css or <a href="https://www.w3schools.com/colors/colors_picker.asp">color coding</a>, it shouldn't be too hard) using notepad, or some code editing program (such as notepad++ on Windows).</p>
<p>To change these you will have to use the right hex codes. You can find a color picker to hex code in <a href="https://www.w3schools.com/colors/colors_picker.asp">this page</a>.
<h4>If you want to edit a file and you want to use notepad (windows), you may see that all code is a wall of text without any line break (the files get compressed like that when uploaded, so there isn't much to do there), in which case you can always drag & drop the file you want to modify into any internet browser window (like firefox) to see the actual code with line breaks, and then copy & paste it back to the open file with notepad, making it regain the line breaks on notepad again.<br />
<br />
This problem doesn't happen if you use a code editor such as notepad++, atom, sublime text...</h4>

<h3>Last update: <b>23/11/2018</b></h3>
<p>Files updated:</p>
<ul>
  <li><b>UserChrome.css</b>: Now you can use scrollable bookmarks multirow (you might have to update the scrollbar file or check the changes there to hide the scrollbars on bookmarks bar).</li>
  <li><b>MultiRowTab-scrollable.uc.js</b>: Now the scrollable multi-row will only show the necessary rows up to a max of the set ones inside it (3 by default), instead of a static number of rows.</li>
  <li><b>addons.css</b>: Added a dark theme for <a href="https://addons.mozilla.org/en-US/firefox/addon/popup-blocker-ultimate/">Popup Blocker Ultimate</a> addon.</li>
</ul>
<h3>Pre-Last update: <b>24/10/2018</b></h3>
<ul>
  <li><b>MultiRowTabLiteforFx*.uc.js</b>: Added notes on multirow tabs so that people using firefox nightly can know how to fix the displaced tabs issue.</li>
  <li><b>addons.css</b>: Updated the <a href="https://addons.mozilla.org/es/firefox/addon/tab-session-manager/">Tab session manager</a> addon buttons color.</li>
</ul>

<h2>Installation</h2>

<h3>Main browser UI</h3>
<img src="https://i.imgur.com/0JYmgPo.png" title="Dark firefox overall UI" />

<p>Depending on if you only want to color dark your Firefox, or want to add some more functionability (like deleting some useless context menu commands, or adding multirow tab support), you will have to use the method described inside one of the 3 main folders of this repository (+ the scrollbars method if you want scrollbars and tooltips themed, or multirow):</p>

<h4>Short version</h4>
<ul>
  <li><b>Theme colors</b>: Only adds dark colors to firefox UI, but not the scrollbars or tooltips.</li>
  <li><b>Theme features</b>: Enables removal of context menu items, multirow bookmarks, changing tab bar position (so that it could be under the bookmarks bar for example)</li>
  <li><b>Full theme (except scrollbars)</b>: Does the same as the other 2 combined.</li>
  <li><b>Scrollbars & tooltips dark theme</b>: Enables injection of JavaScript, letting you theme the scrollbars and the tooltips, as well as enabling multirow tabs</li>
</ul>

<h4>Detailed explanation</h4>
<ul>
  <li><b>Theme colors</b>: Following the method described in this folder you will ONLY color Firefox, coloring everything except tooltips and the scrollbar (those can be themed using the instructions on the <b>Scrollbars & tooltips dark theme</b> folder).<br />
  If you only want to use a dark theme, and keep all the context menu options when right clicking on tabs/the web area (such as "Send image..." or "Send tab to device"), use this one. Apart from the basic Firefox UI theming, you can also theme a few other optional things (they require some editing of userchrome.css, or copying addons.css into the chrome folder):
	<ul>
	  <li>Styling for unloaded and unread tab titles.</li>
	  <li>Can change the tab line color to Windows current theme color (You have to change the commented line that is described in line 19 inside <code>userChrome.css</code>).</li>
	  <li>Can change the background image of your lightweight theme to one of your choice on <code>userChrome.css</code> (You have to be using a lightweight theme instead of the default dark theme of Firefox).</li>
	  <li>Can change the default text color of input boxes for those using a dark OS theme that affects the background of these (You have to change the commented line that is described on line 15 inside <code>usercontent.css</code> to use it)</li>
	  <li>Can set an image as background for the home page (You have to change the commented line that is described in line 19 inside <code>userContent.css</code>).<br />
<img src="https://i.imgur.com/IxMK0t5.png"></li>
	  <li>Change the theme of either of the following addons to a dark version (You have to update the UUIDs of the extensions inside "addons.css" for this): 
	  	<ul>
	  		<li><a href="https://addons.mozilla.org/es/firefox/addon/ublock-origin/">Ublock Origin</a></li>
	  		<li><a href="https://addons.mozilla.org/es/firefox/addon/video-downloadhelper/">Video Download Helper</a></li> 
	  		<li><a href="https://addons.mozilla.org/es/firefox/addon/flash-video-downloader/">Flash Video Downloader</a></li>
	  		<li><a href="https://addons.mozilla.org/es/firefox/addon/tab-session-manager/">Tab session manager</a></li>
	  		<li><a href="https://addons.mozilla.org/es/firefox/addon/undo-closed-tabs-revived/">Undo closed tabs button</a></li>
	  		<li><a href="https://addons.mozilla.org/es/firefox/addon/s3download-statusbar/">Download Manager (S3)</a></li>
	  		<li><a href="https://addons.mozilla.org/es/firefox/addon/privacy-badger17/">Privacy badger</a></li>
	  		<li><a href="https://addons.mozilla.org/es/firefox/addon/noscript/">Noscript</a></li>
	  		<li><a href="https://addons.mozilla.org/en-US/firefox/addon/window-resize/">Window resize</a></li>
	  		<li><a href="https://addons.mozilla.org/es/firefox/addon/s3google-translator/">S3 Translator</a></li>
	  		<li><a href="https://addons.mozilla.org/es/firefox/addon/multi-account-containers/">Multi-accounts containers</a></li>
	  		<li><a href="https://addons.mozilla.org/es/firefox/addon/temporary-containers/">Temporary containers</a></li>
	  		<li><a href="https://addons.mozilla.org/es/firefox/addon/https-everywhere/">HTTPS Everywhere</a></li>
	  		<li><a href="https://addons.mozilla.org/es/firefox/addon/onetab/">OneTab</a></li>
	  		<li><a href="https://addons.mozilla.org/en-US/firefox/addon/gmail-notifier-restartless/">Notifier for Gmail (restartless)</a></li>
	  		<li><a href="https://addons.mozilla.org/en-US/firefox/addon/popup-blocker-ultimate/">Popup Blocker Ultimate</a></li>
	  	</ul>
	  	<img src="https://i.imgur.com/m7TGyqz.png" title="Dark addons" /></li>
	</ul>
  <li><b>Theme features</b>: In this one you will find a userchrome with ONLY the features part of the theme (with the exception of multiple row tabs, which can be only enabled using the <b><code>MultiRowTabLiteforFx.uc.js</code> file inside the scrollbars & tooltips folder</b>). These features are the following:
	<ul>
	  <li>Multiple row tabs.</li>
	  <li>Multiple row bookmarks toolbar (2 usable rows by default, but it is NOT enabled by default. You can add more rows editing userchrome).</li>
	  <li>Hides some rarely used commands on the context menu such as "Set image as desktop background" (you can turn these on again).</li>
	  <li>Changes the tab close button to always be visible.</li>
	  <li>You can hide the sidebar completelly resizing it instead of having to click the sidebar button.</li>
	  <li>Can change the URL bar font (You have to change the commented line on userchrome to use it).</li>
	  <li>Can change the tabs position under the URL bar (You have to change the commented line on userchrome to use it).</li>
	</ul></li>
  <li><b>Full theme (except scrollbars)</b>: This userchrome will have the effect of both the other folders combined (but you will still need to theme the Scrollbars and tooltips apart using the method described in that folder, as well as multi-row tabs).</li>
</ul>

<h4>You can turn the features you want on or off changing the commented lines on the CSS file (To change them you just have to open the userchrome.css with notepad or any code editor, and encase between "/*" and "*/" (without the quotation marks) the lines you don't want to take effect). Of course, if you think that you are NEVER going to use certain feature, you can always delete the specific lines you don't want without any other side-effect.</h4>

<p>You can find a video tutorial on how to install the theme <a href="https://youtu.be/FHV1-LbX_Vo">here</a>.</p>

<h3>The scrollbars</h3>
<img src="https://i.imgur.com/qe6tGJW.png" title="Dark blue scrollbar" />

<p>To install the custom scrollbars to match the dark theme, you will have to use one of the 2 methods found on the "Scrollbars & tooltips dark theme" or "Scrollbars patchers(Old method)" folders inside this repository. You should be using the "Scrollbars & tooltips dark theme" folder method, since it's the most permanent, but if you find some bug, you could try using the old method one instead. The problem with the old method is that you will have to re-patch the scrollbars with each firefox update, so I'm only keeping it in case the other new method stops working in the future.</b>

<h2>FAQ:</h2>
<h3>The tabs bar is messed up on firefox nightly (FF65).</h3>
<p>They changed the selectors on the lastest firefox nightly builds, so you will have to delete a few lines in the <code>MultiRowTabLiteforFx*.uc.js</code> file you are using (it's detailed in CAPS what to delete) for the tabs bar to be right again. Once FF65 hits stable, the files here will be updated to those lines deleted by default.</p>

<h3>The synced tabs sidebar isn't themed.</h3>
<p>Since it's anonymous content of the browser we can't theme it through userChrome or userContent, which is why you will have to apply the scrollbars & tooltips method to be able to use external javascript to modify anonymous content, and then place the <b>Sync-tabs-sidebar.as.css</b> file inside the <code>Scrollbars & tooltips dark theme/Chrome/</code> folder inside this repository inside your chrome folder (The method is the same than for the scrollbars, except you place the sync related file on your chrome folder apart from the other files if you are going to use them as well).</p>

<h3>The bookmarks toolbar text/tabs text color is black and I can't see the letters over the dark background.</h3>
<p>This is caused by your persona (lightweight theme), and while you could change these settings inside userchrome, I thought it was better to just change the settings on the persona directly (since not all personas will look the same). To do so you'd have to open <code>about:config</code>, and search for <b>lightweightThemes.usedThemes</b>. Once there, find the "textcolor" setting and type any color you'd want to use instead of black or the color being used by the theme (use #fff for white). The persona you are currently using should be in the first place in the list. A screenshot of this window can be seen in the first section of this readme.</p>

<h3>The bookmarks multirow shows an empty scrollbar when enabled.</h3>
<p>If you are using an old version of the scrollbars, or you are just plain not using the scrollbars here, you will have to add some code to delete the empty scrollbars that show on the bookmark toolbars. You have to use this code on a "*.ac.css" file (so you would need to have firefox patched with the method explained on the <b>Scrollbars & tooltips dark theme</b> folder), since otherwise it won't work:

<code>
/* This deletes the scrollbar from bookmarks toolbar when using multirow bookmarks */
#PlacesToolbarItems scrollbar {display: none !important}
</code>

<h3>I only want to use the multirow/(Any other) feature, but not the other ones!</h3>
<p>You only need to modify <b>userChrome.css</b>, deleting the lines that you don't want to apply (Every function has a comment above it saying what each ruleset does), or if you think you may want them later, just encase the feature parts that you don't want to apply between /* and */:</p>

<code>/* This is an example of a comment that wouldn't be read on a .css file */</code>

<h3>I'm opening web files locally (as in opening html pages that you have created or downloaded) and the background is not the color it should be.</h3>
<p>To change the directory browsing page and change how .css or some .txt files appear when opened with Firefox, I had to specify it to affect urls that start with "file:///", meaning that any file opened with Firefox will get overriden with those rules as well. To prevent this, go to userContent.css, and comment out the lines that affect this url (This rule should be exactly under the color variables at the start of the file).</p>

<h3>I placed userchrome.css inside my chrome folder and I still don't have multi-row tabs!</h3>
<p>While we only needed to use CSS to enable multi-row tabs, this broke tabs draggability, making reordering tabs when it was enabled a bit erratic, so to fix this, I decided to put all multi-row tabs code inside the <b>MultiRowTabLiteforFx.uc.js</b> file. This means that now Multi-row tabs can be enabled following the method described in the "Scrollbars & tooltips dark theme" folder (to be able to use external javascript files), and then placing the file <b>MultiRowTabLiteforFx.uc.js</b> inside your chrome folder. If you are updating from an old version of this theme, you should delete the lines about multi-row tabs from your old userchrome as well (that way you can enable multi-row by just placing or deleting the previously mentioned file).</p>

<h3>Why use this method instead of using <a href="https://addons.mozilla.org/es/firefox/addon/styl-us/">Stylus</a>?</h3>
<p>The main reason is that you can't style firefox about: pages nor the scrollbar with just stylus.</p>

<h3>The theme is making the text of some addon popups unreadable, how do I fix this?</h3>
<p>The theme is made so that it changes most background colors, including the one of the popups that don't have any background color specified by their original creator. Sadly it doesn't change the text of these by default, so you may have to do it manually, or report the addon you want themed here, or just use the fix inside userchrome.css (at around lines 302-305) to turn the addons back to their white background color.</p>

<h2>Credits</h2>
<p>The original code for the custom scrollbars which we modified here belongs to <b>Arty2</b>, and you can find it <a href="https://gist.github.com/Arty2/fdf19aea2c601032410516f059d58eb1">here</a>.
<p>The original code for the multirow tabs (the CSS part) was written by <b>Andreicristianpetcu</b>, and you can find it <a href="https://discourse.mozilla.org/t/tabs-in-two-or-more-rows-like-tabmixpro-in-quantum/21657/2">here</a>, or for just the code, <a href="https://github.com/andreicristianpetcu/UserChrome-Tweaks/blob/09fa38a304af88b685f4086bc8ea9997dd7db0fd/tabs/multi_row_tabs_firefox_v57.css">here</a>. The fix of multi-row tabs draggability was made by <b>TroudhuK</b>, and you can find the original one <a href="https://github.com/TroudhuK/userChrome.js/blob/patch-1/Firefox-57/Mehrzeilige-Tableiste/MultiRowTabLiteforFx.uc.js">here</a>.</p>
<p>The original code for the multirow bookmarks toolbar belongs to the original creator mentioned in <a href="https://www.reddit.com/r/firefox/comments/75wya9/multiple_row_bookmark_toolbar_for_firefox_5758/">this reddit thread</a>, whose code was fixed by <b>jscher2000</b> to use in our current firefox version.</p>
<p>The code to be able to edit anonymous content (in our case the scrollbars and tooltips) was created thanks to the efforts of <a href="http://mozilla.zeniko.ch/userchrome.js.html">Zeniko</a>, <a href="https://github.com/nuchi/firefox-quantum-userchromejs">Nichu</a>, and <a href="https://github.com/Sporif/firefox-quantum-userchromejs">Sporif</a>.
<p>Special thanks to <b>Messna</b> for noting the class turning into an ID on FF58, and <b>Snwflake</b> for fixing Firefox root folder location on MacOS.</p>
<p>Also thanks to <b>BelladonnavGF</b>, <b>Demir-delic</b>, <b>DallasBelt</b>, <b>Hakerdefo</b>, <b>Tkhquang</b> and <b>YiannisNi</b> for noting some issues with the theme, and <b>BelladonnavGF</b> for the addition of the url font and and tabs below url bar suggestions.</p>

<h2>Contact</h2>
<p>If you have anything to ask or tell me about the theme that isn't a bug or an issue (such as a suggestion, or some clarification I may have missed on the documentation), you can contact me through <a href="https://www.reddit.com/message/compose/">reddit</a> (You will need an account for that), directing the message to <b>Izheil</b>. 
