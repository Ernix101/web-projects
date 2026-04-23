const menuBtn = document.getElementById("menu-toggle");
const navbar = document.getElementById("navbar");



menuBtn.addEventListener("click", () => {

    const isOpen = navbar.classList.toggle("open");
    menuBtn.setAttribute("aria-expanded", isOpen)
});