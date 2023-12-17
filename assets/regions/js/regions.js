

function selectRegion(target) {
    if (target.id === selectedRegion.id)
        return
    // console.log(`target.id = ${target.id}, selected.id = ${selectedRegion.id}`)
    selectedRegion.classList.remove('active')
    target.classList.add('active')
    selectedRegion = target

    selectedMap.classList.remove('active')
    selectedMap = document.getElementById(`map-${target.id}`)
    selectedMap.classList.add('active')
}
