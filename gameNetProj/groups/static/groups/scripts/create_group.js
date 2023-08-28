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