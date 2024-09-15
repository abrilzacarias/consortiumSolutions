document.addEventListener('DOMContentLoaded', function() {
    // Función para crear un nuevo grupo de contacto con estilo Tailwind
    const createContactInputGroup = (empleadoId, contactoId = '', tipoContacto = '', descripcionContacto = '') => {
        const uniqueId = contactoId || `temp-${Date.now()}`; // ID único para nuevos contactos
        return `
            <div class="flex items-center space-x-2 contact-group" data-contacto-id="${uniqueId}">
                <select class="w-3/4 text-sm rounded-lg bg-gray-700 border-gray-600 text-white" name="tipo_contacto_${uniqueId}">
                    <option value="1" ${tipoContacto === '1' ? 'selected' : ''}>Correo Electrónico</option>
                    <option value="2" ${tipoContacto === '2' ? 'selected' : ''}>Teléfono</option>
                    <option value="3" ${tipoContacto === '3' ? 'selected' : ''}>Página Web</option>
                </select>
                <input type="text" class="flex-1 text-sm rounded-lg bg-gray-700 border-gray-600 text-white" name="contacto_${uniqueId}" placeholder="Ingrese el contacto" value="${descripcionContacto}" required>
                <button type="button" class="flex-shrink-0 px-3 py-2 text-sm font-medium text-white bg-red-800 rounded-lg hover:bg-red-400 remove-contact-btn" data-contacto-id="${uniqueId}">-</button>
            </div>
        `;
    };
    // Función para agregar un nuevo contacto
    const addContact = (empleadoId) => {
        const contactsContainer = document.getElementById(`contactsContainerAdd${empleadoId}`);
        if (contactsContainer) {
            const newContactGroup = document.createElement('div');
            newContactGroup.innerHTML = createContactInputGroup(empleadoId);
            contactsContainer.appendChild(newContactGroup.firstElementChild);
        }
    };

    // Agregar event listeners para los botones de agregar contacto
    document.querySelectorAll('[id^="addContactBtnAdd"]').forEach(button => {
        const empleadoId = button.id.replace('addContactBtnAdd', '');
        button.addEventListener('click', () => addContact(empleadoId));
    });

    // Eliminar contacto (usando event delegation)
    document.addEventListener('click', function(e) {
        if (e.target && e.target.classList.contains('remove-contact-btn')) {
            const contactGroup = e.target.closest('.contact-group');
            const contactoId = e.target.getAttribute('data-contacto-id');

            if (contactoId && !contactoId.startsWith('temp-')) { // Evita enviar al backend si es un contacto nuevo
                eliminarContactoDirecto(e.target).then(() => {
                    contactGroup.remove(); // Eliminar del DOM tras confirmación del backend
                }).catch(error => {
                    console.error('Error al eliminar el contacto:', error);
                });
            } else {
                console.log('Contacto temporal, eliminado solo del DOM.');
                contactGroup.remove(); // Eliminar del DOM si es nuevo y no está en la base de datos
            }
        }
    });

    // Función para obtener el token CSRF
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

    // Función para eliminar un contacto directamente
    window.eliminarContactoDirecto = function(buttonElement) {
        console.log("Iniciando proceso de eliminación");

        const contactoId = buttonElement.getAttribute('data-contacto-id');
        console.log('ID del contacto:', contactoId); // Verifica el ID del contacto
        const csrftoken = getCookie('csrftoken');

        if (contactoId && confirm("¿Está seguro de que desea eliminar este contacto?")) {
            return fetch(`/empleados/eliminarContactoEmpleado/${contactoId}/`, {
                method: 'DELETE',
                headers: {
                    'X-CSRFToken': csrftoken
                }
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Error al eliminar el contacto.');
                }
                return response;
            });
        } else {
            console.error('ID del contacto no encontrado o eliminación cancelada.');
            return Promise.reject('Eliminación cancelada o ID no válido');
        }
    };
});
