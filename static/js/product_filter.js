console.log('product_filter.js is connected!')



document.querySelectorAll('.sidebarBtns').forEach(btn=>{
    btn.addEventListener('click',(e)=>{
        processSidebarItem(e,'filter')
    })
})


document.querySelectorAll('sidebarBtns').forEach(btn=>{
    btn.addEventListener('click',(e)=>{
        processSidebarItem(e,'filter')
    })
})

document.querySelectorAll('.ramBtns').forEach(btn=>{
    btn.addEventListener('click',(e)=>{
        var index = e.srcElement.id.substr(1,1)
        console.log(index)
        index = parseInt(index)
        e.target.childNodes[0].checked = true
        // document.getElementById('processorForm').submit()
    })
})
document.querySelectorAll('.ssdBtns').forEach(btn=>{
    btn.addEventListener('click',(e)=>{
        var index = e.srcElement.id.substr(2,1)
        console.log(index)
        index = parseInt(index)
        e.target.childNodes[0].checked = true
        // document.getElementById('processorForm').submit()
    })
})

document.querySelectorAll('.graphicsBtns').forEach(btn=>{
    btn.addEventListener('click',(e)=>{
        var index = e.srcElement.id.substr(1,1)
        console.log(index)
        index = parseInt(index)
        e.target.childNodes[0].checked = true
        // document.getElementById('processorForm').submit()
    })
})

function processSidebarItem(e,processor){
    var index = e.srcElement.id.substr(1,1)
    var s = processor;
    var queryString = window.location.search;
    
    const urlParams = new URLSearchParams(queryString)
   
    var processor = urlParams.get(s)
    
    const processorVal = e.target.childNodes[0].value
    


    if (processor != null){
        if (processor.search(processorVal) == -1){
            processor += ','
            processor += `${e.target.childNodes[0].value}`
        }
        
    }
    else{
        processor = e.target.childNodes[0].value
    }
    index = parseInt(index)
    if (e.target.childNodes[0].checked){
        e.target.childNodes[0].checked = false
    }
    else{
        e.target.childNodes[0].checked = true
    }
    window.location.href = `?${s}=${processor}`
}