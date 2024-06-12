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
        btn.addEventListener('click', () => {

          const tipoCliente = btn.dataset.tipoCliente;
          
          const filasClientes = document.querySelectorAll('tbody tr');
          console.log(filasClientes)
          filasClientes.forEach(fila => {
            if (fila.dataset.tipoCliente === tipoCliente || tipoCliente === 'todos') {
              fila.style.display = 'table-row';
            } else {
              fila.style.display = 'none';
            }
          });
        });
      })
    });