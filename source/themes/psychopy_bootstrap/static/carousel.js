let currentSlide = 0;

function showSlide(index) {
    const track = document.getElementById('carouselTrack');
    const slides = document.querySelectorAll('.carousel-slide');
    const slideWidth = slides[0].offsetWidth;

    track.style.transform = `translateX(-${index * slideWidth}px)`;
    currentSlide = index;
}

function nextSlide() {
    const totalSlides = document.querySelectorAll('.carousel-slide').length;
    currentSlide = (currentSlide + 1) % totalSlides;
    showSlide(currentSlide);
}

function prevSlide() {
    const totalSlides = document.querySelectorAll('.carousel-slide').length;
    currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
    showSlide(currentSlide);
}

function autoSlide() {
    nextSlide();
}

setInterval(autoSlide, 6000);