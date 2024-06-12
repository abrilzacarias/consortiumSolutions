document.addEventListener('DOMContentLoaded', function() {
    function setupToggle(selectId, inputId) {
        var selectElement = document.getElementById(selectId);
        var inputElement = document.getElementById(inputId);

        selectElement.addEventListener('change', function() {
            if (this.value === '1') {
                inputElement.removeAttribute('disabled');
            } else {
                inputElement.setAttribute('disabled', 'disabled');
            }
        });
        if (selectElement.value === '1') {
            inputElement.removeAttribute('disabled');
        } else {
            inputElement.setAttribute('disabled', 'disabled');
        }
    }

    setupToggle('requiere_pago_agregar', 'precio_base_agregar');
    setupToggle('requiere_pago_editar', 'precio_base_editar');
});
