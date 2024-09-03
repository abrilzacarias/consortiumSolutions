$(document).ready(function() {
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

  const createContactInputGroupAdd = () => {
    const newContactAdd = document.createElement('div');
    newContactAdd.className = 'input-group mb-3';
    const uniqueId = Math.random().toString(36).substring(2, 15); 

    newContactAdd.innerHTML = `
      <select class="form-control bg-dark text-light" name="tipo_contacto[]">
        <option value="1">Correo Electrónico</option>
        <option value="2">Teléfono</option>
        <option value="3">URL</option>
      </select>
      <input type="text" class="form-control" name="contacto[]" placeholder="Ingrese el contacto" required>
      <button type="button" class="btn btn-danger remove-contact-btn">-</button>
    `;

    newContactAdd.querySelector('.remove-contact-btn').addEventListener('click', () => {
      newContactAdd.parentElement.removeChild(newContactAdd);
    });

    return newContactAdd;
  };

  const addContactBtnAdd = document.getElementById('addContactBtnAdd');
  const contactsContainerAdd = document.getElementById('contactsContainerAdd');
  addContactBtnAdd.addEventListener('click', () => {
    const newContact = createContactInputGroupAdd();
    contactsContainerAdd.appendChild(newContact);
  });


  const createContactInputGroupEdit = (modalId) => {
    const newContactEdit = document.createElement('div');
    newContactEdit.className = 'input-group mb-3';
    const uniqueId = Math.random().toString(36).substring(2, 15); // Generate a unique ID

    newContactEdit.innerHTML = `
      <select class="form-control bg-dark text-light" name="nuevo_contacto_tipo_${uniqueId}">
        <option value="1">Correo Electrónico</option>
        <option value="2">Teléfono</option>
        <option value="3">URL</option>
      </select>
      <input type="text" class="form-control" name="nuevo_contacto_descripcion_${uniqueId}" placeholder="Ingrese el contacto" required>
      <button type="button" class="btn btn-danger remove-contact-btn">-</button>
    `;

    // Add event listener to the remove button
    newContactEdit.querySelector('.remove-contact-btn').addEventListener('click', () => {
      newContactEdit.parentElement.removeChild(newContactEdit);
    });

    return newContactEdit;
  };

  document.addEventListener('click', (event) => {
    if (event.target && event.target.classList.contains('addContactBtnEdit')) {
      const modalId = event.target.closest('.modal').id;
      const contactsContainerEdit = document.getElementById(modalId).querySelector('.contactsContainerEdit');
      const newContact = createContactInputGroupEdit(modalId);
      contactsContainerEdit.appendChild(newContact);
    }
  });
});

// Function to get CSRF token
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

// Function to delete contact directly
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

      }
    })
    .catch(error => {
      console.error('Error al eliminar el contacto:', error);
    });
  }
}

function confirmarEliminacion() {
  return confirm('¿Está seguro de que desea eliminar este vendedor?');
}