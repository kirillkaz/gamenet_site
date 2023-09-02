const findSubsGroups = (finder) => {
    //get current tab
    let cur_tab = $('.active').get(0);
    cur_tab = cur_tab.innerHTML

    let tab_url = ''


    if (cur_tab == 'Ваши группы'){
        tab_url = 'http://0.0.0.0/groups/ajax/subscriber'
    }

    else if (cur_tab == 'Администрирование'){
        tab_url = 'http://0.0.0.0/groups/ajax/admin'
    }

    $.ajax({
        url: tab_url,
        type: 'GET',
        dataType: 'json',
        success: (data) => {
            data.context = data.context.filter((elem) => elem.name.includes(finder))

            $('#groups_list').empty();

            for (elem of data.context){
                $('#groups_list').append(`<div class="group">
                <div class="group_avatar"><img src="data:image/png;base64,${elem.avatar}"></div>
                <div class="group_text">
                    <div class="group_name">${elem.name}</div>
                    <div class="group_subscribers">Всего подписчиков: ${elem.subscribers}</div>
                </div>
            </div>
            <hr>`);
            }
        },
        error: (error) => {
            console.log(error);
        }
    })
}