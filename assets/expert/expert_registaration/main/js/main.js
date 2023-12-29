async function sendRequest(url, method, body) {
    let csrf_token = document.querySelector('input[name="csrfmiddlewaretoken"]').value
    let xhr = new XMLHttpRequest()
    xhr.open(method, url, true)
    xhr.responseType = 'json'
    xhr.setRequestHeader('Content-Type', 'application/json')
    xhr.setRequestHeader('X-CSRFToken', csrf_token)

    xhr.onload = () => {
        if (xhr.status >= 400) {
            reject(xhr.response)
        }
        else {
            resolve(xhr.response)
        }
    }

    xhr.onerror = () => {
        reject(xhr.response)
    }
    xhr.send(JSON.stringify(body))
}
let url = "http://127.0.0.1:8000/exp_reg/"


let regBtn = document.getElementById("regBtn")
regBtn.onclick = (event) => {
    event.preventDefault();
    const usernameInput = document.getElementById('username_input');
    const usernamePassword = document.getElementById('username_password');

    let body = {
        username: usernameInput.value,
        password: usernamePassword.value
    }
    sendRequest(url, 'POST', body).then(console.log).catch(console.log)


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
