const go_left = document.querySelector('#go_left');
const go_right = document.querySelector('#go_right');
const first_page = document.querySelector('#first_page');
const main_page = document.querySelector('#main_page');

go_right.addEventListener('click', () => {
    main_page.style.display = 'none';
    first_page.style.display = 'block';
})
