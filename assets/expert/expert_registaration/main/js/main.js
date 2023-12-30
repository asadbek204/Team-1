let url = "http://127.0.0.1:1212/expert/login/"


document.getElementById("regBtn").onclick = async (event) => {
    event.preventDefault();
    let csrf_token = document.querySelector('input[name="csrfmiddlewaretoken"]').value
    const usernameInput = document.getElementById('username');
    const usernamePassword = document.getElementById('password');

    let body = {
        username: usernameInput.value,
        password: usernamePassword.value
    }
    let result = await fetch(
        url,
        {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type':'application/json',
                'X-Requested-With':'XMLHttpRequest',
                'X-CSRFToken': csrf_token
            },
            body: JSON.stringify(body)
        }
    )
    let data = await result.json()

    if (!data.ok) {
        document.getElementById("message1").innerText = data.message
        return
    }
    const blurEl = document.getElementById("blur");
    blurEl.classList.toggle("active");
};