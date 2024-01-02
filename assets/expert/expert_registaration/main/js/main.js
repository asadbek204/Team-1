requests.url = url
document.getElementById("regBtn").onclick = async (event) => {
    event.preventDefault()
    const usernameInput = document.getElementById('username')
    const usernamePassword = document.getElementById('password')
    let body = {username: usernameInput.value, password: usernamePassword.value}
    const data = await (await requests.POST(body)).json()
    // if (!data.ok) return document.getElementById("message1").innerText = data.message
    blurPage()
    const popup = document.getElementById('popup')
    popup.classList.toggle('active')
}
