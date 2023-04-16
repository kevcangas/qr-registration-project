//AJAX fot requests
const request = new XMLHttpRequest();
const ip = 'http://127.0.0.1:8000/'
const endpoint = 'v1/users'
const URL = ip + endpoint


//Elements
const reload = document.querySelector('.reload');
const table_header = document.querySelector('thead')
const table_body = document.querySelector('tbody')


//functions
function getUsers() {
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
    
    const titles = document.createElement('tr');
    titles.classList.add('titles')

    const title1 = document.createElement('th');
    title1.innerText = 'ID';

    const title2 = document.createElement('th');
    title2.innerText = 'Name';

    const title3 = document.createElement('th');
    title3.innerText = 'Group ID';

    titles.appendChild(title1)
    titles.appendChild(title2)
    titles.appendChild(title3)
    table_header.appendChild(titles)


    for (user of users){
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
        table_body.appendChild(row)
    }
}


//listeners
window.addEventListener('load', getUsers);
reload.addEventListener('click', _ => location.reload())