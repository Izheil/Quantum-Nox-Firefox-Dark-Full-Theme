<h1>Only functionability CSS tweaks</h1>

<p>The files contained here contain fixes that will let you alter the default behaviour of Firefox. They are intended to be used as a template of the functions that you can use on your own custom <code>userChrome.css</code> for this goal. This means that you shouldn't just copy everything in every file to your userChrome, but instead select the features you are interested on to customize your Firefox in the way that you want.</p> 

<p>With this goal in mind, a base empty <code>userChrome.css</code> is included (with the javascript fix included if you want to use it later, which won't work unless you have <code>userChrome.xml</code> as well), in case you don't have one already, so that you can use any of the tweaks included here without the need to know much CSS (you will just need to copy the things you want, which have a comment above them with a description of what each does).</p>

<p>If you are using the dark theme <code>userChrome.css</code> file, add the fixes from the files here in that one instead.</p>

<p>To make it work, it's as simple as copying the function you want to apply at the bottom of <code>userChrome.css</code>, place it inside <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/wiki/Chrome-and-Root-folders#the-chrome-folder">the chrome folder</a> if you hadn't yet, and restart Firefox.</p>

<h4>You can also keep some tweak inside your <code>userChrome.css</code> without it being enabled by encasing the lines you don't want to apply between "/*" and "*/" (without the quotation marks).</h4>

<h3>Bookmarks+URLbar+Sidebar.css</h3>

<p>This file contains changes that affect the behaviour of the bookmarks bar (such as enabling <b>multirow bookmarks</b> that you can also make auto-hide), the URL bar, and the sidebar.</p>

<ul>
  <li>Allow the sidebar be completelly closed by just resizing it.</li>
  <li>Change the font used on the ULR box to prevent URL spoofing with a more differentiable font.</li>
  <li>Bookmark toolbar auto-hide.</li>
  <li>Fix for an issue with fullscreen not showing bookmark bar nor menu bar.</li>
</ul>

<h3>Context-menu-commands.css</h3>

<p>This file contains selectors that target most commands contained in context menus (like send image, reload tab, etc..), so that you can hide them to make your context menus look less cluttered with commands that you may never or rarely use.</p>

<ul>
  <li>You can hide the following commands from context menus:
  	<ul>
  	  <li>Reload tab.</li>
      <li>Mute tab.</li>
      <li>Mute selected tabs.</li>
      <li>Select all tabs (only the active tab context menu, not the title context menu one).</li>
  	  <li>Pin tab.</li>
      <li>Pin selected tabs.</li>
  	  <li>Duplicate tab.</li>
  	  <li>Open tab in new window.</li>
      <li>Send tab to device.</li>
      <li>Separators left by send tab to device on tabs context menu.</li>
  	  <li>Reload selected tabs (only the active tab context menu, not the title context menu one).</li>
      <li>Bookmark tab.</li>
  	  <li>Bookmark selected tabs.</li>
      <li>Reopen tab in container.</li>
      <li>Move tab.</li>
  	  <li>Close all tabs to the right.</li>
  	  <li>Close all other tabs.</li>
  	  <li>Close tab.</li>
      <li>Open bookmarked page in a new window.</li>
      <li>Open bookmarked page in a new private window.</li>
      <li>Open all bookmarked pages in the bookmark folder.</li>
  	  <li>Navigation buttons (Back, forward and reload buttons) & it's separator (since you can do the same with the keyboard or other buttons).</li>
  	  <li>Send image... (misclicking this when saving an image can happen easily, and waiting for outlook to open to close it gets annoying).</li>
  	  <li>Set image as desktop background...</li>
  	  <li>Bookmark this page (you can do the same with the star icon on the URL bar, or creating the bookmark manually with more control of where it's going to be placed).</li>
  	  <li>Send page...(same as with send image, if you wanted to send something, you'd open your prefered mail yourself).</li>
      <li>Send video... (same as with send page).</li>
      <li>Save video capture.</li>
      <li>Frame selector separator (You can hide it to avoid double separators).</li>
  	  <li>Bookmark this link (same as bookmark this page).</li>
  	  <li>Send link... (same as send image).</li>
      <li>Search highlighted word on your default search engine.</li>
  	  <li>Open link in new tab (You can do the same middle mouse clicking, or holding ctrl while clicking a link).</li>
  	  <li>Open link in a new window.</li>
  	  <li>Open link in a private window.</li>
  	  <li>Take a screenshot and its separator.</li>
  	  <li>Send tab to device and its separators.</li>
  	  <li>Send page to device and its separator.</li>
  	  <li>Send link to device and its separator.</li>
  	</ul></li>
</ul>

<h3>Tab-related-Tweaks.css</h3>

<p>These will let you change the look and position of the tabs and the tab box.</p>

<ul>
  <li><b>Tabs bar below</b> bookmarks or URL box.</li>
  <li>Give tabs rounded corners.</li>
  <li>Tab close button always visible.</li>
  <li>Change tab colors depending on it's read/loaded state.</li>
</ul>

<p>For the unread state to take effect you need to also patch your Firefox to label unread tabs as so (Firefox removed the unread state of tabs a few versions ago). You can do this using the patcher by choosing your Firefox version, and the "Enable unread state on tabs" option.</p>
<p>This will add a "utils" folder and a "setAttribute_unread.uc.js" file to your chrome folder, which are required to customize unread tabs with userChrome.</p> 
<p>Alternatively, if you use MacOS or something goes wrong with the patcher, you can always do the manual patching with the method explained in <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions/JS%20Loader">JS Loader</a> folder from this repository, and then copying the <a href="https://raw.githubusercontent.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/master/CSS%20tweaks/setAttribute_unread.uc.js">setAttribute_unread.uc.js</a> file to your <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/wiki/Chrome-and-Root-folders#the-chrome-folder">chrome folder</a>.</p>

<b>Rounded tabs:</b>
  <img src="https://i.imgur.com/qoG4Iiy.png">

<p>If you want the old style (pre FF57) rounded tabs for firefox, you should add <a href="https://github.com/wilfredwee/photon-australis">australis</a> code to your userChrome.css instead.</p>

<h2>Installation</h2>

<p>All you need to do is paste the tweaks you want to apply inside userChrome.css, and then place this file inside <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/wiki/Chrome-and-Root-folders#the-chrome-folder">the chrome folder</a> of your Firefox profile.</p>

<h4>Step by step:</h4>
<ul>
  <li>Create an empty userchrome.css file, or right click and "save link as..." <a href="https://raw.githubusercontent.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/master/CSS%20tweaks/userChrome.css">this</a>, naming it <code>userChrome.css</code>.</li>
  <li>Type <code>about:support</code> in your URL bar, then go to that page.</li>
  <li>Click the "open folder" button inside the "profile folder" section.</li>
  <li>Create a folder named "chrome" in your profile folder if it doesn't exist yet.</li>
  <li>Place "userChrome.css" inside <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/wiki/Chrome-and-Root-folders#the-chrome-folder">the chrome folder</a>.</li>
  <li>Edit userChrome.css with notepad or any code editor to add the rules that are you interested in from the files "Context-menu-commands.css", "Bookmarks+URLbar+Sidebar.css", or "Tab-related-Tweaks.css" from this repository, or any other CSS rule you want to apply.</li>
</ul>