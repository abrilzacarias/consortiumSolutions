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
    }

    function hideValidationMessage(input) {
        let errorElement = input.nextElementSibling;
        if (errorElement && errorElement.classList.contains("invalid-feedback")) {
            errorElement.remove();
        }
        input.classList.remove("is-invalid");
    }

    // Validación para el formulario de agregar cliente
    const agregarForm = document.querySelector("#agregarClienteForm");
    if (agregarForm) {
        const nombreInput = document.querySelector("#nombre_cliente");
        const apellidoInput = document.querySelector("#apellido_cliente");
        const cuilInput = document.querySelector("#cuitl_cliente");
        const claveInput = document.querySelector("#clave_afgip_cliente");
        const vencimientoMatriculaInput = document.querySelector("#vencimiento_matricula");
        const matriculaInput =  document.querySelector("#matricula_cliente");
        const today = new Date().toISOString().split('T')[0];
        vencimientoMatriculaInput.min = today;

        agregarForm.addEventListener("submit", function(event) {
            let isValid = true;
            if (containsNumbers(nombreInput.value)) {
                isValid = false;
                showValidationMessage(nombreInput, "El nombre no puede contener números.");
            } else {
                hideValidationMessage(nombreInput);
            }
        
            if (containsNumbers(apellidoInput.value)) {
                isValid = false;
                showValidationMessage(apellidoInput, "El apellido no puede contener números.");
            } else {
                hideValidationMessage(apellidoInput);
            }
        
            if (cuilInput.value.length !== 11 || isNaN(cuilInput.value)) {
                isValid = false;
                showValidationMessage(cuilInput, "El CUIL/CUIT debe tener exactamente 11 dígitos y no puede contener letras.");
            } else {
                hideValidationMessage(cuilInput);
            }
            
            if (claveInput.value.length !== 8 || isNaN(claveInput.value)) {
                isValid = false;
                showValidationMessage(claveInput, "La clave AFIP/AGIP debe tener exactamente 8 dígitos y no puede contener letras.");
            } else {
                hideValidationMessage(claveInput);
            }
            
            if (matriculaInput.value.length !== 6 || isNaN(matriculaInput.value)) { 
                isValid = false;
                showValidationMessage(matriculaInput, "La matricula debe tener exactamente 6 dígitos y no puede contener letras.");
            } else {
                hideValidationMessage(matriculaInput);
            }

            if (!isValid) {
                event.preventDefault();
            }
        });

        nombreInput.addEventListener("input", function() {
            if (containsNumbers(nombreInput.value)) {
                showValidationMessage(nombreInput, "El nombre no puede contener números.");
            } else {
                hideValidationMessage(nombreInput);
            }
        });
    
        apellidoInput.addEventListener("input", function() {
            if (containsNumbers(apellidoInput.value)) {
                showValidationMessage(apellidoInput, "El apellido no puede contener números.");
            } else {
                hideValidationMessage(apellidoInput);
            }
        });
    
        cuilInput.addEventListener("input", function() {
            if (cuilInput.value.length !== 11 || isNaN(cuilInput.value)) {
                showValidationMessage(cuilInput, "El CUIL/CUIT debe tener exactamente 11 dígitos y no puede contener letras.");
            } else {
                hideValidationMessage(cuilInput);
            }
        });
    
        claveInput.addEventListener("input", function() {
            if (claveInput.value.length !== 8 || isNaN(claveInput.value)) {
                showValidationMessage(claveInput, "La clave AFIP/AGIP debe tener exactamente 8 dígitos y no puede contener letras.");
            } else {
                hideValidationMessage(claveInput);
            }
        });

        matriculaInput.addEventListener("input", function() {
            if (matriculaInput.value.length !== 6 || isNaN(matriculaInput.value)) { 
                showValidationMessage(matriculaInput, "La matricula debe tener exactamente 6 dígitos y no puede contener letras.");
            } else {
                hideValidationMessage(matriculaInput);
            }
        });
    } else {
        console.error("No se encontró el formulario con el id 'agregarClienteForm'");
    }

    // Validación para el formulario de editar cliente
    const editarForm = document.querySelector("#editarClienteForm");
    if (editarForm) {
        const nombreInputEditar = document.querySelector("#nombre_persona");
        const apellidoInputEditar = document.querySelector("#apellido_persona");
        const cuilInputEditar = document.querySelector("#cuitl_persona");
        const claveInputEditar = document.querySelector("#clave_afgip_cliente");
        const matriculaInputEditar = document.querySelector("#matricula_cliente");
        const vencimientoMatriculaEditar = document.querySelector("#vencimiento_matricula");
        const today = new Date().toISOString().split('T')[0];
        vencimientoMatriculaEditar.min = today;
        
        editarForm.addEventListener("submit", function(event) {
            let isValid = true;

            if (containsNumbers(nombreInputEditar.value)) {
                isValid = false;
                showValidationMessage(nombreInputEditar, "El nombre no puede contener números.");
            } else {
                hideValidationMessage(nombreInputEditar);
            }

            if (containsNumbers(apellidoInputEditar.value)) {
                isValid = false;
                showValidationMessage(apellidoInputEditar, "El apellido no puede contener números.");
            } else {
                hideValidationMessage(apellidoInputEditar);
            }

            if (cuilInputEditar.value.length !== 11 || isNaN(cuilInputEditar.value)) {
                isValid = false;
                showValidationMessage(cuilInputEditar, "El CUIL/CUIT debe tener exactamente 11 dígitos y no puede contener letras.");
            } else {
                hideValidationMessage(cuilInputEditar);
            }

            if (claveInputEditar.value.length !== 8 || isNaN(claveInputEditar.value)) {
                isValid = false;
                showValidationMessage(claveInputEditar, "La clave AFIP/AGIP debe tener exactamente 8 dígitos y no puede contener letras.");
            } else {
                hideValidationMessage(claveInputEditar);
            }

            if (matriculaInputEditar.value.length !== 6 || isNaN(matriculaInputEditar.value)) { 
                isValid = false;
                showValidationMessage(matriculaInputEditar, "La matricula debe tener exactamente 6 dígitos y no puede contener letras.");
            } else {
                hideValidationMessage(matriculaInputEditar);
            }

            if (!isValid) {
                event.preventDefault();
            }
        });

        nombreInputEditar.addEventListener("input", function() {
            if (containsNumbers(nombreInputEditar.value)) {
                showValidationMessage(nombreInputEditar, "El nombre no puede contener números.");
            } else {
                hideValidationMessage(nombreInputEditar);
            }
        });

        apellidoInputEditar.addEventListener("input", function() {
            if (containsNumbers(apellidoInputEditar.value)) {
                showValidationMessage(apellidoInputEditar, "El apellido no puede contener números.");
            } else {
                hideValidationMessage(apellidoInputEditar);
            }
        });

        cuilInputEditar.addEventListener("input", function() {
            if (cuilInputEditar.value.length !== 11 || isNaN(cuilInputEditar.value)) {
                showValidationMessage(cuilInputEditar, "El CUIL/CUIT debe tener exactamente 11 dígitos y no puede contener letras.");
            } else {
                hideValidationMessage(cuilInputEditar);
            }
        });

        claveInputEditar.addEventListener("input", function() {
            if (claveInputEditar.value.length !== 8 || isNaN(claveInputEditar.value)) {
                showValidationMessage(claveInputEditar, "La clave AFIP/AGIP debe tener exactamente 8 dígitos y no puede contener letras.");
            } else {
                hideValidationMessage(claveInputEditar);
            }
        });

        matriculaInputEditar.addEventListener("input", function() {
            if (matriculaInputEditar.value.length !== 6 || isNaN(matriculaInputEditar.value)) { 
                showValidationMessage(matriculaInputEditar, "La matricula debe tener exactamente 6 dígitos y no puede contener letras.");
            } else {
                hideValidationMessage(matriculaInputEditar);
            }
        });
    } else {
        console.error("No se encontró el formulario con el id 'editarClienteForm'");
    }
});
