const usernameInput = document.getElementById('username')
const passwordInput = document.getElementById('password')
requests.url = url
document.getElementById("regBtn").onclick = async (event) => {
    event.preventDefault()
    let body = {username: usernameInput.value, password: passwordInput.value}
    const data = await (await requests.POST(body)).json()
    // if (!data.ok) return document.getElementById("message1").innerText = data.message
    blurPage()
    const popup = document.getElementById('popup')
    popup.classList.toggle('active')
}
document.getElementById('regBtn2').onclick = async (event) => {
    event.preventDefault()
    const newUsernameInput = document.getElementById('newpassword')
    const newPasswordInput = document.getElementById('newpassword')
    if ((usernameInput.value === newUsernameInput.value) || (passwordInput.value === newPasswordInput.value)) return document.getElementById("message2").innerText = "you must change your username and password"

}