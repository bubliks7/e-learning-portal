// let currentPage = 0;

// function showPage(index) {
//     pages.forEach((p, i) => {
//         p.style.display = i === index ? "block" : "none";
//     });
// }
// document.getElementById("go_left").addEventListener("click", () => {
//     if (currentPage > 0) currentPage--;
//     showPage(currentPage);
// });
// document.getElementById("go_right").addEventListener("click", () => {
//     if (currentPage < pages.length - 1) currentPage++;
//     showPage(currentPage);
// });

// showPage(currentPage);

document.querySelectorAll('.course-container').forEach(container => {
    const pages = container.querySelectorAll('.page');
    const leftBtn = container.querySelector('#go_left');
    const rightBtn = container.querySelector('#go_right');
    let current = 0;

    function showPage(n) {
        pages.forEach((p, i) => p.style.display = (i === n ? 'block' : 'none'));
    }

    leftBtn.addEventListener('click', () => {
        if (current > 0) current--;
        showPage(current);
    });

    rightBtn.addEventListener('click', () => {
        if (current < pages.length - 1) current++;
        showPage(current);
    });

    showPage(current);
});