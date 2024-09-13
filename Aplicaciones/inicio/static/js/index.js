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
        dom: 'rt'  // Este es para ocultar la paginación de DataTables!!
    });    

    $('.btn-filtro').on('click', function() {
        var filtro = $(this).text().trim();
        if (filtro === 'Todos') {
            tabla.search('').columns().search('').draw();
        } else {
            tabla.column(1).search(filtro).draw();
        }
    });

    $('a.page-link').on('click', function(e) {
        e.preventDefault();
        var page = $(this).data('page');
        tabla.page(page - 1).draw('page'); 
    });

    tabla.on('draw', function() {
        var info = tabla.page.info();
        $('.pagination-info').text(`Mostrando ${info.start + 1}-${info.end} de ${info.recordsTotal}`);
    });    
});









