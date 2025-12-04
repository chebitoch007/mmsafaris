// Initialization of Swiper for Testimonials
document.addEventListener('DOMContentLoaded', () => {
    // Check if Swiper is loaded before initialization
    if (typeof Swiper !== 'undefined') {
        const swiper = new Swiper('.testimonials-slider', {
            // Optional parameters
            direction: 'horizontal',
            loop: true,
            slidesPerView: 1,
            spaceBetween: 30,

            // If we need pagination
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },

            // Navigation arrows
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },

            // Responsive breakpoints
            breakpoints: {
                // when window width is >= 768px (tablet)
                768: {
                    slidesPerView: 2,
                    spaceBetween: 30
                },
                // when window width is >= 992px (desktop)
                992: {
                    slidesPerView: 3,
                    spaceBetween: 30
                }
            },
            // Accessibility
            a11y: {
                prevSlideMessage: 'Previous slide',
                nextSlideMessage: 'Next slide',
            },
        });
    }

    // Intersection Observer for Fade-in-Up Animation
    const observerOptions = {
        root: null, // viewport
        rootMargin: '0px 0px -10% 0px', // Trigger when 10% of element is in view
        threshold: 0.1
    };

    const observer = new IntersectionObserver(function(entries, observer) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                // Optional: Stop observing once it's visible
                // observer.unobserve(entry.target);
            } else {
                // Optional: Remove class if scrolling back up (for re-triggering)
                // entry.target.classList.remove('is-visible');
            }
        });
    }, observerOptions);

    // Target all elements with the fade-in-up class
    document.querySelectorAll('.fade-in-up').forEach(el => {
        observer.observe(el);
    });
});