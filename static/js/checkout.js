console.log('checkout.js is connected!')
document.getElementById('form').addEventListener('submit',(e)=>{
    e.preventDefault()

})

document.getElementById('confirm-order').addEventListener('click',()=>{
    console.log('confirm order btn clicked!')
    var name = document.getElementById('name').value

    var email = document.getElementById('email').value
    var phone = document.getElementById('phone').value
    var address1 = document.getElementById('address1').value
    var address2 = document.getElementById('address2').value
    
    if(name != '' && email != '' && phone!= '' && address1 != '' && address2 != ''){
        document.getElementById('form').style.display = 'none'
        if(document.getElementById('cashondelivery').checked){
            document.getElementById('form').submit()
        }
        else{
            document.getElementById('paypal-button-container').style.display = 'flex'
        }
    }
})