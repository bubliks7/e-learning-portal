const pages = document.querySelectorAll(".page");
let currentPage = 0;

function showPage(index) {
    pages.forEach((p, i) => {
        p.style.display = i === index ? "block" : "none";
    });
}
document.getElementById("go_left").addEventListener("click", () => {
    if (currentPage > 0) currentPage--;
    showPage(currentPage);
});
document.getElementById("go_right").addEventListener("click", () => {
    if (currentPage < pages.length - 1) currentPage++;
    showPage(currentPage);
});

showPage(currentPage);
