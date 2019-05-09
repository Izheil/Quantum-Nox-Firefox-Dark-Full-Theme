<h1>Quantum nox - Global dark style</h1>
<p>This <a href="https://github.com/openstyles/stylus/wiki/UserCSS">userCSS</a> is aimed to theme most sites you visit with dark colors similar to the ones used in Quantum Nox theme. This userstyle <b>doesn't work flawlessly on every site, nor does it intend to do so</b>, the main purpose is to just darken most sites you don't frequently visit (and thus finding specific userstyles for each one would be cumbersome apart from very inefficient) with an all-around dark style.</p>

<img src="https://i.imgur.com/o94dio6.png">

<p><b>For pages that you DO visit frequently, you should use a site-specific style instead</b>, not only for better compatibility, but also for better visuals. You can do this by looking for an already made userstyle of any page you want themed in the <a href="https://userstyles.org/">official userstyles page</a>.</p>

<p>The advantage of this global dark style over others is that it can be customized from stylus popup to your liking, like changing images contrast, changing the color of links, the background, selected text background color, darkening method...</p>

<img src="https://i.imgur.com/NOuJvbA.png">

<p>You can find the dark theme of stylus used in the image (along with other styles made by the same author) <a href="https://gitlab.com/RaitaroH/Stylus-DeepDark">here</a>.</p>

<h2>How to install</h2>
<p>To use any <a href="https://github.com/openstyles/stylus/wiki/UserCSS">UserCSS</a> style you need Stylus for <a href="https://addons.mozilla.org/en-US/firefox/addon/styl-us/">Firefox</a>, <a href="https://chrome.google.com/webstore/detail/stylus/clngdbkpkpeebahjckkjfobafhncgmne">Chrome</a>, or <a href="https://addons.opera.com/en-gb/extensions/details/stylus/">Opera</a>, depending on the browser you are using.</p>

<p>Once you have the Stylus extension, all you need is to install the file contained here as a userCSS.</p>

[![Install directly with Stylus](https://img.shields.io/badge/Install%20directly%20with-Stylus-00adad.svg)](https://raw.githubusercontent.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/master/Global%20dark%20userstyle/Quantum%20Nox%20-%20Global%20dark%20style.user.css)

<p>This global userstyle won't apply on certain sites (you can also specify your own) that already have a dark mode by default (although you can enable it for those if you want changing the regexp as specified on the section below this one).</p>

<h2>How to add per-site exclusions</h2>
<p>You can exclude certain sites from the userstyle to avoid having to turn it on or off on sites you have other more specific userstyles enabled.</p>

<p>To do so, all you have to do is add the domain you don't want the style to apply inside the regexp line (without the http(s) header), and separate each one with a |, like it's already done for a few sites by default:</p>

<img src="https://i.imgur.com/F2ecrCn.png">

<p>For example, if we already have some rule for some site and <b>wanted to add an exclusion</b> for <i>example.com</i>, the new rule would look like:</p>

<pre>
@-moz-document regexp("https?://(?!(www.nothingtoseehere.com|www.example.com)).*") {
/* Add any other site you don't want to apply inside the regexp encased between |'s ^ */
</pre> 

<p>This would make the userstyle ignore all pages that start with <i>example.com</i> (as well as the <i>nothingtoseehere</i> domain before it), <b>but not the subdomains like <i>subdomain.example.com</i></b>.</p>
<p>If we only wanted to also exclude <i>subdomain.example.com</i> it would be as easy as adding only that one subdomain link to the exclusions, but <b>if we wanted to exclude ALL subdomains</b> (no matter their subdomain name) of <i>example.com</i>, we'd have to use <code>((?!w+)([^\.]+)\.)?</code> for all subdomain names (You don't have to specify the www part before these regexp).</p>

<p>That way, if we wanted to exclude all example subdomains (we assume that some subdomains may have -'s, so we need to use the complex regexp), but NOT the main domain (so we exclude all <i>subdomain.example.com</i> like pages, but not the <i>example.com</i> like pages) it would look like this:</p>

<pre>
@-moz-document regexp("https?://(?!(www.nothingtoseehere.com|((?!w+)([^\.]+)\.)?example.com)).*") {
/* Add any other site you don't want to apply inside the regexp encased between |'s ^ */
</pre>

<p><b>If we wanted to exclude BOTH the subdomains and the domain</b> with just 1 selector, we would write it like <code>((?!w+)([^\.]+)\.)?([^\.]+)\.</code>, otherwise we'd have to specify them apart.</p>

<p>This excludes both the subdomains and the domain:</p>

<pre>
@-moz-document regexp("https?://(?!(www.nothingtoseehere.com|((?!w+)([^\.]+)\.)?([^\.]+)\.example.com)).*") {
/* Add any other site you don't want to apply inside the regexp encased between |'s ^ */
</pre>

<p>This would exclude both the subdomains and the domain of <i>example.com</i>, but wouldn't exclude other location domains like <i>example.org</i>.</p>
<p>To solve this and <b>exclude specific location domains</b>, you can use <code>(com|org)</code> or similar rules with all the location domains of the page. This can be used independently of the previous regexp rules. The full example so far would be:</p>

<pre>
@-moz-document regexp("https?://(?!(www.nothingtoseehere.com|((?!w+)([^\.]+)\.)?([^\.]+)\.example.(com|org))).*") {
/* Add any other site you don't want to apply inside the regexp encased between |'s ^ */
</pre>

<p>Lastly, <b>if we wanted to INCLUDE some path of a domain to be affected by this, while still excluding all other pages of the domain</b>... we would use <code>((?!text-to-include-here).)*$</code> in the place where the text that distinguises the page we want to include would appear.</p>
<p>Following our previous example, let's say we wanted the theme to apply to <i>example.com/home</i>, but NOT on every other <i>example.com</i> domain or subdomain page (like <i>example.com/contact</i> or <i>subdomain.example.com</i>). We'd have to use regexp to create an inclusion for this with "home":</p>

<pre>
@-moz-document regexp("https?://(?!(www.nothingtoseehere.com|((?!w+)([^\.]+)\.)?([^\.]+)\.example.(com|org)((?!home).)*$)).*") {
/* Add any other site you don't want to apply inside the regexp encased between |'s ^ */
</pre>

<h2>Settings explanation</h2>
<p>There are a few settings that you can change clicking the gear icon inside stylus popup that might not be intuitive:</p>

<ul>
	<li><b>Highlight links</b>: Sometimes link coloring will fail due to the site dark link color overwritting the changes of the global style. You can turn this setting on to put a light background color behind links for better visibility.</li>
	<li><b>100% bright img on hover</b>: It will make images show as their default contrast when you hover over them (won't do anything unless you've set <b>Image brightness %</b> to anything lower than 100).</li>
	<li><b>Image brightness %</b>: Will change the brightness of images tagged as <code><img></code>, so banners, header images, and other div background images will still show as default even if you change this setting. An example of images affected would be any that you can find inside posts of most social media sites, and possibly their logo. An exaple of the ones that WON't be affected would be the images that appear as the background of banners that common visual-oriented sites use (like <a href="https://www.gimp.org/">GIMP</a>, or <a href="https://www.apple.com">Apple</a>).</li>
	<li><b>Invert image colors</b>: Shows the negative version of the image, while trying to respect non black/white colors.</li>
	<li><b>Apply on div img background</b>: Applies the image brightness or color inversion changes (if enabled through the other settings) on divs that have an obvious background image (doesn't work with all elements).</li>
	<li><b>Hide div background images</b>: Hides the background images of elements that aren't headers, nor post images. An example would be forums that use a gradient image for the post body of the threads, showing white over the whole post background. It also can hide certain images that act as banners, but won't hide all banners.</li>
	<li><b>Hide header images</b>: Hides background images that act as headers and banners (like the examples provided on image brightness description).</li>
	<li><b>Hide images of links</b>: This will hide all background images of links that have one, including certain buttons that are tagged as links.</li>
	<li><b>Lower header img contrast</b>: This will try to lower the brightness of banners and header images while still showing their background (if hiding header images option is enabled, this one is not necesary).</li>
	<li><b>Dark layers over divs</b>: This will paint semi-transparent dark layers behind most elements to attempt to lower the contrast of some elements that still have background images. You shouldn't need this unless you want to see the background images of divs (rare occasions).</li>
</ul>