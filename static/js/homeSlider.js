console.log('slider.js is connected!')

const sliderWrapper = document.querySelector('.sliders-wrapper');
const slides = document.querySelectorAll('.sliders');
const totalSlides = slides.length;
const radioControlBtns = document.querySelectorAll('.radioControlsBtns')

var currentIndex = 0;
var slideWidth = slides[0].offsetWidth;

function InitiateSlide() {
    sliderWrapper.style.transition = 'none';
    sliderWrapper.style.transform = `translateX(0)`;
    currentIndex = 0;
    radioControlBtns[currentIndex].checked = true
}

function moveSlide() {

    if (currentIndex === totalSlides) {

        sliderWrapper.style.transition = 'none';
        sliderWrapper.style.transform = `translateX(0)`;
        currentIndex = 0;
        radioControlBtns[currentIndex].checked = true


        setTimeout(() => {
            sliderWrapper.style.transition = 'transform 0.5s ease';
        }, 50);
    } else {

        slideWidth = slides[currentIndex].offsetWidth

        sliderWrapper.style.transform = `translateX(-${slideWidth * currentIndex}px)`;
        radioControlBtns[currentIndex].checked = true
        currentIndex++;
    }


}

InitiateSlide()
// Move the slides every 2 seconds
setInterval(moveSlide, 3000);


radioControlBtns.forEach((btn) => {
    btn.addEventListener('click', (e) => {
        let index = e.target.value
        index = parseInt(index)
        currentIndex = index
        sliderWrapper.style.transform = `translateX(-${slideWidth * currentIndex}px)`;
    })
})