let btn = document.querySelector("#btn");
let sidebar = document.querySelector(".sidebar");
let event = document.querySelector("#event");
let a;
let data;
let eventnumber = document.querySelector("#eventNumber")
let eventname = document.querySelector("#eventName")
let eventPIC = document.querySelector("#eventPIC")
let b;
btn.onclick = function() {
    sidebar.classList.toggle("active");
}
function getEvent(a) {
    a.toString();
    let url = "http://127.0.0.1:8000/api/event/" + a + "/";
    let xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.send();
    xhr.onload = function(){
        data = JSON.parse(this.responseText);
        eventnumber.innerHTML = data['eventNumber'];
        getEventName(data['eventName']);
        getDutyList();

    }

}
function getEventName(a) {
    eventname.innerHTML = data['eventName'];
    let url = "http://127.0.0.1:8000/api/eventName/" + a + "/";
    let xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.send();
    xhr.onload = function(){
        data = JSON.parse(this.responseText);
        eventname.innerHTML = data['eventName'];
    }
}
function getDutyList(){
    let url = "http://127.0.0.1:8000/api/dutyList/1/";
    let xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.send();
    xhr.onload = function(){
        data = JSON.parse(this.responseText);
        console.log(data)
        //for(let i = 0; i < data.length;i++){
            //eventPIC.innerHTML = data['building'];
        //}
    }
}