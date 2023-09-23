const textarea_arr = document.getElementsByTagName('textarea');

for (textarea of textarea_arr){
  textarea.addEventListener('input', () => {
    textarea.style.height = 'auto';
    textarea.style.height = `${textarea.scrollHeight}px`;
  });
}

