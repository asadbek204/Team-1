const searchWindow = document.getElementById('search-window')
const generalContainer = document.getElementById('general-container')
const viewport = document.getElementById('viewport')

const searchInput = document.getElementById('search-input')
const searchLabel = document.getElementById('search-label')

const searchUrl = baseUrl + '/search/'
const csrf_token = document.querySelector('input[name="csrfmiddlewaretoken"]').value
const btnCloseWindow = document.getElementById('btn-close-window')
const dateInput = document.getElementById('date-input')
const byDescriptionCheck = document.getElementById('by-description')
const btnSubmit = document.getElementById('btn-submit')

byDescriptionCheck.onchange = (event) => {
    searchLabel.innerText = (event.target.checked) ? 'search by description' : 'search by title'
}

btnSubmit.onclick = (event) => event.preventDefault()

const requests = new Requests(searchUrl)

function blurPage() {
    generalContainer.classList.toggle('blur')
    document.body.classList.toggle('on-search')
}
function openSearchWindow() {
    searchWindow.classList.toggle('active')
    btnCloseWindow.classList.toggle('display-none')
}

async function renderCompetitions(competitions){
    for (let competition of competitions) {
        let a = document.createElement('a')
        a.href = `${baseUrl}/competition/detail/${competition.id}`
        a.className = "competition"
        a.innerHTML = `
            <div class="img-block">
                <img src="${baseUrl}/${competition.photo.url}" alt="">
            </div>
            <div class="info-block">
                <span class="title">${competition.title}</span>
                <p class="description">${competition.description}</p>
            </div>
        `
        viewport.appendChild(a)
    }
}

const getData = async () => {
    const result = await requests.GET()
    const data = await result.json()
    if (data.competitions.length === 0) {
        viewport.innerHTML = `<span class="not-found">${data.message}</span>`
        return
    }
    await renderCompetitions(data.competitions)
}

function formattedDate(d)
{
    const format = (data) => `${(data < 10) ? '0': ''}${(data)}`
    return d.getFullYear()+"-"+format(d.getMonth()+1)+"-"+format(d.getDate())
}

searchInput.oninput = async (event) => {
    const value = event.target.value
    const date = new Date(Date.now())
    let body = {start_date: (dateInput.value.length > 0) ? dateInput.value : formattedDate(date)}
    if (byDescriptionCheck.checked) {
        body.description = value
    }
    else {
        body.title = value
    }
    const result = await requests.POST(body)
    const data = await result.json()
    if (data.competitions.length === 0) {
        viewport.innerHTML = `<span class="not-found">${data.message}</span>`
        return
    }
    await renderCompetitions(data.competitions)
}

btnCloseWindow.onclick = () => {
    openSearchWindow()
    blurPage()
}

document.getElementById('search-button').onclick = () => {
    blurPage()
    openSearchWindow()
    searchInput.focus()
    getData().then()
}
