//AJAX fot requests
const request = new XMLHttpRequest();
const ip = 'http://127.0.0.1:8000/'
const endpoint = 'v1/users/'
const URL = ip + endpoint


//elements
const send = document.querySelector('.send');
const data = document.querySelector('input');

const table_body = document.querySelector('tbody')



//functions
function getUser() {
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

    const name = document.createElement('td');
    name.innerText = user.name;

    const groupID = document.createElement('td');
    groupID.innerText = user.group;

    row.appendChild(ID)
    row.appendChild(name)
    row.appendChild(groupID)
    row.classList.add('old-row')

    table_body.replaceChild(row, old_row)
}


//listeners
send.addEventListener('click', getUser);