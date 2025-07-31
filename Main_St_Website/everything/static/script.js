function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
        rect.top < window.innerHeight/2 &&
        rect.bottom > 0
    );
}

window.addEventListener('scroll', function() {
    document.querySelectorAll('.card').forEach(card => {
        if (isInViewport(card)) {
            card.classList.add('animate');
        } else {
            card.classList.remove('animate');
        }
    });
});

// Optionally, run once on page load
window.dispatchEvent(new Event('scroll'));