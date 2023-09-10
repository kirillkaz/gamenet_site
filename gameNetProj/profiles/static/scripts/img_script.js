function DownloadAvatar(input){
    let wrapper_icon = document.querySelector('.input_field-img-icon');

    let file = input.files[0];
    let reader = new FileReader();
    reader.readAsDataURL(file);

    reader.onload = function() {
        console.log('DownloadAvatar')
        wrapper_icon.src = reader.result;
        wrapper_icon.className = 'loaded_img'
    }
}

function DownloadCover(input){
    let wrapper_cover = document.querySelector('.input_field-cover');

    let file = input.files[0];
    let reader = new FileReader();
    reader.readAsDataURL(file);

    reader.onload = function() {
        console.log('DownloadCover')
        $(wrapper_cover).empty();
        $(wrapper_cover).append(`<img class="loaded_cover" src="${reader.result}">`);
    }
}