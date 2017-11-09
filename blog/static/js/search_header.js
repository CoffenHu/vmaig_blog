/**
 * Created by Coffen on 2017/11/9. Form Baidu
 */
$(document).ready(function() {
	function o() {
		var e = 750;
		return document.body.clientWidth < e
	}
	var e = window.$CONFIG["paths.base"],
		//t = $("#developer-header"),
		t = $("#vmaig-header"),
		n = $(".search .navbar-search"),
		r = $(".navbar-search .form-control"),
		i = $(".navbar-search .glyphicon-search");
	if ($("body").hasClass("header-fixed")) {
		var s = function() {
				var e = $(document).scrollTop(),
					n = "scrolled";
				e > 0 ? t.addClass(n) : t.hasClass(n) && t.removeClass(n)
			};
		s(), $(window).scroll(function() {
			s()
		})
	}
	i.on("click", function(t) {
		var n = "全部",
			i = "ALL",
			s = r.val();
		if (s === "") return;
		return location.href = e + "search?s=" + s, !1
	}), r.keydown(function(e) {
		e.keyCode === 13 && i.click()
	}), n.hover(function() {
		o() || (r.stop(), r.show(), r.animate({
			width: "200px"
		}, 200, function() {
			r.focus()
		}))
	}, function() {
		o() || (r.stop(), r.animate({
			width: "0px"
		}, 200, function() {
			r.hide()
		}))
	})
});