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
var batch = 1,
    need_more_load = true;
function load_posts() {
    if (!need_more_load){
        return 0
    }
    var height_now = $('body').scrollTop();
    console.log(height_now);
    $.ajax({
        'url': '/backend/user/load_more_posts',
        'type': "POST",
        'data': {'batch': batch, 'pages_user_id': pages_user_id},
        'success': function (data) {
            if (data.posts_loaded){
                batch += 1;
                var batch_div = $('<div class="batch"> </div>');
                for(var i = 0; i < data.posts.length; i++){
                    var text = data.posts[i].body,
                        image_link = data.posts[i].image,
                        time_posted = data.posts[i].time_posted,
                        likes = data.posts[i].likes,
                        post_id = data.posts[i].id,
                        liked = data.posts[i].liked;
                    var time_array = time_posted.split(',').map(function (i) {
                        return parseInt(i)
                    });
                    var now = new Date();
                    now = now.format("dd,mm,yyyy");
                    var time_now_array = now.split(',').map(function (i) {
                        return parseInt(i)
                    });
                    if (2000 + time_array[2] < time_now_array[2]){
                        time_posted = time_array[0] + '.' + time_array[1] + '.' + time_array[2] + ' at ' + time_array[3] + ':' + time_array[4]
                    }
                    else{
                        if (time_array[0]  === time_now_array[0] - 1){
                            time_posted = 'yesterday, at' + time_array[3] + ':' + time_array[4]
                        }
                        else if (time_array[0] === time_now_array[0]){
                            time_posted = 'today, at' + time_array[3] + ':' + time_array[4]
                        }
                        else{
                            time_posted = time_array[1] + '.' + time_array[2] + ' at ' + time_array[3] + ':' + time_array[4]
                        }
                    }
                    var post = $(post_template({'body': '', 'image_url': image_link,
                                                'time_posted': time_posted, 'likes': likes, 'post_id': post_id,
                                                'liked': liked}));
                    post.find('.body').html(text.replace(/\n/g, "<br />"));
                    post.appendTo(batch_div)
                }
                batch_div.appendTo($('#posts'));
                if (batch !== 2)
                {
                    window.scrollTo(0, height_now);
                }
            }
            else{
                if (data.posts_ended){
                    need_more_load = false
                }
            }
            $('.like').click(function () {
                var liked_by = $(this).find('.liked_by');
                if (!$(this).hasClass('is-liked')) {
                    liked_by.text(parseInt(liked_by.text()) + 1);
                    $(this).addClass('is-liked');
                    $(this).css('color', '#f62459')
                }
                else{
                    liked_by.text(parseInt(liked_by.text()) - 1);
                    $(this).removeClass('is-liked');
                    $(this).css('color', '#00d1b2')
                }
                like_unlike($(this).attr('post_id'))

            });
        }
    })
}

function check_distance_to_bottom() {
    if ($(document).height() - ($(window).height() + $('body').scrollTop()) < 600 && need_more_load)
    {
        console.log('loading some more post');
        load_posts()
    }
}

$(document).ready(function () {
    load_posts()
});