const searchWindow = document.getElementById('search-window')
const searchInput = document.getElementById('search-input')
const searchLabel = document.getElementById('search-label')
const dateInput = document.getElementById('date-input')
const byDescriptionCheck = document.getElementById('by-description')
const btnSubmit = document.getElementById('btn-submit')
const btnCloseWindow = document.getElementById('btn-close-window')
const generalContainer = document.getElementById('general-container')
const viewport = document.getElementById('viewport')
const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value
let requests = new Requests(baseUrl + '/search/', csrfToken)
function blurPage() {
    generalContainer.classList.toggle('blur')
    document.body.classList.toggle('freeze')
}
function openSearchWindow() {
    searchWindow.classList.toggle('active')
    btnCloseWindow.classList.toggle('display-none')
}
async function renderCompetitions(data){
    if (data.competitions.length === 0) {
        viewport.innerHTML = `<span class="not-found">${data.message}</span>`
        return
    }
    for (let competition of data.competitions) {
        let a = document.createElement('a')
        a.href = `${baseUrl}/competition/detail/${competition.id}`
        a.className = "competition"
        a.innerHTML = `
            <div class="img-block">
                <img class="competition-img" src="${baseUrl}/${competition.photo.url}" alt="">
            </div>
            <div class="info-block">
                <span class="title">${competition.title}</span>
                <p class="description">${competition.description}</p>
            </div>
        `
        viewport.appendChild(a)
    }
}
const format = (data) => `${(data < 10) ? '0': ''}${(data)}`
const formatDate = (d) => d.getFullYear()+"-"+format(d.getMonth()+1)+"-"+format(d.getDate())
const search = async () => {
    const value = searchInput.value.toLowerCase()
    let body = {start_date: (dateInput.value.length > 0) ? dateInput.value : formatDate(new Date(Date.now()))}
    if (byDescriptionCheck.checked) body.description = value
    else body.title = value
    await renderCompetitions(await (await requests.POST(body)).json())
}
searchInput.oninput = search
dateInput.onchange = search
btnCloseWindow.onclick = () => {
    openSearchWindow()
    blurPage()
}
document.getElementById('search-button').onclick = async () => {
    blurPage()
    openSearchWindow()
    searchInput.focus()
    if (viewport.children.length <= 1) await renderCompetitions(await (await requests.GET()).json())
}
byDescriptionCheck.onchange = async (event) => {
    searchLabel.innerText = (event.target.checked) ? 'search by description' : 'search by title'
    await search()
}
btnSubmit.onclick = (event) => {
    event.preventDefault()
}
