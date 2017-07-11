/**
 * Created by MI on 08.07.2017.
 */
function login(username, password) {
    $.ajax({
        'url': '/backend/user/login/',
        'type': "POST",
        'data': {'action': 'login_user', 'username': username, 'password': password},
        'success': function (data) {
        if (data.user_signed_in) {
            location.reload()
        }
        else{
            alert(data.error)
        }
    }
})
}

var post_template = _.template(document.getElementById('post-template').innerHTML);
function tweet(text) {
    $.ajax({
        'url': '/backend/user/tweet/',
        'type': "POST",
        'data': {'body': text },
        'success': function (data) {
        if (data.tweeted) {
            var image_link = false;
            if ($('#image_to_upload')[0].files.length){
                    var formdata = new FormData();
                    var file = $('#image_to_upload')[0].files[0];
                    formdata.append('image', file);
                    $.ajax({
                        'url': '/backend/user/tweet/add_image',
                        'type': "POST",
                        'processData': false,
                        'contentType': false,
                        'data': formdata,
                        'success': function (data) {
                        if (data.image_added) {
                            image_link = data.image_link;
                            var post = $(post_template({'body': '', 'image_url': image_link, 'time_posted': 'Just now'}));
                            post.find('.body').html(text.replace(/\n/g, "<br />"));
                            post.prependTo($('#posts'))
                        }
                        else{
                            alert(data.error)
                        }
                    }
                })
            }
            else{
                var post = $(post_template({'body': '', 'image_url': image_link, 'time_posted': 'Just now'}));
                post.find('.body').html(text.replace(/\n/g, "<br />"));
                post.prependTo($('#posts'))
            }
            $('#tweet-textarea').val('');
            var npe = $('#no_posts_yet');
            if (npe) {
                npe.remove()
            }
        }
        else{
            alert(data.error)
        }
    }
})
}

function like_unlike(post_id){
    $.ajax({
        'url': '/backend/user/like_unlike',
        'type': "POST",
        'data': {'post_id': post_id},
        'success': function (data) {
            if (!data.liked){
                alert(data.error)
            }
        }
    })
}


function follow_un_follow(idol_id) {
    $.ajax({
        'url': '/backend/user/follow_un_follow',
        'type': "POST",
        'data': {'idol_id': idol_id},
        'success': function (data) {
            if (data.followed){
                var button = $('.follow-button'),
                    followers = $('#followers');
                if (!button.hasClass('is-followed')){
                    button.addClass('is-followed');
                    button.css('background-color', '#00d1b2');
                    button.text('Un follow');

                    followers.text(parseInt(followers.text())+ 1)
                }
                else{
                    button.removeClass('is-followed');
                    button.css('background-color', '#276cda');
                    button.text('Follow');
                    followers.text(parseInt(followers.text())- 1)
                }
            }
            else{
                alert(data.error)
            }
        }
    })
}

function check_distance_to_bottom() {
    console.log(- ($(document).height() - ($('body').height() + $('body').scrollTop())));
    if (- ($(document).height() - ($('body').height() + $('body').scrollTop())) > 600){
        alert('Bottom!!!')
    }
}