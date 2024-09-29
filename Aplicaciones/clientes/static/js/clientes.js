// Asegurarse de que el DOM esté completamente cargado antes de ejecutar el código
document.addEventListener('DOMContentLoaded', function () {
    // Obtener los botones y los elementos de cliente
    const btnTodos = document.getElementById('btn-todos');
    const btnProspectos = document.getElementById('btn-prospectos');
    const btnClientes = document.getElementById('btn-clientes');
    const clientes = document.querySelectorAll('.border-b-cliente'); // Seleccionamos todos los clientes

    // Función para mostrar todos los clientes
    btnTodos.addEventListener('click', () => {
        clientes.forEach(cliente => {
            cliente.style.display = 'table-row'; // Mostrar todos
        });
    });

    // Función para mostrar solo prospectos
    btnProspectos.addEventListener('click', () => {
        clientes.forEach(cliente => {
            if (cliente.getAttribute('data-tipo') === '0') {
                cliente.style.display = 'table-row'; // Mostrar prospectos
            } else {
                cliente.style.display = 'none'; // Ocultar otros
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
