const showProfileMenu= () => {
    let arrow = document.getElementById("menu_block_content")
    if (arrow.children.length == 0){
        $.ajax({
            type: "get",
            url: "http://0.0.0.0/profiles/ajax/menu",
            success: (data) => {
                console.log(data)
                $('#menu_block_content').empty();
                $('#menu_block_content').append(data);
            }
        });
    }

    else{
        $("#menu_block_content").empty();
    }
}