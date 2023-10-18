		wow = new WOW();
		wow.init();
	
		$(window).on("scroll", function () {

			var bodyScroll = $(window).scrollTop(),
				navbar = $(".navbar");

			if (bodyScroll > 50) {
				$('.navbar-logo img').attr('src', '/static/img/logos.png');
				navbar.addClass("nav-scroll");

			} else {
				$('.navbar-logo img').attr('src', '/static/img/logos-bg.png');
				navbar.removeClass("nav-scroll");
			}

		});
		$(window).on("load", function () {
			var bodyScroll = $(window).scrollTop(),
				navbar = $(".navbar");

			if (bodyScroll > 50) {
				$('.navbar-logo img').attr('src', '/static/img/logos-bg.png');
				navbar.addClass("nav-scroll");
			} else {
				$('.navbar-logo img').attr('src', '/static/img/logo.png');
				navbar.removeClass("nav-scroll");
			}

			$.scrollIt({

				easing: 'swing',      // the easing function for animation
				scrollTime: 900,       // how long (in ms) the animation takes
				activeClass: 'active', // class given to the active nav element
				onPageChange: null,    // function(pageIndex) that is called when page is changed
				topOffset: -63
			});
		});

		