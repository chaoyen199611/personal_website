
let controller = new ScrollMagic.Controller();
let timeline = new TimelineMax();

timeline
  .fromTo(".title", { opacity: 0 }, { opacity: 1, duration: 3 })
  .fromTo(".about-context", { opacity: 0 }, { opacity: 1, duration: 5 })
let scene = new ScrollMagic.Scene({
  triggerElement: "#secondsec",
  duration: "100%",
  triggerHook: 0.3,
})
  .setTween(timeline)
  .setPin("#secondsec")
  .addTo(controller);

var swiper = new Swiper(".slide-content", {
  slidesPerView: 3,
  spaceBetween: 30,
  loop: true,
  centerSlide: 'true',
  fade: 'true',
  grabCursor: 'true',
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
    dynamicBullets: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },

  breakpoints:{
      0: {
          slidesPerView: 1,
      },
      520: {
          slidesPerView: 2,
      },
      950: {
          slidesPerView: 3,
      },
  },
});