!function() {
    "use strict";
    function n(n, t) {
        if (t = t || e,
        n.app_id = $$ucLog.app,
        n.path = $$ucLog.path,
        n = JSON.stringify(n),
        !navigator.sendBeacon || !navigator.sendBeacon(t, n)) {
            var o = new XMLHttpRequest;
            o.open("post", t, !0),
            o.setRequestHeader("Content-Type", "application/x-www-form-urlencoded"),
            o.send(n)
        }
    }
    function t() {
        var t = $$ucLog.errs;
        if (t && t.length) {
            for (var e = 0, o = t.length; e < o; e++)
                n(t[e]);
            $$ucLog.errs = []
        }
    }
    var e = location.protocol + "//bench.uc.cn/c"
      , o = window.performance.timing
      , r = $$ucLog.chance ? 100 * Math.random() < $$ucLog.chance : 100 * Math.random() < 30;
    r && setInterval(function() {
        t()
    }, 5e3),
    $$ucLog.sendPerform = function(t) {
        if (r) {
            var a = o.responseEnd - o.navigationStart
              , c = o.domContentLoadedEventEnd - o.navigationStart
              , s = t.uc_param_str || "ntnwcpfr";
            t.uc_param_str && delete t.uc_param_str,
            (o.requestStart || o.responseStart || o.responseEnd || a || c) && (t.dns = o.domainLookupEnd - o.domainLookupStart,
            t.conn = o.connectEnd - o.connectStart,
            t.req = o.responseStart - o.requestStart,
            t.res = o.responseEnd - o.responseStart,
            t.rt = a,
            t.intr = c,
            t.is_ssl = "https:" === location.protocol ? 1 : 0,
            n(t, e + "?uc_param_str=" + s))
        }
    }
}();