$(document).ready(function() {

	//just to pratice Jquery and Pyramid request
	
	$('#form-message').submit(function() {
		$('.error-msg-author').css('display','none');
		$('.error-msg-content').css('display','none');
		var author = jQuery.trim($('#author').val());
		var content = jQuery.trim($('#content_textarea').val());
    	
    	if (author.length <= 0) {
    		$('.error-msg-author').html('Required Field').fadeIn();
    		$('.error-msg-author').css('display','block');
    		return false
    	}else if (content.length <= 0){
    		$('.error-msg-content').html('Required Field').fadeIn();
    		$('.error-msg-content').css('display','block');
    		return false
    	}
    });
});


                    