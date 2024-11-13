document.addEventListener("DOMContentLoaded", function() {
    // Función para verificar si la cadena contiene números
    function containsNumbers(str) {
        return /\d/.test(str);
    }

    // Función para mostrar el mensaje de error
    function showValidationMessage(inputElement, errorElementId, message) {
        const errorElement = document.getElementById(errorElementId);
        if (errorElement) {
            errorElement.textContent = message;
            errorElement.classList.remove('hidden'); // Mostrar el mensaje
            console.log("Mensaje de error mostrado: " + message); // Añadido para verificar
        } else {
            console.log("No se encontró el elemento de error con id: " + errorElementId); // Añadido para depuración
        }
    }

    // Función para ocultar el mensaje de error
    function hideValidationMessage(inputElement, errorElementId) {
        const errorElement = document.getElementById(errorElementId);
        if (errorElement) {
            errorElement.textContent = '';
            errorElement.classList.add('hidden'); // Ocultar el mensaje
            console.log("Mensaje de error ocultado."); // Añadido para verificar
        } else {
            console.log("No se encontró el elemento de error con id: " + errorElementId); // Añadido para depuración
        }
    }


    // Función para habilitar/deshabilitar el campo precio
    function togglePrecioBaseInput() {
        const requierePagoSelect = document.querySelector('[name="requiere_pago"]');
        const precioBaseInput = document.querySelector('[name="precio_base_servicio"]');
        if (requierePagoSelect.value === '0') { // Si la opción "No" está seleccionada
            precioBaseInput.disabled = true;  // Deshabilitar el campo de precio
            precioBaseInput.value = '';  // Limpiar el valor
        } else {
            precioBaseInput.disabled = false;  // Habilitar el campo de precio
        }
    }
    // Validación para el formulario de agregar servicio
    const agregarServicioForms = document.querySelectorAll('[id^="agregarServicioForm-"]');
    agregarServicioForms.forEach(form => {
        const nombreServicioInput = form.querySelector('[name="nombre_servicio"]');
        const precioBaseInput = form.querySelector('[name="precio_base_servicio"]');
        const requierePagoSelect = form.querySelector('[name="requiere_pago"]');
        const errorNombre = form.querySelector('[id^="errorNombre"]');
        const errorPrecioBase = form.querySelector('[id^="errorPrecioBase"]');

        // Inicializar el estado del campo precio según la opción "requiere_pago"
        togglePrecioBaseInput();

        // Evento para verificar si el precio debe ser habilitado/deshabilitado
        requierePagoSelect.addEventListener('change', togglePrecioBaseInput);

        // Validación en tiempo real para el nombre del servicio
        nombreServicioInput.addEventListener("input", function() {
            const value = nombreServicioInput.value.trim();
            
            // Verificamos ambas condiciones: menos de 4 caracteres y contiene números
            if (value.length < 4 && containsNumbers(value)) {
                showValidationMessage(nombreServicioInput, errorNombre.id, "El nombre del servicio debe tener al menos 4 caracteres y no puede contener números.");
            } 
            // Si solo es menor a 4 caracteres
            else if (value.length < 4) {
                showValidationMessage(nombreServicioInput, errorNombre.id, "El nombre del servicio debe tener al menos 4 caracteres.");
            } 
            // Si contiene números
            else if (containsNumbers(value)) {
                showValidationMessage(nombreServicioInput, errorNombre.id, "El nombre del servicio no puede contener números.");
            } 
            // Si no hay errores, escondemos el mensaje
            else {
                hideValidationMessage(nombreServicioInput, errorNombre.id);
            }
        });
        
        // Validación en tiempo real para el precio base
        precioBaseInput.addEventListener("input", function() {
            const value = parseFloat(precioBaseInput.value.trim());
            if (!precioBaseInput.disabled && (isNaN(value) || value <= 0)) {
                showValidationMessage(precioBaseInput, errorPrecioBase.id, "Ingrese un precio base válido (debe ser mayor a cero).");
            } else {
                hideValidationMessage(precioBaseInput, errorPrecioBase.id);
            }
        });

        // Validación al enviar el formulario
        form.addEventListener("submit", function(event) {
            let isValid = true;

            // Validación del nombre del servicio
            const nombreServicioValue = nombreServicioInput.value.trim();
            if (nombreServicioValue.length < 4 || containsNumbers(nombreServicioValue)) {
                isValid = false;
                showValidationMessage(nombreServicioInput, errorNombre.id, "El nombre del servicio debe tener al menos 4 caracteres y no puede contener números.");
            } else {
                hideValidationMessage(nombreServicioInput, errorNombre.id);
            }

            // Validación del precio base solo si no está deshabilitado
            if (!precioBaseInput.disabled) {
                const precioBaseValue = parseFloat(precioBaseInput.value.trim());
                if (isNaN(precioBaseValue) || precioBaseValue <= 0) {
                    isValid = false;
                    showValidationMessage(precioBaseInput, errorPrecioBase.id, "Ingrese un precio base válido (debe ser mayor a cero).");
                } else {
                    hideValidationMessage(precioBaseInput, errorPrecioBase.id);
                }
            }

            if (!isValid) {
                event.preventDefault(); // Previene el envío si hay errores
            }
        });
    });
    // Seleccionar todos los formularios de edición de servicios
    const editarServicioForms = document.querySelectorAll('form[id^="editServicioModal"]');

    editarServicioForms.forEach(function(editarServicioForm) {
        const servicioId = editarServicioForm.id.replace('editServicioModal', '');
        console.log(servicioId);
        
        // Obtener los campos específicos para este formulario
        const nombreServicioInput = editarServicioForm.querySelector(`#nombre_servicio_${servicioId}`);
        const precioBaseInput = editarServicioForm.querySelector(`#precio_base_servicio`);
        const categoriaServicioSelect = editarServicioForm.querySelector(`#categoria_servicio`);
        
        // Validación al enviar el formulario
        editarServicioForm.addEventListener("submit", function(event) {
            let isValid = true;

            // Validación del nombre del servicio
            if (nombreServicioInput && nombreServicioInput.value.trim() === '') {
                isValid = false;
                showValidationMessage(nombreServicioInput, `errorNombre_${servicioId}`, "El nombre del servicio es obligatorio.");
            } else if (nombreServicioInput) {
                hideValidationMessage(nombreServicioInput, `errorNombre_${servicioId}`);
            }

            // Validación del precio base del servicio (debe ser un número positivo)
            if (precioBaseInput && (isNaN(precioBaseInput.value) || parseFloat(precioBaseInput.value) <= 0)) {
                isValid = false;
                showValidationMessage(precioBaseInput, `errorPrecioBase`, "El precio base debe ser un número positivo.");
            } else if (precioBaseInput) {
                hideValidationMessage(precioBaseInput, `errorPrecioBase`);
            }

            // Validación de la categoría del servicio
            if (categoriaServicioSelect && categoriaServicioSelect.value === '') {
                isValid = false;
                showValidationMessage(categoriaServicioSelect, `errorCategoria_${servicioId}`, "La categoría de servicio es obligatoria.");
            } else if (categoriaServicioSelect) {
                hideValidationMessage(categoriaServicioSelect, `errorCategoria_${servicioId}`);
            }

            // Prevenir el envío si hay errores
            if (!isValid) {
                event.preventDefault();
            }
        });

        // Imprimir el valor del campo cuando cambia
        // Validación en tiempo real para el nombre del servicio
        if (nombreServicioInput) {
            nombreServicioInput.addEventListener("input", function() {
                const value = this.value.trim();
                console.log("Valor del nombre del servicio:", value);
                
                // Verificamos ambas condiciones: menos de 4 caracteres y contiene números
                if (value.length < 4 && containsNumbers(value)) {
                    showValidationMessage(this, `errorNombre_${servicioId}`, "El nombre del servicio debe tener al menos 4 caracteres y no puede contener números.");
                } 
                // Si solo es menor a 4 caracteres
                else if (value.length < 4) {
                    showValidationMessage(this, `errorNombre_${servicioId}`, "El nombre del servicio debe tener al menos 4 caracteres.");
                } 
                // Si contiene números
                else if (containsNumbers(value)) {
                    showValidationMessage(this, `errorNombre_${servicioId}`, "El nombre del servicio no puede contener números.");
                } 
                // Si no hay errores, escondemos el mensaje
                else {
                    hideValidationMessage(this, `errorNombre_${servicioId}`);
                }
            });
        }

        if (precioBaseInput) {
            precioBaseInput.addEventListener("input", function() {
                if (isNaN(this.value) || parseFloat(this.value) <= 0) {
                    showValidationMessage(this, `errorPrecioBase`, "El precio base debe ser un número positivo.");
                } else {
                    hideValidationMessage(this, `errorPrecioBase`);
                }
            });
        }

        if (categoriaServicioSelect) {
            categoriaServicioSelect.addEventListener("change", function() {
                if (this.value === '') {
                    showValidationMessage(this, `errorCategoria_${servicioId}`, "La categoría de servicio es obligatoria.");
                } else {
                    hideValidationMessage(this, `errorCategoria_${servicioId}`);
                }
            });
        }
    });

});
