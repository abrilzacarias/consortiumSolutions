function detallesPresupuesto(buttonElement) {
    const idPresupuesto = buttonElement.getAttribute('data-id-presupuesto');

    fetch(`presupuesto/${idPresupuesto}`)
    .then(response => response.json())
    .then(data => {
        console.log('Datos recibidos:', data); // Verifica los datos recibidos

        // Limpiar el contenido previo de la tabla
        const tbody = document.querySelector('#detalleBody');
        tbody.innerHTML = '';

        if (Array.isArray(data) && data.length > 0) {
            data.forEach(detalle => {
                // Crear una nueva fila
                const row = document.createElement('tr');
                row.classList.add('border-b');

                // Agregar las celdas a la fila
                row.innerHTML = `
                    <td class="px-4 py-3">${detalle.nombre_servicio || 'No disponible'}</td>
                    <td class="px-4 py-3">${detalle.cantidad_detalle_presupuesto || 'No disponible'}</td>
                    <td class="px-4 py-3">${detalle.precio_unitario_detalle_presupuesto || 'No disponible'}</td>
                    <td class="px-4 py-3">${detalle.precio_total_detalle_presupuesto || 'No disponible'}</td>
                `;

                // Agregar la fila al tbody
                tbody.appendChild(row);
            });
        } else {
            tbody.innerHTML = '<tr><td colspan="4" class="px-4 py-3 text-center">No se encontraron detalles para este presupuesto.</td></tr>';
        }

        // Mostrar el modal
        const modal = document.querySelector('#readProductModal');
        if (modal) {
            modal.classList.remove('hidden');
        }
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });
}

// Función para abrir el modal y cargar los datos
function agregarPresupuestoModal() {
    // Llamada a los vendedores
    fetch('/vendedores')
        .then(response => response.json())
        .then(data => {
            let vendedorSelect = document.getElementById('vendedor_asignado');
            vendedorSelect.innerHTML = ''; // Limpiar el select antes de agregar opciones
            data.forEach(vendedor => {
                let option = document.createElement('option');
                option.value = vendedor.id_vendedor;
                option.textContent = `${vendedor.nombre_persona} ${vendedor.apellido_persona}`;
                vendedorSelect.appendChild(option);
            });
        })
        .catch(error => console.error('Error fetching vendedores:', error));

    // Llamada a los servicios
    fetch('/servicios')
        .then(response => response.json())
        .then(data => {
            let servicioSelect = document.getElementById('servicio_asignado');
            servicioSelect.innerHTML = ''; // Limpiar el select antes de agregar opciones
            data.forEach(servicio => {
                let option = document.createElement('option');
                option.value = servicio.id_servicio;
                option.textContent = servicio.nombre_servicio;
                servicioSelect.appendChild(option);
            });
        })
        .catch(error => console.error('Error fetching servicios:', error));
}
