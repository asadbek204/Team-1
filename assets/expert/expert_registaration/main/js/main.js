const toggleBlur = async (event) => {
    event.preventDefault();
    let url = "http://127.0.0.1:8000/exp_reg/"
    let csrf_token = document.querySelector('input[name="csrfmiddlewaretoken"]').value
    const usernameInput = document.getElementById('username_input');
    const usernamePassword = document.getElementById('username_password');
    console.log(usernameInput.value)
    const data = new URLSearchParams();
    data.append('username', usernameInput.value);
    data.append('password', usernamePassword.value);
    let result = await fetch(url, {
        method: 'POST', headers: {
            'Content-Type': 'application/json;charset=utf-8', 'X-CSRFToken': csrf_token
        }, body: data
    })

    const blurEl = document.getElementById("blur");
    blurEl.classList.toggle("active");

    const popupEl = document.getElementById("popup");
    popupEl.classList.toggle("active");
};

let regBtn = document.getElementById("regBtn")
regBtn.onclick = toggleBlur


// const usernameInput = document.getElementById('username_input');
// const usernamePassword = document.getElementById('username_password');
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
