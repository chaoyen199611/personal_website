
let controller = new ScrollMagic.Controller();
let timeline = new TimelineMax();

timeline
  .fromTo(".title", { opacity: 0 }, { opacity: 1, duration: 3 })
  .fromTo(".about-context", { opacity: 0 }, { opacity: 1, duration: 5 })
  .fromTo("#title",{opacity:0},{opacity:1,duration:3});
let scene = new ScrollMagic.Scene({
  triggerElement: "#secondsec",
  duration: "100%",
  triggerHook: 0,
})
  .setTween(timeline)
  .setPin("#secondsec")
  .addTo(controller);