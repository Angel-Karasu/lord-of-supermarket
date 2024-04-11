let search_input, sort, order;

function search() {
    window.location = `/search/?search=${search_input.value}&sort=${sort.value}&order=${order.value}`;
}

window.onload = () => {
    search_input = document.querySelector('#search-input');
    sort = document.querySelector('#sort');
    order = document.querySelector('#order');

    search_input.onchange = search;
    document.querySelector('#search-button').onclick = search;
}