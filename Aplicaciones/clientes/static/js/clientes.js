 $(document).ready(function() {
  $('#tableClientes').DataTable({
    language: {
      info: 'Mostrando página _PAGE_ de _PAGES_',
      infoEmpty: 'No hay vendedores cargados.',
      infoFiltered: '(Se ha filtrado de _MAX_ registros totales.)',
      lengthMenu: 'Mostrar _MENU_ registros por página.',
      zeroRecords: 'No se ha encontrado ningún registro.',
      search: 'Buscar: '
    },
    lengthMenu: [
      [5, 10, 25, -1],
      [5, 10, 25, 'Todos']
  ],
  scrollX: true
  });


});

document.addEventListener('DOMContentLoaded', (event) => {
  const btnsFiltro = document.querySelectorAll('.btn-filtro');
  
   btnsFiltro.forEach(btn => {
        // Agregamos un event listener para el evento click
        btn.addEventListener('click', () => {
          // Obtenemos el tipo de cliente que queremos filtrar
          const tipoCliente = btn.dataset.tipoCliente;
          
      
          // Obtenemos todas las filas de clientes
          const filasClientes = document.querySelectorAll('tbody tr');
          console.log(filasClientes)
          // Iteramos sobre cada fila de cliente
          filasClientes.forEach(fila => {
            // Comprobamos si el tipo de cliente de la fila coincide con el tipo de cliente que queremos filtrar
            if (fila.dataset.tipoCliente === tipoCliente || tipoCliente === 'todos') {
              // Mostramos la fila si coincide con el filtro o si el filtro es "todos"
              fila.style.display = 'table-row';
            } else {
              // Ocultamos la fila si no coincide con el filtro
              fila.style.display = 'none';
            }
          });
        });
      })
    });