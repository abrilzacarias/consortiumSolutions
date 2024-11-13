document.addEventListener('DOMContentLoaded', function() {
    function setupToggle(selectId, inputId) {
        var selectElement = document.getElementById(selectId);
        var inputElement = document.getElementById(inputId);

        function togglePrecioBase() {
            if (selectElement.value === '1') {
                inputElement.removeAttribute('disabled');
            } else {
                inputElement.setAttribute('disabled', 'disabled');
                inputElement.value = ''; // Limpiar el valor cuando se deshabilita
            }
        }

        selectElement.addEventListener('change', togglePrecioBase);
        togglePrecioBase(); // Llamar a togglePrecioBase inicialmente para establecer el estado correcto
    }

    // Configuración para el formulario de agregar
    setupToggle('requiere_pago_agregar', 'precio_base_agregar');

    // Configuración para el formulario de editar
    document.querySelectorAll('.modal').forEach(modal => {
        modal.addEventListener('shown.bs.modal', function() {
            const editarServicioForm = modal.querySelector("#editarServicioForm");
            if (editarServicioForm) {
                const requierePagoSelectEditar = modal.querySelector("#requiere_pago_editar");
                const precioBaseInputEditar = modal.querySelector("#precio_base_editar");

                function togglePrecioBaseEditar() {
                    if (requierePagoSelectEditar.value === '1') {
                        precioBaseInputEditar.removeAttribute('disabled');
                    } else {
                        precioBaseInputEditar.setAttribute('disabled', 'disabled');
                        precioBaseInputEditar.value = ''; // Limpiar el valor cuando se deshabilita
                    }
                }

                requierePagoSelectEditar.addEventListener('change', togglePrecioBaseEditar);
                togglePrecioBaseEditar(); // Llamar inicialmente para establecer el estado correcto
            }
        });
    });
});
