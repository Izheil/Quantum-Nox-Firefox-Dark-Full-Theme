<h1>Theme and multirow installers</h1>
<p>If you don't want to copy the files manually to install the theme or multirow, you can do it with these batch files instead.</p>
<p>These batch files install either the full dark theme (without any CSS tweak), or multirow tabs (if you have your own userchrome.css you will still have to edit it to make it compatible). <b>Make sure your Firefox is up to date, since the files here assume you have the lastest stable version.</b>.</p>
<p>Currently there are only windows installers for it, so Linux and Mac users will still have to <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Full%20dark%20theme#installation">install it manually with the explanations of the repository</a>.</p>

<h2>The batch files</h2>
<h3>For dark OS themes versions</h3>
<p>These will install the dark theme without inverting the colors of checkboxes, so if you have an OS that turns them dark by default, use this version (by default windows paints them white, so use the white OS theme version if you aren't using a custom dark windows theme)</p>

<h3>For white OS themes versions</h3>
<p>These will install the dark theme inverting the colors of checkboxes and select boxes so that they are shown darkish (which are white by default on white OS themes like windows).</p>

<h3>Multirows ONLY</h3>
<p>These will install multirow as well as an empty <code>userchrome.css</code> that enables the use of <code>userchrome.xml</code>, so if you have a custom <code>userchrome.css</code> already, make a backup, or exit the batch file when it tells you that it's going to copy that file.</p>
<p>If you are going to use your own custom <code>userchrome.css</code>, make sure to add the following rule to it:</p>
<pre>
/* This enables the use of JS external files */
toolbarbutton#alltabs-button {
    -moz-binding: url("userChrome.xml#js")}
</pre>

<h3>Non scrollable multirow tabs</h3>
<p>This version of multirow tabs shows all tabs you currently have open splitting them on rows, without any limit to the amount of rows to show. Choose this option if you want to always see all the tabs you have open without limits to the number of rows.</p>
<img src="https://i.imgur.com/GWSgqD9.png">

<h3>Scrollable multirow tabs</h3>
<p>This version shows all tabs you currently have open splitting them on rows up to a max of 3 rows by default (can be changed using the variable inside the file). After the max number of rows has been reached, a scrollbar will be shown to be able to scroll around the extra tabs.</p>
<img src="https://i.imgur.com/qqQn4Ky.png">

