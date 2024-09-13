$(document).ready(function() {
    // Inicializar DataTables
    var tabla = $('#tableActividades').DataTable({
        language: {
            info: 'Mostrando página _PAGE_ de _PAGES_',
            infoEmpty: 'No hay vendedores cargados.',
            infoFiltered: '(Se ha filtrado de _MAX_ registros totales.)',
            lengthMenu: 'Mostrar _MENU_ registros por página.',
            zeroRecords: 'No se ha encontrado ningún registro.',
            search: 'Buscar: '
        }
    });

    // Función para filtrar la tabla según el tipo de actividad
    $('.btn-filtro').on('click', function() {
        var filtro = $(this).text().trim(); // Asegúrate de eliminar espacios adicionales
        if (filtro === 'Todos') {
            tabla.search('').columns().search('').draw();
        } else {
            tabla.column(1).search(filtro).draw();
        }
    });
});
