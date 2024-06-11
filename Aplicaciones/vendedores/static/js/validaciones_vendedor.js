document.addEventListener("DOMContentLoaded", function() {
    console.log("Document is ready");

    // Función para validar si un string contiene números
    function containsNumbers(str) {
        return /\d/.test(str);
    }

    // Función para mostrar un mensaje de validación
    function showValidationMessage(input, message) {
        let errorElement = input.nextElementSibling;
        if (!errorElement || !errorElement.classList.contains("invalid-feedback")) {
            errorElement = document.createElement("div");
            errorElement.className = "invalid-feedback";
            input.parentNode.appendChild(errorElement);
        }
        errorElement.textContent = message;
        input.classList.add("is-invalid");
        console.log(`Validation message shown: ${message}`);
    }

    // Función para ocultar un mensaje de validación
    function hideValidationMessage(input) {
        let errorElement = input.nextElementSibling;
        if (errorElement && errorElement.classList.contains("invalid-feedback")) {
            errorElement.remove();
        }
        input.classList.remove("is-invalid");
        console.log("Validation message hidden");
    }

    // Agregar Vendedor
    const agregarForm = document.querySelector("#agregarVendedorForm");
    if (agregarForm) {
        console.log("Agregar form found");

        const nombreInputAgregar = document.querySelector("#nombre_persona");
        const apellidoInputAgregar = document.querySelector("#apellido_persona");
        const cuilInputAgregar = document.querySelector("#cuitl_persona");

        agregarForm.addEventListener("submit", function(event) {
            console.log("Agregar form submit event");

            let isValid = true;

            if (containsNumbers(nombreInputAgregar.value)) {
                isValid = false;
                showValidationMessage(nombreInputAgregar, "El nombre no puede contener números.");
            } else {
                hideValidationMessage(nombreInputAgregar);
            }

            if (containsNumbers(apellidoInputAgregar.value)) {
                isValid = false;
                showValidationMessage(apellidoInputAgregar, "El apellido no puede contener números.");
            } else {
                hideValidationMessage(apellidoInputAgregar);
            }

            const cuilValue = cuilInputAgregar.value;
            if (cuilValue.length !== 11 || isNaN(cuilValue)) {
                isValid = false;
                showValidationMessage(cuilInputAgregar, "El CUIL/CUIT debe tener exactamente 11 dígitos y no puede contener letras.");
            } else {
                hideValidationMessage(cuilInputAgregar);
            }

            if (!isValid) {
                event.preventDefault();
                console.log("Form submission prevented due to validation errors");
            }
        });

        nombreInputAgregar.addEventListener("input", function() {
            if (containsNumbers(nombreInputAgregar.value)) {
                showValidationMessage(nombreInputAgregar, "El nombre no puede contener números.");
            } else {
                hideValidationMessage(nombreInputAgregar);
            }
        });

        apellidoInputAgregar.addEventListener("input", function() {
            if (containsNumbers(apellidoInputAgregar.value)) {
                showValidationMessage(apellidoInputAgregar, "El apellido no puede contener números.");
            } else {
                hideValidationMessage(apellidoInputAgregar);
            }
        });

        cuilInputAgregar.addEventListener("input", function() {
            const cuilValue = cuilInputAgregar.value;
            if (cuilValue.length !== 11 || isNaN(cuilValue)) {
                showValidationMessage(cuilInputAgregar, "El CUIL/CUIT debe tener exactamente 11 dígitos y no puede contener letras.");
            } else {
                hideValidationMessage(cuilInputAgregar);
            }
        });
    }

       
    // Editar Vendedor
    document.querySelectorAll('.editarVendedorModal').forEach(modal => {
        modal.addEventListener('shown.bs.modal', function() {
            const id = modal.getAttribute('id').replace('editarVendedorModal', '');
            const editarForm = document.querySelector(`#editarVendedorForm${id}`);
            const nombreInputEditar = document.querySelector(`#nombre_persona_editar_${id}`);
            const apellidoInputEditar = document.querySelector(`#apellido_persona_editar_${id}`);
            const cuilInputEditar = document.querySelector(`#cuitl_persona_editar_${id}`);

            if (editarForm) {
                console.log(`Editar form found for vendedor id: ${id}`);

                editarForm.addEventListener("submit", function(event) {
                    console.log(`Editar form submit event for vendedor id: ${id}`);

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

                    const cuilValue = cuilInputEditar.value;
                    if (cuilValue.length !== 11 || isNaN(cuilValue)) {
                        isValid = false;
                        showValidationMessage(cuilInputEditar, "El CUIL/CUIT debe tener exactamente 11 dígitos y no puede contener letras.");
                    } else {
                        hideValidationMessage(cuilInputEditar);
                    }

                    if (!isValid) {
                        event.preventDefault();
                        console.log(`Form submission prevented for vendedor id: ${id} due to validation errors`);
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
                    const cuilValue = cuilInputEditar.value;
                    if (cuilValue.length !== 11 || isNaN(cuilValue)) {
                        showValidationMessage(cuilInputEditar, "El CUIL/CUIT debe tener exactamente 11 dígitos y no puede contener letras.");
                    } else {
                        hideValidationMessage(cuilInputEditar);
                    }
                });
            }
        });
    });
});