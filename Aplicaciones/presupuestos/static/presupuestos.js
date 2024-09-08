$(document).ready(function() {
    // Inicializar DataTables
    var tabla = $('#tableActividades').DataTable({
        language: {
            info: 'Mostrando página _PAGE_ de _PAGES_',
            infoEmpty: 'No hay presupuestos cargados.',
            infoFiltered: '(Se ha filtrado de _MAX_ registros totales.)',
            lengthMenu: 'Mostrar _MENU_ registros por página.',
            zeroRecords: 'No se ha encontrado ningún registro.',
            search: 'Buscar: '
        }
    });

    // Mostrar modal
    $('#tableActividades').on('click', '.btn-detalles', function() {
        $('#detailsModal').removeClass('hidden');
    });

    // Cerrar el modal
    $('#closeModal').on('click', function() {
        $('#detailsModal').addClass('hidden');
    });

    // Cerrar el modal al hacer clic fuera del contenido del modal
    $('#detailsModal').on('click', function(event) {
        if ($(event.target).is('#detailsModal')) {
            $('#detailsModal').addClass('hidden');
        }
    });
});
