const searchWindow = document.getElementById('search-window')
const generalContainer = document.getElementById('general-container')

const searchInput = document.getElementById('search-input')

function blurPage() {
    generalContainer.classList.toggle('blur')
    document.body.classList.toggle('on-search')
}
function openSearchWindow() {
    searchWindow.classList.toggle('active')
}

document.getElementById('search-input').oninput = async () => {

}

document.getElementById('search-button').onclick = () => {
    blurPage()
    openSearchWindow()
    searchInput.focus()
}
