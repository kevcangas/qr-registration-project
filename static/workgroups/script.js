//AJAX fot requests
const request = new XMLHttpRequest();
//const ip = 'http://192.168.1.76:8000/'
const ip = 'http://127.0.0.1:8000/'


//Elements
const main = document.querySelector('.main-container')
//Elements to show all users
const btn_all_workgroups = document.querySelector('.all-workgroups');
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


//Elements to create new workgroup
const form_create_container = document.querySelector('.form-create-container')
const btn_create_workgroup = document.querySelector('.create')
const form_new_workgroup_superviser = document.querySelector('.new-workgroup-superviser')
const btn_send_new_workgroup = document.querySelector('.send-new-workgroup')


//Elements to assign group
const form_assign_container = document.querySelector('.form-assign-container')
const form_group_id = document.querySelector('.group-id-assign')
const btn_send_group_id = document.querySelector('.send-group-id')


//functions
//functions to all users
function getUsers() {
    const endpoint = 'v1/workgroups'
    const URL = ip + endpoint
    
    request.open('GET', URL);
    request.responseType = 'json';
    request.onload = function () {
        if (this.status == 200){
            var users = this.response;
            showWorkgroups(users.detail)
        } else {
            console.log(`An error occurred during your request! Code: ${request.status}`);
        }
    }
    request.send();
}


function showWorkgroups(workgroups) {
    
    for (workgroup of workgroups){

        const row = document.createElement('tr');

        const checkContainer = document.createElement('td')

        const checkUser = document.createElement('input')
        checkUser.type = 'checkbox'
        checkUser.classList.add('checkbox')

        const ID = document.createElement('td');
        ID.innerText = workgroup.id;

        checkUser.name = ID.innerText

        const superviser = document.createElement('td')
        superviser.innerText = workgroup.superviser

        checkContainer.appendChild(checkUser)

        row.appendChild(checkContainer)
        row.appendChild(ID)
        row.appendChild(superviser)
        table_body.appendChild(row)
    }
        
    checkboxes = document.querySelectorAll('.checkbox');

    for (checkbox of checkboxes){
        checkbox.addEventListener('input', selectUser);
    }
    
}


function showWorkgroupUsers(users) {
    
    const rows = document.querySelectorAll('.table-search .table-body table tbody tr')

    
    for (row of rows){
        table_body_search.removeChild(row)
    }

    for (user of users){
       
        const row = document.createElement('tr');

        const ID = document.createElement('td');
        ID.innerText = user.id;

        const name = document.createElement('td')
        name.innerText = user.name

        row.appendChild(ID)
        row.appendChild(name)

        table_body_search.appendChild(row)
    }
}


//functions to show a user by id
var searched = null
function getUser() {
    const endpoint = 'v1/workgroups/'
    const URL = ip + endpoint

    id = data.value;
    console.log(id);

    request.open('GET', URL + id + '/users');
    request.responseType = 'json';
    request.onload = function () {
        if (this.status == 200){
            var workgroup_users = this.response;
            showWorkgroupUsers(workgroup_users.detail.users)
        } else {
            console.log(`An error occurred during your request! Code: ${request.status}`);
            var user = {name: 'No exists', id: 'No exists', group: 'No exists'}
            showUser(user)
        }
    }
    request.send();
}


//functions to activate or deactivate views
function activateAllWorkgroups() {
    window.location.reload()
}


function activateSearchUser() {
    table_container.style.display='none'

    form_container.style.display='flex'
    table_search.style.display='flex'

    form_create_container.style.display='none'

    form_assign_container.style.display='flex'

    data.value = null
    form_new_workgroup_name.value = null
    form_group_id.value = null
}


function activateCreateWorkgroup() {
    table_container.style.display='none'

    form_container.style.display='none'
    table_search.style.display='none'

    form_create_container.style.display='flex'

    form_assign_container.style.display='none'

    data.value = null
    form_new_workgroup_name.value = null
    form_group_id.value = null
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
        const endpoint = 'v1/workgroups/'
        const URL = ip + endpoint

        console.log(id);

        request.open('DELETE', URL + id);
        request.responseType = 'json';
        request.onload = function () {
            if (this.status == 200){
                window.location.reload()
            } 
            else {
                console.log(`An error occurred during your request! Code: ${request.status}`);
            }
        }
        request.send();
    } 
    else {
        console.log("User and searched user don't match");
    }
}


//Functions to create users
function createWorkgroup() {
    
    const endpoint = 'v1/workgroups/'
    const URL = ip + endpoint

    newWorkgroup = {
        superviser_id: form_new_workgroup_superviser.value
    }

    console.log(JSON.stringify(newWorkgroup));

    request.open('POST', URL);
    request.responseType = 'json';
    request.onload = function () {
        if (this.status == 200){
            activateAllWorkgroups()
        } 
        else {
            console.log(`An error occurred during your request! Code: ${request.status}`);   
        }
    }
    request.setRequestHeader('Content-Type', 'application/json')
    request.send(JSON.stringify(newWorkgroup));
        
}


//listeners
window.addEventListener('load', getUsers);

btn_all_workgroups.addEventListener('click', activateAllWorkgroups)

btn_search.addEventListener('click', activateSearchUser)

btn_send.addEventListener('click', getUser);

btn_create_workgroup.addEventListener('click', activateCreateWorkgroup)

btn_send_new_workgroup.addEventListener('click', createWorkgroup)


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