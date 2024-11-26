let currentSlide = 0;
const slides = document.querySelectorAll('.partner-slide');
const totalSlides = slides.length;

function moveSlide(direction) {
    const slider = document.querySelector('.slider');
    currentSlide = (currentSlide + direction + totalSlides) % totalSlides;
    slider.style.transform = `translateX(-${currentSlide * 25}%)`;
}
