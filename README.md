<img src="https://i.imgur.com/F7qziom.png" title="Quantum Nox"/>

<h3>Previously known as "Firefox 57+ full dark theme with scrollbars and multirow tabs", I decided to give it an actual name instead of leaving it as just a description.</h3>
<pre>Since Firefox 69, you have to enable <code>toolkit.legacyUserProfileCustomizations.stylesheets</code> 
in <code>about:config</code> for userChrome and userContent to be loaded at all as per <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=1541233#c35">bug #1541233</a>.</pre>

<p>This theme is mainly <b>intended to be used alongside a lightweight theme</b>, and for the stable release of Firefox (<b>This means that while it will most probably work with nightly and ESR for the most part, it may have less support for those versions</b>).</p>
<p>You can use it to fully change the colors of most of firefox UI to dark-gray colors (with #222-#444 colors mostly), including scrollbars, tooltips, sidebar, as well as dialogs. With the files here you can also as remove some context menu options, enable multirow tabs, change the font of the url bar...</p>

<p>If you want to know how to change some colors of the theme, check the <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Info#Editting CSS files">Info</a> section.</p>

<h3>Last update: <b>08/03/2020</b></h3>
<p>Files updated:</p>
<ul>
	<li><b>userContent.css</b>: Added a translucid black box on pinned sites for speed dial titles for better visibility when using a background image on <code>about:home</code>.</li>
</ul>
<h3>Pre-Last update: <b>06/03/2019</b></h3>
<ul>
	<li><b>userChrome.css</b>: Tabs should have a transparent background instead of the manually set background.</li>
</ul>

<h3>A note on people looking to replace some Tab Mix Plus features:</h3>
<p>You can find some of the basic settings that can be simulated through <code>about:config</code>, some userscripts, and some addons <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Info#Replacing-some-Tab-Mix-Plus-features">here</a>.</p>

<h2>Main browser UI</h2>
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

<h2>General sites dark theme</h2>
<p>You can find an all-around sites stylesheet that will paint every site you visit dark <a href="https://github.com/Izheil/Dark-userstyles/tree/master/Global%20dark%20userstyle">here</a>. <b>You need <a href="https://addons.mozilla.org/es/firefox/addon/styl-us/">Stylus addon</a> to use it</b>.</p>

<p>While it's not perfect (meaning that you should still use per-site styles for the sites you visit often), it can help to darken most sites when browsing around general sites that you don't visit often, and thus don't want/can't find a specific userstyle for them.</p>
<img src="https://i.imgur.com/mbeHNQp.png">

<h2>Addon dark themes</h2>
<p>You can apply a dark theme to certain addons changing the UUID's of them inside the <code>addons.css</code> file inside the "Full dark theme" folder (more instructions on how to do that inside the addons file).</p>
<img src="https://i.imgur.com/bEleqP7.png" title="Dark addons" />
<p>Here is a list of the themed addons:</p>
<ul>
	<li><a href="https://addons.mozilla.org/en-US/firefox/addon/video-downloader-player/">Ant Video Downloader</a></li>
	<li><a href="https://addons.mozilla.org/en-US/firefox/addon/cookie-autodelete/">Cookie autodelete</a></li>
	<li><a href="https://addons.mozilla.org/en-US/firefox/addon/s3download-statusbar/">Download Manager (S3)</a></li>
	<li><a href="https://addons.mozilla.org/en-US/firefox/addon/history-autodelete/">History autodelete</a></li>
	<li><a href="https://addons.mozilla.org/en-US/firefox/addon/https-everywhere/">HTTPS Everywhere</a></li>
	<li><a href="https://addons.mozilla.org/en-US/firefox/addon/noscript/">Noscript</a></li>
	<li><a href="https://addons.mozilla.org/en-US/firefox/addon/gmail-notifier-restartless/">Notifier for Gmail (restartless)</a></li>
	<li><a href="https://addons.mozilla.org/en-US/firefox/addon/multi-account-containers/">Multi-accounts containers</a></li>
	<li><a href="https://addons.mozilla.org/en-US/firefox/addon/onetab/">OneTab</a></li>
	<li><a href="https://addons.mozilla.org/en-US/firefox/addon/popup-blocker-ultimate/">Popup Blocker Ultimate</a></li>
	<li><a href="https://addons.mozilla.org/en-US/firefox/addon/privacy-badger17/">Privacy badger</a></li>
	<li><a href="https://addons.mozilla.org/en-US/firefox/addon/tab-session-manager/">Tab session manager</a></li>
	<li><a href="https://addons.mozilla.org/en-US/firefox/addon/temporary-containers/">Temporary containers</a></li>
	<li><a href="https://addons.mozilla.org/en-US/firefox/addon/ublock-origin/">Ublock Origin</a></li>
	<li><s><a href="https://addons.mozilla.org/en-US/firefox/addon/undo-closed-tabs-revived/">Undo closed tabs button</a></s> -> You should use <a href="https://addons.mozilla.org/en-US/firefox/addon/undoclosetabbutton/">Undo close tab</a> instead (which requires no theming).</li>
	<li><a href="https://addons.mozilla.org/en-US/firefox/addon/video-downloadhelper/">Video Download Helper</a></li> 
	<li><a href="https://addons.mozilla.org/en-US/firefox/addon/viewhance/">Viewhance</a></li>
</ul>

<p>You might have noticed that we no longer have <a href="https://gist.github.com/Izheil/49db523ee66d88995401bb6844605763">Lastpass dark theme</a> inside <code>addons.css</code> anymore. This is because at the time that addon was themed, I didn't know much about it. After some research it seems like Lastpass has had a history of security issues (in 2011, 2015, 2016, and 2017), as well as there being other open source alternatives out there that seem to be more reliable, like <b>Bitwarden</b> (it also has a built-in dark mode) which is available for all major browsers.</p>

<h3>The scrollbars</h3>

<p>This theme colors scrollbars using <code>userContent.css</code> to give them a basic re-color.</p> 
<img src="https://i.imgur.com/hqwoq9n.png" title="Re-colored dark scrollbar" />

<p>If you <b>want a different style on the scrollbars</b>, you can try using the <code>scrollbars.as.css</code> file inside the <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Full%20dark%20theme/Alternative%20scrollbars%20%26%20tooltips/Alternative%20scrollbars">Alternative scrollbars</a> folder, which will make the scrollbars look more rounded and will have some sort of "puffy" effect when clicking them.</p>
<img src="https://i.imgur.com/sOHN1ds.gif" title="Custom dark blue scrollbar" />

<p>If instead you just <b>don't want scrollbars to show at all but keep scrollability</b>, you can do this through <code>userContent.css</code> setting the variable <code>--scrollbars-width</code> to none (should be the first rule on the <code>:root</code> section (almost at the start)), and deleting <code>scrollbars.as.css</code>.</p>
<p>If you aren't using the userContent provided here for some reason, you can always just add this code to your self-created <code>userContent.css</code>:</p><code>*|* {scrollbar-width: none !important}</code>
<br /><br />

<h3>F.A.Q.</h3>
<p>You can find the frequently asked questions in <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Info#Frequently-asked-questions">here</a>.</p>

<h2>Credits</h2>
<p>The original code for the custom scrollbars which we modified here belongs to <b>Arty2</b>, and you can find it <a href="https://gist.github.com/Arty2/fdf19aea2c601032410516f059d58eb1">here</a>.
<p>The original code for the multirow tabs (the CSS part) was written by <b>Andreicristianpetcu</b>, and you can find it <a href="https://discourse.mozilla.org/t/tabs-in-two-or-more-rows-like-tabmixpro-in-quantum/21657/2">here</a>, or for just the code, <a href="https://github.com/andreicristianpetcu/UserChrome-Tweaks/blob/09fa38a304af88b685f4086bc8ea9997dd7db0fd/tabs/multi_row_tabs_firefox_v57.css">here</a>. The fix of multi-row tabs draggability was made by <b>TroudhuK</b>, and you can find the original one <a href="https://github.com/TroudhuK/userChrome.js/blob/patch-1/Firefox-57/Mehrzeilige-Tableiste/MultiRowTabLiteforFx.uc.js">here</a>.</p>
<p>The original code for the multirow bookmarks toolbar belongs to the original creator mentioned in <a href="https://www.reddit.com/r/firefox/comments/75wya9/multiple_row_bookmark_toolbar_for_firefox_5758/">this reddit thread</a>, whose code was fixed by <b>jscher2000</b> to use in our current firefox version.</p>
<p>The fix to be able to theme unread tabs again after FF61 (see <a href="https://bugzilla.mozilla.org/show_bug.cgi?format=default&id=1453957">bug 1453957</a> on bugzilla) as mentioned in <a href="https://www.reddit.com/r/FirefoxCSS/comments/8yruy8/tabbrowsertabunread_backgroundimage/">this reddit thread</a>, was made by <b>moko1960</b> to use in Firefox 61+.</p>
<p>The code to be able to edit anonymous content (in our case the scrollbars and tooltips) was created thanks to the efforts of <a href="http://mozilla.zeniko.ch/userchrome.js.html">Zeniko</a>, <a href="https://github.com/nuchi/firefox-quantum-userchromejs">Nichu</a>, and <a href="https://github.com/Sporif/firefox-quantum-userchromejs">Sporif</a>, and <a href="https://github.com/xiaoxiaoflood/firefox-scripts">Xiaoxiaoflood</a>.
<p>Special thanks to <b>Messna</b> for noting the class turning into an ID on FF58, and <b>Snwflake</b> for fixing Firefox root folder location on MacOS.</p>
<p>Also thanks to <b>532910</b>, <b>BelladonnavGF</b>, <b>DallasBelt</b>, <b>Demir-delic</b>, <b>Gitut2007</b>, <b>Hakerdefo</b>, <b>Tkhquang</b> and <b>YiannisNi</b> for noting some issues with the theme, and the requests for new features that extended this project.</p>

<h2>Donations</h2>
<p>If you want to support this project, consider buying me a coffee to motivate me keep this repository up and running.</p>
​
<a href="https://ko-fi.com/K3K4TQ97" target="_blank"><img height="36" style="border:0px;height:36px;" src="https://az743702.vo.msecnd.net/cdn/kofi2.png?v=2" border="0" alt="Buy Me a Coffee at ko-fi.com" /></a>

<p>...or any other amount you see fit on paypal.</p>

<a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=BMUFYBSRA7ENL&source=url"><img alt="" border="0" src="https://www.paypalobjects.com/webstatic/mktg/logo/pp_cc_mark_74x46.jpg"/></a>
