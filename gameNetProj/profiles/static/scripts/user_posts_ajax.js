const ShowComments = (post_id) =>{
    $.ajax({
        type: "get",
        url: `http://0.0.0.0/profiles/ajax/comments/${post_id}`,
        success: (data) => {
            $(`#comments-block-${post_id}`).empty();
            $(`#comments-block-${post_id}`).append(data);
        }
    });
}

const CreateComment = (u_login, u_password, post_id) => {
    let form_data = new FormData($(`#create-comment-form-${post_id}`).get(0))
    let textarea_value = document.getElementById(`textfield_id-${post_id}`).value

    if (textarea_value == ''){
        $('#empty-comment-error').empty();
        $('#empty-comment-error').append('<div class="error-text">К сожалению вы не можете отправить пустой комментарий.</div>');
    }

    else{
        $.ajax({
            type: "post",
            url: `http://0.0.0.0/activities/users/comments/${post_id}`,
            dataType: 'json',
            contentType: false,
            processData: false,
            username: u_login,
            password: u_password,
            data: form_data,
            success: (data) => {
            }
        });
        ShowComments(post_id)
    }
}

const ShowPosts = (username) => {
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