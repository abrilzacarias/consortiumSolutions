$(document).ready(function() {
    var tabla = $('#tableActividades').DataTable({
        language: {
            info: 'Mostrando página _PAGE_ de _PAGES_',
            infoEmpty: 'No hay actividades cargadas.',
            infoFiltered: '(Filtrado de _MAX_ registros totales.)',
            lengthMenu: 'Mostrar _MENU_ registros por página.',
            zeroRecords: 'No se ha encontrado ningún registro.',
            search: 'Buscar: '
        },
        paging: true, 
        pageLength: 10,
        lengthChange: false,
        dom: 'rt'  // Este es para ocultar la paginación de DataTables
    });    

    // Función para generar los botones de paginación
    function generarBotonesPaginacion() {
        var info = tabla.page.info();
        var pagination = $('.pagination');
        pagination.empty(); // Limpiar los botones previos

        // Solo generar botones si hay más de 10 registros
        if (info.recordsTotal > 10) {
            // Botón "Anterior"
            if (info.page > 0) {
                pagination.append(`
                    <li>
                        <a href="#" class="page-link flex items-center justify-center h-full py-1.5 px-3 ml-0 text-gray-500 bg-gray-800 rounded-l-lg border border-gray-700 hover:bg-gray-700 hover:text-white" data-page="${info.page}">
                            <span class="sr-only">Anterior</span>
                            <svg class="w-5 h-5" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z" clip-rule="evenodd" />
                            </svg>
                        </a>
                    </li>
                `);
            }

            // Botones de página
            for (var i = 1; i <= info.pages; i++) {
                pagination.append(`
                    <li>
                        <a href="#" class="page-link flex items-center justify-center text-sm py-2 px-3 leading-tight ${i === info.page + 1 ? 'bg-gray-800 text-white' : 'text-gray-500 bg-white'} border border-gray-300 hover:bg-gray-100 hover:text-gray-700" data-page="${i}">
                            ${i}
                        </a>
                    </li>
                `);
            }

            // Botón "Siguiente"
            if (info.page < info.pages - 1) {
                pagination.append(`
                    <li>
                        <a href="#" class="page-link flex items-center justify-center h-full py-1.5 px-3 leading-tight text-gray-500 bg-gray-800 rounded-r-lg border border-gray-700 hover:bg-gray-700 hover:text-white" data-page="${info.page + 2}">
                            <span class="sr-only">Siguiente</span>
                            <svg class="w-5 h-5" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" />
                            </svg>
                        </a>
                    </li>
                `);
            }

            // Asignar eventos a los botones generados
            $('a.page-link').on('click', function(e) {
                e.preventDefault();
                var page = $(this).data('page');
                tabla.page(page - 1).draw('page');
            });
        }
    }

    // Actualizar información de paginación y generar los botones al cambiar la página
    tabla.on('draw', function() {
        var info = tabla.page.info();
        $('.pagination-info').text(`Mostrando ${info.start + 1}-${info.end} de ${info.recordsTotal}`);
        generarBotonesPaginacion();
    });

    // Generar los botones inicialmente
    generarBotonesPaginacion();