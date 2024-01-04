const colors = ['#F5C24D', '#F6510A', '#0000FF', '#F5CF4B', '#F5F24D', '#F651AA', '#000FFF', '#F5B24C']
for (let id of array) document.getElementById(id).style.backgroundColor = colors[Math.round(Math.random()*10+1)]
const nameInput = document.getElementById('name')
const surnameInput = document.getElementById('surname')
const phoneInput = document.getElementById('phone')
const emailInput = document.getElementById('email')
const birthDateInput = document.getElementById('birth-date')
const addressInput = document.getElementById('address')
const maleInput = document.getElementById('male-check')
const femaleInput = document.getElementById('female-check')
const maleCheck = document.getElementById('male')
const femaleCheck = document.getElementById('female')
requests.url = url
const focused = {input: null, value: null, type: null, message: null}
const unFocus = () => {
    focused.input.type = focused.type
    focused.input.value = focused.value
    hideMessage()
}
const focus = (input) => {
    focused.input = input
    focused.value = input.value
    focused.type = input.type
    focused.message = document.getElementById(`${input.id}-message`)
}
const showMessage = (message) => {
    focused.message.className = 'message'
    focused.message.innerText = message
}
const hideMessage = () => {
    focused.message.className = 'display-none'
    focused.message.innerText = ''
}
async function setGender() {
    let isMale = maleInput.checked
    maleCheck.src = `/static/profile/img/check-${isMale}.png`
    femaleCheck.src = `/static/profile/img/check-${!isMale}.png`
    await requests.PUT({gender: isMale})
}
const Gender = (input) => async (event) => {
    if (event.target.checked === !input.checked) return
    input.checked = !event.target.checked
    await setGender()
}
const Submit = (input) => async (event) => {
    if (event.key !== 'Enter') return
    if (input.value === focused.value) return input.blur()
    if (!input.validity.valid) return showMessage(`invalid ${input.name}`)
    if (input.value.length < 4) return showMessage('min length 4')
    let body = {}
    body[input.name] = input.value
    let data = await (await requests.PUT(body)).json()
    if (!data.ok) return showMessage(data.message)
    hideMessage()
    focused.value = input.value
    input.blur()
}
const Select = (type) => (event) => {
    let input = event.target
    focus(input)
    input.type = type
    input.focus()
    input.addEventListener('focusout', unFocus)
    input.addEventListener('keydown', (Submit(input)))
}
nameInput.onclick = Select('text')
surnameInput.onclick = Select('text')
phoneInput.onclick = Select('number')
emailInput.onclick = Select('email')
birthDateInput.onclick = Select('date')
addressInput.onclick = Select('text')
maleCheck.onclick = maleInput.click
femaleCheck.onclick = femaleInput.click
maleInput.onclick = Gender(femaleInput)
femaleInput.onclick = Gender(maleInput)
for (let input of document.getElementsByTagName('input')){input.onpaste = e => false; input.ondrop = e => false}
setGender().then()
const btnClose = document.getElementById('btn-close')
const modalChangePassword = document.getElementById('modal-change-pass')
const btnChangePassword = document.getElementById('btn-change-password')
const oldPasswordInput = document.getElementById('old-password')
const newPasswordInput = document.getElementById('new-password')
const reNewPasswordInput = document.getElementById('re-new-password')
const confirmChangePassword = document.getElementById('confirm-change-password')
const close = (modal) => (event) => {
    blurPage()
    modal.classList.add('display-none')
}
btnChangePassword.onclick = (event) => {
    const Select = (subInput=undefined) => (event) => {
        let input = event.target
        input.oninput = (event) => {
            confirmChangePassword.disabled = true
            if (!input.validity.valid) return showMessage(`invalid ${input.name}`)
            if (input.value.length < 8) return showMessage('min length 4')
            hideMessage()
            if (subInput) subInput.disabled = false
            else confirmChangePassword.disabled = false
        }
        focus(input)
    }
    oldPasswordInput.onfocus = Select(newPasswordInput)
    newPasswordInput.onfocus = Select(reNewPasswordInput)
    reNewPasswordInput.onfocus = Select()
    btnClose.className = 'btn-close'
    btnClose.onclick = close(modalChangePassword)
    blurPage()
    modalChangePassword.classList.remove('display-none')
    confirmChangePassword.onclick = async (event) => {
        focused.message = document.getElementById('change-password-message')
        const data = await (await requests.POST({password: oldPasswordInput.value, newpassword: newPasswordInput.value})).json()
        if (!data.ok) return showMessage(data.message)
        document.location.reload(true)
    }
}
const modalLogout = document.getElementById('modal-logout')
const passwordInput = document.getElementById('password')
const btnLogout = document.getElementById('btn-logout')
const confirmLogout = document.getElementById('confirm-logout')
btnLogout.onclick = (event) => {
    requests.url += 'logout/'
    passwordInput.onfocus = Select('password')
    passwordInput.removeEventListener('focusout', unFocus)
    btnClose.className = 'btn-close'
    btnClose.onclick = close(modalLogout)
    blurPage()
    modalLogout.classList.remove('display-none')
    confirmLogout.onclick = async (event) => {
        focused.message = document.getElementById('logout-message')
        const data = await (await requests.POST({password: passwordInput.value})).json()
        if (!data.ok) return showMessage(data.message)
        document.location.reload(true)
    }
}