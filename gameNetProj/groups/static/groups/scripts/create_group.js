const showCreateWindow = () => {
    $.ajax({
        type: "get",
        url: "http://37.139.33.69/groups/ajax/groupcreation",
        success: (data) => {
            console.log(data)
            $('#group_creation').empty();
            $('#group_creation').append(data);
        }
    });
}

const hideCreateWindow = () => {
    $('#group_creation').empty()
}
