(function(){
	if (location.href != 'chrome://browser/content/browser.xhtml') return;

	let func = {
		
			add : function(e){
				e.target.setAttribute('unread', 'true');
			},
			remove : function(e){
				e.target.removeAttribute('unread');
			}
	};
		gBrowser.tabContainer.addEventListener('TabOpen', func.add, false);
		gBrowser.tabContainer.addEventListener('TabSelect', func.remove, false);
		gBrowser.tabContainer.addEventListener('TabClose', func.remove, false);
	window.addEventListener('unload', function uninit(){
		gBrowser.tabContainer.removeEventListener('TabOpen', func.add, false);
		gBrowser.tabContainer.removeEventListener('TabSelect', func.remove, false);
		gBrowser.tabContainer.removeEventListener('TabClose', func.remove, false);
		window.removeEventListener('unload', uninit, false);
	}, false);
})()