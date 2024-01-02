requests = new Requests(url, csrfToken)
document.getElementById("regBtn").onclick = async (event) => {
    event.preventDefault();
    let csrf_token = document.querySelector('input[name="csrfmiddlewaretoken"]').value
    const usernameInput = document.getElementById('username');
    const usernamePassword = document.getElementById('password');

    let body = {
        username: usernameInput.value,
        password: usernamePassword.value
    }

    const result = await requests.POST(body)

    let data = await result.json()

    if (!data.ok) {
        document.getElementById("message1").innerText = data.message
        return
    }
    const blurEl = document.getElementById("blur");
    const popup = document.getElementById('popup')
    blurEl.classList.toggle("active");
    popup.classList.toggle('active')
};