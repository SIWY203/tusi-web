
window.addEventListener('scroll', function () {
    const hero = document.getElementById('hero');
    const offer = document.querySelector('.offer-bg');
    const scrollY = window.scrollY;
    const top = 0.75 * window.innerHeight - 200;

    if (scrollY > 200) {
        hero.style.position = 'absolute';
        hero.style.top = '200px';
        offer.style.position = 'absolute';
        offer.style.top = `${top}px`;
    } else {
        hero.style.position = 'fixed';
        hero.style.top = '0';
        offer.style.position = 'fixed';
        offer.style.top = '75vh';
    }
});


