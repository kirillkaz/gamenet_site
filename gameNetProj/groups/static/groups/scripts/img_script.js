let wrapper_icon = document.querySelector('.input_field-img-icon');
let wrapper = document.querySelector('.input_field-img-icon-wrapper');

console.log(wrapper_icon)
function download(input){
    let file = input.files[0];
    let reader = new FileReader();
    reader.readAsDataURL(file);

    reader.onload = function() {
        wrapper_icon.src = reader.result;
        wrapper_icon.className = 'loaded_img'
        $(wrapper).removeClass('dotted-border');
    }
}