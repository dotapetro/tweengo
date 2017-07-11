/**
 * Created by MI on 08.07.2017.
 */
String.prototype.isEmpty = function() {
    return (this.length === 0 || !this.trim());
};

$('#sign-in').click(function () {
    login($('#login-username').val(), $('#login-password').val())
});



$('#tweet-button').click(function () {
    var text = $('#tweet-textarea').val();
    if (!text.isEmpty()){
        tweet(text)
    }
});

$('.like').click(function () {
    var liked_by = $(this).find('.liked_by');
    if (!$(this).hasClass('is-liked')) {
        liked_by.text(parseInt(liked_by.text()) + 1);
        $(this).addClass('is-liked')
    }
    else{
        liked_by.text(parseInt(liked_by.text()) - 1);
        $(this).removeClass('is-liked')
    }
    like_unlike($(this).attr('post_id'))

});

$('.follow-button').click(function () {
   follow_un_follow(parseInt($(this).attr('idol_id')))
});

setInterval(check_distance_to_bottom, 300);

