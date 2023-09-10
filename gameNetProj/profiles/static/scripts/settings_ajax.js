const ShowSettingsBlock = (setting) => {
    $.ajax({
        type: "get",
        url: `http://0.0.0.0/profiles/ajax/settings/${setting}`,
        success: (data) => {
            $('.content').empty();
            $('.content').append(data);
        }
    });
}

const SaveSettings = (setting, u_login, u_password) => {
    let form_data = new FormData($('#settings_form').get(0))

    $.ajax({
        type: "post",
        url: `http://0.0.0.0/profiles/ajax/settings/${setting}`,
        dataType: 'json',
        contentType: false,
        processData: false,
        mimeType: 'multipart/form-data',
        username: u_login,
        password: u_password,
        data: form_data,
        success: (data) => {
            console.log('Успех!')
        }
    });
}