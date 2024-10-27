document.addEventListener("DOMContentLoaded", function() {
    function containsNumbers(str) {
        return /\d/.test(str);
    }

    function showValidationMessage(input, message) {
        let errorElement = input.nextElementSibling;
        if (!errorElement || !errorElement.classList.contains("invalid-feedback")) {
            errorElement = document.createElement("div");
            errorElement.className = "invalid-feedback";
            input.parentNode.appendChild(errorElement);
        }
        errorElement.textContent = message;
        input.classList.add("is-invalid");
        console.log(`Validation failed for ${input.id}: ${message}`);
    }

    function hideValidationMessage(input) {
        let errorElement = input.nextElementSibling;
        if (errorElement && errorElement.classList.contains("invalid-feedback")) {
            errorElement.remove();
        }
        input.classList.remove("is-invalid");
        console.log(`Validation passed for ${input.id}`);
    }

    const agregarForm = document.querySelector("#agregarClienteForm");
    if (agregarForm) {
        const nombreInput = document.querySelector("#nombre_cliente");
        const apellidoInput = document.querySelector("#apellido_cliente");
        const cuilInput = document.querySelector("#cuitl_cliente");
        const claveInput = document.querySelector("#clave_afgip_cliente");
        const matriculaInput = document.querySelector("#matricula_cliente");

        // Asigna un evento "input" a cada campo para la validación en tiempo real
        nombreInput.addEventListener("input", function() {
            console.log("Nombre input:", nombreInput.value); // Log para verificar el evento en tiempo real
            if (containsNumbers(nombreInput.value)) {
                showValidationMessage(nombreInput, "El nombre no puede contener números.");
            } else {
                hideValidationMessage(nombreInput);
            }
        });

        apellidoInput.addEventListener("input", function() {
            console.log("Apellido input:", apellidoInput.value); // Log para verificar el evento en tiempo real
            if (containsNumbers(apellidoInput.value)) {
                showValidationMessage(apellidoInput, "El apellido no puede contener números.");
            } else {
                hideValidationMessage(apellidoInput);
            }
        });

        cuilInput.addEventListener("input", function() {
            console.log("CUIL/CUIT input:", cuilInput.value); // Log para verificar el evento en tiempo real
            if (cuilInput.value.length !== 11 || isNaN(cuilInput.value)) {
                showValidationMessage(cuilInput, "El CUIL/CUIT debe tener exactamente 11 dígitos y no puede contener letras.");
            } else {
                hideValidationMessage(cuilInput);
            }
        });

        claveInput.addEventListener("input", function() {
            console.log("Clave input:", claveInput.value); // Log para verificar el evento en tiempo real
            if (claveInput.value.length !== 8 || isNaN(claveInput.value)) {
                showValidationMessage(claveInput, "La clave AFIP/AGIP debe tener exactamente 8 dígitos y no puede contener letras.");
            } else {
                hideValidationMessage(claveInput);
            }
        });

        matriculaInput.addEventListener("input", function() {
            console.log("Matrícula input:", matriculaInput.value); // Log para verificar el evento en tiempo real
            if (matriculaInput.value.length !== 6 || isNaN(matriculaInput.value)) {
                showValidationMessage(matriculaInput, "La matrícula debe tener exactamente 6 dígitos y no puede contener letras.");
            } else {
                hideValidationMessage(matriculaInput);
            }
        });
    }
});
