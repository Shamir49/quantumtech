console.log('add_pc_builder.js is connected!')
console.log(type)


document.querySelectorAll('.add-btns').forEach(btn=>{
    btn.addEventListener('click',addToPCBuilder)
})

document.querySelectorAll('.delete-btn').forEach(btn=>{
    console.log('Delete btns')
    btn.addEventListener('click',DeleteFromPCBuilder)
})

var csrftoken = getCookie('csrftoken')

function addToPCBuilder(e){
    console.log(e.target.value)
    var url = '/addtopcbuilder'
    var data = {'id':e.target.value}
    fetch(url,{
        method:"POST",
        headers: {'Content-Type':"application/json","X-CSRFToken":csrftoken},
        body: JSON.stringify({data})
    })
    .then(res=>res.json())
    .then(data=>{
        console.log(data)
        window.location.href = '/pcBuilder'
    })
    .catch(error=>{
        console.log(error)
    })
}
function DeleteFromPCBuilder(e){
    console.log(e.target.value)
    var url = '/deletefrompcbuilder'
    var data = {'id':e.target.value}
    fetch(url,{
        method:"POST",
        headers: {'Content-Type':"application/json","X-CSRFToken":csrftoken},
        body: JSON.stringify({data})
    })
    .then(res=>res.json()
    )
    .then(data=>{
        console.log(data)
        window.location.reload()
    })
    .catch(error=>{
        console.log(error)
    })
}

