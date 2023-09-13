const CreatePost = (u_login, u_password) => {
    let form_data = new FormData($('#create-post-form').get(0))

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
            console.log('Успех!')
        }
    });
}