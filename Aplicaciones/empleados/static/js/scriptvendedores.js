$(document).ready(function() {
  // Inicializar DataTables
  $('#tableVendedores').DataTable({
    language: {
      info: 'Mostrando página _PAGE_ de _PAGES_',
      infoEmpty: 'No hay vendedores cargados.',
      infoFiltered: '(Se ha filtrado de _MAX_ registros totales.)',
      lengthMenu: 'Mostrar _MENU_ registros por página.',
      zeroRecords: 'No se ha encontrado ningún registro.',
      search: 'Buscar: '
    },
  });

    $(document).ready(function() {
      // Función para crear un nuevo grupo de contacto con estilo
      const createContactInputGroup = () => {
          return `
              <div class="flex items-center mb-4 contact-group">
                  <select style="width: 30%; padding: 8px; border: 1px solid #ccc; background-color: #4a5568; color: white;" name="tipo_contacto[]">
                  <option value="1">Correo Electrónico</option>
                  <option value="2">Teléfono</option>
                  <option value="3">Página Web</option>
                </select>
                <input type="text" style="width: 60%; padding: 8px; border: 1px solid #ccc; background-color: white; color: black;" name="contacto[]" placeholder="Ingrese el contacto" required>
                <button type="button" style="margin-left: 8px; background-color: red; color: white; padding: 8px; border-radius: 4px;" onclick="this.parentElement.remove()">-</button>
              `;
      };

      // Evita que el evento se adjunte múltiples veces
      $('#addContactBtnAdd').on('click', function() {
          $('#contactsContainerAdd').append(createContactInputGroup());
      });

      // Manejar la eliminación de contactos con event delegation
      $('#contactsContainerAdd').on('click', '.remove-contact-btn', function() {
          $(this).closest('.contact-group').remove();
      });

      // Verifica la visibilidad y el estilo del primer input al cargar
      const checkInitialVisibility = () => {
          $('#contactsContainerAdd .contacto-input').each(function() {
              if ($(this).val() === '') {
                  $(this).css('background-color', 'gray'); // Asegura que el fondo sea blanco
                  $(this).css('color', 'black'); // Asegura que el texto sea negro
              }
          });
      };

      // Llama a la función para verificar la visibilidad del primer input al cargar
      checkInitialVisibility();
  });


  // Función para crear un nuevo contacto en el formulario de edición
  const createContactInputGroupEdit = (modalId) => {
    const newContactEdit = document.createElement('div');
    newContactEdit.className = 'input-group mb-3';

    newContactEdit.innerHTML = `
      <select class="form-control bg-dark text-light" name="nuevo_contacto_tipo[]">
        <option value="1">Correo Electrónico</option>
        <option value="2">Teléfono</option>
        <option value="3">URL</option>
      </select>
        <input type="text" class="form-control" name="nuevo_contacto_descripcion[]" placeholder="Ingrese el contacto" required>
        <button type="button" class="btn btn-danger remove-contact-btn">-</button>
    `;
    return newContactEdit;
  };

  // Delegar eventos de agregar contacto en el formulario de edición
  $(document).on('click', '.addContactBtnEdit', function() {
    const modalId = $(this).closest('.modal').attr('id');
    const contactsContainerEdit = $('#' + modalId).find('.contactsContainerEdit');
    const newContact = createContactInputGroupEdit(modalId);
    contactsContainerEdit.append(newContact);
  });

  // Delegar eventos de eliminación de contactos en el formulario de edición
  $(document).on('click', '.remove-contact-btn', function() {
    $(this).closest('.input-group').remove();
  });


// Función para obtener el token CSRF
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// Función para eliminar un contacto directamente
function eliminarContactoDirecto(buttonElement) {
  const contactoId = buttonElement.getAttribute('data-contacto-id');
  var csrftoken = getCookie('csrftoken');

  if (confirm("¿Está seguro de que desea eliminar este contacto?")) {
    fetch(`/vendedores/eliminarContacto/${contactoId}`, {
      method: 'DELETE',
      headers: {
        'X-CSRFToken': csrftoken
      }
    })
    .then(response => {
      if (response.ok) {
        const contactElement = document.getElementById(`contacto_${contactoId}`);
        contactElement.parentElement.removeChild(contactElement);
        const modalBody = document.querySelector('.modal-body');
        const successMessage = document.createElement('p');
        successMessage.classList.add('alert', 'alert-success');
        successMessage.textContent = 'Contacto eliminado exitosamente.';
        modalBody.appendChild(successMessage);
        setTimeout(() => successMessage.remove(), 2000); 
      } else {
        console.error('Error al eliminar el contacto.');
      }
    })
    .catch(error => {
      console.error('Error al eliminar el contacto:', error);
    });
  }
}

function confirmarEliminacion() {
  return confirm('¿Está seguro de que desea eliminar este vendedor?');
}})