<h1>Patching Firefox to enable JS injection (userchromeJS)</h1>
<p>The files here are a fork of the work of <a href="https://github.com/xiaoxiaoflood/firefox-scripts">xiaoxiaoflood</a>, fixed to work with FF69+, and only loading the necessary things to load external JS and CSS files.</p>

<h2>Installation</h2>
<p>You can patch your Firefox using the installer in the <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/releases">releases</a> section. The patcher will choose the default profile folder, so if you have more than 1 profile you should go to <code>about:profiles</code> and make sure that the path the patcher selects is the same as the one of the profile that you are currently using.</p>

<b>If you are using Firefox portable, you will need to change the default root and profile folders to the ones of portable Firefox, so check the <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/wiki/Chrome-and-Root-folders#firefox-root-folder">firefox root folder</a> and <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/wiki/Chrome-and-Root-folders#the-chrome-folder">chrome folder</a> sections to locate them first.<b>

<p>Alternatively you can follow the explanations below for the manual installation.</p>

<h3>Manual installation</h3>
<p>To patch firefox with this method, you will have to locate both <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/wiki/Chrome-and-Root-folders#firefox-root-folder">firefox root folder</a>, and your profile <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/wiki/Chrome-and-Root-folders#the-chrome-folder">chrome folder</a>.</p>

<h4>Step by step:</h4>
<ol>
  <li>Copy <code>defaults</code> folder and <code>config.js</code> files inside <code>root</code> to <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/wiki/Chrome-and-Root-folders#firefox-root-folder">firefox root folder</a>.</li>
  <li>Copy <code>utils</code> folder to your <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/wiki/Chrome-and-Root-folders#the-chrome-folder">chrome folder</a>.</li>
</ol>

<p>Next time you start up firefox, changes should take effect.</p>

<p>If you did it right, the structure of firefox root folder should look like this:</p>
<ul>
  <li>browser (folder)</li>
  <li>defaults (folder)</li>
  <ul>
    <li>pref (folder)</li>
    <ul>
      <li>channel-prefs.js</li>
      <li>config-prefs.js</li>
    </ul>
  </ul>
  <li>fonts (folder)</li>
  <li>gmp-clearkey (folder)</li>
  <li>uninstall (folder)</li>
  <li>firefox.exe/firefox</li>
  <li>config.js</li>
  <li>Other .dll files</li>
</ul>

<p>And the structure of the chrome folder should look like:</p>
<ul>
  <li>utils (folder)</li>
  <li>Any other optional file like userChrome.css, userContent.css, MultiRowTabLiteforFx.uc.js, etc...</li>
</ul>

<p>The files inside the "utils" folder will enable both <code>*.uc.js</code> and <code>*.as.css</code> files inside your chrome folder.</p>
<p>To override CSS styles that can't be changed in any other way (like for scrollbars, or certain tooltips), you must give the CSS files you want to use the extension <code>.as.css</code>, since they won't be read at all if you don't (unless you import them directly through <code>userChrome.css</code> with an <b>@import</b> rule, but they will be read with the same privileges as userChrome.css).</p>