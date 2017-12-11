<h1>Scrollbar patchers</h1>

<p>There is a different patcher depending on your OS, so use the one that applies to yours.</p>
<p>There is also an explanation on what to do on each of the "readme!.txt" on each of the folders.</p>
<p><b>Linux and mac shell scripts should be functional, but if you find any issue, report it here and I'll fix them right away</b>.</p>

<h3>What each file does</h3>
<p>The "Scrollbars first time patch" adds the line <code>override chrome://global/skin/scrollbars.css scrollbars.css</code> to the <code>chrome.manifest</code> file. It also moves the scrollbars.css file from the folder the batch file is the one where the manifest is (which is why it should only be used the first time only).</p>
<p>The "Scrollbars re-patcher" only edits the <code>chrome.manifest</code> file (just like the first time patch).
