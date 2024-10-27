//para mostrar el mensaje de exito o error al agregar
function showModal() {
    const modal = document.getElementById('small-modal');
    modal.classList.remove('hidden');
}

function hideModal() {
    const modal = document.getElementById('small-modal');
    modal.classList.add('hidden');
}

document.addEventListener('DOMContentLoaded', function () {
    const messagesData = document.getElementById('messages-data');
    const hasMessages = messagesData.dataset.hasMessages === 'true';
    
    if (hasMessages) {
        showModal();
    }

    const closeButtons = document.querySelectorAll('[data-modal-hide="small-modal"]');
    closeButtons.forEach(button => {
        button.addEventListener('click', hideModal);
    });

    window.addEventListener('click', function(event) {
        const modal = document.getElementById('small-modal');
        if (event.target === modal) {
            hideModal();
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    // Función para crear un nuevo grupo de contacto en agregar nuevo empleado
    const crearGrupoInputContactoAgregar = (idUnico) => `
        <div class="flex items-center space-x-2 contact-group" data-contacto-id="${idUnico}">
            <select class="w-1/75 text-sm rounded-lg bg-gray-700 border-gray-600 text-white" 
                    name="tipo_contacto[]"
                    onchange="validarContacto(this.nextElementSibling)">
                <option value="2">Teléfono</option>
                <option value="3">Página Web</option>
            </select>
            <input type="text" 
                class="flex-1 text-sm rounded-lg bg-gray-700 border-gray-600 text-white" 
                name="contacto[]" 
                placeholder="Ingrese el contacto" 
                required 
                oninput="validarContacto(this)">
            <button type="button" 
                    class="flex-shrink-0 px-3 py-2 text-sm font-medium text-white bg-red-800 rounded-lg hover:bg-red-400 remove-contact-btn"
                    data-contacto-id="${idUnico}">-</button>
            <div class="text-red-500 text-sm font-semibold mt-1 hidden"></div>
        </div>
    `;

    // Función para crear un nuevo grupo de contacto en editar empleado
    const crearGrupoInputContactoEditar = (idContacto, tipoContactoId, descripcionContacto) => `
        <div class="flex items-center space-x-2 contact-group" data-contacto-id="${idContacto}">
            <select class="w-1/75 text-sm rounded-lg bg-gray-700 border-gray-600 text-white" 
                    name="tipo_contacto_${idContacto}"
                    onchange="validarContacto(this.nextElementSibling)">
                <option value="2" ${tipoContactoId == 2 ? 'selected' : ''}>Teléfono</option>
                <option value="3" ${tipoContactoId == 3 ? 'selected' : ''}>Página Web</option>
            </select>
            <input type="text" 
                class="flex-1 text-sm rounded-lg bg-gray-700 border-gray-600 text-white" 
                name="contacto_${idContacto}" 
                value="${descripcionContacto || ''}" 
                required 
                oninput="validarContacto(this)">
            <button type="button" 
                    class="flex-shrink-0 px-3 py-2 text-sm font-medium text-white bg-red-800 rounded-lg hover:bg-red-400 remove-contact-btn"
                    data-contacto-id="${idContacto}">-</button>
            <div class="text-red-500 text-sm font-semibold mt-1 hidden"></div>
        </div>
    `;

    // Función de validación de contacto
    window.validarContacto = function(input) {
        const grupoContacto = input.closest('.contact-group');
        if (!grupoContacto) return false;

        const tipoContacto = grupoContacto.querySelector('select').value;
        const valorContacto = input.value.trim();
        let divError = grupoContacto.nextElementSibling;

        // Si no existe el div de error, lo creamos
        if (!divError || !divError.classList.contains('text-red-500')) {
            divError = document.createElement('div');
            divError.className = 'text-red-500 text-sm font-semibold mt-1 hidden';
            grupoContacto.parentNode.insertBefore(divError, grupoContacto.nextSibling);
        }

        let esValido = true;
        let mensajeError = '';

        switch (tipoContacto) {
            case '1': // Correo Electrónico
                const regexEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (!regexEmail.test(valorContacto)) {
                    esValido = false;
                    mensajeError = 'Ingrese un correo electrónico válido.';
                }
                break;
            case '2': // Teléfono
                const regexTelefono = /^[+]?[\d\s()-]+$/;
                if (!regexTelefono.test(valorContacto)) {
                    esValido = false;
                    mensajeError = 'Ingrese un número de teléfono válido (solo números, +, espacios, guiones y paréntesis).';
                }
                break;
            case '3': // Página Web
                const regexUrl = /^https?:\/\/.+/i;
                if (!regexUrl.test(valorContacto)) {
                    esValido = false;
                    mensajeError = 'La página web debe comenzar con http:// o https://';
                }
                break;
        }

        if (!esValido && valorContacto !== '') {
            divError.textContent = mensajeError;
            divError.classList.remove('hidden');
            input.classList.add('border-red-500');
        } else {
            divError.classList.add('hidden');
            input.classList.remove('border-red-500');
        }

        return esValido;
    };

    // Función para agregar un nuevo contacto
    const agregarContacto = (containerId, isEditMode = false, existingContact = {}) => {
        console.log('Agregando nuevo contacto');
        const contenedorContactos = document.getElementById(containerId);
        if (contenedorContactos) {
            const idUnico = `temp-${Date.now()}`;
            const nuevoGrupoContactoHTML = isEditMode 
                ? crearGrupoInputContactoEditar(idUnico, existingContact.tipo || '', existingContact.descripcion || '')
                : crearGrupoInputContactoAgregar(idUnico);
        
            // Crear un nuevo div a partir del HTML generado
            const nuevoGrupoContacto = document.createElement('div');
            nuevoGrupoContacto.innerHTML = nuevoGrupoContactoHTML;
        
            // Append the newly created contact group to the container
            contenedorContactos.appendChild(nuevoGrupoContacto.firstElementChild);
        
            console.log('Nuevo contacto agregado al DOM');
        
            // Re-seleccionar los elementos del DOM
            const nuevoGrupoAgregado = contenedorContactos.querySelector(`[data-contacto-id="${idUnico}"]`);
            const nuevoSelect = nuevoGrupoAgregado.querySelector('select');
            const nuevoInput = nuevoGrupoAgregado.querySelector('input');
        
            if (nuevoSelect && nuevoInput) {
                nuevoSelect.addEventListener('change', () => validarContacto(nuevoInput));
                nuevoInput.addEventListener('input', () => validarContacto(nuevoInput));
                console.log('Event listeners agregados correctamente');
            } else {
                console.log('Error al agregar los event listeners');
            }
        } else {
            console.log('Contenedor de contactos no encontrado');
        }
    };

    // Event listener para el botón de agregar contacto
    document.addEventListener('click', function(e) {
        if (e.target && e.target.classList.contains('add-contact-btn')) {
            const containerId = e.target.getAttribute('data-container-id');
            const isEditMode = e.target.getAttribute('data-edit-mode') === 'true';
            agregarContacto(containerId, isEditMode);
        }
    });

    // Event listener para eliminar contactos (usando delegación de eventos)
    document.addEventListener('click', function(e) {
        if (e.target && e.target.classList.contains('remove-contact-btn')) {
            const contactoId = e.target.getAttribute('data-contacto-id');
            console.log('ID del contacto para eliminar:', contactoId); // Verifica el ID del contacto
            if (contactoId) {
                eliminarContactoDirecto(e.target)
                    .then(() => {
                        // Eliminar el grupo de contacto del DOM después de una eliminación exitosa
                        const grupoContacto = e.target.closest('.contact-group');
                        if (grupoContacto) {
                            grupoContacto.remove();
                            const divError = grupoContacto.nextElementSibling;
                            if (divError) divError.remove();
                        }
                    })
                    .catch(error => {
                        console.error('Error al eliminar el contacto:', error);
                    });
            } else {
                console.error('ID del contacto no encontrado');
            }
        }
    });

    // Agregar validación a los contactos existentes
    const agregarValidacionExistente = (containerId) => {
        document.querySelectorAll(`#${containerId} select`).forEach(select => {
            select.addEventListener('change', function() {
                validarContacto(this.nextElementSibling);
            });
        });

        document.querySelectorAll(`#${containerId} input[name^="contacto_"]`).forEach(input => {
            input.addEventListener('input', function() {
                validarContacto(this);
            });
        });
    };

    // Inicializar modales de edición y agregar contacto
    const inicializarModales = () => {
        // Inicializar modales de edición
        document.querySelectorAll('[id^="editarEmpleadoModal_"]').forEach(modal => {
            const empleadoId = modal.id.split('_')[1];
            const addContactBtn = document.getElementById(`addContactBtnAdd${empleadoId}`);
            const contactsContainer = document.getElementById(`contactsContainerAdd${empleadoId}`);

            if (addContactBtn && contactsContainer) {
                addContactBtn.addEventListener('click', () => agregarContacto(`contactsContainerAdd${empleadoId}`, true));
                agregarValidacionExistente(`contactsContainerAdd${empleadoId}`);
            }
        });

        // Inicializar el modal de agregar nuevo empleado
        const addContactBtnGeneral = document.getElementById('addContactBtnAdd');
        const contactsContainerGeneral = document.getElementById('contactsContainerAdd'); // Contenedor de contactos del formulario general

        if (addContactBtnGeneral && contactsContainerGeneral) {
            addContactBtnGeneral.addEventListener('click', () => {
                console.log('Botón de agregar contacto clickeado');
                agregarContacto('contactsContainerAdd');
            });
        
            agregarValidacionExistente('contactsContainerAdd');
        } else {
            console.log('Botón o contenedor no encontrados.');
        }
    };

    // Inicializar todos los modales y el botón general
    inicializarModales();

    // Validación del formulario antes de enviar
    const validarFormulario = (form) => {
        let formularioValido = true;

        // Validar todos los contactos
        form.querySelectorAll('.contact-group input[name^="contacto_"]').forEach(input => {
            if (!validarContacto(input)) {
                formularioValido = false;
            }
        });

        return formularioValido;
    };

    document.querySelectorAll('#empleadoForm').forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            if (validarFormulario(this)) {
                this.submit();
            }
        });
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
    function eliminarContactoDirecto(buttonElement) {
        console.log("Iniciando proceso de eliminación");
    
        const contactoId = buttonElement.getAttribute('data-contacto-id');
        console.log('ID del contacto:', contactoId); // Verifica el ID del contacto
    
        // Verificar si el ID es temporal
        if (contactoId.startsWith('temp-')) {
            console.log('ID temporal detectado. Eliminando del DOM.');
            // Eliminar el contacto solo del DOM
            const grupoContacto = buttonElement.closest('.contact-group');
            if (grupoContacto) {
                grupoContacto.remove();
                const divError = grupoContacto.nextElementSibling;
                if (divError) divError.remove();
            }
            return Promise.resolve(); // No se hace una solicitud al servidor para IDs temporales
        }
    
        // ID válido, proceder con la eliminación del servidor
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
    }
    
});
