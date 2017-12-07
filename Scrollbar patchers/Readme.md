<h1>Scrollbar patchers</h1>

<h3>Which one to use and how:</h3>
<p><b>If using for the first time, make sure that the "scrollbars.css" file is in the same folder as the .bat files, and then apply the "First time patch".</b></p>
<p>After this, you should only need to apply the re-patcher after each firefox update (No need to have the scrollbars.css file to re-patch).</p>

<ul>
  <li>Use Scrollbars re-patcher (32-bits) if you have a 64-bits Windows and you are using a 32-bits Firefox.</li>
  <li>Use Scrollbars re-patcher (64-bits) if you have a 32-bits Windows, or a 64-bits Windows and you are using a 64-bits 
  Firefox.</li>
</ul>

<p>If you have a program files (x86) on your C: drive, you have a 64-bits Windows</p>
<p>If for some reason you installed firefox in some other drive other than C:, you will have to change the .bat files paths 
yourself (using notepad or any other code editor).</p>

<h3>What each one does</h3>
<p>The "Scrollbars first time patch.bat" adds the line <code>override chrome://global/skin/scrollbars.css scrollbars.css</code> to the <code>chrome.manifest</code> file. It also moves the scrollbars.css file from the folder the batch file is to your firefox root folder (which is why it should only be used the first time only).</p>
<p>The "Scrollbars re-patcher.bat" only edits the <code>chrome.manifest</code> file (just like the first time patch).
