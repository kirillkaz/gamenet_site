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
    let cur_tab = $('.active').get(0);
    cur_tab = cur_tab.innerHTML

    $('#group_creation').empty()

    if (cur_tab == 'Ваши группы'){
        getSubsGroups()
    }

    else if (cur_tab == 'Администрирование'){
        getAdmGroups()
    }
}
