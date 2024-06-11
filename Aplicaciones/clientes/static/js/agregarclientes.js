// In your Javascript (external .js resource or <script> tag)
$(document).ready(function() {
  $('.js-example-basic-single').select2({
    width: '100%', // need to override the changed default
    height: '100%'
  });
});

document.addEventListener("DOMContentLoaded", () => {
    // Function to create a new contact input group for adding a new vendor
  const createContactInputGroupAdd = () => {
    const newContactAdd = document.createElement('div');
    newContactAdd.className = 'input-group mb-3';


    newContactAdd.innerHTML = `
      <select class="form-control bg-dark text-light" name="tipo_contacto[]">
        <option value="1">Correo Electrónico</option>
        <option value="2">Teléfono</option>
        <option value="3">URL</option>
      </select>
      <input type="text" class="form-control" name="contacto[]" placeholder="Ingrese el contacto" required>
      <button type="button" class="btn btn-danger remove-contact-btn">-</button>
    `;

    // Add event listener to the remove button
    newContactAdd.querySelector('.remove-contact-btn').addEventListener('click', () => {
      newContactAdd.parentElement.removeChild(newContactAdd);
    });

    return newContactAdd;
  };

  // Event listener to add a new contact input group for adding a new vendor
  const addContactBtnAdd = document.getElementById('addContactBtnAdd');
  const contactsContainerAdd = document.getElementById('contactsContainerAdd');
  addContactBtnAdd.addEventListener('click', () => {
    const newContact = createContactInputGroupAdd();
    contactsContainerAdd.appendChild(newContact);
  });
})