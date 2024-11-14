function detallesPresupuesto(buttonElement) {
    const idPresupuesto = buttonElement.getAttribute('data-id-presupuesto');

    fetch(`presupuesto/${idPresupuesto}`)
    .then(response => response.json())
    .then(data => {
        // Limpiar el contenido previo de la tabla

            // Limpiar modales existentes antes de crear nuevos
        const existingModals = document.querySelectorAll('[id^="observacionesPresupuestoModal_"], [id^="agregarObservacionModal_"]');
        existingModals.forEach(modal => modal.remove());
        const tbody = document.querySelector('#detalleBody');
        tbody.innerHTML = '';

        if (Array.isArray(data) && data.length > 0) {
            data.forEach(detalle => {
                // Crear el modal de observaciones existentes
                const observacionesModalHTML = `
                    <div id="observacionesPresupuestoModal_${detalle.id_detalle_presupuesto}" 
                         tabindex="-1" 
                         aria-hidden="true" 
                         class="hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 items-center justify-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full">
                        <div class="relative p-4 w-full max-w-2xl max-h-full">
                            <div class="relative p-4 rounded-lg shadow bg-gray-800 sm:p-5">
                                <div class="flex justify-between items-center pb-4 mb-4 rounded-t border-b sm:mb-5">
                                    <h3 class="text-lg font-semibold text-white">Observaciones de ${detalle.nombre_servicio}</h3>
                                    <div class="flex items-center">
                                        <button type="button" 
                                                class="flex items-center justify-center text-white bg-green-700 hover:bg-green-800 focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-sm px-4 py-2 focus:outline-none"
                                                data-modal-target="agregarObservacionModal_${detalle.id_detalle_presupuesto}"
                                                data-modal-toggle="agregarObservacionModal_${detalle.id_detalle_presupuesto}">
                                            <svg class="h-3.5 w-3.5 mr-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                                                <path clip-rule="evenodd" fill-rule="evenodd" d="M10 3a1 1 0 011 1v5h5a1 1 0 110 2h-5v5a1 1 0 11-2 0v-5H4a1 1 0 110-2h5V4a1 1 0 011-1z" />
                                            </svg>
                                            Añadir Observación
                                        </button>
                                        <button type="button" 
                                                class="text-gray-200 bg-transparent hover:text-gray-700 rounded-lg text-sm p-1.5 ml-4 inline-flex items-center" 
                                                data-modal-hide="observacionesPresupuestoModal_${detalle.id_detalle_presupuesto}">
                                            <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                                <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"/>
                                            </svg>
                                            <span class="sr-only">Cerrar</span>
                                        </button>
                                    </div>
                                </div>
                                <div class="overflow-x-auto">
                                    <table class="w-full text-sm text-left text-gray-400">
                                        <thead class="text-xs text-white-700 uppercase bg-gray-700">
                                            <tr class="border-b">
                                                <th scope="col" class="px-4 py-4">Fecha</th>
                                                <th scope="col" class="px-4 py-4">Hora</th>
                                                <th scope="col" class="px-4 py-4">Descripción</th>
                                                <th scope="col" class="px-4 py-4">Observador</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            ${detalle.observaciones ? detalle.observaciones.map(obs => `
                                                <tr class="border-b">
                                                    <td class="px-4 py-3">${obs.fecha_observacion || ''}</td>
                                                    <td class="px-4 py-3">${obs.hora_observacion || ''}</td>
                                                    <td class="px-4 py-3">${obs.descripcion_observacion || ''}</td>
                                                    <td class="px-4 py-3">${obs.nombre_observador || ''}</td>
                                                </tr>
                                            `).join('') : '<tr><td colspan="3" class="px-4 py-3 text-center">No hay observaciones registradas</td></tr>'}
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>
                    </div>
                `;

                // El modal de agregar observación permanece igual
                const agregarObservacionModalHTML = `
                <div id="agregarObservacionModal_${detalle.id_detalle_presupuesto}" 
                     tabindex="-1" 
                     aria-hidden="true" 
                     class="hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full" style="top: -220px; /* Ajusta este valor según lo que necesites */">
                    <div class="relative p-4 w-full max-w-2xl max-h-full">
                        <div class="relative p-4 rounded-lg shadow bg-gray-800 sm:p-5">
                            <div class="flex justify-between items-center pb-4 mb-4 rounded-t border-b sm:mb-5">
                                <h3 class="text-lg font-semibold text-white">Agregar Observación a ${detalle.nombre_servicio}</h3>
                                <button type="button" 
                                        class="text-gray-200 bg-transparent hover:text-gray-700 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" 
                                        data-modal-hide="agregarObservacionModal_${detalle.id_detalle_presupuesto}">
                                    <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                        <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"/>
                                    </svg>
                                    <span class="sr-only">Cerrar</span>
                                </button>
                            </div>
                            <form id="ObservacionForm_${detalle.id_detalle_presupuesto}" 
                                  action="/presupuestos/agregarObservacionPresupuesto/${detalle.id_detalle_presupuesto}/"
                                  method="POST">
                                <div class="grid gap-4 mb-4 sm:grid-cols-2">
                                    <input type="hidden" name="csrfmiddlewaretoken" value="${document.querySelector('[name=csrfmiddlewaretoken]').value}">
                                    <div class="mb-0">
                                        <label for="descripcion_observacion_${detalle.id_detalle_presupuesto}" class="block mb-2 text-sm font-medium text-white">Descripción</label>
                                        <textarea name="descripcion_observacion" 
                                                  id="descripcion_observacion_${detalle.id_detalle_presupuesto}" 
                                                  class="text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white" 
                                                  placeholder="Ingrese su observación aquí..." 
                                                  required></textarea>
                                    </div>
                                    <input type="hidden" name="id_presupuesto" value="${idPresupuesto}">
                                    <input type="hidden" name="id_detalle_presupuesto" value="${detalle.id_detalle_presupuesto}">
                                    <div class="flex justify-end mb-4">
                                        <button type="submit" class="text-white bg-green-800 inline-flex items-center hover:bg-green-900 font-medium rounded-lg text-sm px-5 py-2.5 text-center">
                                            <svg class="mr-1 w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                                <path fill-rule="evenodd" d="M10 5a1 1 0 011 1v3h3a1 1 0 110 2h-3v3a1 1 0 11-2 0v-3H6a1 1 0 110-2h3V6a1 1 0 011-1z" clip-rule="evenodd"/>
                                            </svg>
                                            Agregar Observación
                                        </button>
                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            `;

                // Insertar ambos modales en el DOM
                document.body.insertAdjacentHTML('beforeend', observacionesModalHTML);
                document.body.insertAdjacentHTML('beforeend', agregarObservacionModalHTML);

                // El resto del código para crear la fila permanece igual
                const row = document.createElement('tr');
                row.classList.add('border-b');
                row.innerHTML = `
                    <td class="px-4 py-3">${detalle.nombre_servicio || 'No disponible'}</td>
                    <td class="px-4 py-3">${detalle.precio_servicio || 'No requiere pago'}</td>
                    <td class="px-4 py-3">${detalle.cantidad_detalle_presupuesto || 'No disponible'}</td>
                    <td class="px-4 py-3">${detalle.costo_extra_presupuesto || 'No disponible'}</td>
                    <td class="px-4 py-3">${detalle.precio_total_detalle_presupuesto || 'No disponible'}</td>
                    <td class="px-4 py-3">
                        <button id="${detalle.id_detalle_presupuesto}-dropdown-button" 
                                data-dropdown-toggle="${detalle.id_detalle_presupuesto}-dropdown" 
                                class="inline-flex items-center text-sm font-medium hover:bg-gray-100 p-1.5 text-center text-gray-500 hover:text-gray-800 rounded-lg focus:outline-none" 
                                type="button">
                            <svg class="w-5 h-5" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                <path d="M6 10a2 2 0 11-4 0 2 2 0 014 0zM12 10a2 2 0 11-4 0 2 2 0 014 0zM16 12a2 2 0 100-4 2 2 0 000 4z"/>
                            </svg>
                        </button>
                        <div id="${detalle.id_detalle_presupuesto}-dropdown" 
                             class="hidden z-10 w-44 bg-white rounded divide-y divide-gray-100 shadow">
                            <ul class="py-1 text-sm text-gray-700" 
                                aria-labelledby="${detalle.id_detalle_presupuesto}-dropdown-button">
                                <li>
                                    <button type="button" 
                                            data-modal-target="observacionesPresupuestoModal_${detalle.id_detalle_presupuesto}" 
                                            data-modal-toggle="observacionesPresupuestoModal_${detalle.id_detalle_presupuesto}" 
                                            class="flex w-full items-center py-2 px-4 hover:bg-gray-100 text-gray-700">
                                        <svg class="w-4 h-4 mr-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 18">
                                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5h9M5 9h5m8-8H2a1 1 0 0 0-1 1v10a1 1 0 0 0 1 1h4l3.5 4 3.5-4h5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1Z"/>
                                        </svg>
                                        Observaciones
                                    </button>
                                </li>
                            </ul>
                        </div>
                    </td>
                `;

                tbody.appendChild(row);
            });

            // Inicializar Flowbite después de agregar los elementos al DOM
            initFlowbite();
        } else {
            tbody.innerHTML = '<tr><td colspan="6" class="px-4 py-3 text-center">No se encontraron detalles para este presupuesto.</td></tr>';
        }

            // Mostrar el modal usando Flowbite
            const modalElement = document.getElementById('readProductModal');
            const modal = new Modal(modalElement);
            modal.show();

            // Inicializar Flowbite
            initFlowbite();
    })
    .catch(error => {
        console.error("Error al cargar los detalles del presupuesto:", error);
    });
}

function initializeSelect2Components() {
    initializeSelect2('#vendedor_asignado', '/presupuestos/vendedores/', vendedorFormatter);
    initializeSelect2('#cliente_asignado', '/presupuestos/clientes/', clienteFormatter);
    initializeSelect2('#edificio_asignado', '/presupuestos/edificios/', edificioFormatter); // Inicializa select2 para edificios
}

function initializeSelect2(selector, url, formatter) {
    $(selector).select2({
        ajax: {
            url: url,
            dataType: 'json',
            delay: 250,
            data: function(params) {
                return {
                    q: params.term,
                    page: params.page || 1
                };
            },
            processResults: function(data, params) {
                params.page = params.page || 1;
                return {
                    results: data.map(formatter),
                };
            },
            cache: true
        },
        placeholder: 'Seleccionar',
        minimumInputLength: 0,
        width: '100%',
    });
}

function vendedorFormatter(vendedor) {
    return {
        id: vendedor.id_empleado,
        text: `${vendedor.id_persona__nombre_persona} ${vendedor.id_persona__apellido_persona}`
    };
}

function clienteFormatter(cliente) {
    return {
        id: cliente.id_cliente,
        text: `${cliente.id_persona__nombre_persona} ${cliente.id_persona__apellido_persona}`
    };
}

function edificioFormatter(edificio) {
    return {
        id: edificio.id_edificio,
        text: edificio.nombre_edificio
    };
}

function setupClienteChangeListener() {
    var edificioSelect = $('#edificio_asignado');
    edificioSelect.prop('disabled', true); // Deshabilita el select durante la carga

    $('#cliente_asignado').on('change', function() {
        var clienteId = $(this).val();
        

        if (clienteId) {
            fetch(`/presupuestos/edificios/${clienteId}/`)
                .then(response => response.json())
                .then(data => {
                    var options = data.map(edificio => ({
                        id: edificio.id_edificio,
                        text: edificio.nombre_edificio
                    }));
                    
                    edificioSelect.select2({
                        data: options,
                        placeholder: 'Seleccione un edificio',
                        minimumInputLength: 0,
                        width: '100%'
                    });

                    edificioSelect.prop('disabled', false); // Habilita el select después de la carga
                })
                .catch(error => {
                    console.error('Error fetching edificios:', error);
                    edificioSelect.select2({
                        data: [{ id: '', text: 'Error al cargar edificios' }],
                        placeholder: 'Seleccione un edificio',
                        minimumInputLength: 0,
                        width: '100%'
                    });

                    edificioSelect.prop('disabled', false); // Habilita el select aunque haya error
                });
        } else {
            edificioSelect.select2({
                data: [{ id: '', text: 'Seleccione un cliente primero' }],
                placeholder: 'Seleccione un edificio',
                minimumInputLength: 0,
                width: '100%'
            });
            edificioSelect.prop('disabled', true); // Deshabilita el select
        }
    });
}

// Inicializa Select2 y setup listener
$(document).ready(function() {
    initializeSelect2Components();
    setupClienteChangeListener();
});


document.addEventListener('DOMContentLoaded', function() {

    let serviciosSeleccionados = new Set(); 


    // Función para inicializar Select2
    function initSelect2(selector) {
        if ($(selector).length) {
            $(selector).select2({
                placeholder: "Seleccione un servicio",
                allowClear: true,
                language: {
                    noResults: function() {
                        return "No hay más servicios disponibles";
                    }
                },
                escapeMarkup: function(markup) {
                    return markup;
                }
            });
        }
    }

    // Función para obtener las categorías y servicios
    function obtenerServicios() {
        return fetch('/presupuestos/servicios')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            });
    }

    function crearDropdownServicios(servicios, currentValue = '') {
        let selectHtml = '<select name="servicios[]" required class="select2 service-dropdown w-full text-sm rounded-lg bg-gray-700 border-gray-600 text-white">';
        selectHtml += '<option value="">Seleccione un servicio</option>';
    
        servicios.forEach(categoria => {
            // Filtrar los servicios disponibles para esta categoría
            let serviciosDisponibles = categoria.servicios.filter(servicio => {
                const servicioId = servicio.id.toString();
                // Un servicio está disponible si no está seleccionado o es el valor actual
                return !serviciosSeleccionados.has(servicioId) || servicioId === currentValue;
            });
    
            // Solo crear el optgroup si hay servicios disponibles
            if (serviciosDisponibles.length > 0) {
                selectHtml += `<optgroup label="${categoria.categoria}">`;
                serviciosDisponibles.forEach(servicio => {
                    const selected = servicio.id.toString() === currentValue ? 'selected' : '';
                    selectHtml += `<option value="${servicio.id}" 
                                         data-precio="${servicio.precio}" 
                                         ${selected}>
                                    ${servicio.nombre} - $${servicio.precio}
                                 </option>`;
                });
                selectHtml += '</optgroup>';
            }
        });
    
        selectHtml += '</select>';
        return selectHtml;
    }

    function actualizarEstadoInputs(servicioElement) {
        const select = servicioElement.querySelector('.select2');
        const cantidadInput = servicioElement.querySelector('input[name="cantidades[]"]');
        const costoExtraInput = servicioElement.querySelector('input[name="costos_extra[]"]');
    
        const isServiceSelected = select.value !== '';
        cantidadInput.disabled = !isServiceSelected;
        costoExtraInput.disabled = !isServiceSelected;
    }


// Función para agregar un nuevo servicio
function agregarServicio(servicios) {
    const serviciosContainer = document.getElementById('serviciosContainer');
    const nuevoServicio = document.createElement('div');
    
    nuevoServicio.className = 'flex flex-col md:flex-row md:items-center space-y-2 md:space-y-0 md:space-x-2 w-full';

    nuevoServicio.innerHTML = `
        <div class="w-full">
            ${crearDropdownServicios(servicios)}
        </div>

        <div class="w-full md:w-1/6">
            <input name="cantidades[]" type="number" class="quantity-service w-full text-sm rounded-lg bg-gray-700 border-gray-600 text-white" placeholder="Cantidad" value="1" min="1" disabled>
        </div>
        <div class="w-full md:w-1/5">
            <input name="costos_extra[]" type="number" class="extra-cost w-full text-sm rounded-lg bg-gray-700 border-gray-600 text-white" placeholder="Costo extra" min="0" disabled>
        </div>
        <div class="w-full md:w-1/5">
            <span name="subtotales[]" class="subtotal-service text-sm text-white">Subtotal: $0.00</span>
            <input type="hidden" name="precios_unitarios[]" class="precios-unitarios" value="0.00">
            <input name="subtotales[]" type="hidden" class="subtotal-service-value" value="0.00">
        </div>
        <div class="w-full md:w-auto flex-shrink-0">
            <button type="button" class="px-3 py-2 w-full md:w-auto text-sm font-medium text-white bg-red-800 rounded-lg hover:bg-red-400 remove-service-btn">-</button>
        </div>
    `;

    serviciosContainer.appendChild(nuevoServicio);

    // Inicializar Select2 en el nuevo dropdown
    initSelect2(nuevoServicio.querySelector('.select2'));

    // Actualizar estado de inputs inicialmente
    actualizarEstadoInputs(nuevoServicio);

    // Añadir listener para actualizar el estado de los inputs cuando cambie el select
    $(nuevoServicio).find('.select2').on('change', function() {
        const previousValue = this.getAttribute('data-previous-value');
        if (previousValue) {
            serviciosSeleccionados.delete(previousValue);
        }
        
        const selectedValue = this.value;
        if (selectedValue) {
            serviciosSeleccionados.add(selectedValue);
            this.setAttribute('data-previous-value', selectedValue);
        }

        actualizarTodosLosDropdowns(servicios);
        actualizarEstadoInputs(nuevoServicio); // Llamar para habilitar/deshabilitar inputs
        calcularTotal();
    });

    // Agregar evento de eliminación
    nuevoServicio.querySelector('.remove-service-btn').addEventListener('click', function() {
        nuevoServicio.remove();
        calcularTotal();
    });
}

    // Función mejorada para actualizar todos los dropdowns
    function actualizarTodosLosDropdowns(servicios) {
        $('.service-select2').each(function() {
            const currentValue = $(this).val();
            const container = $(this).closest('.select-container');
            
            // Solo destruir si está inicializado
            if ($(this).hasClass('select2-hidden-accessible')) {
                $(this).select2('destroy');
            }
            
            // Actualizar el HTML
            container.html(crearDropdownServicios(servicios, currentValue));
            
            // Reinicializar Select2 específicamente para el servicio
            initServiceSelect2(container.find('.service-select2'));
        });
    }
    

    // Obtener los servicios al cargar la página
    obtenerServicios()
        .then(servicios => {
            agregarServicio(servicios);

            // Al hacer clic en "Agregar Otro Servicio"
            const addServiceBtn = document.getElementById('addServiceBtn');
            if (addServiceBtn) {
                addServiceBtn.addEventListener('click', function() {
                    agregarServicio(servicios);
                });
            }

            // Al eliminar un servicio
            const serviciosContainer = document.getElementById('serviciosContainer');
            if (serviciosContainer) {
                serviciosContainer.addEventListener('click', function(event) {
                    if (event.target.classList.contains('remove-service-btn')) {
                        event.target.closest('.flex').remove();
                        calcularTotal();  // Recalcular total
                    }
                });
            }

            // Calcular el total cada vez que se cambia un dropdown, cantidad o se ingresa un costo extra
            $('#serviciosContainer').on('change', '.service-dropdown, .quantity-service, .extra-cost', function() {
            calcularTotal();
        });
        })
        .catch(() => {
            console.error('Error al cargar los servicios.');
        });

});


function calcularTotal() {
    let total = 0;
    const serviceDropdowns = document.querySelectorAll('.service-dropdown');

    serviceDropdowns.forEach(dropdown => {
        // Obtener el valor seleccionado con Select2
        const selectedValue = $(dropdown).val(); // Valor seleccionado en el dropdown
        const selectedOption = Array.from(dropdown.options).find(option => option.value == selectedValue);

        // Asegurar que selectedOption y precioServicio siempre tengan un valor válido
        const precioServicio = selectedOption ? parseFloat(selectedOption.dataset.precio) || 0 : 0;
        const cantidadServicio = parseInt(dropdown.closest('.flex').querySelector('.quantity-service').value) || 1;
        const costoExtra = parseFloat(dropdown.closest('.flex').querySelector('.extra-cost').value) || 0;
        const subtotal = (precioServicio * cantidadServicio) + costoExtra;

        // Asegurarse de que subtotal siempre sea un número válido
        if (!isNaN(subtotal)) {
            dropdown.closest('.flex').querySelector('.subtotal-service').textContent = `Subtotal: $${subtotal.toFixed(2)}`;
            dropdown.closest('.flex').querySelector('.subtotal-service-value').value = subtotal.toFixed(2);
            dropdown.closest('.flex').querySelector('.precios-unitarios').value = precioServicio;

            total += subtotal;
        } else {
            dropdown.closest('.flex').querySelector('.subtotal-service').textContent = `Subtotal: $0.00`;
        }
    });

    document.getElementById('totalCost').value = total.toFixed(2); // Actualiza el valor del campo oculto
    document.getElementById('totalCostDisplay').textContent = 'Total: $' + total.toFixed(2); // Actualiza la visualización opcional
}

