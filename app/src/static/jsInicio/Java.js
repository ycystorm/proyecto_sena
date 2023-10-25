//el java del menu responsivo
const menuBtn = document.querySelector(".menu-btn");

const Navegation = document.querySelector(".navegacion");

menuBtn.addEventListener("click", () => {
    menuBtn.classList.toggle("active");
    Navegation.classList.toggle("active");
});

//El java del slider
const btns = document.querySelectorAll(".nav-btn");
const slides = document.querySelectorAll(".video-slide");
    const contents = document.querySelectorAll(".content");

var sliderNav = function(manual){
btns.forEach((btn) => {
btn.classList.remove("active");
});

slides.forEach((slide) => {
slide.classList.remove("active");
});

contents.forEach((content) => {
content.classList.remove("active");
});

btns[manual].classList.add("active");
slides[manual].classList.add("active");
    contents[manual].classList.add("active");
}

btns.forEach((btn, i) => {
btn.addEventListener("click", () => {
sliderNav(i);
});
});