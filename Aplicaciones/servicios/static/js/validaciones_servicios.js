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
<<<<<<< HEAD
=======
        console.log(`Validation message shown: ${message}`);
    }

    function hideValidationMessage(input) {
        let errorElement = input.nextElementSibling;
        if (errorElement && errorElement.classList.contains("invalid-feedback")) {
            errorElement.remove();
        }
        input.classList.remove("is-invalid");
        console.log("Validation message hidden");
    }

    const agregarForm = document.querySelector("#agregarCategoriaForm");
    if (agregarForm) {
        const categoriaInputAgregar = document.querySelector("#categoria"); 
        console.log("Agregar form found");

        agregarForm.addEventListener("submit", function(event) {
            console.log("Agregar form submit event");

            let isValid = true;

            if (containsNumbers(categoriaInputAgregar.value)) {
                isValid = false;
                showValidationMessage(categoriaInputAgregar, "El nombre de la categoría no puede contener números.");
            } else {
                hideValidationMessage(categoriaInputAgregar);
            }

            if (!isValid) {
                event.preventDefault();
                console.log("Form submission prevented due to validation errors");
            }
        });

        categoriaInputAgregar.addEventListener("input", function() {
            if (containsNumbers(categoriaInputAgregar.value)) {
                showValidationMessage(categoriaInputAgregar, "El nombre de la categoría no puede contener números.");
            } else {
                hideValidationMessage(categoriaInputAgregar);
            }
        });
    }
});

document.addEventListener("DOMContentLoaded", function() {
    const nombreServicioInput = document.querySelector("#nombre_servicio");
    const precioBaseInput = document.querySelector("#precio_base_agregar");

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
>>>>>>> d53db1686a5aaa6cc42bddccc8f232efe52407f8
    }

    function hideValidationMessage(input) {
        let errorElement = input.nextElementSibling;
        if (errorElement && errorElement.classList.contains("invalid-feedback")) {
            errorElement.remove();
        }
        input.classList.remove("is-invalid");
    }

<<<<<<< HEAD
    // Validación para el formulario de agregar servicio
    const agregarServicioForm = document.querySelector("#agregarServicioForm");
    if (agregarServicioForm) {
        const nombreServicioInput = document.querySelector("#nombre_servicio");
        const precioBaseInput = document.querySelector("#precio_base_agregar");

=======
    // Validación para el formulario de agregar
    const agregarServicioForm = document.querySelector("#agregarServicioForm");
    if (agregarServicioForm) {
>>>>>>> d53db1686a5aaa6cc42bddccc8f232efe52407f8
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
<<<<<<< HEAD
            if (isNaN(value) || value < 0) {
=======
            if (isNaN(value) || value <= 0) {
>>>>>>> d53db1686a5aaa6cc42bddccc8f232efe52407f8
                showValidationMessage(precioBaseInput, "Ingrese un precio base válido.");
            } else {
                hideValidationMessage(precioBaseInput);
            }
        });
    }

<<<<<<< HEAD
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
=======
    const nombreServicioInputEditar = document.querySelector("#nombre_servicio_editar");

    // Validación para el formulario de editar
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
});

>>>>>>> d53db1686a5aaa6cc42bddccc8f232efe52407f8
