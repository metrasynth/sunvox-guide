$(function() { $('a[href$="wav"]').each(function() {
    var audioURL = $(this).attr('href');
	$(this).before('<audio controls src="'+audioURL+'" type="audio/wav" preload="none"></audio><br/>');
})});
