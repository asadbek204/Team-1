const storeUser = async () => {localStorage.setItem('username', username.value); localStorage.setItem('password', password.value)}
const clearUser = async () => {localStorage.setItem('username', ''); localStorage.setItem('password', '')}
const rememberUser = async () => ({username: localStorage.getItem('username'), password: localStorage.getItem('password')})
const rememberCheck = document.getElementById('remember')
const rememberInput = document.getElementById('remember-me')
const username = document.getElementById('username')
const password = document.getElementById('password')
const messageBox = document.getElementById('login-message')
const checkIcon = document.getElementById('check-icon')
requests.url = url
rememberCheck.onclick = () => {rememberInput.click(); checkIcon.classList.toggle('display-none')}
const showMessage = (message) => {messageBox.className = 'message'; messageBox.innerText = message}
const hideMessage = () => {messageBox.className = 'display-none'; messageBox.innerText = ''}
username.oninput = (e) => {e.target.value = e.target.value.toLowerCase()}
document.getElementById('btn-login').onclick = async (e) => {
    e.preventDefault()
    if (username.value.length < 4) return showMessage('username is to short')
    if (password.value.length < 8) return showMessage('password is to short')
    const data = await (await requests.POST({username: username.value, password: password.value})).json()
    if (!data.ok) {
        if (data.message === 'wrong password')
            btnForgotPassword.disabled = false
        return showMessage(data.message)
    }
    if (rememberInput.checked) await storeUser()
    else await clearUser()
    document.location.reload(true)
}
rememberUser().then(({name, pass}) => {if (name && pass) {username.value = name; password.value = pass}})
const focused = {input: null, value: null, type: null, message: null}
const close = modal => event => {
    closeBlock.className = 'display-none'
    modal.classList.add('display-none')
    event.target.className = 'display-none'
    blurPage()
    hideMessage()
    focused.input.value = ''
    requests.url = url
}
const btnClose = document.getElementById('btn-close')
const closeBlock = document.getElementById('close-block')
const modalForgotPassword = document.getElementById('modal-forgot-password')
const modalConfirmPassword = document.getElementById('modal-confirm-password')
const email2forgotInput = document.getElementById('email2forgot')
const password2forgotInput = document.getElementById('password2forgot')
const btnForgotPassword = document.getElementById('btn-forgot-password')
const sendEmailPassword = document.getElementById('send-email')
const confirmEmail = document.getElementById('confirm-email')
btnForgotPassword.onclick = event => {
    closeBlock.className = 'close-block'
    btnClose.className = 'btn-close'
    btnClose.onclick = close(modalForgotPassword)
    blurPage()
    focus(email2forgotInput)
    email2forgotInput.oninput = (event) => {
        let input = event.target
        if (!input.validity.valid) return showMessage(`invalid ${input.name}`)
        hideMessage()
        sendEmailPassword.disabled = false
    }
    requests.url = baseUrl + 'account/forgot_password/'
    focused.message = document.getElementById('forgot-password-message')
    modalForgotPassword.classList.remove('display-none')
    sendEmailPassword.onclick = async (event) => {
        const data = await (await requests.POST({username: username.value, email: email2forgotInput.value})).json()
        if (!data.ok) return showMessage(data.message)
        modalForgotPassword.classList.add('display-none')
        await confirm()
    }
}
const confirm = async () => {
    closeBlock.className = 'close-block'
    btnClose.className = 'btn-close'
    btnClose.onclick = close(modalConfirmPassword)
    password2forgotInput.oninput = (event) => {
        let input = event.target
        focus(input)
        if (!input.validity.valid) return showMessage(`invalid ${input.name}`)
        hideMessage()
        confirmEmail.disabled = false
    }
    requests.url = baseUrl + 'account/forgot_password/'
    focused.message = document.getElementById('forgot-password-message')
    modalConfirmPassword.classList.remove('display-none')
    showMessage('please check your email')
    confirmEmail.onclick = async (event) => {
        const data = await (await requests.PUT({username: username.value, email: email2forgotInput.value, password: password2forgotInput.value})).json()
        if (!data.ok) return showMessage(data.message)
        document.location.reload(true)
    }
}
