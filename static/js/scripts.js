function handleAction() {
    // Trigger the click event of the hidden link
    document.getElementById('ctaLink').click();
}

document.addEventListener('keydown', function (event) {
    if (event.keyCode === 32) { // Check for spacebar (keyCode 32)
        handleAction();
    }
});

// Handle tap or click event
document.getElementById('clickText').addEventListener('click', handleAction);
