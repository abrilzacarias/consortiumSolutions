document.getElementById('email').addEventListener('input', function() {
    var errorMessage = document.getElementById('error-message');
    if (errorMessage) {
        errorMessage.style.display = 'none';
    }
});

document.getElementById('reset-form').addEventListener('submit', function(event) {
    var email = document.getElementById('email').value;
    var errorMessage = document.getElementById('error-message');
    if (email.trim() === "") {
        event.preventDefault();
        if (errorMessage) {
            errorMessage.style.display = 'block';
            errorMessage.textContent = 'Por favor, ingrese un correo electrónico.';
        }
    } else {
        errorMessage.style.display = 'none';
    }
});

window.onload = function() {
    var errorMessage = document.getElementById('error-message');
    if (errorMessage.textContent.trim() !== "") {
        errorMessage.style.display = 'block';
    }
};
