const colors = ['#F5C24D', '#F6510A', '#0000FF', '#F5CF4B', '#F5F24D', '#F651AA', '#000FFF', '#F5B24C']
if (array.length === 0) document.getElementById('competitions-view').innerText = 'Competitions not found'
else for (let id of array) document.getElementById(id).style.backgroundColor = colors[Math.round(Math.random()*10+1)]
const a = document.getElementById('certificates-view')
if (a.children.length <= 1)  {
    b = document.createElement('span')
    b.className = 'cer-not-found'
    b.innerText = 'Certificates not found'
    a.appendChild(b)
}
const nameInput = document.getElementById('name')
const surnameInput = document.getElementById('surname')
const phoneInput = document.getElementById('phone')
const emailInput = document.getElementById('email')
const birthDateInput = document.getElementById('birth-date')
const addressInput = document.getElementById('address')
const maleInput = document.getElementById('male-check')
const femaleInput = document.getElementById('female-check')
const femaleIcon = document.getElementById('female-icon')
const maleCheck = document.getElementById('male')
const femaleCheck = document.getElementById('female')
const maleIcon = document.getElementById('male-icon')
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
maleIcon.onclick = maleInput.click
femaleCheck.onclick = femaleInput.click
femaleIcon.onclick = femaleInput.click
maleInput.onclick = Gender(femaleInput)
femaleInput.onclick = Gender(maleInput)
setGender().then()
const btnClose = document.getElementById('btn-close')
const closeBlock = document.getElementById('close-block')
const modalChangePassword = document.getElementById('modal-change-pass')
const btnChangePassword = document.getElementById('btn-change-password')
const oldPasswordInput = document.getElementById('old-password')
const newPasswordInput = document.getElementById('new-password')
const reNewPasswordInput = document.getElementById('re-new-password')
const confirmChangePassword = document.getElementById('confirm-change-password')
const close = (modal) => (event) => {
    blurPage()
    closeBlock.className = 'display-none'
    modal.classList.add('display-none')
    event.target.className = 'display-none'
    hideMessage()
    focused.input.value = ''
    requests.url = url
}
btnChangePassword.onclick = (event) => {
    const Select = (subInput=undefined) => (event) => {
        let input = event.target
        input.oninput = (event) => {
            confirmChangePassword.disabled = true
            if (input.value.length < 8) return showMessage('min length 8')
            hideMessage()
            if (subInput) subInput.disabled = false
            else if (newPasswordInput.value === input.value) confirmChangePassword.disabled = false
            else showMessage('passwords not equal')
        }
        focus(input)
    }
    oldPasswordInput.onfocus = Select(newPasswordInput)
    newPasswordInput.onfocus = Select(reNewPasswordInput)
    reNewPasswordInput.onfocus = Select()
    closeBlock.className = 'close-block'
    btnClose.className = 'btn-close'
    btnClose.onclick = close(modalChangePassword)
    focus(oldPasswordInput)
    blurPage()
    modalChangePassword.classList.remove('display-none')
    confirmChangePassword.onclick = async (event) => {
        event.preventDefault()
        focused.message = document.getElementById('change-password-message')
        const data = await (await requests.PUT({password: oldPasswordInput.value, newpassword: newPasswordInput.value})).json()
        if (!data.ok) {
            btnForgotPassword.className = 'btn-forgot-password'
            return showMessage(data.message)
        }
        document.location.reload(true)
    }
}
const modalLogout = document.getElementById('modal-logout')
const passwordInput = document.getElementById('password')
const btnLogout = document.getElementById('btn-logout')
const confirmLogout = document.getElementById('confirm-logout')
btnLogout.onclick = (event) => {
    passwordInput.oninput = (event) => {
        let input = event.target
        focus(input)
        if (input.value.length < 8) return showMessage('min length 8')
        hideMessage()
        confirmLogout.disabled = false
    }
    closeBlock.className = 'close-block'
    btnClose.className = 'btn-close'
    btnClose.onclick = close(modalLogout)
    blurPage()
    modalLogout.classList.remove('display-none')
    confirmLogout.onclick = async (event) => {
        event.preventDefault()
        focused.message = document.getElementById('logout-message')
        const data = await (await requests.PUT({password: passwordInput.value})).json()
        if (!data.ok) {
            btnForgotPassword2.className = 'btn-forgot-password'
            return showMessage(data.message)
        }
        document.location.reload(true)
    }
}
const modalForgotPassword = document.getElementById('modal-forgot-password')
const email2forgotInput = document.getElementById('email2forgot')
const btnForgotPassword = document.getElementById('btn-forgot-password')
const btnForgotPassword2 = document.getElementById('btn-forgot-password2')
const confirmForgotPassword = document.getElementById('send-email')
const forgotPassword = async event => {
    btnClose.click()
    email2forgotInput.oninput = (event) => {
        let input = event.target
        focus(input)
        if (!input.validity.valid) return showMessage(`invalid ${input.name}`)
        hideMessage()
        confirmForgotPassword.disabled = false
    }
    closeBlock.className = 'close-block'
    btnClose.className = 'btn-close'
    btnClose.onclick = close(modalForgotPassword)
    blurPage()
    requests.url += 'forgot_password/'
    focused.message = document.getElementById('forgot-password-message')
    modalForgotPassword.classList.remove('display-none')
    await requests.GET()
    showMessage('please check your email')
    confirmForgotPassword.onclick = async (event) => {
        const data = await (await requests.PUT({password: email2forgotInput.value})).json()
        if (!data.ok) return showMessage(data.message)
        document.location.reload(true)
    }
}
btnForgotPassword.onclick = forgotPassword
btnForgotPassword2.onclick = forgotPassword