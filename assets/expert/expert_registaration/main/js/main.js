let url = "http://127.0.0.1:8000/exp_reg/"


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
        console.log(data.message)
        return
    }
    const blurEl = document.getElementById("blur");
    blurEl.classList.toggle("active");

    const popupEl = document.getElementById("popup");
    popupEl.classList.toggle("active");
};


//
//
// const onChangeWrap = (input) => (e) => {
//     input.innerText = e.target.value;
//     console.log(e.target.value)
// }
//
//
// usernameInput.addEventListener('input', onChangeWrap(usernameInput));
// usernamePassword.addEventListener('input', onChangeWrap(usernamePassword));
