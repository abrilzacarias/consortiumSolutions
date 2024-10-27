document.addEventListener('DOMContentLoaded', function () {
    // Obtener los botones y los elementos de factura
    const btnTodos = document.getElementById('btn-todos');
    const btnPendientes = document.getElementById('btn-pendientes');
    const btnProceso = document.getElementById('btn-proceso');
    const btnPagados = document.getElementById('btn-pagados');
    const facturas = document.querySelectorAll('.border-b-factura');

    // Función para mostrar todos las facturas
    btnTodos.addEventListener('click', () => {
        facturas.forEach(factura => {
            factura.style.display = 'table-row';
        });
    });

    // Función para mostrar solo pendientes
    btnPendientes.addEventListener('click', () => {
        facturas.forEach(factura => {
            if (factura.getAttribute('data-tipo') === '1') {
                factura.style.display = 'table-row';
            } else {
                factura.style.display = 'none';
            }
        });
    });

    // Función para mostrar solo pagados
    btnPagados.addEventListener('click', () => {
        facturas.forEach(factura => {
            if (factura.getAttribute('data-tipo') === '2') {
                factura.style.display = 'table-row';
            } else {
                factura.style.display = 'none';
            }
        });
    });

    // Función para mostrar solo en proceso
    btnProceso.addEventListener('click', () => {
        facturas.forEach(factura => {
            if (factura.getAttribute('data-tipo') === '3') {
                factura.style.display = 'table-row';
            } else {
                factura.style.display = 'none';
            }
        });
    });
});