<h1>Additional information</h1>
<p>You can find additional information about the repository files here.</p>

<h2>Editting CSS files</h2>

<p><b>You can edit any of the files to color your firefox any way you want</b>, the only thing you'd have to do is change the correct values (what each class or id does is commented above each) in the .css files (as far as you know some 
basic css or <a href="https://www.w3schools.com/colors/colors_picker.asp">color coding</a>, it shouldn't be too hard) using notepad, or some code editing program (such as notepad++ on Windows).</p>
<p>To change these you will have to use the right hex codes. You can find a color picker to hex code in <a href="https://www.w3schools.com/colors/colors_picker.asp">this page</a>.</p>
<h4>You can also turn the features you want on or off changing the commented lines on <code>userChrome.css</code> (To change them you just have to open it with notepad or any code editor, and encase between "/*" and "*/" (without the quotation marks) the lines you don't want to take effect). Of course, if you think that you are NEVER going to use certain feature, you can always delete the specific lines you don't want without any other side-effect.</h4>

<h2>Replacing some Tab Mix Plus features</h2>

<p>The files in this repository cover <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions/Multirow%20tabs">multi-row tabs</a>, <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/CSS%20tweaks">keep the close button on tabs always visible</a>, <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions/Other%20experimental%20features#Switch-to-tab-on-hoverucjs">focus tab on hover</a>, and color-coding tabs when they are loaded, unloaded (<a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/CSS%20tweaks">CSS Tweaks section</a>), etc...</p>
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

<h2>Frequently Asked Questions</h2>

<h3>How do I submit an issue?</h3>
<s><p>As of 26/03/2019 I stopped offering active support for new features or issues. This doesn't mean that I won't be mantaining the project, it just means I won't be taking feature requests nor unrelated issues to the functionability offered by the files inside this repository anymore.</p>

<p>If you find some problem that is <b>directly related</b> with any of the functions offered by any of the files in this repository, you can comment it inside the relevant commit that you think may have affected the function that is giving you trouble. If you can't tell which, comment in the last one. Comments about new functionability or things that aren't related to the actual functionability of the files will be ignored (You can already ask about problems you may have with firefox on <a href="https://www.reddit.com/r/firefox/">r/firefox</a> or <a href="https://www.reddit.com/r/firefoxcss/">r/firefoxCSS</a> subreddits, or on <a href="https://support.mozilla.org/">Firefox support</a> pages).</p></s>

<p>Issues are open, so click the issues tab, and try to be as descriptive as you can be with the problem you found in any of the files of this repository. Any problem that is NOT directly related to any of the files here will be closed without further warning.</p>

<h3>Why isn't there an installer for the full theme for Firefox?</h3>
<p>The theme here was created back when the default dark theme didn't cover any <code>about:</code> page, nor any menu/sidebar, and when no other full theme existed. Since then, <b>Firefox default dark theme was updated to cover many of these elements (if still missing some dialogs), so there isn't much of a need for an external theme anymore</b>. If you are using Windows or any other OS that paints all program dialogs white, you can install any custom theme to paint them dark (there are plenty in deviantart), which will also affect Firefox dialogs.
I made this theme for personal use since I didn't like how everything was flashing white, but now it's not really needed anymore, so I stopped working on upgrading it as often. This doesn't mean that I won't patch things in it (since I still use it myself), but <b>I won't be trying to make installers for the theme part</b>.</p>
<p>Right now the focus is on the Javascript functions that can't be emulated with webextensions.</p>

<h3>Why did you remove the <code>userchrome.xml</code> method?</h3>
<p>Mozilla has finally removed all XBL bindings from Firefox, and it's only a matter of time until they remove support for this method (which depended on it), so I decided to switch to this new method as soon as possible to avoid the upcoming problems. If you still use the userchrome.xml method you can still use it until Mozilla removes support for it, in which case you will have to switch to the new one.</p>
<p>You can find the new patching method in the <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow and other functions/JS Loader">JS Loader</a> folder.</p>

<h3>I placed the files inside the chrome folder but I don't see any change</h3>
<p>Make sure you downloaded the raw files from the repository (either cloning the whole repository, downloading the RAW version of the files, or copying the code you are interested in yourself), and placed them inside the chrome folder inside the root profile folder (more information on that inside the dark theme section of this repository).</p>
<p>If you are using Firefox 69+, you also need to have enabled <code>toolkit.legacyUserProfileCustomizations.stylesheets</code> in <code>about:config</code> for userChrome or userContent (or any file in the chrome folder) to be loaded at all as per <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=1541233#c35">bug #1541233</a>.</p>
<p>If you instead are only using the multi-row files, make sure that you patched firefox root folder along with the chrome folder as explained in <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow and other functions/JS Loader">JS Loader</a>.</p>

<h3>The pre-loading screen of websites is still white, how can I change this?</h3>
<p>The fastest way to solve the "blinking" white screen is to change the default web background color on Firefox settings > General > "Colors..." button > Background, which will make the blinking dissapear and be changed to the color you set up. This, although, can cause some issues on some very few and specific pages like BBC, where they don't set a background color to override the one set here (the number of sites with this problem is very small, most sites override the background color set by this setting).</p>

<h3>The tabs toolbar background has the default windows 7 color instead of dark colors.</h3>
<p>Since this only happens when not using a persona, either install a lightweight theme, or uncomment the rule in line 38 (#TabsToolbar one) on <code>userChrome.css</code>. To do so, just delete the ending "/*" in the line above it.</p>

<h3>Some dialog buttons still appear as white.</h3>
<p>After FF69+, it's not possible to change the color of hover buttons on these dialogs with CSS (seems to be a bug with Firefox), so the only way to do this without JS is to invert the colors. The problem is that people that have an OS that paints these buttons dark would get the colors inverted to white... So if you are experiencing this issue, delete the ending "/*" on line 22 on userChrome.css</a></p>
<pre>/* This inverts the button color of dialog boxes. If using an OS that paints buttons white,
uncomment this line (by deleting the ending /* ->) */
  --dialog-buttons-fix: invert(80%) hue-rotate(190deg);</pre>

<h3>The urlbar shows as white background with white text over it after installing the theme.</h3>
<p>This only happens when using Firefox default theme, either use firefox built-in dark theme along with this one, or use any other lightweight theme you like.</p>

<h3>The synced tabs sidebar isn't themed.</h3>
<p>Since it's anonymous content of the browser we can't theme it through userChrome or userContent, which is why you will have to apply the fix inside <code>Sync-tabs-sidebar.as.css</code>. It requires the use of external CSS files loading, which is enabled through the use of the files inside <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow and other functions/JS Loader">JS Loader</a> folder.</p>

<h3>Some context menu commands dissapear after installing userChrome.</h3>
<p>If you only want the dark theme, use the default <code>userChrome.css</code> file inside "Full dark theme", which won't make the context menu commands dissapear. In case you want to use the features part of the theme, just delete everything after the line that says <code>/* CONTEXT MENU COMMANDS */</code> (you can find it using the search option on notepad, or the code editor you are using).</p>
<p>In case you still want to delete some commands but not all, just comment out the ones that you want to appear, and leave as active the ones that you want to dissapear.</p>
<p>For example, this is active, so the command is hidden:</p>
<pre>/* Send image... */
#context-sendimage,</pre>
<p>...But this is commented out, so the command will show on the context menu:</p>
<pre>/* Send image... *//*
#context-sendimage,*/</pre>
<p>You will see that the ones that I have commented out by default only have the starting "/*" of the comment after the description of what they are, since the closing "*/" would come from the next description comment below them.</p>

<h3>The bookmarks toolbar text/tabs text color is black and I can't see the letters over the dark background.</h3>
<p>This is caused by your persona (lightweight theme), and while you could change these settings inside userChrome, I thought it was better to just change the settings on the persona directly (since not all personas will look the same). To do so you'd have to open <code>about:config</code>, and search for <b>lightweightThemes.usedThemes</b>. Once there, find the "textcolor" setting and type any color you'd want to use instead of black or the color being used by the theme (use #fff for white). The persona you are currently using should be in the first place in the list.</p>

<h3>The bookmarks multirow shows an empty scrollbar when enabled.</h3>
<p>If you are using an old version of the scrollbars, or you are just plain not using the scrollbars here, you will have to add some code to delete the empty scrollbars that show on the bookmark toolbars. You have to use this code on a "*.ac.css" file (so you would need to have firefox patched with the method explained on the <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions">Multirow and other functions</a> folder), since otherwise it won't work:

<pre>
/* This deletes the scrollbar from bookmarks toolbar when using multirow bookmarks */
#PlacesToolbarItems scrollbar {display: none !important}
</pre>

<h3>I only want to use the multirow/(Any other) feature, but not the other ones!</h3>
<p>If you only want to use multirow, then first patch firefox with the method in <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow and other functions/JS Loader">JS Loader</a>, and then just use any of the multirow files inside <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions/Multirow%20tabs">Multirow tabs</a> folder. You don't need to use <code>userChrome.css</code> nor <code>userContent.css</code> for this at all with the new patching method.</p>

<p>You only need to modify <b>userChrome.css</b>, deleting the lines that you don't want to apply (Every function has a comment above it saying what each ruleset does), or if you think you may want them later, just encase the feature parts that you don't want to apply between /* and */:</p>

<code>/* This is an example of a comment that wouldn't be read on a .css file */</code>

<h3>I'm opening web files locally (as in opening html pages that you have created or downloaded) and the background is not the color it should be.</h3>
<p>To change the directory browsing page and change how .css or some .txt files appear when opened with Firefox, I had to specify it to affect urls that start with "file:///", meaning that any file opened with Firefox will get overriden with those rules as well. To prevent this, go to userContent.css, and comment out the lines that affect this url (This rule should be exactly under the color variables at the start of the file).</p>

<h3>I placed <code>userChrome.css</code> inside my chrome folder and I still don't have multi-row tabs!</h3>
<p>While we only needed to use CSS to enable multi-row tabs, this breaks tabs draggability, making reordering tabs when it was enabled a bit erratic, so to fix this, I decided to put all multi-row tabs code inside the <b>MultiRowTabLiteforFx.uc.js</b> file. This means that now Multi-row tabs can be enabled following the method described inside the <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions/Multirow%20tabs">Multirow tabs</a> folder. If you were using CSS code on your <code>userChrome.css</code> to enable multirow tabs, delete (or comment it out) for the js file to take effect.</p>

<h3>Why use this method instead of using <a href="https://addons.mozilla.org/es/firefox/addon/styl-us/">Stylus</a>?</h3>
<p>The main reason is that you can't style firefox about: pages nor dialog windows with just stylus.</p>

<h3>The theme is making the text of some addon popups unreadable, how do I fix this?</h3>
<p>The theme is made so that it changes most background colors, including the one of the popups that don't have any background color specified by their original creator. Sadly it doesn't change the text of these by default, so you may have to do it manually, or report the addon you want themed here, or just use the fix inside userChrome.css (at around lines 926-929) to turn the addons back to their white background color.</p>