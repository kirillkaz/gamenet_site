const ShowPosts = (username) => {
    console.log('pam paaamm..')
    $.ajax({
        type: "get",
        url: `http://0.0.0.0/profiles/ajax/posts/${username}`,
        success: (data) => {
            $('#posts_block').empty();
            $('#posts_block').append(data);
        }
    });
}

const CreatePost = (u_login, u_password) => {
    let form_data = new FormData($('#create-post-form').get(0))
    let textarea_value = document.getElementsByClassName('post-input')[0].value

    if (textarea_value == ''){
        $('#empty-post-error').empty();
        $('#empty-post-error').append('<div class="error-text">К сожалению вы не можете создать пустой пост.</div>');
    }

    else{
        $.ajax({
            type: "post",
            url: `http://0.0.0.0/activities/users/posts`,
            dataType: 'json',
            contentType: false,
            processData: false,
            username: u_login,
            password: u_password,
            data: form_data,
            success: (data) => {
            }
        });
        ShowPosts(u_login)
    }
}

//show posts onload
let username = new URL(document.location).pathname.split('/')[2]
ShowPosts(username)