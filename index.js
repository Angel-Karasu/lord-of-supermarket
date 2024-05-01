document.cookie = JSON.stringify({'supermarkets_id':[0, 12, 126]});
const cookies = JSON.parse(document.cookie);

const supermarket_scraper_api_url = cookies['supermarket_scraper_api_url'] || 'http://localhost:5500';

let search_products_html, search_products_input, sortby, descending_order,
    products_html, product_template;

let page = 1;
let supermarkets_id = cookies['supermarkets_id'].reduce((acc, id) => acc+'&supermarkets_id='+id, '');

function search_products() {
    const search = `search=${search_products_input.value}&page=${page}&sortby=${sortby.value}&descending_order=${descending_order.checked}`;
    window.location.hash = search;

    fetch(`${supermarket_scraper_api_url}/search_product?${search}${supermarkets_id}`).then(res => res.json()).then(products => {
        products_html.innerHTML = '';
        products.forEach(([id, product]) => {
            const prod = product_template.cloneNode(true);
            
            prod.href = product.product_url;
            prod.querySelector('img').src = product.image_url;

            prod.querySelector('.brand').textContent = product.brand;
            prod.querySelector('.supermarket-id').textContent = id;

            prod.querySelector('.description').textContent = product.description;
            
            prod.querySelector('.price_relative').textContent = product.price_relative;
            prod.querySelector('.quantity_unit').textContent = product.quantity_unit;
            prod.querySelector('.price_absolute').textContent = product.price_absolute;
            Array.from(prod.querySelectorAll('.price_unit')).map(p => p.textContent = product.price_unit);

            products_html.appendChild(prod);
        })
    });
}

function set_cookie(key, value) {
    cookies[key] = value;
    document.cookie = JSON.stringify(cookies);
}

window.onload =  () => {
    search_products_html = document.querySelector('#search-products');

    search_products_input = search_products_html.querySelector('input');
    sortby = search_products_html.querySelector('#sortby');
    descending_order = search_products_html.querySelector('input[type="checkbox"]');
    products_html = document.querySelector('#products');
    
    product_template = document.querySelector('.product').cloneNode(true);
    product_template.style.display = '';

    search_products_input.onsearch = search_products;
    search_products_html.querySelector('button').onclick = search_products;

    fetch(`${supermarket_scraper_api_url}/get_sortby_methods`).then(res => res.json()).then(sortby_methods => {
        sortby_methods.forEach(method => {
            let option = document.createElement('option');
            option.value = method;
            option.innerHTML = method.charAt(0).toUpperCase() + method.substr(1).replace('_', ' ');
            sortby.appendChild(option);
        });

        if (window.location.hash) {
            let params = (new URL(window.location.href.replace('#', '?'))).searchParams;
            search_products_input.value = params.get('search');
            sortby.value = params.get('sortby');
            descending_order.checked = params.get('descending_order') == 'true';
            search_products();
        }
    }).catch(() => {
        alert('API not found');
        document.querySelector('header').innerHTML = document.querySelector('header h1').outerHTML;
        document.querySelector('main').innerHTML = `<span id="error">API not found</span>`;

        let input = document.createElement('input');
        input.type = 'text';
        input.placeholder = 'Set the API url';
        input.onchange = () => {
            set_cookie('supermarket_scraper_api_url', input.value);
            window.location.reload();
        };
        document.querySelector('main').appendChild(input);
    });
}