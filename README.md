<h1>Firefox 57+ full dark theme with dark scrollbars and multirow tabs/bookmarks</h1>

<p>This repository includes the files requires to (almost) fully dark theme firefox quantum to dark-gray colors 
(with #222-#444 colors mostly). </p>
<p><b>Of course... you could as well use these files to color your firefox any way you wanted</b>, the only thing you'd have to do is change the correct values (what each class or id does is commented above each) in the .css files (as far as you know some 
basic css or <a href="https://www.w3schools.com/colors/colors_picker.asp">color coding</a>, it shouldn't be too hard)</p>
<p>What this "theme" will not affect will be your persona, the text color used by it, and the accent color (line above active tab). To change those settings, you can change them manually through the <code>about:config</code> page, searching 
<b>lightweightThemes.usedThemes</b> there, and changing the textcolor or accentcolor codes of your used persona respectively as seen on the image below:</p>
<img src="https://i.imgur.com/3lzN95E.png">
<p>To change these you will have to use the right hex codes. You can find a color picker to hex code in <a href="https://www.w3schools.com/colors/colors_picker.asp">this page</a>.

<h3>Last update: <b>10/12/2017</b></h3>
<p>Files updated:</p>
<ul>
  <li><b>Usercontent</b> -> Themed the "donate" buttons on the <code>about:home</code> and <code>about:newtab</code> pages.</li>
  <li><b>Userchrome</b> -> Fixed some issues with the context menu separators (they would randomly go full width upon hover).</li>
</ul>
<h3>Pre-Last update: <b>08/12/2017</b></h3>
<p>Files updated:</p>
<ul>
  <li><b>Scrollbar patchers</b> -> Created Linux and Mac patchers to change the scrollbars of firefox in a more automated way (You still need to re-patch using these after a firefox update).</li>
</ul>

<h2>FAQ:</h2>

<h3>The scrollbars go back to the default ones after a firefox update!</h3>
<p>To fix this you have to re-patch the <code>chrome.manifest</code> file after each firefox update either following the manual steps found in here, <b>or applying the right re-patcher found on the "Scrollbar patchers" folder</b> (which should at least give you one or two months before having to re-patch it until the next firefox update).</p>
<p>This problem happens because firefox overwrites the omni.ja and the <code>chrome.manifest</code> file with each firefox update to "clear" any possible problem with the old version, making our change only temporary without re-patching it after each update.</p>

<h3>Why use this method instead of using <a href="https://addons.mozilla.org/es/firefox/addon/styl-us/">Stylus</a>?</h3>
<p>The main reason is that you can't style firefox about: pages nor the scrollbar with just stylus.</p>

<h3>What features does this theme have?</h3>
<p>The main features (apart from the theming) are:</p>
<ul>
  <li>Multiple row tabs.</li>
  <li>Multiple row bookmarks toolbar (2 usable rows by default, but it is NOT enabled by default. You can add more rows editing userchrome).</li>
  <li>Hides some rarely used commands on the context menu such as "Set image as desktop background".</li>
  <li>Changes the tab close button to always be visible.</li>
  <li>You can hide the sidebar completelly resizing it instead of having to click the sidebar button.</li>
  <li>Can change the URL bar font (You have to change the commented line on userchrome to use it).</li>
  <li>Can change the tabs position under the URL bar (You have to change the commented line on userchrome to use it).</li>
  <li>Change the Ublock Origin blocking page to a dark version (You need to change the commented line on usercontent).</li>
</ul>
<p>You can turn these features on or off changing the commented lines on the CSS file (To change them you just have to open the userchrome.css with notepad or any code editor, and encase between "/*" and "*/" (without the quotation marks) the lines you don't want to take effect)</p>

<h2>Installation</h2>

<h3>Main browser UI</h3>

<img src="https://i.imgur.com/dmIuudb.png" title="Dark firefox overall UI" />

<p>Most of the job is already done with the userContent.css and userChrome.css files that you have to place in the 
chrome folder of your firefox profile (Look below for "the chrome folder" section if you don't know where that is). For this to work as intended, you should be using a persona (aka lightweight theme) or the default dark theme (The persona used on the screenshot is "<a href="https://addons.mozilla.org/en-US/firefox/addon/deep-dark-blue-forest/">Deek Dark Blue forest</a>" by <b>Sondergaard</b>).</p>
<p>If you are only looking for how to change the default scrollbars, you can apply just that without the need
of using the usercontent or userchrome files provided here.</p>

<h3>The scrollbars</h3>
<p>The scrollbars file isn't as easy to install as userchrome or usercontent (but still pretty simple). 
The reason for this is that to style the scrollbars we can't use external styles through the stylus extension or userchrome.</p>
<p>To install the scrollbars, you will have to overwrite (or BVmxY.png?1" title="Dark blue scrollbar" /></a>

<p>Same as with the other files, you can edit the scrollbars appearance using the scrollbars.css, editing only past the 
"New Scrollbar starts here" line. The reason for this is that to change the scrollbars we had to override the actual scrollbars
default file of the program, so you have to keep the original lines above your changes to prevent firefox from crashing (as
well as having a default scrollbar in case you wanted to play around with the new scrollbar attributes).</p>

<h2>Credits</h2>
<p>The original code for the custom scrollbars belongs to <b>Arty2</b>, and you can find it <a href="https://gist.github.com/Arty2/fdf19aea2c601032410516f059d58eb1">here</a>.
<p>The original code for the multirow tabs was written by <b>Andreicristianpetcu</b>, and you can find it <a href="https://discourse.mozilla.org/t/tabs-in-two-or-more-rows-like-tabmixpro-in-quantum/21657/2">here</a>, or for just the code, <a href="https://github.com/andreicristianpetcu/UserChrome-Tweaks/blob/09fa38a304af88b685f4086bc8ea9997dd7db0fd/tabs/multi_row_tabs_firefox_v57.css">here</a>.
<p>The original code for the multirow bookmarks toolbar belongs to the original creator mentioned in <a href="https://www.reddit.com/r/firefox/comments/75wya9/multiple_row_bookmark_toolbar_for_firefox_5758/">this reddit thread</a>, whose code was fixed by <b>jscher2000</b> to use in our current firefox.
<p>Thanks to <b>BelladonnavGF</b>, <b>Hakerdefo</b> and <b>YiannisNi</b> for noting some issues with the theme, and <b>BelladonnavGF</b> for the addition of the url font and and tabs below url bar suggestions.</p>
