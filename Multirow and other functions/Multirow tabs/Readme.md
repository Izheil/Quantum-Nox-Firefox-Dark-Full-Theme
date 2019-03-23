<h2>Multi-row tabs</h2>
<p>You can have multi-row tabs using any of these javascript files.</p>
<p>There are 2 versions, one that creates infinite rows of bars as you keep opening tabs, and another that shows a max number of rows that you can specify before showing a scrollbar to show the rest of rows.</p>

<p>You need to place <b>userchrome.xml</b> (If you already have one from this repository, you don't need to change it) on your <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions#the-chrome-folder">chrome folder</a> along with any of these files for them to work, along with it's binding rule on <code>userchrome.css</code>, which is already added in any of the userchrome versions of this repository. If you don't want to use any of the <code>userchrome.css</code> files from this repository, all you need to do is create your own with this code:</p>

<pre>
/* DO NOT DELETE THIS LINE */
@namespace url("http://www.mozilla.org/keymaster/gatekeeper/there.is.only.xul");

/* This enables the use of JS external files */
toolbarbutton#alltabs-button {
    -moz-binding: url("userChrome.xml#js")}
</pre>
<p>... or just the <b>toolbarbutton</b> rule if you had an existing userchrome that didn't come from this repository.</p>

<h3>MultiRowTabLiteforFx.uc.js</h3>
<p>Works with Firefox 66+. Shows all tabs you currently have open splitting them on rows, without any limit to the amount of rows to show. Choose this option if you want to always see all the tabs you have open without limits to the number of rows.</p>
<img src="https://i.imgur.com/GWSgqD9.png">

<h3>MultiRowTab-scrollable.uc.js</h3>
<p>Works with Firefox 66+. Shows all tabs you currently have open splitting them on rows up to a max of 3 rows by default (can be changed using the variable inside the file). After the max number of rows has been reached, a scrollbar will be shown to be able to scroll around the extra tabs.</p>
<img src="https://i.imgur.com/qqQn4Ky.png">

<h3>MultiRowTab-scrollable-autohide.uc.js</h3>
<p>Works with Firefox 66+. This version is the same as scrollable multirow, except the scrollbars are only shown when you hover over the tabs area. It fixes some very specific issue when loading a session restore and loading a page in a session-restored blank page.</p>
