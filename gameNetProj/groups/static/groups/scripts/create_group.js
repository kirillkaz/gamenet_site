// $.ajaxSetup({ 
//     beforeSend: function(xhr, settings) {
//         function getCookie(name) {
//             var cookieValue = null;
//             if (document.cookie && document.cookie != '') {
//                 var cookies = document.cookie.split(';');
//                 for (var i = 0; i < cookies.length; i++) {
//                     var cookie = jQuery.trim(cookies[i]);
//                     // Does this cookie string begin with the name we want?
//                     if (cookie.substring(0, name.length + 1) == (name + '=')) {
//                         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                         break;
//                     }
//                 }
//             }
//             return cookieValue;
//         }
//         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
//             // Only send the token to relative URLs i.e. locally.
//         console.log('all_is good')
//         xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
//         }
//         xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
//         console.log('it s work but...')
//     } 
// });

const showCreateWindow = () => {
    $.ajax({
        type: "get",
        url: "http://0.0.0.0/groups/ajax/groupcreation",
        success: (data) => {
            console.log(data)
            $('#group_creation').empty();
            $('#group_creation').append(data);
        }
    });
}

const CreateGroup = (u_login, u_password) => {
    let form_data = new FormData($('#group_creationform').get(0))

    console.log(form_data)
    $.ajax({
        type: "post",
        url: "http://0.0.0.0/groups/ajax/groupcreation",
        dataType: 'json',
        contentType: false,
        processData: false,
        mimeType: 'multipart/form-data',
        username: u_login,
        password: u_password,
        data: form_data,
        success: (data) => {
            hideCreateWindow()
        }
    });
}

const hideCreateWindow = () => {
    $('#group_creation').empty()
}
