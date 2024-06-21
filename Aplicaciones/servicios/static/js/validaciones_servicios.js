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

    // Validación para el formulario de agregar servicio
    const agregarServicioForm = document.querySelector("#agregarServicioForm");
    if (agregarServicioForm) {
        const nombreServicioInput = document.querySelector("#nombre_servicio");
        const precioBaseInput = document.querySelector("#precio_base_agregar");

        nombreServicioInput.addEventListener("input", function() {
            const value = nombreServicioInput.value.trim();
            if (value.length < 4) {
                showValidationMessage(nombreServicioInput, "El nombre del servicio debe tener al menos 4 caracteres.");
            } else if (containsNumbers(value)) {
                showValidationMessage(nombreServicioInput, "El nombre del servicio no puede contener números.");
            } else {
                hideValidationMessage(nombreServicioInput);
            }
        });

        precioBaseInput.addEventListener("input", function() {
            const value = parseFloat(precioBaseInput.value.trim());
            if (isNaN(value) || value < 0) {
                showValidationMessage(precioBaseInput, "Ingrese un precio base válido.");
            } else {
                hideValidationMessage(precioBaseInput);
            }
        });
    }

    // Asociar validaciones cuando se muestra el modal de editar servicio
    document.querySelectorAll('.modal').forEach(modal => {
        modal.addEventListener('shown.bs.modal', function() {
            const editarServicioForm = modal.querySelector("#editarServicioForm");
            if (editarServicioForm) {
                const nombreServicioInputEditar = modal.querySelector("#nombre_servicio_editar");
                const precioBaseInputEditar = modal.querySelector("#precio_base_editar");

                if (nombreServicioInputEditar) {
                    nombreServicioInputEditar.addEventListener("input", function() {
                        const value = nombreServicioInputEditar.value.trim();
                        if (value.length < 4) {
                            showValidationMessage(nombreServicioInputEditar, "El nombre del servicio debe tener al menos 4 caracteres.");
                        } else if (containsNumbers(value)) {
                            showValidationMessage(nombreServicioInputEditar, "El nombre del servicio no puede contener números.");
                        } else {
                            hideValidationMessage(nombreServicioInputEditar);
                        }
                    });
                }

                if (precioBaseInputEditar) {
                    precioBaseInputEditar.addEventListener("input", function() {
                        const value = parseFloat(precioBaseInputEditar.value.trim());
                        if (isNaN(value) || value < 0) {
                            showValidationMessage(precioBaseInputEditar, "Ingrese un precio base válido.");
                        } else {
                            hideValidationMessage(precioBaseInputEditar);
                        }
                    });
                }

                editarServicioForm.addEventListener("submit", function(event) {
                    let isValid = true;

                    const nombreValue = nombreServicioInputEditar.value.trim();
                    if (nombreValue.length < 4 || containsNumbers(nombreValue)) {
                        isValid = false;
                        showValidationMessage(nombreServicioInputEditar, "El nombre del servicio debe tener al menos 4 caracteres y no puede contener números.");
                    } else {
                        hideValidationMessage(nombreServicioInputEditar);
                    }

                    const precioValue = parseFloat(precioBaseInputEditar.value.trim());
                    if (isNaN(precioValue) || precioValue < 0) {
                        isValid = false;
                        showValidationMessage(precioBaseInputEditar, "Ingrese un precio base válido.");
                    } else {
                        hideValidationMessage(precioBaseInputEditar);
                    }

                    if (!isValid) {
                        event.preventDefault();
                    }
                });
            }
        });
    });
});
