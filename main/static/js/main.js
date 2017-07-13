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



$('.follow-button').click(function () {
   follow_un_follow(parseInt($(this).attr('idol_id')))
});

setInterval(check_distance_to_bottom, 300);

