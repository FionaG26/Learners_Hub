// Learners_Hub/static/js/scripts.js

// Add your custom JavaScript here
document.addEventListener('DOMContentLoaded', function () {
    console.log('Custom JavaScript Loaded');
    
    // Example: Toggle a CSS class on click
    const toggleButton = document.getElementById('toggle-button');
    if (toggleButton) {
        toggleButton.addEventListener('click', function () {
            const elementToToggle = document.getElementById('element-to-toggle');
            elementToToggle.classList.toggle('active');
        });
    }
});
