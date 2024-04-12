let search_input, sort, order;
let page = 1;

function search() {
    window.location.hash = `search=${search_input.value}&sort=${sort.value}&order=${order.value}`;

    fetch('/search/', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({search: search_input.value, page: 1, sort: sort.value, order: order.value})
    }).then(response => response.json()).then(data => console.log(data));
}

window.onload = () => {
    search_input = document.querySelector('#search-input');
    sort = document.querySelector('#sort');
    order = document.querySelector('#order');

    search_input.onchange = search;
    document.querySelector('#search-button').onclick = search;
}