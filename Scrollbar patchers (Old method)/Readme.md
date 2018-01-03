<h1>Scrollbar patchers</h1>

<p>There is a different patcher depending on your OS, so use the one that applies to yours.</p>
<p>There is also an explanation on what to do on each of the "readme!.txt" on each of the folders.</p>
<p><b>Linux and mac shell scripts should be functional, but if you find any issue, report it here and I'll fix them right away</b>.</p>

<h3>What each file does</h3>
<p>The "Scrollbars first time patch" adds the line <code>override chrome://global/skin/scrollbars.css scrollbars.css</code> to the <code>chrome.manifest</code> file. It also moves the scrollbars.css file from the folder the batch file is the one where the manifest is (which is why it should only be used the first time only).</p>
<p>The "Scrollbars re-patcher" only edits the <code>chrome.manifest</code> file (just like the first time patch).
  
<h3>Installation</h3>

<p>The scrollbars file isn't as easy to install as userchrome or usercontent (but still pretty simple). 
The reason for this is that to style the scrollbars we can't use external styles through the stylus extension or userchrome.</p>
<p>To install the scrollbars, you will have to overwrite (or edit it, since it's just a line) a file (<code>chrome.manifest</code>), as well as <b>placing the scrollbars.css file in the same folder as the <code>chrome.manifest</code> we have to edit</b>.</p>

<p>To overwrite <code>chrome.manifest</code>, and place the scrollbars.css file in the correct folder, you can either use the batch files inside the "Scrollbars patchers" folder found in this repository <b>with admin rights</b> (which will do the job for you), or you can do it manually.<p>
  
<p><b>Since firefox resets the <code>chrome.manifest</code> file with each new update, you will have to change it each time firefox updates</b> (which should at least give you one or two months before having to re-edit it). Again, you can do this manually, or applying the right "re-patcher" batch file (giving it admin rights) on the "Scrollbar patchers" folder after each firefox update.</p>

<p>For those that want (or have) to do it manually, I'll explain the method to patch the scrollbars below. The first thing to do is find the right <code>chrome.manifest</code> file. On Linux and Mac there is only one <code>chrome.manifest</code>, so you'd only have to place the scrollbar in the same folder where you find the manifest.<p>
  
<p>Depending on your OS, the root folder will be in a different location (information taken from <a href="http://kb.mozillazine.org/Installation_directory">here</a>):</p>

<h4>For Windows, you can find firefox root folder here:</h4>

<pre>32bits Firefox -> C:\Program Files (x86)\Mozilla Firefox\
64bits Firefox -> C:\Program Files\Mozilla Firefox\</pre>

<p>If you have a 32-bits Windows, you will only see the 64-bits path.</p>

<h4>For Linux, you can find the manifest file by default in this path:</h4>

<pre>/usr/lib/firefox/browser</pre>

<p>In some cases you might find a difference between 32 and 64 bits program installation paths in Linux, in that case you'd find the path here:</p> 

<pre>/usr/lib64/firefox/browser</pre>

<p>The installation directory path may also vary depending on the distribution, and if you use a package manager to install the application from their repository.</p>

<h4>For Mac, you can find the chrome manifest in this path:</h4>

<pre>/Applications/Firefox.app/content/resources</pre>

<p>To open "Firefox.app", Ctrl-click it and select Show Package Contents. If you simply click it, you will start the application.</p>

<p>Once you have located the <code>chrome.manifest</code> file on the right firefox folder (On Windows you will find a second <code>chrome.manifest</code> inside the "browser" folder that you don't have to edit), overwrite it with the <code>chrome.manifest</code> uploaded here.</p>
<p>If for some reason you wanted to edit it yourself, you can do so by editing it with notepad, kate, or any code editor program you see fit for the job (but do NOT use Word or any other enriched text editor). You will see a blank file (it was 0kb heavy after all), where you should add the line:</p>

<pre>override chrome://global/skin/scrollbars.css scrollbars.css</pre>

<p>If you have done everything correctly, firefox should have the custom-made scrollbars now (or after you restart firefox if
you had it open).</p>
  
<h4>Short version (Windows):</h4>
<ul>
  <li>Download the repository files, and go to the windows scrollbar patchers folder.</li>
  <li>Make sure there is a "scrollbars.css" file inside the folder where the .bat files are.</li>
  <li>Find out if you have a 32-bits windows or a 64-bits one (If you have a "program files (x86)" folder on your c: drive you have a 64-bits Windows).</li>
  <li>If you have a 32-bits windows, launch the "First time patch (64-bits).bat" file (Yes, the 64 bits one).</li>
  <li>If you have a 64-bits windows, open firefox, open the hamburguer menu, go to help > about firefox, and check if you have a 32-bits or a 64-bits firefox. If 32-bits firefox, launch "First time patch (32-bits).bat", otherwise the 64-bits one.</li>
  <li>Restart firefox if you had it open for the changes to apply.</li>
  <li>(Optional) Copy the "re-patcher.bat" file that applies to your windows and firefox somewhere so that you can re-apply it after a firefox update to get back the custom scrollbars (only once after each update).</li>
</ul>

<h4>Short version (Linux):</h4>
<ul>
  <li>Download the repository files, and go to the linux scrollbar patchers folder.</li>
  <li>Make sure there is a "scrollbars.css" file inside the folder where the .sh files are.</li>
  <li>(Optional) Move the "scrollbars.css" and "1st-patch.sh" files to a short path folder.</li>
  <li>If you have a custom path for firefox installation folder, update the path routes on the patch files.</li>
  <li>Open a terminal, and type <code>chmod +x /(the path where the 1st-patch.sh file is)/1st-patch.sh</code>.</li>
  <li>Type <code>sh /(the path where the 1st-patch.sh file is)/1st-patch.sh</code>.</li>
  <li>Restart firefox if you had it open for the changes to apply.</li>
  <li>(Optional) Copy the "re-patcher.sh" file somewhere safe so that you can re-apply it after a firefox update to get back the custom scrollbars (only once after each update).</li>
</ul>

<h4>Short version (Mac):</h4>
<ul>
  <li>Download the repository files, and go to the linux scrollbar patchers folder.</li>
  <li>Make sure there is a "scrollbars.css" file inside the folder where the patch files are.</li>
  <li>If you have a custom path for firefox installation folder, update the path routes on the patch files.</li>
  <li>Execute the first time patch (Or run it's commands on a terminal)</li>
  <li>Restart firefox if you had it open for the changes to apply.</li>
  <li>(Optional) Copy the re-patch file somewhere safe so that you can re-apply it after a firefox update to get back the custom scrollbars (only once after each update).</li>
</ul>
