// Asegurarse de que el DOM esté completamente cargado antes de ejecutar el código
document.addEventListener('DOMContentLoaded', function () {
    // Obtener los botones y los elementos de cliente
    const btnTodos = document.getElementById('btn-todos');
    const btnPendientes = document.getElementById('btn-pendientes');
    const btnProceso = document.getElementById('btn-proceso');
    const btnPagados = document.getElementById('btn-pagados');
    const facturas = document.querySelectorAll('.border-b-factura'); // Seleccionamos todos los clientes

    // Función para mostrar todos los clientes
    btnTodos.addEventListener('click', () => {
        facturas.forEach(cliente => {
            factura.style.display = 'table-row'; // Mostrar todos
        });
    });

    // Función para mostrar solo prospectos
    btnPendientes.addEventListener('click', () => {
        facturas.forEach(factura => {
            if (factura.getAttribute('data-tipo') === '1') {
                factura.style.display = 'table-row'; // Mostrar prospectos
            } else {
                factura.style.display = 'none'; // Ocultar otros
            }
        });
    });
    // Función para mostrar solo prospectos
    btnPagados.addEventListener('click', () => {
        facturas.forEach(factura => {
            if (factura.getAttribute('data-tipo') === '2') {
                factura.style.display = 'table-row'; // Mostrar prospectos
            } else {
                factura.style.display = 'none'; // Ocultar otros
            }
        });
    });

    // Función para mostrar solo prospectos
    btnProceso.addEventListener('click', () => {
        facturas.forEach(factura => {
            if (factura.getAttribute('data-tipo') === '3') {
                factura.style.display = 'table-row'; // Mostrar prospectos
            } else {
                factura.style.display = 'none'; // Ocultar otros
            }
        });
    });
    // Función para mostrar solo clientes
    btnClientes.addEventListener('click', () => {
        clientes.forEach(cliente => {
            if (cliente.getAttribute('data-tipo') === '1') {
                cliente.style.display = 'table-row'; // Mostrar clientes
            } else {
                cliente.style.display = 'none'; // Ocultar otros
            }
        });
    });
});