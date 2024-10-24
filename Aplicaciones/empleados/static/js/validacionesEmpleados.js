document.addEventListener("DOMContentLoaded", function() {
    // Función para validar si un string contiene solo letras
    function containsOnlyLetters(str) {
        return /^[A-Za-zÁÉÍÓÚáéíóúñÑ\s]+$/.test(str);
    }

    // Función para validar si un string contiene solo números
    function containsOnlyNumbers(str) {
        return /^\d+$/.test(str);
    }

    // Función para validar si un string tiene exactamente 11 dígitos
    function isValidCuilCuit(str) {
        return /^\d{11}$/.test(str);
    }

    // Función para validar la dirección
    function isValidDireccion(str) {
        return /^[A-Za-z0-9\s°]+$/.test(str);
    }

    // Función para validar si un string es un correo electrónico válido
    function isValidEmail(email) {
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    }

    // Función para mostrar un mensaje de validación
    function showValidationMessage(input, errorId, message) {
        const errorElement = document.getElementById(errorId);
        errorElement.textContent = message;
        errorElement.classList.remove('hidden');
        input.classList.add('border-red-500');
    }

    // Función para ocultar un mensaje de validación
    function hideValidationMessage(input, errorId) {
        const errorElement = document.getElementById(errorId);
        errorElement.textContent = '';
        errorElement.classList.add('hidden');
        input.classList.remove('border-red-500');
    }

    // Función para validar un formulario
    function validateForm(formId) {
        const form = document.getElementById(formId);

        if (!form) return;

        const isEditForm = formId.startsWith('editarEmpleadoForm');

        const fields = [
            {inputName: 'nombre_persona', errorId: 'errorNombre', validate: containsOnlyLetters, message: "El nombre solo puede contener letras."},
            {inputName: 'apellido_persona', errorId: 'errorApellido', validate: containsOnlyLetters, message: "El apellido solo puede contener letras."},
            {inputName: 'cuitl_persona', errorId: 'errorCuitl', validate: value => containsOnlyNumbers(value) && isValidCuilCuit(value), message: "El CUIL/CUIT debe contener solo números y tener exactamente 11 dígitos."},
            {inputName: 'direccion_persona', errorId: 'errorDireccion', validate: isValidDireccion, message: "La dirección solo puede contener letras, números, espacios y el carácter especial '°'."},
            {inputName: 'correo_electronico', errorId: 'errorCorreo', validate: isValidEmail, message: "El correo electrónico no es válido."}, // Validación para el correo electrónico
            {inputName: 'descripcion_contacto_correo', errorId: 'errorCorreoEditar', validate: isValidEmail, message: "El correo electrónico no es válido."} // Cambiado a 'descripcion_contacto_correo'
        ];
        

        fields.forEach(field => {
            const input = form.querySelector(`[name="${field.inputName}${isEditForm ? '_editar' : ''}"]`);
            const errorId = isEditForm ? `${field.errorId}${formId.match(/\d+$/)[0]}` : field.errorId;

            if (input) {
                input.addEventListener("input", function() {
                    console.log(`Validando ${field.inputName}: ${input.value}`); // Agrega esto
                    if (!field.validate(input.value)) {
                        showValidationMessage(input, errorId, field.message);
                    } else {
                        hideValidationMessage(input, errorId);
                    }
                });
            }
        });

        form.addEventListener("submit", function(event) {
            let isValid = true;

            fields.forEach(field => {
                const input = form.querySelector(`[name="${field.inputName}${isEditForm ? '_editar' : ''}"]`);
                const errorId = isEditForm ? `${field.errorId}${formId.match(/\d+$/)[0]}` : field.errorId;

                if (input) {
                    if (!field.validate(input.value)) {
                        isValid = false;
                        showValidationMessage(input, errorId, field.message);
                    } else {
                        hideValidationMessage(input, errorId);
                    }
                }
            });

            if (!isValid) {
                event.preventDefault();
            }
        });
    }

    // Validar el formulario de agregar
    validateForm('empleadoForm');

    
    // Validar todos los formularios de editar
    document.querySelectorAll('form[id^="editarEmpleadoForm"]').forEach(form => {
        validateForm(form.id);
    });
});