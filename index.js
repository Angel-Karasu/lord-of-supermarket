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

let search_products_html, search_products_input, sortby, descending_order,
    products_html, product_template;
let page = 1;

function search_products() {
    let search = `search=${search_products_input.value}&page=${page}&sortby=${sortby.value}&descending_order=${descending_order.checked}&list_supermarket_id=0&list_supermarket_id=116`;
    window.location.hash = search;

    fetch(`${supermarket_scraper_api_url}/search_product?${search}`).then(res => res.json()).then(products => {
        products_html.innerHTML = '';
        products.forEach(([id, product]) => {
            let prod = product_template.cloneNode(true);
            
            prod.querySelector('img').src = product.image_url;
            prod.querySelector('.brand').textContent = product.brand;
            prod.querySelector('.description').textContent = product.description;
            prod.querySelector('.price_relative').textContent = product.price_relative;
            prod.querySelector('.quantity_unit').textContent = product.quantity_unit;
            prod.querySelector('.price_absolute').textContent = product.price_absolute;
            Array.from(prod.querySelectorAll('.price_unit')).map(p => p.textContent = product.price_unit);

            products_html.appendChild(prod);
        })
    });
}

window.onload = async () => {
    search_products_html = document.querySelector('#search-products');
    await supermarkets;
    console.log(await supermarkets);

    if (!API_activated) {
        document.querySelector('header').innerHTML = document.querySelector('header h1').outerHTML;
        document.querySelector('main').innerHTML = `<span id="error">${await supermarkets}</span>`;
        return;
    }

    search_products_input = search_products_html.querySelector('input');
    sortby = search_products_html.querySelector('#sortby');
    descending_order = search_products_html.querySelector('input[type="checkbox"]');
    products_html = document.querySelector('#products');
    product_template = document.querySelector('.product').cloneNode(true);

    fetch(`${supermarket_scraper_api_url}/get_sortby_methods`).then(res => res.json()).then(sortby_methods => sortby_methods.forEach(method => {
        let option = document.createElement('option');
        option.value = method;
        option.innerHTML = method.charAt(0).toUpperCase() + method.substr(1).replace('_', ' ');
        sortby.appendChild(option);
    }));

    search_products_input.onsearch = search_products;
    search_products_html.querySelector('button').onclick = search_products;
}