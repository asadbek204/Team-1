const storeUser = async () => {localStorage.setItem('username', username.value); localStorage.setItem('password', password.value)}
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
    if (username.value.length <= 4) return showMessage('username is to short')
    if (password.value.length <= 8) return showMessage('password is to short')
    const data = await (await requests.POST({username: username.value, password: password.value})).json()
    if (!data.ok) return showMessage(data.message)
    if (rememberCheck.checked) await storeUser()
    document.location.reload(true)
}
rememberUser().then(({name, pass}) => {if (name && pass) {username.value = name; password.value = pass}})