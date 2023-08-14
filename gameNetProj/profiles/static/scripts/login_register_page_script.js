
const showForm = (str) => {
    let registerF = 0
    let authF = 100

    let header_auth = document.getElementsByClassName('text_auth')[0]
    let header_register = document.getElementsByClassName('text_register')[0]
    if (str == 'auth'){
        registerF = 100
        authF = 0
        header_auth.classList.add('active')
        header_register.classList.remove('active')
    }

    else if (str == 'register'){
        header_auth.classList.remove('active')
        header_register.classList.add('active')
    }

    let registerForm = document.getElementsByClassName('registerForm')[0]
    registerForm.style.cssText = `\
    display: flex; \
    flex-direction: column; \
    vertical-align: middle; \
    \
    position: absolute; \
    top: 20%; \
    right: ${registerF}%; \
    \
    width: 100%; \
    height: 100%; \
    \
    margin: auto; \
    z-index: 20;\
    transition: 0.25s;`

    let authForm = document.getElementsByClassName('authForm')[0]
    authForm.style.cssText = `\
    display: flex;\
    flex-direction: column;\
    position: absolute;\
    top: 35.5%;\
    left: ${authF}%;\
    width: 100%;\
    height: 100%;\
    \
    margin: auto;\
    z-index: 30;\
    transition: 0.25s;`
}

const app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    
    data(){
        return{
        message: 'vue работает!'
        }
    },
    
    methods:{
        showAuthForm(){
            showForm('auth')
        },

        showRegisterForm(){
            showForm('register')
        }
    }
})