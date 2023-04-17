//AJAX fot requests
const request = new XMLHttpRequest();
const ip = 'http://127.0.0.1:8000/'


//Elements
//Elements to show all users
const btn_all_users = document.querySelector('.all-users');
const table_container = document.querySelector('.table-container')
const table_body = document.querySelector('.table-container tbody')


//Elements to search a user by id
const btn_search = document.querySelector('.search')

const table_search = document.querySelector('.table-search')
const table_body_search = document.querySelector('.table-search tbody')

const form_container = document.querySelector('.form-container')
const btn_send = document.querySelector('.send');
const data = document.querySelector('.form-container input');


//Elements to delete slected user
const btn_delete = document.querySelector('.del')
var checkboxes


//functions
//functions to all users
function getUsers() {
    const endpoint = 'v1/users'
    const URL = ip + endpoint
    
    request.open('GET', URL);
    request.responseType = 'json';
    request.onload = function () {
        if (this.status == 200){
            var users = this.response;
            showUsers(users.detail)
        } else {
            console.log(`An error occurred during your request! Code: ${request.status}`);
        }
    }
    request.send();
}


function showUsers(users) {
    
    return new Promise((resolve, reject) =>{
        for (user of users){

            const row = document.createElement('tr');

            const checkContainer = document.createElement('td')

            const checkUser = document.createElement('input')
            checkUser.type = 'checkbox'
            checkUser.classList.add('checkbox')

            const ID = document.createElement('td');
            ID.innerText = user.id;

            checkUser.name = ID.innerText

            const name = document.createElement('td');
            name.innerText = user.name;

            const groupID = document.createElement('td');
            groupID.innerText = user.group;

            checkContainer.appendChild(checkUser)

            row.appendChild(checkContainer)
            row.appendChild(ID)
            row.appendChild(name)
            row.appendChild(groupID)
            table_body.appendChild(row)
        }
        resolve()
    })
    .then(() => {
            checkboxes = document.querySelectorAll('.checkbox');

            for (checkbox of checkboxes){
                checkbox.addEventListener('input', selectUser);
            }
        })
}


//functions to show a user by id
var searched = null
function getUser() {
    const endpoint = 'v1/users/'
    const URL = ip + endpoint

    id = data.value;
    console.log(id);

    request.open('GET', URL + id);
    request.responseType = 'json';
    request.onload = function () {
        if (this.status == 200){
            var users = this.response;
            showUser(users.detail)
        } else {
            console.log(`An error occurred during your request! Code: ${request.status}`);
            var user = {name: 'No exists', id: 'No exists', group: 'No exists'}
            showUser(user)
        }
    }
    request.send();
}


function showUser(user) {
    const old_row = document.querySelector('.old-row')
    
    const row = document.createElement('tr');

    const ID = document.createElement('td');
    ID.innerText = user.id;
    searched = parseInt(ID.innerText)

    const name = document.createElement('td');
    name.innerText = user.name;

    const groupID = document.createElement('td');
    groupID.innerText = user.group;

    row.appendChild(ID)
    row.appendChild(name)
    row.appendChild(groupID)
    row.classList.add('old-row')

    table_body_search.replaceChild(row, old_row)
}


//functions to activate or deactivate views
function activateAllUsers() {
    table_container.style.display='flex'

    form_container.style.display='none'
    table_search.style.display='none'
}


function activateSearchUser() {
    table_container.style.display='none'

    form_container.style.display='flex'
    table_search.style.display='flex'
}


//functions to delete a selected person
var id_checkbox = null
function selectUser() {
    
    if (this.checked){
        id_checkbox = parseInt(this.name)
        for (checkbox of checkboxes){
            if (checkbox != this) checkbox.disabled = true
        }
    }
    else {
        id_checkbox = 0
        for (checkbox of checkboxes){
            if (checkbox != this) checkbox.disabled = false
        }
    }
}


function deleteUser(id, searched) {
    if (id == searched){
        return new Promise((resolve,reject) =>{
            const endpoint = 'v1/users/'
            const URL = ip + endpoint

            console.log(id);

            request.open('DELETE', URL + id);
            request.responseType = 'json';
            request.onload = function () {
                if (this.status == 200){
                    var users = this.response;
                    showUser(users.detail)
                } else {
                    console.log(`An error occurred during your request! Code: ${request.status}`);
                    var user = {name: 'No exists', id: 'No exists', group: 'No exists'}
                    showUser(user)
                }
            }
            request.send();
            resolve()
        })
        .then(() => window.location.reload())
    } 
    else {
        console.log("User and searched user don't match");
    }
}


//listeners
window.addEventListener('load', getUsers);

btn_all_users.addEventListener('click', activateAllUsers)

btn_search.addEventListener('click', activateSearchUser)

btn_send.addEventListener('click', getUser);


btn_delete.addEventListener('click', () => {
    if (table_container.style.display == 'flex' | table_container.style.display == ''){
        console.log('hola');
        searched = id_checkbox
        deleteUser(id_checkbox, searched)
    }
    else {
        deleteUser(parseInt(data.value), searched)
    }
});
