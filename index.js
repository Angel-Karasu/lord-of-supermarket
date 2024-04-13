const supermarket_scraper_api_url = 'http://localhost:5500'

let search_input, sort, order;
let page = 1;

function search() {
    window.location.hash = `search=${search_input.value}&sort=${sort.value}&order=${order.value}`;

    fetch(`${supermarket_scraper_api_url}/get_sortby_methods`, {
        method: 'GET',
        headers: {'Content-Type': 'application/json'},
    }).then(response => response.json()).then(data => console.log(data));
}

window.onload = () => {
    search_input = document.querySelector('#search-input');
    sort = document.querySelector('#sort');
    order = document.querySelector('#order');

    search_input.onchange = search;
    document.querySelector('#search-button').onclick = search;
}