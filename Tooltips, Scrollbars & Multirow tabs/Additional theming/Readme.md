<h1>Custom Scrollbars, tooltips and checkboxes</h1>
<img src="https://i.imgur.com/qe6tGJW.png" title="Dark blue scrollbar">
<h3>If you only want scrollbars, or the tooltips, you DON'T need any of the files from the theme folders.</h3>
<p>All you need is to create your own empty userchrome.css with this content:</p>

<pre>
/* DO NOT DELETE THIS LINE */
@namespace url("http://www.mozilla.org/keymaster/gatekeeper/there.is.only.xul");

/* This enables the use of JS external files */
toolbarbutton#alltabs-button {
    -moz-binding: url("userChrome.xml#js")}
</pre>

<p>... or just the <b>toolbarbutton</b> rule if you had an existing userchrome that didn't come from this repository.</p> 
  
<h2>Installation</h2>
<ul>
  <li>Copy <code>checkboxes.as.css</code>, <code>scrollbars.as.css</code>, <code>Sync-tabs-sidebar.as.css</code>, <code>tooltips.as.css</code>, and <code>userChrome.xml</code> inside here to the chrome folder on your firefox profile folder (Don't copy <code>checkboxes.as.css</code> to your chrome folder if you have an OS that colors checkboxes dark, since it will invert their color) if you want the dark themed scrollbars and tooltips.</li>
  <li><b>Optional</b>: You can try the other scrollbar types inside the "alternative scrollbars" folder.</li>
  <li><b>Optional</b>: You can try the other tooltip types inside the "alternative tooltips" folder, such as the semi-transparent background one.</li>
</ul>

<p>If you have done everything right, you should see the custom scrollbars next time you open firefox (or after you restart it)</p>