function verDetallesVenta(buttonElement) {
    const idVenta = buttonElement.getAttribute('data-id-venta');

    fetch(`/venta/${idVenta}`) // URL que devuelve los detalles de la venta
        .then(response => response.json())
        .then(data => {
            // Limpiar el contenido anterior del tbody
            const tbody = document.querySelector('#detalleVentaBody');
            tbody.innerHTML = '';

            // Verificar si hay detalles de venta
            if (Array.isArray(data) && data.length > 0) {
                data.forEach(detalle => {
                    // Crear una nueva fila para cada detalle
                    const row = document.createElement('tr');
                    row.classList.add('border-b');

                    // Agregar el contenido de cada celda de la fila
                    row.innerHTML = `
                        <td class="px-4 py-3">${detalle.nombre_metodo_pago || 'No disponible'}</td>
                        <td class="px-4 py-3">${detalle.nombre_servicio || 'No disponible'}</td>
                        <td class="px-4 py-3">${detalle.cantidad_detalle_venta || 'No disponible'}</td>
                        <td class="px-4 py-3">${detalle.precio || 'No disponible'}</td>
                        <td class="px-4 py-3">${detalle.costo_extra_detalle_venta || 'No disponible'}</td>
                        <td class="px-4 py-3">${detalle.descripcion_estado_venta || 'No disponible'}</td>
                    `;

                    // Agregar la fila al tbody
                    tbody.appendChild(row);
                });
            } else {
                tbody.innerHTML = '<tr><td colspan="6" class="px-4 py-3 text-center">No se encontraron detalles para esta venta.</td></tr>';
            }

            // Mostrar el modal
            const modal = document.querySelector('#verVentaModal');
            if (modal) {
                modal.classList.remove('hidden');
            }
        })
        .catch(error => {
            console.error('Error al obtener los detalles:', error);
        });
}

$(document).ready(function() {
    // Inicializar select2 para el estado de venta
    $('#estado_venta').select2({
        placeholder: 'Seleccione un estado',
        width: '100%',
        minimumInputLength: 0
    });

    // Función para abrir el modal con datos precargados
    function abrirModalEditarEstadoVenta(idVenta, estadoActual) {
        $('#id_venta_editar').val(idVenta);
        $('#estado_venta').val(estadoActual).trigger('change');
        $('#editarEstadoVentaModal').removeClass('hidden');
    }

    // Manejo de cierre del modal
    $('[data-modal-toggle="editarEstadoVentaModal"]').on('click', function() {
        $('#editarEstadoVentaModal').addClass('hidden');
    });
});

