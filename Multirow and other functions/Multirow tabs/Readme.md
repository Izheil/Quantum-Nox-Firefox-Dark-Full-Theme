<h2>Multi-row tabs</h2>
<p>You can have multi-row tabs using any of these javascript files.</p>
<p>There are 2 versions, one that creates infinite rows of bars as you keep opening tabs, and another that shows a max number of rows that you can specify before showing a scrollbar to show the rest of rows.</p>

<p>You need to place <b>userChrome.xml</b> (If you already have one from this repository, you don't need to change it) on your <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions#the-chrome-folder">chrome folder</a> along with any of these files for them to work, along with it's binding rule on <code>userChrome.css</code>, which is already added in any of the userChrome versions of this repository.</p>
<p>For just the <code>userChrome.css</code> with the binding (and no other code), use the one inside this folder, unless you want to add it to your own custom userChrome, in which case you have to copy this rule inside it:</p>

<pre>
/* This enables the use of JS external files */
hbox#fullscr-toggler {
    -moz-binding: url("userChrome.xml#js")}
</pre>

<b>To avoid problems using multiple files with the tabs below fixes, I split the tabs below tweak into a standalone file. If you want to have tabs below the url bar, use the files inside the <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions/Tabs%20below">tabs below</a> folder.</b>

<h3>MultiRowTabLiteforFx.uc.js</h3>
<p>Works with Firefox 69+. Shows all tabs you currently have open splitting them on rows, without any limit to the amount of rows to show. Choose this option if you want to always see all the tabs you have open without limits to the number of rows.</p>
<img src="https://i.imgur.com/GWSgqD9.png">

<h3>MultiRowTab-scrollable.uc.js</h3>
<p>Works with Firefox 69+. Shows all tabs you currently have open splitting them on rows up to a max of 3 rows by default (can be changed using the variable inside the file). After the max number of rows has been reached, a scrollbar will be shown to be able to scroll around the extra tabs.</p>
<img src="https://i.imgur.com/qqQn4Ky.png">

<h3>MultiRowTab-scrollable-autohide.uc.js</h3>
<p>Works with Firefox 69+. This version is the same as scrollable multirow, except the scrollbars are only shown when you hover over the tabs area. It fixes some very specific issue when loading a session restore and loading a page in a session-restored blank page.</p>

<h3>MultiRowTab-*-spacing.uc.js</h3>
<p>Works with Firefox 69+. The spacing versions do the same as the others, except they try to imitate firefox default tab moving animation. <b>This version is more resource-heavy while you are moving tabs</b>, which shouldn't be much of an issue if you don't usually hold tabs in the air for minutes, but if you have a low-end computer, or are worried about resource usage or performance, you should consider using any of the other non-spacing versions instead.</p> 
<p>There is also a small issue with tabs from the upper rows forcing a space in the rows directly below it when dragging the tab to the upper rows.</p>
<img src="https://i.imgur.com/ZfKRlWQ.png">

<h2>Tab sizing</h2>
<p>The size of tabs in the last row is by default resizable, (like in the pictures above, which is the default Firefox behaviour) which will make them shrink as more tabs are fit inside the row. If you want to make all the tabs have a fixed width (so that tabs in the last row won't resize depending on how many tabs are open in that row), you will have to edit the file and change the variable <code>--tab-growth</code> to 0 (which will use the value of <code>browser.tabs.tabMinWidth</code> in <b>about:config</b> as their fixed width).</p>
<img src="https://i.imgur.com/twzsQ6V.png">

<p>It's also possible to keep tab resizability but change the min-width of tabs through <code>browser.tabs.tabMinWidth</code> as well.</p>
<p>As for tab max size, it can't be changed without causing issues with tab session managers (The issue made tab session managers to save the last 3 closed tabs when they were not suposed to), which is the reason why there isn't an option to change this inside here anymore.</p>