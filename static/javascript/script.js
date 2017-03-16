$( ".hamburger" ).click(function() {
	$(this).toggleClass("active");
	$(".menu ul").toggleClass("active");
});