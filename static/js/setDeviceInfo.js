function uuidv4() {
    return ([1e7]+-1e3+-4e3+-8e3+-1e11).replace(/[018]/g, c =>
      (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)
    );
  }
  function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
  }
  if (getCookie('deviceID') == null || getCookie('deviceID') == undefined || getCookie('deviceID') == ''){
    console.log('Setting cookies of deviceID')
    let uid = uuidv4()
    var datetime1 = new Date();
    let month = (datetime1.getMonth() + 1) % 11
    var datetime2 = new Date(datetime1.getFullYear()+1,month,datetime1.getDay(),datetime1.getHours(),datetime1.getMinutes(),datetime1.getSeconds(),datetime1.getMilliseconds())
    console.log(datetime2)
    document.cookie = `deviceID=${uid}; expires=${datetime2}; path=/`;
  }
  console.log(getCookie('deviceID').length)

console.log(getCookie('deviceID'))