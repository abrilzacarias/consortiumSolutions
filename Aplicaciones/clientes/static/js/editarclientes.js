// Función para crear un nuevo grupo de contacto
function createContactGroup(clienteId, contactoId = null, tipoContacto = '', descripcionContacto = '') {
  const div = document.createElement('div');
  div.className = 'flex items-center space-x-2 contact-group';
  if (contactoId) {
      div.setAttribute('data-contacto-id', contactoId);
  }

  div.innerHTML = `
      <select class="w-1/4 text-sm rounded-lg bg-gray-700 border-gray-600 text-white" name="tipo_contacto_${contactoId || 'nuevo'}">
          <option value="2" ${tipoContacto === '2' ? 'selected' : ''}>Teléfono</option>
          <option value="3" ${tipoContacto === '3' ? 'selected' : ''}>Página Web</option>
      </select>
      <input type="text" class="flex-1 text-sm rounded-lg bg-gray-700 border-gray-600 text-white" name="contacto_${contactoId || 'nuevo'}" value="${descripcionContacto}" required>
      <button type="button" class="flex-shrink-0 px-3 py-2 text-sm font-medium text-white bg-red-800 rounded-lg hover:bg-red-400 remove-contact-btn">-</button>
  `;

  div.querySelector('.remove-contact-btn').addEventListener('click', function() {
      if (contactoId) {
          eliminarContacto(clienteId, contactoId, div);
      } else {
          div.remove();
      }
  });

  return div;
}

// Función para agregar un nuevo contacto
function addNewContact(clienteId) {
  const contactsContainer = document.querySelector(`#contactsContainerAdd${clienteId}`);
  const newContactGroup = createContactGroup(clienteId);
  contactsContainer.appendChild(newContactGroup);
}

// Función para eliminar un contacto
function eliminarContacto(clienteId, contactoId, contactElement) {
  if (confirm("¿Está seguro de que desea eliminar este contacto?")) {
      fetch(`/clientes/eliminarContacto/${contactoId}/`, {
          method: 'DELETE',
          headers: {
              'X-CSRFToken': getCookie('csrftoken')
          }
      })
      .then(response => {
          if (response.ok) {
              contactElement.remove();
              mostrarMensaje(clienteId, 'Contacto eliminado exitosamente.', 'success');
          } else {
              mostrarMensaje(clienteId, 'Error al eliminar el contacto.', 'error');
          }
      })
      .catch(error => {
          console.error('Error al eliminar el contacto:', error);
          mostrarMensaje(clienteId, 'Error al eliminar el contacto.', 'error');
      });
  }
}

// Función para mostrar mensajes
function mostrarMensaje(clienteId, mensaje, tipo) {
  const modalBody = document.querySelector(`#editarClienteModal_${clienteId}`);
  const messageDiv = document.createElement('div');
  messageDiv.textContent = mensaje;
  messageDiv.className = `text-sm ${tipo === 'success' ? 'text-green-500' : 'text-red-500'} mt-2`;
  modalBody.appendChild(messageDiv);
  setTimeout(() => messageDiv.remove(), 3000);
}

// Inicializar los eventos para cada modal de cliente
document.addEventListener('DOMContentLoaded', function() {
  const clienteModals = document.querySelectorAll('[id^="editarClienteModal_"]');
  
  clienteModals.forEach(modal => {
      const clienteId = modal.id.split('_')[1];
      
      // Agregar evento al botón de agregar contacto
      const addContactBtn = modal.querySelector(`#addContactBtnAdd${clienteId}`);
      if (addContactBtn) {
          addContactBtn.addEventListener('click', () => addNewContact(clienteId));
      }

      // Inicializar eventos para los botones de eliminar contacto existentes
      const removeContactBtns = modal.querySelectorAll('.remove-contact-btn');
      removeContactBtns.forEach(btn => {
          const contactoId = btn.closest('.contact-group').getAttribute('data-contacto-id');
          btn.addEventListener('click', function() {
              eliminarContacto(clienteId, contactoId, this.closest('.contact-group'));
          });
      });
  });
});

// Función auxiliar para obtener el token CSRF
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}




