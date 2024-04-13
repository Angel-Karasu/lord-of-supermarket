const supermarket_scraper_api_url = 'http://localhost:5500'

let search_input, sortby, descending_order;
let page = 1;

function search_product() {
    let search = `search=${search_input.value}&page=1&sortby=${sortby.value}&descending_order=${descending_order.checked}&list_supermarket_id=0&list_supermarket_id=116`;
    window.location.hash = search;

    fetch(`${supermarket_scraper_api_url}/search_product?${search}`, {
        method: 'GET',
        headers: {'Content-Type': 'application/json'},
    }).then(response => response.json()).then(data => console.log(data));
}

window.onload = () => {
    search_input = document.querySelector('#search-input');
    sortby = document.querySelector('#sortby');
    descending_order = document.querySelector('#descending-order-checkbox');

    fetch(`${supermarket_scraper_api_url}/get_sortby_methods`, {
        method: 'GET',
        headers: {'Content-Type': 'application/json'},
    }).then(res => res.json()).then(sortby_methods => sortby_methods.forEach(method => {
        let option = document.createElement('option');
        option.value = method;
        option.innerHTML = method.charAt(0).toUpperCase() + method.substr(1).replace('_', ' ');
        sortby.appendChild(option);
    }));

    search_input.onchange = search_product;
    document.querySelector('#search-button').onclick = search_product;
}