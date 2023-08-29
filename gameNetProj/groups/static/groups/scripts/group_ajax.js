const getSubsGroups = () => {
    $.ajax({
        url: `http://37.139.33.69/groups/ajax/subscriber`,
        type: 'GET',
        dataType: 'json',
        success: (data) => {
            $('#groups_list').empty();
            
            $('#user_subscriber').addClass('active');
            $('#user_admin').removeClass('active');

            console.log(data);
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

const getAdmGroups = () => {
    $.ajax({
        url: `http://37.139.33.69/groups/ajax/admin`,
        type: 'GET',
        dataType: 'json',
        success: (data) => {
            $('#groups_list').empty();
            
            $('#user_subscriber').removeClass('active');
            $('#user_admin').addClass('active');

            console.log(data);
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
// $(document).ready(function() {
//     getSubsGroups()
//     getAdmGroups()
// })

// $(document).ajaxStop(function() {
//     getSubsGroups()
//     getAdmGroups()
// })
