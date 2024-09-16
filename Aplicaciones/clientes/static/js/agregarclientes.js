document.addEventListener('DOMContentLoaded', function() {
  const addContactBtn = document.getElementById('addContactBtnAdd');
  const contactsContainer = document.getElementById('contactsContainerAdd');

  function createContactInputGroup() {
      const newContactGroup = document.createElement('div');
      newContactGroup.className = 'flex items-center space-x-2';
      newContactGroup.innerHTML = `
          <select class="w-1/75 text-sm rounded-lg bg-gray-700 border-gray-600 text-white" name="tipo_contacto[]">
              <option value="1">Correo Electrónico</option>
              <option value="2">Teléfono</option>
              <option value="3">Página Web</option>
          </select>
          <input type="text" class="flex-1 text-sm rounded-lg bg-gray-700 border-gray-600 text-white" name="contacto[]" placeholder="Ingrese el contacto" required>
          <button type="button" class="flex-shrink-0 px-3 py-2 text-sm font-medium text-white bg-red-800 rounded-lg hover:bg-red-400 remove-contact-btn">-</button>
      `;
      return newContactGroup;
  }

  function addContact() {
      const newContactGroup = createContactInputGroup();
      contactsContainer.appendChild(newContactGroup);
  }

  if (addContactBtn) {
      addContactBtn.addEventListener('click', addContact);
  }

  // Event delegation for removing contact groups
  contactsContainer.addEventListener('click', function(e) {
      if (e.target && e.target.classList.contains('remove-contact-btn')) {
          e.target.closest('.flex.items-center.space-x-2').remove();
      }
  });
});