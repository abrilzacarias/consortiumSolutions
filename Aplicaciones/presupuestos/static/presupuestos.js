function detallesPresupuesto(buttonElement) {
    const idPresupuesto = buttonElement.getAttribute('data-id-presupuesto');

    fetch(`presupuesto/${idPresupuesto}`)
    .then(response => response.json())
    .then(data => {
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
                    <td class="px-4 py-3">${detalle.precio_servicio || 'No disponible'}</td>
                    <td class="px-4 py-3">${detalle.cantidad_detalle_presupuesto || 'No disponible'}</td>
                    <td class="px-4 py-3">${detalle.costo_extra_presupuesto || 'No disponible'}</td>
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
        let selectHtml = '<select name="servicios[]" class="select2 service-dropdown w-full text-sm rounded-lg bg-gray-700 border-gray-600 text-white">';
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

    // Función para agregar un nuevo servicio
    function agregarServicio(servicios) {
        const serviciosContainer = document.getElementById('serviciosContainer');
        const nuevoServicio = document.createElement('div');
        
        // Añadir diseño en columna para dispositivos móviles
        nuevoServicio.className = 'flex flex-col md:flex-row md:items-center space-y-2 md:space-y-0 md:space-x-2 w-full';
    
        nuevoServicio.innerHTML = `
            <div class="w-full">
                ${crearDropdownServicios(servicios)}
            </div>
    
            <div class="w-full md:w-1/6">
                <input name="cantidades[]" type="number" class="quantity-service w-full text-sm rounded-lg bg-gray-700 border-gray-600 text-white" placeholder="Cantidad" value="1" min="1">
            </div>
            <div class="w-full md:w-1/5">
                <input name="costos_extra[]" type="number" class="extra-cost w-full text-sm rounded-lg bg-gray-700 border-gray-600 text-white" placeholder="Costo extra" min="0">
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
    
        // Inicializar Select2 en el nuevo dropdown.
        initSelect2(nuevoServicio.querySelector('.select2'));

        // Agregar listener para el cambio
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

