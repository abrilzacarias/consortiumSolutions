document.addEventListener("DOMContentLoaded", function() {
    function containsNumbers(str) {
        return /\d/.test(str);
    }

    function showValidationMessage(inputElement, errorElementId, message) {
        const errorElement = document.getElementById(errorElementId);
        if (errorElement) {
            errorElement.textContent = message;
            errorElement.classList.remove('hidden');
            errorElement.style.display = 'block';
        }
    }

    function hideValidationMessage(errorElementId) {
        const errorElement = document.getElementById(errorElementId);
        if (errorElement) {
            errorElement.textContent = '';
            errorElement.classList.add('hidden');
            errorElement.style.display = 'none';
        }
    }

    function togglePrecioBaseInput(form) {
        const requierePagoSelect = form.querySelector('[name="requiere_pago"]');
        const precioBaseInput = form.querySelector('[name="precio_base_servicio"]');
        if (requierePagoSelect.value === '0') {
            precioBaseInput.disabled = true;
            precioBaseInput.value = '';
            hideValidationMessage(`errorPrecioBase_${form.id}`);
        } else {
            precioBaseInput.disabled = false;
        }
    }

    function validateNombreServicio(value, errorElementId) {
        if (value.length < 4 && containsNumbers(value)) {
            showValidationMessage(null, errorElementId, "El nombre del servicio debe tener al menos 4 caracteres y no puede contener números.");
            return false;
        } else if (value.length < 4) {
            showValidationMessage(null, errorElementId, "El nombre del servicio debe tener al menos 4 caracteres.");
            return false;
        } else if (containsNumbers(value)) {
            showValidationMessage(null, errorElementId, "El nombre del servicio no puede contener números.");
            return false;
        } else {
            hideValidationMessage(errorElementId);
            return true;
        }
    }

    function validatePrecioBase(value, errorElementId) {
        const precioValue = parseFloat(value.replace(',', '.'));
        if (isNaN(precioValue) || precioValue <= 0) {
            showValidationMessage(null, errorElementId, "Ingrese un precio base válido (debe ser mayor a cero).");
            return false;
        } else {
            hideValidationMessage(errorElementId);
            return true;
        }
    }

    function handleFormSubmit(event, isEditForm) {
        event.preventDefault();
        const form = event.target;
        let isValid = true;

        const nombreServicioInput = form.querySelector('[name="nombre_servicio"]');
        const nombreServicioValue = nombreServicioInput.value.trim();
        const errorNombreId = isEditForm ? `errorNombre_${form.id.replace('editServicioModal', '')}` : form.querySelector('[id^="errorNombre"]').id;
        
        if (!validateNombreServicio(nombreServicioValue, errorNombreId)) {
            isValid = false;
        }

        const precioBaseInput = form.querySelector('[name="precio_base_servicio"]');
        const requierePagoSelect = form.querySelector('[name="requiere_pago"]');
        const errorPrecioBaseId = `errorPrecioBase_${form.id.replace('editServicioModal', '')}`;
    
        if (requierePagoSelect.value === '1' && !precioBaseInput.disabled) {
            if (!validatePrecioBase(precioBaseInput.value, errorPrecioBaseId)) {
                isValid = false;
            }
        } else {
            hideValidationMessage(errorPrecioBaseId);
        }

        if (isValid) {
            form.submit();
        }
    }

    const agregarServicioForms = document.querySelectorAll('[id^="agregarServicioForm-"]');
    agregarServicioForms.forEach(form => {
        const nombreServicioInput = form.querySelector('[name="nombre_servicio"]');
        const precioBaseInput = form.querySelector('[name="precio_base_servicio"]');
        const requierePagoSelect = form.querySelector('[name="requiere_pago"]');
        const errorNombre = form.querySelector('[id^="errorNombre"]');
        const errorPrecioBase = form.querySelector('[id^="errorPrecioBase"]');

        togglePrecioBaseInput(form);
        requierePagoSelect.addEventListener('change', () => togglePrecioBaseInput(form));

        nombreServicioInput.addEventListener("input", function() {
            validateNombreServicio(this.value.trim(), errorNombre.id);
        });

        precioBaseInput.addEventListener("input", function() {
            if (!this.disabled) {
                validatePrecioBase(this.value.trim(), errorPrecioBase.id);
            }
        });

        form.addEventListener("submit", function(event) {
            handleFormSubmit(event, false);
        });
    });

    const editarServicioForms = document.querySelectorAll('form[id^="editServicioModal"]');
    editarServicioForms.forEach(function(editarServicioForm) {
        const servicioId = editarServicioForm.id.replace('editServicioModal', '');
        const nombreServicioInput = editarServicioForm.querySelector(`#nombre_servicio_${servicioId}`);
        const precioBaseInput = editarServicioForm.querySelector(`#precio_base_servicio`);
        const requierePagoSelect = editarServicioForm.querySelector('[name="requiere_pago"]');
        
        togglePrecioBaseInput(editarServicioForm);
        requierePagoSelect.addEventListener('change', () => togglePrecioBaseInput(editarServicioForm));

        nombreServicioInput.addEventListener("input", function() {
            validateNombreServicio(this.value.trim(), `errorNombre_${servicioId}`);
        });

        precioBaseInput.addEventListener("input", function() {
            if (!this.disabled) {
                validatePrecioBase(this.value.trim(), `errorPrecioBase_${servicioId}`);
            }
        });

        editarServicioForm.addEventListener("submit", function(event) {
            handleFormSubmit(event, true);
        });
    });
});
