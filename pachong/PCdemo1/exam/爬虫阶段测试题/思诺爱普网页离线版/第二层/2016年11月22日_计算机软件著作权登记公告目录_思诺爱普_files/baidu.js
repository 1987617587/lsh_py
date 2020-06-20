(function() {
	var bp = document.createElement('script');
	var curProtocol = window.location.protocol.split(':')[0];
	if(curProtocol === 'https') {
		bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
	} else {
		bp.src = 'http://push.zhanzhang.baidu.com/push.js';
	}
	var s = document.getElementsByTagName("script")[0];
	s.parentNode.insertBefore(bp, s);
})();

(function() {
	var src = (document.location.protocol == "http:") ? "http://js.passport.qihucdn.com/11.0.1.js?3d77d73099bb3fcbac46c59a48b3055c" : "https://jspassport.ssl.qhimg.com/11.0.1.js?3d77d73099bb3fcbac46c59a48b3055c";
	document.write('<script src="' + src + '" id="sozz"><\/script>');
})();

(function(i, s, o, g, r, a, m) {
	i['GoogleAnalyticsObject'] = r;
	i[r] = i[r] || function() {
		(i[r].q = i[r].q || []).push(arguments)
	}, i[r].l = 1 * new Date();
	a = s.createElement(o),
		m = s.getElementsByTagName(o)[0];
	a.async = 1;
	a.src = g;
	m.parentNode.insertBefore(a, m)
})(window, document, 'script', 'https://www.google-analytics.com/analytics.js', 'ga');
ga('create', 'UA-84988928-1', 'auto');
ga('send', 'pageview');