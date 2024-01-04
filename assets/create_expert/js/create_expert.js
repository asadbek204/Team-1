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

const Checker = (subInput) => async (event) => {
    let input = event.target
    if (event.key !== 'Enter') return
    if (input.value === focused.value) return input.blur()
    if (input.value.length < 4) return showMessage('min length 4')
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
    input.addEventListener('keydown', (Checker(input)))
}
for (let input of document.getElementsByTagName('input')) {
    input.onpaste = e => false;
    input.ondrop = e => false
}
const btnClose = document.getElementById('btn-close')
const closeBlock = document.getElementById('close-block')
const modalCreateExpert = document.getElementById('modal-create-expert')
const usernameInput = document.getElementById('username')
const passwordInput = document.getElementById('password')
const close = (modal) => (event) => {
    blurPage()
    closeBlock.className = 'display-none'
    modal.classList.add('display-none')
    event.target.className = 'display-none'
    hideMessage()
    focused.input.value = ''
}
document.getElementById('btn-create').onclick = (event) => {
    event.preventDefault()
    blurPage()
    closeBlock.className = 'close-block'
    btnClose.className = 'btn-close'
    btnClose.onclick = close(modalCreateExpert)
    modalCreateExpert.classList.remove('display-none')
}