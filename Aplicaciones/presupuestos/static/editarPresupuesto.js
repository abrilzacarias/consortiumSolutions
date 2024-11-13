function fetchVendedores() {
    return fetch('/presupuestos/vendedores/')
        .then(response => response.json())
        .catch(error => console.error('Error fetching vendedores:', error));
}

function fetchClientes() {
    return fetch('/presupuestos/clientes/')
        .then(response => response.json())
        .catch(error => console.error('Error fetching clientes:', error));
}

function fetchEdificios(clienteId) {
    return fetch(`/presupuestos/edificios/${clienteId}/`)
        .then(response => response.json())
        .catch(error => console.error('Error fetching edificios:', error));
}

function fetchServicios() {
    return fetch('/presupuestos/servicios')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Servicios fetched:', data); // Agrega este console.log para verificar los datos
            return data;
        })
        .catch(error => console.error('Error fetching servicios:', error));
}


function initializeSelect2Editar(selector, data, formatter) {
    $(selector).select2({
        data: data.map(formatter),
        placeholder: 'Selecciona una opción', // Puedes personalizar el placeholder
        minimumInputLength: 0, // Opcional: Número mínimo de caracteres para activar la búsqueda
        allowClear: true, // Opcional: Permite limpiar la selección
        width: '100%', // Opcional: Ancho del select
    });
}

// Función para crear un nuevo campo de servicio
function addNewService(servicios) {
    console.log("Servicios disponibles para agregar:", servicios); // Verificar servicios disponibles
    const serviciosContainer = document.getElementById('serviciosContainerEditar');

    // Obtener servicios ya seleccionados para evitar duplicados
    const serviciosSeleccionados = Array.from(document.querySelectorAll('select[name="servicios_editar[]"]'))
        .map(select => select.value);

    const nuevoServicio = document.createElement('div');
    nuevoServicio.className = 'flex items-center space-x-2 w-full';
    nuevoServicio.innerHTML = `
        <div class="w-1/3">
            <input type="hidden" name="id_detalles_editar[]" value="${null}">
            <select name="servicios_editar[]" class="select2 service-dropdown-editar w-full text-sm rounded-lg bg-gray-700 border-gray-600 text-white" data-precio="" required>
                ${Object.values(servicios).map(servicio => {
                    // Si el servicio ya fue seleccionado, no incluirlo en el select
                    if (serviciosSeleccionados.includes(servicio.id.toString())) {
                        return '';
                    }
                    console.log("Generando opción para servicio:", servicio); // Verificar cada servicio
                    return `
                        <option value="${servicio.id}" data-precio="${servicio.precio}">
                            ${servicio.nombre} - $${servicio.precio}
                        </option>
                    `;
                }).join('')}
            </select>
        </div>
        <div class="w-1/6">
            <input name="cantidades_editar[]" type="number" class="quantity-service-editar w-full text-sm rounded-lg bg-gray-700 border-gray-600 text-white" value="1" min="1">
        </div>
        <div class="w-1/5">
            <input name="costos_extra_editar[]" type="number" class="extra-cost-editar w-full text-sm rounded-lg bg-gray-700 border-gray-600 text-white" value="0" min="0">
        </div>
        <div class="w-1/5">
            <span name="subtotales_editar[]" class="subtotal-service-editar text-sm text-white">Subtotal: $0.00</span>
            <input name="subtotales_editar[]" type="hidden" class="subtotal-service-value-editar" value="0.00">
        </div>
        <div class="w-auto">
            <button type="button" class="flex-shrink-0 px-3 py-2 text-sm font-medium text-white bg-red-800 rounded-lg hover:bg-red-400 remove-service-btn-editar">-</button>
        </div>
    `;

    serviciosContainer.appendChild(nuevoServicio);

    // Inicializar select2 para el nuevo dropdown creado
    $(nuevoServicio.querySelector('.select2')).select2();

    // Añadir eventos para recalcular el total cuando cambie algún valor
    $(nuevoServicio).on('change', 'select, input', calcularTotalEditar);

    nuevoServicio.querySelector('.remove-service-btn-editar').addEventListener('click', function() {
        nuevoServicio.remove();
        calcularTotalEditar();
    });

    // Recalcular el total inicial
    calcularTotalEditar();
}

// Función para configurar los manejadores de eventos una sola vez
function setupGlobalHandlers() {
    document.addEventListener('click', function(event) {
        if (event.target && event.target.id === 'addServiceBtnEditar') {
            console.log('Add New Service Button Clicked');
            fetchServicios().then(servicios => {
                const serviciosMap = servicios.reduce((map, categoria) => {
                    categoria.servicios.forEach(servicio => {
                        map[servicio.id] = servicio;
                    });
                    return map;
                }, {});
                addNewService(serviciosMap);
            });
        }
    });
}

// Llama a esta función una sola vez al cargar la página
setupGlobalHandlers();

function setupEditPresupuestoHandlers(buttonElement) {
    const idPresupuesto = buttonElement.getAttribute('data-id-presupuesto-editar');
    document.getElementById('id_presupuesto_editar').value = idPresupuesto;
    fetch(`/presupuestos/obtenerPresupuesto/${idPresupuesto}/`)
        .then(response => response.json())
        .then(data => {
            // Realiza las solicitudes de datos
            return Promise.all([fetchVendedores(), fetchClientes(), fetchEdificios(data.presupuesto.id_cliente), fetchServicios()])
                .then(([vendedores, clientes, edificios, servicios]) => {
                    // Inicializa Select2 para cada selector
                    initializeSelect2Editar('#vendedor_asignado_editar', vendedores, vendedorFormatter);
                    initializeSelect2Editar('#cliente_asignado_editar', clientes, clienteFormatter);
                    initializeSelect2Editar('#edificio_asignado_editar', edificios, edificioFormatter);

                    // Asigna los valores a los selects después de la inicialización
                    $('#vendedor_asignado_editar').val(data.presupuesto.id_vendedor).trigger('change');
                    $('#cliente_asignado_editar').val(data.presupuesto.id_cliente).trigger('change');
                    $('#edificio_asignado_editar').val(data.presupuesto.id_edificio).trigger('change');

                    const serviciosContainer = document.getElementById('serviciosContainerEditar');

                    serviciosContainer.innerHTML = '';

                    // Generar un mapa de servicios por ID para facilitar la búsqueda
                    const serviciosMap = servicios.reduce((map, categoria) => {
                        categoria.servicios.forEach(servicio => {
                            map[servicio.id] = servicio;
                        });
                        return map;
                    }, {});

                    // Poblar los servicios del presupuesto
                    data.detalles.forEach(detalle => {
                        const servicio = serviciosMap[detalle.id_servicio]; // Obtener el servicio correspondiente
                        if (!servicio) {
                            console.error(`Servicio con ID ${detalle.id_servicio} no encontrado.`);
                            return; // Salir si no se encuentra el servicio
                        }

                        const nuevoServicio = document.createElement('div');
                        nuevoServicio.className = 'flex items-center space-x-2 w-full';
                        nuevoServicio.innerHTML = `
                            <div class="w-1/3">
                            <input type="hidden" name="id_detalles_editar[]" value="${detalle.id_detalle_presupuesto}">
                                <select name="servicios_editar[]" class="select2 service-dropdown-editar w-full text-sm rounded-lg bg-gray-700 border-gray-600 text-white" data-precio="${servicio.precio}">
                                    ${Object.values(serviciosMap).map(servicio => `
                                        <option value="${servicio.id}" ${servicio.id === detalle.id_servicio ? 'selected' : ''} data-precio="${servicio.precio}">
                                            ${servicio.nombre} - $${servicio.precio}
                                        </option>
                                    `).join('')}
                                </select>
                            </div>
                            <div class="w-1/6">
                                <input name="cantidades_editar[]" type="number" class="quantity-service-editar w-full text-sm rounded-lg bg-gray-700 border-gray-600 text-white" value="${detalle.cantidad}" min="1">
                            </div>
                            <div class="w-1/5">
                                <input name="costos_extra_editar[]" type="number" class="extra-cost-editar w-full text-sm rounded-lg bg-gray-700 border-gray-600 text-white" value="${detalle.costo_extra}" min="0">
                            </div>
                            <div class="w-1/5">
                                <span name="subtotales_editar[]" class="subtotal-service-editar text-sm text-white">Subtotal: $${parseFloat(detalle.precio_total).toFixed(2)}</span>
                                <input name="subtotales_editar[]" type="hidden" class="subtotal-service-value-editar" value="${parseFloat(detalle.precio_total).toFixed(2)}">
                            </div>
                            <div class="w-auto">
                                <button type="button" class="flex-shrink-0 px-3 py-2 text-sm font-medium text-white bg-red-800 rounded-lg hover:bg-red-400 remove-service-btn-editar" data-detalle-id="${detalle.id_detalle_presupuesto}">-</button>
                            </div>
                        `;

                        serviciosContainer.appendChild(nuevoServicio);

                        // Inicializar select2 para los nuevos dropdowns creados
                        $(nuevoServicio.querySelector('.select2')).select2();

                        // Añadir eventos para recalcular el total cuando cambie algún valor
                        $(nuevoServicio).on('change', 'select, input', calcularTotalEditar);

                        nuevoServicio.querySelector('.remove-service-btn-editar').addEventListener('click', function() {
                            // Mostrar alerta de confirmación
                            if (confirm('¿Estás seguro de que deseas eliminar este detalle de presupuesto?')) {
                                // Obtener el ID del detalle que deseas eliminar
                                const detalleId = nuevoServicio.querySelector('.remove-service-btn-editar').dataset.detalleId; 
                                
                                // Realizar la solicitud fetch para eliminar el detalle
                                fetch(`/presupuestos/eliminar_detalle/${detalleId}/`, {
                                    method: 'DELETE', // Usar el método DELETE
                                    headers: {
                                        'X-CSRFToken': getCookie('csrftoken') // Asegúrate de enviar el token CSRF
                                    }
                                })
                                .then(response => {
                                    if (response.ok) {
                                        return response.json(); // Convertir la respuesta a JSON
                                    }
                                    throw new Error('Error al eliminar el detalle de presupuesto');
                                })
                                .then(data => {
                                    alert(data.message); // Mostrar mensaje basado en la respuesta del servidor
                                    nuevoServicio.remove(); // Eliminar el servicio de la vista
                                    calcularTotalEditar(); // Llamar a la función para recalcular total
                                })
                                .catch(error => {
                                    alert(error.message); // Mostrar error si ocurre
                                });
                            }
                        });
                        
                        // Función para obtener el token CSRF
                        function getCookie(name) {
                            let cookieValue = null;
                            if (document.cookie && document.cookie !== '') {
                                const cookies = document.cookie.split(';');
                                for (let i = 0; i < cookies.length; i++) {
                                    const cookie = cookies[i].trim();
                                    // Comprobar si esta cookie comienza con el nombre que buscamos
                                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                                        break;
                                    }
                                }
                            }
                            return cookieValue;
                        }
                        
                    });

                    // Recalcular el total inicial
                    calcularTotalEditar();
                });
        })
        .catch(error => console.error('Error:', error));
}

function calcularTotalEditar() {
    let total = 0;
    const serviceDropdownsEditar = document.querySelectorAll('.service-dropdown-editar');

    serviceDropdownsEditar.forEach(dropdown => {
        // Obtener el valor seleccionado con Select2
        const selectedValue = $(dropdown).val(); // Valor seleccionado en el dropdown
        const selectedOption = Array.from(dropdown.options).find(option => option.value == selectedValue);

        // Obtener el precio del servicio desde el atributo data-precio de la opción seleccionada
        const precioServicio = parseFloat(selectedOption?.dataset.precio) || 0;
        const cantidadServicio = parseInt(dropdown.closest('.flex').querySelector('.quantity-service-editar').value) || 1;
        const costoExtra = parseFloat(dropdown.closest('.flex').querySelector('.extra-cost-editar').value) || 0;
        const subtotal = (precioServicio * cantidadServicio) + costoExtra;

        dropdown.closest('.flex').querySelector('.subtotal-service-editar').textContent = `Subtotal: $${subtotal.toFixed(2)}`;
        dropdown.closest('.flex').querySelector('.subtotal-service-value-editar').value = subtotal.toFixed(2);

        total += subtotal;
    });

    document.getElementById('totalCostEditar').value = total.toFixed(2); // Actualiza el valor del campo oculto
    document.getElementById('totalCostDisplayEditar').textContent = 'Total: $' + total.toFixed(2); // Actualiza la visualización opcional
}