function download(input){
    let wrapper_icon = document.querySelector('.input_field-img-icon');
    let wrapper = document.querySelector('.input_field-img-icon-wrapper');

    let file = input.files[0];
    let reader = new FileReader();
    reader.readAsDataURL(file);

    reader.onload = function() {
        wrapper_icon.src = reader.result;
        wrapper_icon.className = 'loaded_img'
    }
}