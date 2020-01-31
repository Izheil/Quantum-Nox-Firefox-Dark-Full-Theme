<h1>JS function installers</h1>
<p>If you don't want to copy the files manually to install multirow, tabs below, or focus tab on hover, you can do it with this installer.</p>
<b>Make sure your Firefox is up to date, since the userscripts installed with this assume you have the lastest firefox version.</b>
<p>This is the python version of the installer, which requires all files and folders in here to work. For the single file installer go to the <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/releases">releases</a> page.</p>
<p>You need <a href="https://www.python.org/downloads/release/python-375/">Python 3.7</a> installed to use these, along with the <b>elevate</b> module.</p>

<p>In linux you might need to install pip (to install the elevate module) after installing Python 3.7, which you can do with:</p>
<code>sudo apt install python3-pip</code>

<p>...As well as tkinter</p>
<code>sudo apt-get install python3-tk</code>

<p>You will also need to install the required module after installing Python and pip (on any OS) using:</p>
<code>pip3 install elevate</code>

<p>After that you can run <code>Quantum-Nox-Installer.py</code> to start the patcher.</p>

<h2>The functions</h2>
<p>You can find more explanations in the folders inside <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions">Multirow and other functions</a> folder in this repository.</p>

<h3>Multi-row Tabs</h3>

<h4>Scrollable rows</h4>
<p>This version shows all tabs you currently have open splitting them on rows up to a max of 3 rows by default (can be changed using the variable inside the file). After the max number of rows has been reached, a scrollbar will be shown to be able to scroll around the extra tabs.</p>
<img src="https://i.imgur.com/qqQn4Ky.png">

<h4>Autohide Scrollable rows</h4>
<p>Same as scrollable multirow tabs, but it will autohide the scrollbar when not hovering over the tabs.</p>

<h4>All rows visible</h4>
<p>This version of multirow tabs shows all tabs you currently have open splitting them on rows, without any limit to the amount of rows to show. Choose this option if you want to always see all the tabs you have open without limits to the number of rows.</p>
<img src="https://i.imgur.com/GWSgqD9.png">

<h3>Tabs below URL bar</h3>
<p>These will swap the tab bar position under the URL bar, while keeping the menu bar on top.</p>
<img src="https://i.imgur.com/5vbG6mh.png">

<h3>Focus tab on hover</h3>
<p>This will activate the tab you hover over with your mouse after the delay you specify.</p>