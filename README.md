<h1>Firefox 57+ full dark theme with dark scrollbars and multirow tabs/bookmarks</h1>

<p>This repository includes the files requires to fully dark theme firefox quantum to dark-gray colors 
(with #222-#444 colors mostly). </p>
<p><b>Of course... you could as well use these files to color your firefox any way you wanted</b>, the only thing you'd have to do is change the correct values (what each class or id does is commented above each) in the .css files (as far as you know some 
basic css or <a href="https://www.w3schools.com/colors/colors_picker.asp">color coding</a>, it shouldn't be too hard) using notepad, or some code editing program (such as notepad++ on Windows).</p>
<p>What this "theme" will not affect will be your persona (aka the lightweight themes you install through firefox addons page), the text color used by it, and the accent color (line above active tab). To change those settings, you can change them manually through the <code>about:config</code> page, searching 
<b>lightweightThemes.usedThemes</b> there, and changing the textcolor or accentcolor codes of your used persona respectively as seen on the image below:</p>
<img src="https://i.imgur.com/3lzN95E.png">
<p>To change these you will have to use the right hex codes. You can find a color picker to hex code in <a href="https://www.w3schools.com/colors/colors_picker.asp">this page</a>.
<h4>If you want to edit a file and you want to use notepad (windows), you may see that all code is a wall of text without any line break (the files get compressed like that when uploaded, so there isn't much to do there), in which case you can always drag & drop the file you want to modify into any internet browser window (like firefox) to see the actual code with line breaks, and then copy & paste it back to the open file with notepad, making it regain the line breaks on notepad again.<br />
<br />
This problem doesn't happen if you use a code editor such as notepad++, atom, sublime text...</h4>

<h3>Last update: <b>26/03/2018</b></h3>
<p>Files updated:</p>
<ul>
  <li><b>addons.css</b>: Fixed some issue with some parts of the VHD addon theme.</li>
  <li><b>checkboxes.uc.js</b>: Fixed some issues with the VHD addon select boxes appearing as white even on dark OS's.</li>
</ul>
<h3>Pre-Last update: <b>24/03/2018</b></h3>
<ul>
  <li>Created an installation video, which you can check <a href="https://youtu.be/z0o8DatRyjk">here</a>.</li>
</ul>

<h2>FAQ:</h2>
<h3>The synced tabs sidebar isn't themed.</h3>
<p>Since it's anonymous content of the browser we can't theme it through userChrome or userContent, which is why you will have to apply the scrollbars & tooltips method to be able to use external javascript to modify anonymous content, and then place the <b>Sync-tabs-sidebar.uc.js</b> file inside the <code>Scrollbars & tooltips dark theme/Profile/</code> folder inside this repository inside your chrome folder (The method is the same than for the scrollbars, except you place the sync related file on your chrome folder apart from the other files if you are going to use them as well).</p>

<h3>I only want to use the multirow/(Any other) feature, but not the other ones!</h3>
<p>You only need to modify <b>userChrome.css</b>, deleting the lines that you don't want to apply (Every function has a comment above it saying what each ruleset does), or if you think you may want them later, just encase the feature parts that you don't want to apply between /* and */:</p>

<code>/* This is an example of a comment that wouldn't be read on a .css file */</code>

<h3>Multirow tabs draggability isn't working right!</h3>
<p>There is currently a problem with the multirow-tab code when you have more than 1 row of tabs visible that makes dragging tabs to other rows a bit erratic, so it will only drag the tabs to the previous row for some reason. I'll be trying to find a solution, but meanwhile... yeah, that's all there is.</p>

<h3>Why use this method instead of using <a href="https://addons.mozilla.org/es/firefox/addon/styl-us/">Stylus</a>?</h3>
<p>The main reason is that you can't style firefox about: pages nor the scrollbar with just stylus.</p>

<h2>Description</h2>

<h3>Main browser UI</h3>
<img src="https://i.imgur.com/0JYmgPo.png" title="Dark firefox overall UI" />

<p>Depending on if you only want to color dark your Firefox, or want to add some more functionability (like deleting some useless context menu commands, or adding multirow tab support), you will have to use the method described inside one of the 3 following folders of this repository:</p>

<ul>
  <li><b>Theme colors</b>: Following the method described in this folder you will ONLY color Firefox, coloring everything except tooltips and the scrollbar (those can be themed using the instructions on the <b>Scrollbars & tooltips dark theme</b> folder).<br />
  If you only want to use a dark theme but you aren't interested on using multirow tabs, or want to keep all the context menu options when right clicking on tabs/the web area (such as "Send image..." or "Send tab to device"), use this one. Apart from the basic Firefox UI theming, you can also theme a few other optional things (they require some editing of userchrome.css, or copying addons.css into the chrome folder):
	<ul>
	  <li>Styling for unloaded and unread tab titles.</li>
	  <li>Can change the tab line color to Windows current theme color (You have to change the commented line that is described in line 28 inside userChrome.css).</li>
	  <li>Can change the default text color of input boxes for those using a dark OS theme that affects the background of these (You have to change the commented line that is described on line 82 inside usercontent.css to use it)</li>
	  <li>Can set an image as background for the home page (You have to change the commented line that is described in line 170 inside userContent.css).<br />
<img src="https://i.imgur.com/IxMK0t5.png"></li>
	  <li>Change the theme of either of <a href="https://addons.mozilla.org/es/firefox/addon/ublock-origin/">Ublock Origin</a>, <a href="https://addons.mozilla.org/es/firefox/addon/video-downloadhelper/">Video Download Helper</a>, <a href="https://addons.mozilla.org/es/firefox/addon/flash-video-downloader/">Flash Video Downloader</a>, <a href="https://addons.mozilla.org/es/firefox/addon/tab-session-manager/">Tab session manager</a>, <a href="https://addons.mozilla.org/es/firefox/addon/undo-closed-tabs-revived/">Undo closed tabs button</a>, <a href="https://addons.mozilla.org/es/firefox/addon/s3download-statusbar/">Download Manager (S3)</a>, <a href="https://addons.mozilla.org/es/firefox/addon/privacy-badger17/">Privacy badger</a>, <a href="https://addons.mozilla.org/es/firefox/addon/noscript/">Noscript</a> or <a href="https://addons.mozilla.org/es/firefox/addon/s3google-translator/">S3 Translator</a> extensions to a dark version. You have to update the UUIDs of the extensions inside "addons.css" for this. <br /><img src="https://i.imgur.com/m7TGyqz.png" title="Dark addons" /></li>
	</ul>
  <li><b>Theme features</b>: In this one you will find a userchrome with ONLY the features part of the theme. These features are the following:
	<ul>
	  <li>Multiple row tabs.</li>
	  <li>Multiple row bookmarks toolbar (2 usable rows by default, but it is NOT enabled by default. You can add more rows editing userchrome).</li>
	  <li>Hides some rarely used commands on the context menu such as "Set image as desktop background" (you can turn these on again).</li>
	  <li>Changes the tab close button to always be visible.</li>
	  <li>You can hide the sidebar completelly resizing it instead of having to click the sidebar button.</li>
	  <li>Can change the URL bar font (You have to change the commented line on userchrome to use it).</li>
	  <li>Can change the tabs position under the URL bar (You have to change the commented line on userchrome to use it).</li>
	</ul></li>
  <li><b>Full theme (except scrollbars)</b>: This userchrome will have the effect of both the other folders combined (but you will still need to theme the Scrollbars and tooltips apart using the method described on the folder with that name if you want those themed too).</li>
</ul>

<h4>You can turn the features you want on or off changing the commented lines on the CSS file (To change them you just have to open the userchrome.css with notepad or any code editor, and encase between "/*" and "*/" (without the quotation marks) the lines you don't want to take effect). Of course, if you think that you are NEVER going to use certain feature, you can always delete the specific lines you don't want without any other side-effect.</h4>

<h3>The scrollbars</h3>
<img src="https://i.imgur.com/qe6tGJW.png" title="Dark blue scrollbar" />

<p>To install the custom scrollbars to match the dark theme, you will have to use one of the 2 methods found on the "Scrollbars & tooltips dark theme" or "Scrollbars patchers(Old method)" folders inside this repository. You should be using the "Scrollbars & tooltips dark theme" folder method, since it's the most permanent, but if you find some bug or if the scrollbars lag for you, you could try using the old method one instead. The problem with the old method is that you will have to re-patch the scrollbars with each firefox update, so I'm only keeping it in case the other new method stops working in the future.</b>

<h2>Credits</h2>
<p>The original code for the custom scrollbars belongs to <b>Arty2</b>, and you can find it <a href="https://gist.github.com/Arty2/fdf19aea2c601032410516f059d58eb1">here</a>.
<p>The original code for the multirow tabs was written by <b>Andreicristianpetcu</b>, and you can find it <a href="https://discourse.mozilla.org/t/tabs-in-two-or-more-rows-like-tabmixpro-in-quantum/21657/2">here</a>, or for just the code, <a href="https://github.com/andreicristianpetcu/UserChrome-Tweaks/blob/09fa38a304af88b685f4086bc8ea9997dd7db0fd/tabs/multi_row_tabs_firefox_v57.css">here</a>. Also thanks to <b>Messna</b> for noting the class turning into an ID on FF58.</p>
<p>The original code for the multirow bookmarks toolbar belongs to the original creator mentioned in <a href="https://www.reddit.com/r/firefox/comments/75wya9/multiple_row_bookmark_toolbar_for_firefox_5758/">this reddit thread</a>, whose code was fixed by <b>jscher2000</b> to use in our current firefox.
<p>Thanks to <b>BelladonnavGF</b>, <b>Demir-delic</b>, <b>Hakerdefo</b> and <b>YiannisNi</b> for noting some issues with the theme, and <b>BelladonnavGF</b> for the addition of the url font and and tabs below url bar suggestions.</p>
<p>Also thanks to <a href="http://mozilla.zeniko.ch/userchrome.js.html">Zeniko</a>, <a href="https://github.com/Endor8/userChrome.js">Endor8</a>, and <b>RAZR_96</b> <a href="https://www.reddit.com/r/firefox/comments/7dtcpm/restyle_an_userstyle_manager_that_can_edit/">in this reddit comment</a> for the userChrome.js way of editing anonymous content (in our case the scrollbars and tooltips).</p>

<h2>Contact</h2>
<p>If you have anything to ask or tell me about the theme that isn't a bug or an issue (such as a suggestion, or some clarification I may have missed on the documentation), you can contact me through <a href="https://www.reddit.com/message/compose/">reddit</a> (You will need an account for that), directing the message to <b>Izheil</b>. 
