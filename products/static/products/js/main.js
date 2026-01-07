document.addEventListener("DOMContentLoaded", () => {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll("nav a");

    navLinks.forEach(link => {
        const href = link.getAttribute("href");
        if (!href) return;

        if (currentPath.startsWith(href)) {
            link.classList.add("active");
        }
    });

    const header = document.querySelector("header");
    if (header) {
        const toggleHeader = () => {
            if (window.scrollY > 10) {
                header.classList.add("header--scrolled");
            } else {
                header.classList.remove("header--scrolled");
            }
        };

        toggleHeader();
        window.addEventListener("scroll", toggleHeader);
    }

    const cards = document.querySelectorAll(".category-card, .product-card");
    cards.forEach(card => {
        card.addEventListener("click", () => {
            card.classList.toggle("card--expanded");
        });
    });

    const toggle = document.getElementById("adminToggle");
    if (!toggle) return;

    toggle.addEventListener("change", () => {
        document.querySelectorAll(".admin-actions").forEach(block => {
            block.classList.toggle("hidden", !toggle.checked);
        });
    });
});
