const supermarket_scraper_api_url = 'http://localhost:5500';
let API_activated = true;

const supermarkets = fetch(`${supermarket_scraper_api_url}/get_supermarkets`).then(res => {
    if (!res.ok) throw new Error('API not activated');
    return res.json();
}).catch(err => {
    alert(err);
    API_activated = false;
    return err;
});

let search_products, search_products_input, sortby, descending_order;
let page = 1;

function search_product() {
    let search = `search=${search_products_input.value}&page=${page}&sortby=${sortby.value}&descending_order=${descending_order.checked}&list_supermarket_id=0&list_supermarket_id=116`;
    window.location.hash = search;

    fetch(`${supermarket_scraper_api_url}/search_product?${search}`).then(res => res.json()).then(data => console.log(data));
}

window.onload = async () => {
    search_products = document.querySelector('#search-products');
    await supermarkets;
    console.log(await supermarkets);

    if (!API_activated) {
        document.querySelector('header').innerHTML = document.querySelector('header h1').outerHTML;
        document.querySelector('main').innerHTML = `<span id="error">${await supermarkets}</span>`;
        return;
    }

    search_products_input = search_products.querySelector('input');
    sortby = search_products.querySelector('#sortby');
    descending_order = search_products.querySelector('input[type="checkbox"]');

    fetch(`${supermarket_scraper_api_url}/get_sortby_methods`).then(res => res.json()).then(sortby_methods => sortby_methods.forEach(method => {
        let option = document.createElement('option');
        option.value = method;
        option.innerHTML = method.charAt(0).toUpperCase() + method.substr(1).replace('_', ' ');
        sortby.appendChild(option);
    }));

    search_products_input.onsearch = search_product;
    search_products.querySelector('button').onclick = search_product;
}