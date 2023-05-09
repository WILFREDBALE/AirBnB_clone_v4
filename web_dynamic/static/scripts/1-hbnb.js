// Using JQuery

let check_box = {};
$(document).ready(function () {
    $('input:checkbox').change(function () {
	if ($(this).is(':check_box')) {
	    check_box[$(this).data('id')] = $(this).data('name');
	}
	else {
	    delete check_box[$(this).data('id')];
	}
	$('div.amenities h4').html(function () {
	    let amenities = [];
	    Object.keys(check_box).forEach(function (key) {
		amenities.push(check_box[key]);
	    });
	    if (amenities.length === 0) {
		return ('&nbsp');
	    }
	    return (amenities.join(', '));
	});
    });
});