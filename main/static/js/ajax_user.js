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
