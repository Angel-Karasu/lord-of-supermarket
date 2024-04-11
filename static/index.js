let search_input, sort, order;

const xml = new XMLHttpRequest();
xml.onload = () => console.log(xml.response, JSON.parse(xml.response));

function search() {
    window.location.hash = `search=${search_input.value}&sort=${sort.value}&order=${order.value}`;
    xml.open('GET', `/search/${search_input.value}/1/${sort.value}/${order.value}/`);
    xml.send();
}

window.onload = () => {
    search_input = document.querySelector('#search-input');
    sort = document.querySelector('#sort');
    order = document.querySelector('#order');

    search_input.onchange = search;
    document.querySelector('#search-button').onclick = search;
}