const usernameInput = document.getElementById('username')
const passwordInput = document.getElementById('password')
const message = document.getElementById("message2")
requests.url = url
document.getElementById("regBtn").onclick = async (event) => {
    event.preventDefault()
    let body = {username: usernameInput.value, password: passwordInput.value}
    const data = await (await requests.POST(body)).json()
    if (!data.ok) return document.getElementById("message1").innerText = data.message
    blurPage()
    const popup = document.getElementById('popup')
    popup.classList.toggle('active')
}
document.getElementById('regBtn2').onclick = async (event) => {
    event.preventDefault()
    const newUsernameInput = document.getElementById('newusername')
    const newPasswordInput = document.getElementById('newpassword')
    if ((usernameInput.value === newUsernameInput.value) || (passwordInput.value === newPasswordInput.value)) return message.innerText = "you must change your username and password"
    let body = {username: usernameInput.value, password: passwordInput.value, newusername: newUsernameInput.value, newpassword: newPasswordInput.value}
    const data = await (await requests.PUT(body)).json()
    if (!data.ok) return message.innerText = data.message
    document.location.reload(true)
}