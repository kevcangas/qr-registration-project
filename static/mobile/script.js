//AJAX fot requests
const request = new XMLHttpRequest();
const ip = 'http://192.168.1.76:8000/'


//Elements
//Elements for actions with database
const btn_add = document.querySelector('.add')
const btn_delete = document.querySelector('.delete')

const id_group = document.querySelector('.group-id')
const id_user = document.querySelector('#result')


//Elements for alerts
const close = document.getElementsByClassName("closebtn");
const succes_alert = document.querySelector('.success')
const warning_alert = document.querySelector('.warning')



//Functions
function addUserGroup() {
    const endpoint = 'v1/users/'
    const URL = ip + endpoint + id_user.innerText

    data = {
        group: parseInt(id_group.value) 
    }

    request.open('PUT', URL);
    request.responseType = 'json';
    request.onload = function () {
        if (this.status == 200){
            displaySucces()
        } else {
            displayWarning()
        }
    }

    request.setRequestHeader('Content-Type', 'application/json')
    request.send(JSON.stringify(data));
}


function deletePetition(id) {
    const endpoint = 'v1/users/'
    const URL = ip + endpoint + id_user.innerText

    if (id == parseInt(id_group.value)){
        data = {
            group: null 
        }
    
        request.open('PUT', URL);
        request.responseType = 'json';
        request.onload = function () {
            if (this.status == 200){
                displaySucces()
            } else {
                console.log(this.response);
                displayWarning()
            }
        }
        request.setRequestHeader('Content-Type', 'application/json')
        request.send(JSON.stringify(data));
    }
    else{
        displayWarning()
        console.log(id);
        console.log(parseInt(id_group.value));
    }   
}


//functions to show a user by id
function deleteUserGroup() {
    const endpoint = 'v1/users/'
    const URL = ip + endpoint

    id = id_user.innerText;

    request.open('GET', URL + id);
    request.responseType = 'json';
    request.onload = function () {
        if (this.status == 200){
            var users = this.response;
            console.log(users);
            deletePetition(users.detail.group)
        } else {
            console.log(`An error occurred during your request! Code: ${request.status}`);
        }
    }
    request.send();
}


//Functions for alerts
close[0].onclick = function(){
    succes_alert.style.opacity = "0";
    setTimeout(function(){ succes_alert.style.display = "none"; }, 600);
}

close[1].onclick = function(){
    warning_alert.style.opacity = "0";
    setTimeout(function(){ warning_alert.display = "none"; }, 600);
}


function displaySucces(){
    succes_alert.style.display = 'flex'
    succes_alert.style.opacity = '100'
    setTimeout(() => {
        succes_alert.style.opacity = '0'
        setTimeout(() => succes_alert.style.display = "none", 600)
    }, 1000)
}


function displayWarning(){
    warning_alert.style.display = 'flex'
    warning_alert.style.opacity = '100'
    setTimeout(() => {
        warning_alert.style.opacity = '0'
        setTimeout(() => warning_alert.style.display = "none", 600)
    }, 1000)
}


//Listeners
btn_add.addEventListener('click', addUserGroup)
btn_delete.addEventListener('click', deleteUserGroup)