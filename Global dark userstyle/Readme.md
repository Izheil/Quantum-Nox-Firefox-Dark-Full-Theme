<h1>Quantum nox - Global dark style</h1>
<p>This <a href="https://github.com/openstyles/stylus/wiki/UserCSS">userCSS</a> style is a fork of the <a href="https://userstyles.org/styles/31267/global-dark-style-changes-everything-to-dark">userstyle made by Stormi</a>, and is aimed to theme most sites you visit with dark colors similar to the ones used in Quantum Nox theme. This userstyle <b>doesn't work flawlessly on every site, nor does it intend to do so</b>, the main purpose is to just darken most sites you don't frequently visit (and thus finding specific userstyles for each one would be cumbersome apart from very inefficient) with an all-around dark style.</p>

<img src="https://i.imgur.com/S34ylDn.png">

<p><b>For pages that you DO visit frequently, you should use a site-specific style instead</b>, not only for better compatibility, but also for better visuals. You can do this by looking for an already made userstyle of any page you want themed in the <a href="https://userstyles.org/">official userstyles page</a>.</p>

<p>The advantage of this global dark style over others (or even the original version it came from) is that it can be customized from stylus popup to your liking, like changing images contrast, changing the color of links, the background, selected text background color, darkening method...</p>

<img src="https://i.imgur.com/NOuJvbA.png">

<p>You can find the dark theme of stylus used in the image (along with other styles made by the same author) <a href="https://gitlab.com/RaitaroH/Stylus-DeepDark">here</a>.</p>

<h2>How to install</h2>
<p>To use any <a href="https://github.com/openstyles/stylus/wiki/UserCSS">UserCSS</a> style you need Stylus for <a href="https://addons.mozilla.org/en-US/firefox/addon/styl-us/">Firefox</a>, <a href="https://chrome.google.com/webstore/detail/stylus/clngdbkpkpeebahjckkjfobafhncgmne">Chrome</a>, or <a href="https://addons.opera.com/en-gb/extensions/details/stylus/">Opera</a>, depending on the browser you are using.</p>

<p>Once you have the Stylus extension, all you need is to install the file contained here as a userCSS.</p>

[![Install directly with Stylus](https://img.shields.io/badge/Install%20directly%20with-Stylus-00adad.svg)](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/blob/master/Global%20dark%20userstyle/Quantum%20Nox%20-%20Global%20dark%20style.user.css)

<p>This global userstyle won't apply on certain sites (you can also specify your own) that already have a dark mode by default (although you can enable it for those if you want changing the regexp as specified on the section below this one).</p>

<h2>How to add per-site exclusions</h2>
<p>You can exclude certain sites from the userstyle to avoid having to turn it on or off on sites you have other more specific userstyles enabled.</p>

<p>To do so, all you have to do is add the domain you don't want the style to apply inside the regexp line (without the http(s) header), and separate each one with a \|, like it's already done for a few sites by default:</p>

<img src="https://i.imgur.com/eaeJP0D.png">

<p>For example, if we wanted to add an exclusion for tumblr, the full rule would look like:</p>

<pre>
@-moz-document regexp("https?://(?!(www.tvtime.com|www.t411.al|www.nespresso.com|www.wechoosethemoon.org|www.nasa.gov|((?!w+)([^\.]+)\.)?([^\.]+)\.google.(com|es|de)|duckduckgo.com|www.youtube.com|www.reddit.com|twitter.com|gfycat.com|www.tumblr.com)).*") {
/* Add any other site you don't want to apply inside the regexp encased between |'s ^ */
</pre> 

<p>This would only make the userstyle ignore all pages that start with www.tumblr.com, <b>but not the subdomains like example.tumblr.com</b>.</p>
<p>If we only wanted to also exclude example.tumblr.com it would be as easy as adding only that one subdomain, but if we wanted to exclude ALL subdomains (no matter their subdomain name), we'd have to use <code>((?!w+)([^\.]+)\.)?</code> for all subdomain names (You don't have to specify the www. part before these regexp).</p>

<p>That way, if we wanted to exclude all tumblr subdomains (we assume that some subdomains have -'s, so we need to use the complex regexp) would look like this</p>

<pre>
@-moz-document regexp("https?://(?!(www.tvtime.com|www.t411.al|www.nespresso.com|www.wechoosethemoon.org|www.nasa.gov|((?!w+)([^\.]+)\.)?([^\.]+)\.google.(com|es|de)|duckduckgo.com|www.youtube.com|www.reddit.com|twitter.com|gfycat.com|((?!w+)([^\.]+)\.)?tumblr.com)).*") {
/* Add any other site you don't want to apply inside the regexp encased between |'s ^ */
</pre>

<p>If we wanted to exclude BOTH the subdomains and the domain with just 1 selector, we would write it like <code>((?!w+)([^\.]+)\.)?([^\.]+)\.</code>, otherwise we'd have to specify them apart.</p>

<p>This excludes both the subdomains and the domain:</p>

<pre>
@-moz-document regexp("https?://(?!(www.tvtime.com|www.t411.al|www.nespresso.com|www.wechoosethemoon.org|www.nasa.gov|((?!w+)([^\.]+)\.)?([^\.]+)\.google.(com|es|de)|duckduckgo.com|www.youtube.com|www.reddit.com|twitter.com|gfycat.com|((?!w+)([^\.]+)\.)?([^\.]+)\.tumblr.com)).*") {
/* Add any other site you don't want to apply inside the regexp encased between |'s ^ */
</pre>

<p>This would exclude both the subdomains and the domain of www.tumblr.com, but wouldn't exclude other location domains like www.tumblr.es (if that even existed).</p>
<p>To solve this, you can also use <b>.(com|de|es|uk)</b> or similar rule with all the location domains of the page (see the google regexp already included by default), and can be used even without the subdomain regexp ones.</p>