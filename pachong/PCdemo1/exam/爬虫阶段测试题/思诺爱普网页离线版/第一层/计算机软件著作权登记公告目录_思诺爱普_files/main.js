/* settings block  
var settings_block = '<div id="color_picker" class="block_color_picker">\
    	<div class="picker_skin">\
        	<p>Base skins</p>\
            <div class="picker_line"></div>\
            <div class="picker_select">\
            	<select class="settings_custom_select">\
                	<option value="0">Normal</option>\
                    <option value="1">Boxed</option>\
                </select>\
            </div>\
        </div>\
        <a href="javascript:void(0)" id="picker_close"><img src="settings/images/trans.gif" alt="Close" title="Close" /></a>\
    </div>';
$(function(){$('body').append(settings_block);});
document.write('<link rel="stylesheet" href="settings/style.css" type="text/css">');
document.write('<script type="text/javascript" src="settings/js/jquery.cookies.min.js"></script>');
document.write('<script type="text/javascript" src="settings/js/main.js"></script>');
settings block end */

/* browser selection */
var ie8 = ($.browser.msie && $.browser.version == '8.0') ? true : false;

/* mobile */
var isMobile = false;

function isMobile_f() {
	var array_mobileIds = new Array('iphone', 'android', 'ipad', 'ipod');
	var uAgent = navigator.userAgent.toLowerCase();

	for (var i = 0; i < array_mobileIds.length; i++) {
		if (uAgent.search(array_mobileIds[i]) > -1) {
			isMobile = true;
		}
	}
}
isMobile_f();

function init_menu() {
	var timer = new Array();
	$('.big_dropdown').hover(
		function() {
			var content = $(this).attr('data-content');
			clearTimeout(timer[$('.main_menu li').index(this)]);
			$(this).addClass('hover');
			$('.block_big_dropdown[data-menu=' + content + ']').show();
		},
		function() {
			var content = $(this).attr('data-content');
			var _this = this;
			timer[$('.main_menu li').index(this)] = setTimeout(function() {
				$(_this).removeClass('hover');
				$('.block_big_dropdown[data-menu=' + content + ']').hide();
			}, 10);
		}
	);

	$('.block_big_dropdown').hover(
		function() {
			var menu = $(this).attr('data-menu');
			var num = $('.main_menu li').index($('.main_menu li[data-content=' + menu + ']'));
			clearTimeout(timer[num]);
			$(this).show();
			$('.main_menu li[data-content=' + menu + ']').addClass('hover');
		},
		function() {
			var menu = $(this).attr('data-menu');
			var num = $('.main_menu li').index($('.main_menu li[data-content=' + menu + ']'));
			var _this = this;
			timer[num] = setTimeout(function() {
				$('.main_menu li[data-content=' + menu + ']').removeClass('hover');
				$(_this).hide();
			}, 10);
		}
	);

	if (isMobile) {
		$('.main_menu .big_dropdown > a').click(function(e) {
			if (!$(this).hasClass('a_hover')) e.preventDefault();

			var content = $(this).parent().attr('data-content');
			$('.main_menu .big_dropdown > a').removeClass('a_hover');
			$(this).addClass('a_hover');
			$('.block_big_dropdown[data-menu=' + content + ']').show();
		});
	}

	build_responsive_menu();
}

function build_responsive_menu() {
	var full_nav = $('header .main_menu').html();
	if (full_nav != null) {
		$('header .section_main_menu .inner').append('<div id="responsive_navigation" class="responsive_navigation"><div class="button_menu">点击这里打开导航菜单...</div><div class="r_menu"></div></div>');
		$('#responsive_navigation .r_menu').html(full_nav);

		$('#responsive_navigation .button_menu').click(function() {
			$('#responsive_navigation > .r_menu').slideToggle();
		});
	}

	var full_secondary_menu = $('header .secondary_menu').html();
	if (full_secondary_menu != null) {
		$('header .section_secondary_menu .inner').append('<div id="responsive_secondary_menu" class="responsive_secondary_menu"><a href="#" class="left"></a><a href="#" class="right"></a><div class="r_menu"></div></div>');

		$('#responsive_secondary_menu .r_menu').html(full_secondary_menu);

		var viewport = $('#responsive_secondary_menu .r_menu').width();
		var full_width = 0;
		$('#responsive_secondary_menu .r_menu li').each(function() {
			full_width += $(this).outerWidth();
		});
		$('#responsive_secondary_menu ul').css({
			'width': full_width + 'px',
			'left': '0px'
		});

		$(window).resize(function() {
			viewport = $('#responsive_secondary_menu .r_menu').width();
		});

		$('#responsive_secondary_menu .left').click(function(e) {
			var old_position = parseInt($('#responsive_secondary_menu ul').css('left'));
			var new_position = old_position + 150;
			if (new_position >= 0) new_position = 0;

			$('#responsive_secondary_menu ul').animate({
				left: new_position
			}, 100);

			e.preventDefault();
		});

		$('#responsive_secondary_menu .right').click(function(e) {
			var old_position = parseInt($('#responsive_secondary_menu ul').css('left'));
			var new_position = old_position - 150;
			if (new_position <= (viewport - full_width)) new_position = viewport - full_width;

			$('#responsive_secondary_menu ul').animate({
				left: new_position
			}, 300);

			e.preventDefault();
		});
	}
}

function init_sticky_footer() {
	if ($('.wrapper').hasClass('sticky_footer')) {
		var bot_height = $('footer').outerHeight();
		//var inn_height = $('#content > .inner').outerHeight();
		//if (inn_height < 500) {
		//	$('#content > .inner').CSS('height', '500px');
		//}
		$('#content > .inner').css('margin-bottom', bot_height + 'px');
	}
}

function init_r_corner() {
	$('.r_corner').each(function() {
		var path = $(this).find('img').attr('src');
		$(this).css('background-image', 'url(' + path + ')');
	});
}

function init_iframe_size() {
	var max_width = false;
	if ($('.wrapper').outerWidth() >= 768) {
		var max_width = 612;
	}
	if ($('.wrapper').outerWidth() < 950 && $('.wrapper').outerWidth() >= 768) {
		var max_width = 472;
	}
	if ($('.wrapper').outerWidth() < 768 && $('.wrapper').outerWidth() >= 480) {
		var max_width = 412;
	}
	if ($('.wrapper').outerWidth() < 480) {
		var max_width = 292;
	}

	$('.block_video iframe').each(function() {
		if (max_width) {
			var iframe_width = $(this).attr('width');
			var iframe_height = $(this).attr('height');

			iframe_height = parseInt((max_width * iframe_height) / iframe_width);

			$(this).attr('width', max_width);
			$(this).attr('height', iframe_height);
		}
	});
}

function init_fields() {
	$('.w_def_text').each(function() {
		var text = $(this).attr('title');

		if ($(this).val() == '') {
			$(this).val(text);
		}
	});

	$(document).on('click', '.w_def_text', function() {
		var text = $(this).attr('title');

		if ($(this).val() == text) {
			$(this).val('');
		}

		$(this).focus();
	});

	$(document).on('blur', '.w_def_text', function() {
		var text = $(this).attr('title');

		if ($(this).val() == '') {
			$(this).val(text);
		}
	});

	$('.custom_select').each(function() {
		$(this).css('opacity', '0');
		$(this).parent().append('<span />');
		var text = $(this).find('option:selected').html();
		$(this).parent().find('span').html(text);
	});

	$(document).on('change', '.custom_select', function() {
		var text = $(this).find('option:selected').html();
		$(this).parent().find('span').html(text);
	});
}

function init_validation(target) {
	function validate(target) {
		var valid = true;
		$(target).find('.req').each(function() {
			if ($(this).val() == '') {
				valid = false;
				$(this).parent().addClass('errored');
			} else {
				$(this).parent().removeClass('errored');
			}
		});
		return valid;
	}

	$(document).on('submit', 'form.w_validation', function(e) {
		var valid = validate(this);
		if (!valid) e.preventDefault();
	});

	if (target) {
		return validate(target);
	}
}

function init_pretty_photo() {
	if (!isMobile) {
		$("a[data-rel^='prettyPhoto']").prettyPhoto({
			deeplinking: false,
			keyboard_shortcuts: false
		});
	}
}

function add_zero(num) {
	return (num < 10) ? '0' + num : num;
}

function init_time_n_date() {
	var timer;
	window.clearTimeout(timer);
	var now = new Date();
	var months = [
		'January',
		'February',
		'March',
		'April',
		'May',
		'June',
		'July',
		'August',
		'September',
		'October',
		'November',
		'December'
	];
	var months_short = [
		'Jan',
		'Feb',
		'Mar',
		'Aprl',
		'May',
		'Jun',
		'Jul',
		'Aug',
		'Sep',
		'Oct',
		'Nov',
		'Dec'
	];
	var days = [
		'Sunday',
		'Monday',
		'Tuesday',
		'Wednesday',
		'Thursday',
		'Friday',
		'Saturday'
	]

	var minute = add_zero(now.getMinutes());
	var hour = add_zero(now.getHours());
	var day = add_zero(now.getDate());
	var day_week = now.getDay();
	var month = now.getMonth();
	var year = now.getFullYear();

	$('#num_top').html(day);

	if ($('.wrapper').outerWidth() < 480) {
		$('#month_top').html(months_short[month]);
	} else {
		$('#month_top').html(months[month]);
	}
	$('#year_top').html(year);
	$('#day_top').html(days[day_week]);
	$('#time').html(hour + ':' + minute);

	timer = window.setTimeout(init_time_n_date, 1000);
}

function init_popup() {
	$('.open_popup').click(function(e) {
		var target = $(this).attr('href');
		$('#overlay').show();
		$(target).show(500);

		e.preventDefault();
	});

	$('.block_popup .close').click(function(e) {
		var target = $(this).attr('href');
		$('.block_popup').hide(500, function() {
			$('#overlay').hide();
		});

		e.preventDefault();
	});
}

function init_pic_hover() {
	$('.general_pic_hover').each(function() {
		if (!$(this).hasClass('initialized')) {
			$(this).append('<span class="hover"><span class="icon"></span></span>');
			$(this).addClass('initialized');
		}

		var no_fx = $(this).hasClass('no_fx');

		$(this).bind('mouseenter', function(e) {
			var icon = $(this).find('.icon');
			var overlay = $(this).find('.hover');

			if (no_fx) {
				if (!ie8) {
					overlay.show().css('opacity', '0');
					overlay.stop(true).delay(100).animate({
						opacity: 1
					}, 200);
				} else {
					overlay.css('display', 'block');
				}
			} else {
				overlay.show();

				var w = $(this).width();
				var h = $(this).height();
				var x = (e.pageX - $(this).offset().left - (w / 2)) * (w > h ? (h / w) : 1);
				var y = (e.pageY - $(this).offset().top - (h / 2)) * (h > w ? (w / h) : 1);
				var direction = Math.round((((Math.atan2(y, x) * (180 / Math.PI)) + 180) / 90) + 3) % 4;

				/** do your animations here **/
				switch (direction) {
					case 0:
						/** animations from the TOP **/
						icon.css({
							'left': '0px',
							'top': '-100%',
							'right': 'auto',
							'bottom': 'auto'
						});
						icon.stop(true).delay(300).animate({
							top: 0
						}, 300);
						break;
					case 1:
						/** animations from the RIGHT **/
						icon.css({
							'left': '100%',
							'top': '0',
							'right': 'auto',
							'bottom': 'auto'
						});
						icon.stop(true).delay(300).animate({
							left: 0
						}, 300);
						break;
					case 2:
						/** animations from the BOTTOM **/
						icon.css({
							'left': '0px',
							'top': 'auto',
							'right': 'auto',
							'bottom': '-100%'
						});
						icon.stop(true).delay(300).animate({
							bottom: 0
						}, 300);
						break;
					case 3:
						/** animations from the LEFT **/
						icon.css({
							'left': 'auto',
							'top': '0',
							'right': '100%',
							'bottom': 'auto'
						});
						icon.stop(true).delay(300).animate({
							right: 0
						}, 300);
						break;
				}
			}
		});

		$(this).bind('mouseleave', function(e) {
			var icon = $(this).find('.icon');
			var overlay = $(this).find('.hover');

			if (no_fx) {
				if (!ie8) {
					overlay.stop(true).animate({
						opacity: 0
					}, 200);
				} else {
					overlay.css('display', 'none');
				}
			} else {
				var w = $(this).width();
				var h = $(this).height();
				var x = (e.pageX - $(this).offset().left - (w / 2)) * (w > h ? (h / w) : 1);
				var y = (e.pageY - $(this).offset().top - (h / 2)) * (h > w ? (w / h) : 1);
				var direction = Math.round((((Math.atan2(y, x) * (180 / Math.PI)) + 180) / 90) + 3) % 4;

				/** do your animations here **/
				switch (direction) {
					case 0:
						/** animations from the TOP **/
						icon.css({
							'left': '0px',
							'top': '0px',
							'right': 'auto',
							'bottom': 'auto'
						});
						icon.stop(true).animate({
							top: -h
						}, 300, function() {
							overlay.hide()
						});
						break;
					case 1:
						/** animations from the RIGHT **/
						icon.css({
							'left': 'auto',
							'top': '0px',
							'right': '0px',
							'bottom': 'auto'
						});
						icon.stop(true).animate({
							right: -w
						}, 300, function() {
							overlay.hide()
						});
						break;
					case 2:
						/** animations from the BOTTOM **/
						icon.css({
							'left': '0px',
							'top': 'auto',
							'right': 'auto',
							'bottom': '0px'
						});
						icon.stop(true).animate({
							bottom: -h
						}, 300, function() {
							overlay.hide()
						});
						break;
					case 3:
						/** animations from the LEFT **/
						icon.css({
							'left': '0px',
							'top': '0px',
							'right': 'auto',
							'bottom': 'auto'
						});
						icon.stop(true).animate({
							left: -w
						}, 300, function() {
							overlay.hide()
						});
						break;
				}
			}
		});

	});
}

function init_message_boxes() {
	$(document).on('click', '.general_info_box .close', function() {
		$(this).parent().fadeOut(300);
	});
}

function init_pricing_table() {
	$('.block_pricing_table_1').each(function() {
		var table = $(this);
		table.find('.column.category .cell p').each(function() {
			var name = '<span class="alt_text">' + $(this).html() + '</span> ';
			var num = $('.column.category .cell p').index(this);
			table.find('.column:not(.category)').each(function() {
				$(this).find('.cell p').eq(num).prepend(name);
			});
		});
	});
}

/**
 * 初始化版本信息条，为版本信息条添加链接，指向更新日志
 */
function init_version_whatsnew() {
	$('#JD_sign').on('click', function() {
		top.location.href = "/whatsnew/";
	});
}

/**
 * 加入收藏夹
 */
function AddFavorite() {
	var title = '商标查询-思诺爱普';
	var urls = 'http://www.ipyear.cn/';
	try
	{
		window.external.AddFavorite(urls, title);
	}
	catch(e)
	{
		try
		{
			window.sidebar.addPanel(title, urls, "");
		}
		catch(e)
		{
			alert("添加到收藏夹失败，可能是浏览器不支持，请按下Ctrl+D快捷键或手动添加。");
		}
	}
}

/**
 * 用户已登录时要显示的右上角内容
 */
var newshow = '<li><a href="/user/changepwd.php">修改密码</a></li><li><a href="javascript:logout();">安全退出</a></li>';

/**
 * 用户登出
 */
function logout() {
	$.ajax({
		url: "/service/UserLogout.php",
		timeout: 15000,
		type: "GET",
		cache: false,
		dataType: "json",
		error: function() {
			alert("退出时出现错误，建议稍后再次尝试。");
		},
		success: function(data) {
			state = data.state;
			if (state === 1)
				top.location = "/";
			else
				alert(data.notice);
		}
	});
}

/**
 * 检查用户登录状态
 */
function init_login_state() {
	$.ajax({
		url: "/service/UserLoginChk.php",
		timeout: 60000,
		type: "GET",
		cache: false,
		dataType: "json",
		error: function() {
			//do nothing
		},
		success: function(data) {
			if (data.login)
			{
				if (data.user_group)
					newshow = '<li><a href="/about/member_grade.html">' + data.username + ' (' + data.user_group + ')</a></li>' + newshow;
				$("#login_show_trigger").html(newshow);
			}
		}
	});
}

/**
 * 订阅邮件
 */
function subscribed_email() {
	var params = $("#subscribed").serialize();
	$.ajax({
		url: "/service/SubscribedEmail.php",
		timeout: 35000,
		type: "POST",
		cache: false,
		data: params,
		dataType: "text",
		error: function() {
			alert("订阅邮件时出错，请稍后再试！");
		},
		success: function(data) {
			alert(data);
		}
	});
}

/*
 * 意见反馈
 */
function opinion_feedback() {
	var params = $("#opinion_feedback").serialize();
	$.ajax({
		url: "/service/OpinionFeedback.php",
		timeout: 35000,
		type: "POST",
		cache: false,
		data: params,
		dataType: "text",
		error: function() {
			alert("发送反馈意见失败，请稍后再试！");
		},
		success: function(data) {
			alert(data);
		}
	});
}

$(document).ready(function() {
	init_sticky_footer();
	init_iframe_size();
	init_fields();
	init_r_corner();
	init_time_n_date();
	//init_popup();
	init_pic_hover();
	init_validation();
	init_message_boxes();
	init_pricing_table();
	init_login_state();
	init_version_whatsnew();
	$('.block_to_top a').click(function(e) {
		$.scrollTo(0, 500);
		e.preventDefault();
	});
	//$('audio, video').mediaelementplayer();

});

$(window).resize(function() {
	init_sticky_footer();
	init_iframe_size();
	init_time_n_date();
});

$(function() {
	init_menu();
	//暂时没有用到此插件
	//init_pretty_photo();
});