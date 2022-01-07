let eventnumber = document.querySelector("#eventNumber")
let eventname = document.querySelector("#eventName")
let eventtime = document.querySelector("#eventTime")
function getEvent(a) {
    a.toString();
    let url = "http://120.110.115.151:8000/apiRead/event/" + a + "/";
    let xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.send();
    xhr.onload = function(){
        data = JSON.parse(this.responseText);
        eventnumber.innerHTML = data['eventNumber'];
        eventname.innerHTML = data['eventName'];
        eventtime.innerHTML = data['eventTime'].substr(0, 10).replaceAll('-', '/') +
                                " " + data['eventTime'].substr(11, 8);
        console.log(data['device']);
        console.log(data);
    }
}