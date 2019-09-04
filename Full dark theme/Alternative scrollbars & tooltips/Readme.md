<h1>Alternative Scrollbars and tooltips</h1>
<img src="https://i.imgur.com/qe6tGJW.png" title="Dark blue scrollbar">
<h3>If you only want scrollbars, or the tooltips, you need <code>userChrome.xml</code> and <code>userChrome.css</code> to enable it.</h3>
<p>All you need is to create your own empty <code>userChrome.css</code> (if you aren't using the <code>userChrome.css</code> file from this repository) with this content and place it in <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Full%20dark%20theme#the-chrome-folder">the chrome folder</a>:</p>

<pre>
/* DO NOT DELETE THIS LINE */
@namespace url("http://www.mozilla.org/keymaster/gatekeeper/there.is.only.xul");

/* This enables the use of JS external files */
hbox#fullscr-toggler {
    -moz-binding: url("userChrome.xml#js")}
</pre>

<p>... or just the <b>hbox#fullscr-toggler</b> rule if you had an existing userchrome that didn't come from this repository.</p> 
  
<h2>Installation</h2>
<ul>
  <li>Replace the <code>scrollbars.as.css</code> or <code>tooltips.as.css</code> you had from the dark theme (or create the <code>userChrome.css</code> file mentioned above) for any of the ones inside the "alternative scrollbars" or "alternative tooltips" style folders. Make sure to also have <code>userChrome.xml</code> as well inside <a href="https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Full%20dark%20theme#the-chrome-folder">the chrome folder</a> on your firefox profile folder.</li>
</ul>

<p>If you have done everything right, you should see the different styled scrollbars or tooltips next time you open firefox (or after you restart it)</p>