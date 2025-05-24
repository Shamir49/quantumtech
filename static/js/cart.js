console.log('cart.js is connected!')

document.querySelectorAll('.buy-btn').forEach(btn=>{
    console.log(btn)
    btn.addEventListener('click',addToCart)
})
var csrftoken = getCookie('csrftoken')

function addToCart(e){
    console.log(e.target.value)
    var url = '/addtocart'
    var data = {'id':e.target.value}
    fetch(url,{
        method:"POST",
        headers: {'Content-Type':"application/json","X-CSRFToken":csrftoken},
        body: JSON.stringify({data})
    })
    .then(res=>res.json())
    .then(data=>{
        document.getElementById('cartCount').innerHTML = data
    })
    .catch(error=>{
        console.log(error)
    })
}

document.querySelectorAll('.delete-btn').forEach(btn=>{
    btn.addEventListener('click',removeFromCart)
})
function removeFromCart(e){
    console.log(e.target.value)
    var data = {'id':e.target.value}
    var url = '/removefromcart'
    fetch(url,{
        method:'POST',
        headers:{'Content-Type':'application/json',"X-CSRFToken":csrftoken},
        body: JSON.stringify({data})
    })
    .then(res=>res.json())
    .then(data=>{
        document.getElementById('cartCount').innerHTML = data
        window.location.reload(true)
    })
    .catch(error=>{
        console.log(error)
    })

    // window.location.reload(true)
}