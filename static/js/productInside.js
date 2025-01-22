console.log('productInside.js is connected!')

document.getElementById('rating1').addEventListener('change',()=>{
    document.getElementById('id_rating').value = 1
    console.log('radio button 1 clicked!')
})
document.getElementById('rating2').addEventListener('change',()=>{
    document.getElementById('id_rating').value = 2
    console.log('radio button 1 clicked!')
})
document.getElementById('rating3').addEventListener('change',()=>{
    document.getElementById('id_rating').value = 3
    console.log('radio button 1 clicked!')
})

document.getElementById('rating4').addEventListener('change',()=>{
    document.getElementById('id_rating').value = 4
    console.log('radio button 1 clicked!')
})

document.getElementById('rating5').addEventListener('change',()=>{
    document.getElementById('id_rating').value = 5
    console.log('radio button 1 clicked!')
})













//Keep this at the end
async function HideSuccessContainer(){
    var successContainerElement = document.getElementById('sc')
    await new Promise(resolve=>{
        return setTimeout(resolve,3000)
    })

    try{
        successContainerElement.style.display = 'none'
    }
    catch{
        console.log('Did not hide anything!')
    }
    
}
HideSuccessContainer()