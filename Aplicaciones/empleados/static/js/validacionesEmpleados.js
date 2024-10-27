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
    // Función para validar un formulario
    function validateForm(formId) {
        const form = document.getElementById(formId);
        if (!form) return;

        const isEditForm = formId.startsWith('editarEmpleadoForm');
        const employeeId = isEditForm ? formId.replace('editarEmpleadoForm', '') : '';

        const fields = [
            {
                inputName: 'nombre_persona',
                errorId: 'errorNombre',
                validate: containsOnlyLetters,
                message: "El nombre solo puede contener letras."
            },
            {
                inputName: 'apellido_persona',
                errorId: 'errorApellido',
                validate: containsOnlyLetters,
                message: "El apellido solo puede contener letras."
            },
            {
                inputName: 'cuitl_persona',
                errorId: 'errorCuitl',
                validate: value => containsOnlyNumbers(value) && isValidCuilCuit(value),
                message: "El CUIL/CUIT debe contener solo números y tener exactamente 11 dígitos."
            },
            {
                inputName: 'direccion_persona',
                errorId: 'errorDireccion',
                validate: isValidDireccion,
                message: "La dirección solo puede contener letras, números, espacios y el carácter especial '°'."
            }
        ];

        // Agregar validación específica para el correo electrónico
        if (isEditForm) {
            // Buscar el campo de correo por ID específico del empleado
            const emailInput = form.querySelector(`#correo_persona_editar_${employeeId}`);
            if (emailInput) {
                // Validación en tiempo real
                emailInput.addEventListener("input", function() {
                    console.log('Validando email:', this.value);
                    if (!isValidEmail(this.value)) {
                        showValidationMessage(this, `errorCorreoEditar${employeeId}`, "El correo electrónico no es válido.");
                    } else {
                        hideValidationMessage(this, `errorCorreoEditar${employeeId}`);
                    }
                });
            }
        }

        // Validación de campos regulares
        fields.forEach(field => {
            const inputName = `${field.inputName}${isEditForm ? '_editar' : ''}`;
            const input = form.querySelector(`[name="${inputName}"]`);
            const errorId = isEditForm ? `${field.errorId}${employeeId}` : field.errorId;

            if (input) {
                input.addEventListener("input", function() {
                    if (!field.validate(input.value)) {
                        showValidationMessage(input, errorId, field.message);
                    } else {
                        hideValidationMessage(input, errorId);
                    }
                });
            }
        });

        // Validación al enviar el formulario
        form.addEventListener("submit", function(event) {
            let isValid = true;

            // Validar campos regulares
            fields.forEach(field => {
                const inputName = `${field.inputName}${isEditForm ? '_editar' : ''}`;
                const input = form.querySelector(`[name="${inputName}"]`);
                const errorId = isEditForm ? `${field.errorId}${employeeId}` : field.errorId;

                if (input && !field.validate(input.value)) {
                    isValid = false;
                    showValidationMessage(input, errorId, field.message);
                }
            });

            // Validar correo electrónico
            if (isEditForm) {
                const emailInput = form.querySelector(`#correo_persona_editar_${employeeId}`);
                if (emailInput && !isValidEmail(emailInput.value)) {
                    isValid = false;
                    showValidationMessage(emailInput, `errorCorreoEditar${employeeId}`, "El correo electrónico no es válido.");
                }
            }

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