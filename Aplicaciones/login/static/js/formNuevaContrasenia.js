const form = document.getElementById('reset-form');
const newPassword1 = document.getElementById('new_password1');
const newPassword2 = document.getElementById('new_password2');
const errorNewPassword1 = document.getElementById('error-new_password1');
const errorNewPassword2 = document.getElementById('error-new_password2');

function validatePassword() {
    let errors = [];

    if (/^\d+$/.test(newPassword1.value)) {
        errors.push('No puede ser completamente numérica');
    }

    if (newPassword1.value.length < 8) {
        errors.push('Debe contener al menos 8 caracteres');
    }

    errorNewPassword1.innerHTML = errors.join('. ');
    errorNewPassword1.style.display = errors.length > 0 ? 'block' : 'none';

    return errors.length === 0;
}

function validatePasswordsMatch() {
    let errors = [];

    if (newPassword1.value !== newPassword2.value) {
        errors.push('Las contraseñas no coinciden');
    }

    errorNewPassword2.innerHTML = errors.join('. ');
    errorNewPassword2.style.display = errors.length > 0 ? 'block' : 'none';

    return errors.length === 0;
}

form.addEventListener('submit', function(event) {
    const isPasswordValid = validatePassword();
    const doPasswordsMatch = validatePasswordsMatch();

    if (!isPasswordValid || !doPasswordsMatch) {
        event.preventDefault();
    }
});

newPassword1.addEventListener('input', validatePassword);
newPassword2.addEventListener('input', validatePasswordsMatch);
