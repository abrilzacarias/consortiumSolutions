document.addEventListener('DOMContentLoaded', function() {
    // Función para crear un nuevo grupo de contacto en agregar nuevo empleado
    const crearGrupoInputContactoAgregar = (idUnico) => `
        <div class="flex items-center space-x-2 contact-group" data-contacto-id="${idUnico}">
            <select class="w-1/75 text-sm rounded-lg bg-gray-700 border-gray-600 text-white" 
                    name="tipo_contacto[]"
                    onchange="validarContacto(this.nextElementSibling)">
                <option value="1">Correo Electrónico</option>
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
                <option value="1" ${tipoContactoId == 1 ? 'selected' : ''}>Correo Electrónico</option>
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
    // Función modificada para agregar un nuevo contacto
    const agregarContacto = (containerId, isEditMode = false, existingContact = {}) => {
        console.log('Agregando nuevo contacto');
        const contenedorContactos = document.getElementById(containerId);
        if (contenedorContactos) {
            const idUnico = `temp-${Date.now()}`;
            const nuevoGrupoContactoHTML = isEditMode 
                ? crearGrupoInputContactoEditar(idUnico, existingContact.tipo || '', existingContact.descripcion || '')
                : crearGrupoInputContactoAgregar(idUnico);

            // Crear un elemento div temporal para parsear el HTML
            const tempDiv = document.createElement('div');
            tempDiv.innerHTML = nuevoGrupoContactoHTML;

            // Obtener el primer (y único) hijo del div temporal
            const nuevoGrupoContacto = tempDiv.firstElementChild;

            // Añadir el nuevo grupo de contacto al contenedor
            contenedorContactos.appendChild(nuevoGrupoContacto);

            console.log('Nuevo contacto agregado al DOM');

            // Añadir event listeners al nuevo grupo de contacto
            const nuevoSelect = nuevoGrupoContacto.querySelector('select');
            const nuevoInput = nuevoGrupoContacto.querySelector('input');

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

    // Función para añadir un solo event listener a un botón
    const addSingleEventListener = (button, containerId, isEditMode) => {
        if (button && !button.hasAttribute('data-listener-added')) {
            button.addEventListener('click', (e) => {
                e.preventDefault(); // Prevenir comportamiento por defecto
                e.stopPropagation(); // Detener propagación del evento
                agregarContacto(containerId, isEditMode);
            });
            button.setAttribute('data-listener-added', 'true');
        }
    };

   
    // Event listener modificado para el botón de agregar contacto
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
        document.querySelectorAll('[id^="editarClienteModal_"]').forEach(modal => {
            const clienteId = modal.id.split('_')[1];
            const addContactBtn = document.getElementById(`addContactBtnAdd${clienteId}`);
            const contactsContainer = document.getElementById(`contactsContainerAdd${clienteId}`);

            if (addContactBtn && contactsContainer) {
                addSingleEventListener(addContactBtn, `contactsContainerAdd${clienteId}`, true);
                agregarValidacionExistente(`contactsContainerAdd${clienteId}`);
            }
        });

        // Inicializar el modal de agregar nuevo empleado
        const addContactBtnGeneral = document.getElementById('addContactBtnAdd');
        const contactsContainerGeneral = document.getElementById('contactsContainerAdd');

        if (addContactBtnGeneral && contactsContainerGeneral) {
            addSingleEventListener(addContactBtnGeneral, 'contactsContainerAdd', false);
            agregarValidacionExistente('contactsContainerAdd');
        } else {
            console.log('Botón o contenedor no encontrados.');
        }
    };

    // Llamar a inicializarModales al final del DOMContentLoaded
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

    document.querySelectorAll('#agregarClienteForm').forEach(form => {
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
            return fetch(`/empleados/eliminarContactoCliente/${contactoId}/`, {
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
