// products/static/products/js/main.js

document.addEventListener("DOMContentLoaded", () => {
    // ---------- 1. Подсветка активной ссылки меню ----------
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll("nav a");

    navLinks.forEach(link => {
        const href = link.getAttribute("href");
        if (!href) return;

        // если путь начинается с href — считаем ссылку активной
        if (currentPath.startsWith(href)) {
            link.classList.add("active");
        }
    });

    // ---------- 2. Сжатие хедера при скролле ----------
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

    // ---------- 3. Раскрытие карточек категорий/товаров по клику ----------
    // Работает для элементов с классами .category-card и .product-card (если добавишь их в шаблон)
    const cards = document.querySelectorAll(".category-card, .product-card");
    cards.forEach(card => {
        card.addEventListener("click", () => {
            card.classList.toggle("card--expanded");
        });
    });

    // Просто милое приветствие в консоли :)
    console.log("🐾 Ласкаво просимо до Peachy love – вашого затишного зоомагазину!");
});
