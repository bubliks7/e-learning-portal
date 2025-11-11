const pages = document.querySelectorAll(".page");
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
    const left = container.querySelector('#go_left');
    const right = container.querySelector('#go_right');
    let current = 0;

    function showPage(i) {
        pages.forEach((p, n) => p.style.display = (n === i) ? 'block' : 'none');
    }

    left.addEventListener('click', () => { if (current > 0) current--; showPage(current); });
    right.addEventListener('click', () => { if (current < pages.length - 1) current++; showPage(current); });

    showPage(current);
});
