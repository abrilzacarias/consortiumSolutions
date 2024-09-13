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

document.addEventListener('DOMContentLoaded', function() {
    initializeSelect2Components();
    setupClienteChangeListener();
});

function initializeSelect2Components() {
    initializeSelect2('#vendedor_asignado', '/presupuestos/vendedores/', vendedorFormatter);
    initializeSelect2('#cliente_asignado', '/presupuestos/clientes/', clienteFormatter);
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
                    page: params.page
                };
            },
            processResults: function(data, params) {
                params.page = params.page || 1;
                return {
                    results: data.map(formatter),
                    pagination: {
                        more: (params.page * 30) < data.total_count
                    }
                };
            },
            cache: true
        },
        placeholder: `Seleccionar`,
        minimumInputLength: 0,
        width: '100%'
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

function setupClienteChangeListener() {
    $('#cliente_asignado').on('change', function() {
        var clienteId = $(this).val();
        var edificioSelect = document.getElementById('edificio_asignado');
        
        if (clienteId) {
            edificioSelect.disabled = true;
            fetch(`/presupuestos/edificios/${clienteId}/`)
                .then(response => response.json())
                .then(data => {
                    edificioSelect.innerHTML = '<option value="">Seleccione un edificio</option>';
                    data.forEach(edificio => {
                        var option = document.createElement('option');
                        option.value = edificio.id_edificio;
                        option.textContent = edificio.nombre_edificio;
                        edificioSelect.appendChild(option);
                    });
                    edificioSelect.disabled = false;
                })
                .catch(error => {
                    console.error('Error fetching edificios:', error);
                    edificioSelect.innerHTML = '<option value="">Error al cargar edificios</option>';
                    edificioSelect.disabled = false;
                });
        } else {
            edificioSelect.innerHTML = '<option value="">Seleccione un cliente primero</option>';
            edificioSelect.disabled = true;
        }
    });
}
$(document).ready(function() {
    // Inicializar select2
    function initSelect2(selector) {
        $(selector).select2({
            placeholder: "Seleccione un servicio",
            allowClear: true,
            width: '100%',
        });
    }

    // Función para obtener las categorías y servicios
    function obtenerServicios() {
        return $.ajax({
            url: '/presupuestos/servicios',  // Ajusta la ruta aquí
            method: 'GET',
            dataType: 'json',
        });
    }

    // Función para crear un nuevo dropdown de servicios
    function crearDropdownServicios(servicios) {
        let selectHtml = '<select name= class="servicios[]" service-dropdown w-1/3 text-sm rounded-lg bg-gray-700 border-gray-600 text-white">';
        selectHtml += '<option value="">Seleccione un servicio</option>';

        servicios.forEach(function(categoria) {
            selectHtml += `<optgroup label="${categoria.categoria}">`;
            categoria.servicios.forEach(function(servicio) {
                selectHtml += `<option value="${servicio.id}" data-precio="${servicio.precio}">${servicio.nombre} - $${servicio.precio}</option>`;
            });
            selectHtml += '</optgroup>';
        });

        selectHtml += '</select>';
        return selectHtml;
    }

    // Función para agregar un nuevo servicio
    function agregarServicio(servicios) {
        const serviciosContainer = $('#serviciosContainer');
        const nuevoServicio = $(`
            <div class="flex items-center space-x-2 w-full">
                <div class="w-1/3">
                    ${crearDropdownServicios(servicios)}
                </div>
                <div class="w-1/6">
                    <input name="cantidades[]" type="number" class="quantity-service w-full text-sm rounded-lg bg-gray-700 border-gray-600 text-white" placeholder="Cantidad" value="1" min="1">
                </div>
                <div class="w-1/5">
                    <input name="costos[]" type="number" class="extra-cost w-full text-sm rounded-lg bg-gray-700 border-gray-600 text-white" placeholder="Costo extra" min="0">
                </div>
                <div class="w-1/5">
                    <span name="subtotales[]" class="subtotal-service text-sm text-white">Subtotal: $0.00</span>
                </div>
                <div class="w-auto">
                    <button type="button" class="flex-shrink-0 px-3 py-2 text-sm font-medium text-white bg-red-800 rounded-lg hover:bg-red-400 remove-service-btn">-</button>
                </div>
            </div>
        `);
    
        serviciosContainer.append(nuevoServicio);
        initSelect2(nuevoServicio.find('select'));
    }
    

    // Función para calcular el total
    function calcularTotal() {
        let total = 0;

        // Iterar sobre cada dropdown de servicios
        $('.service-dropdown').each(function() {
            const precioServicio = $(this).find(':selected').data('precio') || 0;
            const cantidadServicio = parseInt($(this).closest('.flex').find('.quantity-service').val()) || 1;
            const costoExtra = parseFloat($(this).closest('.flex').find('.extra-cost').val()) || 0;

            // Calcular el subtotal para este servicio
            const subtotal = (precioServicio * cantidadServicio) + costoExtra;

            // Mostrar el subtotal en el span correspondiente
            $(this).closest('.flex').find('.subtotal-service').text(`Subtotal: $${subtotal.toFixed(2)}`);

            // Sumar el subtotal al total general
            total += subtotal;
        });

        // Mostrar el total general
        $('#totalCost').text('Total: $' + total.toFixed(2));
    }

    // Obtener los servicios al cargar la página
    obtenerServicios().done(function(servicios) {
        // Inicializar el primer dropdown de servicios
        agregarServicio(servicios);

        // Al hacer clic en "Agregar Otro Servicio"
        $('#addServiceBtn').click(function() {
            agregarServicio(servicios);
        });

        // Al eliminar un servicio
        $('#serviciosContainer').on('click', '.remove-service-btn', function() {
            $(this).closest('.flex').remove();
            calcularTotal();  // Recalcular total
        });

        // Calcular el total cada vez que se cambia un dropdown, cantidad o se ingresa un costo extra
        $('#serviciosContainer').on('change', '.service-dropdown, .quantity-service, .extra-cost', function() {
            calcularTotal();
        });
    }).fail(function() {
        console.error('Error al cargar los servicios.');
    });
});
