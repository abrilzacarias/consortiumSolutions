document.addEventListener("DOMContentLoaded", function() {
    function containsNumbers(str) {
        return /\d/.test(str);
    }

    function containsInvalidCharacters(str) {
        // Permite solo letras, números, espacios y el símbolo °
        const regex = /^[a-zA-Z0-9°\s]*$/;
        return !regex.test(str); // Si contiene caracteres no permitidos, devuelve true
    }


    // Función para mostrar un mensaje de validación
    function showValidationMessage(input, errorId, message) {
        const errorElement = document.getElementById(errorId);
        errorElement.textContent = message;
        errorElement.classList.remove('hidden');
        input.classList.add('border-red-500');
    }

    // Función para ocultar un mensaje de validación
    function hideValidationMessage(input, errorId) {
        const errorElement = document.getElementById(errorId);
        errorElement.textContent = '';
        errorElement.classList.add('hidden');
        input.classList.remove('border-red-500');
    }

    function isValidEmail(email) {
        // Expresión regular para validar el formato del correo electrónico
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    // Validación para el formulario de agregar cliente
    const agregarForm = document.querySelector("#agregarClienteForm");
    if (agregarForm) {
        const nombreInput = document.querySelector("#nombre_cliente");
        const apellidoInput = document.querySelector("#apellido_cliente");
        const cuilInput = document.querySelector("#cuitl_cliente");
        const claveInput = document.querySelector("#clave_afgip_cliente");
        const matriculaInput = document.querySelector("#matricula_cliente");
        const direccionInput = document.querySelector("#direccion_cliente"); // Campo de dirección
        const correoInput = document.querySelector("#correo_electronico"); // Campo de correo electrónico
        const today = new Date().toISOString().split('T')[0];
        const vencimientoMatriculaInput = document.querySelector("#vencimiento_matricula");
        vencimientoMatriculaInput.min = today;

        agregarForm.addEventListener("submit", function(event) {
            let isValid = true;

            // Validación de nombre
            if (containsNumbers(nombreInput.value)) {
                isValid = false;
                showValidationMessage(nombreInput, "errorNombre", "El nombre no puede contener números.");
            } else {
                hideValidationMessage(nombreInput, "errorNombre");
            }

            // Validación de apellido
            if (containsNumbers(apellidoInput.value)) {
                isValid = false;
                showValidationMessage(apellidoInput, "errorApellido", "El apellido no puede contener números.");
            } else {
                hideValidationMessage(apellidoInput, "errorApellido");
            }

            // Validación de dirección
            if (containsInvalidCharacters(direccionInput.value)) {
                isValid = false;
                showValidationMessage(direccionInput, "errorDireccion", "La dirección solo puede contener letras, números, espacios y el símbolo °.");
            } else {
                hideValidationMessage(direccionInput, "errorDireccion");
            }

            // Validación de CUIL/CUIT
            if (cuilInput.value.length !== 11 || isNaN(cuilInput.value)) {
                isValid = false;
                showValidationMessage(cuilInput, "errorCuitl", "El CUIL/CUIT debe tener exactamente 11 dígitos y no puede contener letras.");
            } else {
                hideValidationMessage(cuilInput, "errorCuitl");
            }

            // Validación de clave AFIP/AGIP
            if (claveInput.value.length !== 8 || isNaN(claveInput.value)) {
                isValid = false;
                showValidationMessage(claveInput, "errorClave", "La clave AFIP/AGIP debe tener exactamente 8 dígitos y no puede contener letras.");
            } else {
                hideValidationMessage(claveInput, "errorClave");
            }

            // Validación de matrícula
            if (matriculaInput.value.length !== 6 || isNaN(matriculaInput.value)) { 
                isValid = false;
                showValidationMessage(matriculaInput, "errorMatricula", "La matrícula debe tener exactamente 6 dígitos y no puede contener letras.");
            } else {
                hideValidationMessage(matriculaInput, "errorMatricula");
            }

            if (!isValidEmail(correoInput.value)) {
                isValid = false;
                showValidationMessage(correoInput, "errorCorreo", "El formato del correo electrónico no es válido.");
            } else {
                hideValidationMessage(correoInput, "errorCorreo");
            }

            // Previene el envío del formulario si hay errores
            if (!isValid) {
                event.preventDefault();
            }
        });

        // Validación en tiempo real para el nombre
        nombreInput.addEventListener("input", function() {
            if (containsNumbers(nombreInput.value)) {
                showValidationMessage(nombreInput, "errorNombre", "El nombre no puede contener números.");
            } else {
                hideValidationMessage(nombreInput, "errorNombre");
            }
        });

        // Validación en tiempo real para el apellido
        apellidoInput.addEventListener("input", function() {
            if (containsNumbers(apellidoInput.value)) {
                showValidationMessage(apellidoInput, "errorApellido", "El apellido no puede contener números.");
            } else {
                hideValidationMessage(apellidoInput, "errorApellido");
            }
        });

        // Validación en tiempo real para dirección
        direccionInput.addEventListener("input", function() {
            if (containsInvalidCharacters(direccionInput.value)) {
                showValidationMessage(direccionInput, "errorDireccion", "La dirección solo puede contener letras, números, espacios y el símbolo °.");
            } else {
                hideValidationMessage(direccionInput, "errorDireccion");
            }
        });

        // Validación en tiempo real para CUIL/CUIT
        cuilInput.addEventListener("input", function() {
            if (cuilInput.value.length !== 11 || isNaN(cuilInput.value)) {
                showValidationMessage(cuilInput, "errorCuitl", "El CUIL/CUIT debe tener exactamente 11 dígitos y no puede contener letras.");
            } else {
                hideValidationMessage(cuilInput, "errorCuitl");
            }
        });

        // Validación en tiempo real para clave
        claveInput.addEventListener("input", function() {
            if (claveInput.value.length !== 8 || isNaN(claveInput.value)) {
                showValidationMessage(claveInput, "errorClave", "La clave AFIP/AGIP debe tener exactamente 8 dígitos y no puede contener letras.");
            } else {
                hideValidationMessage(claveInput, "errorClave");
            }
        });

        // Validación en tiempo real para matrícula
        matriculaInput.addEventListener("input", function() {
            if (matriculaInput.value.length !== 6 || isNaN(matriculaInput.value)) { 
                showValidationMessage(matriculaInput, "errorMatricula", "La matrícula debe tener exactamente 6 dígitos y no puede contener letras.");
            } else {
                hideValidationMessage(matriculaInput, "errorMatricula");
            }
        });

        // Validación en tiempo real para correo electrónico
        correoInput.addEventListener("input", function() {
            if (!isValidEmail(correoInput.value)) {
                showValidationMessage(correoInput, "errorCorreo", "El formato del correo electrónico no es válido.");
            } else {
                hideValidationMessage(correoInput, "errorCorreo");
            }
        });
    } else {
        console.error("No se encontró el formulario con el id 'agregarClienteForm'");
    }

    // Validación para el formulario de editar cliente
    // Obtener todos los formularios de edición
    const editarForms = document.querySelectorAll('form[id^="editarClienteForm"]');

    editarForms.forEach(function(editarForm) {
        const clienteId = editarForm.id.replace('editarClienteForm', '');
        
        // Obtener los campos específicos para este formulario
        const nombreInputEditar = editarForm.querySelector(`#nombre_persona_${clienteId}`);
        const apellidoInputEditar = editarForm.querySelector(`#apellido_persona_${clienteId}`);
        const cuilInputEditar = editarForm.querySelector(`#cuitl_persona_${clienteId}`);
        const claveInputEditar = editarForm.querySelector(`#clave_afgip_cliente_${clienteId}`);
        const matriculaInputEditar = editarForm.querySelector(`#matricula_cliente_${clienteId}`);
        const direccionInputEditar = editarForm.querySelector(`#direccion_persona_${clienteId}`);
        const correoInputEditar = editarForm.querySelector(`input[name="descripcion_contacto_correo"]`);
        const vencimientoMatriculaEditar = editarForm.querySelector(`#vencimiento_matricula_${clienteId}`);

        // Establecer fecha mínima para vencimiento
        const today = new Date().toISOString().split('T')[0];
        if (vencimientoMatriculaEditar) {
            vencimientoMatriculaEditar.min = today;
        }

        // Validación al enviar el formulario
        editarForm.addEventListener("submit", function(event) {
            let isValid = true;

            // Validación de nombre
            if (nombreInputEditar && containsNumbers(nombreInputEditar.value)) {
                isValid = false;
                showValidationMessage(nombreInputEditar, `errorNombre_${clienteId}`, "El nombre no puede contener números.");
            } else if (nombreInputEditar) {
                hideValidationMessage(nombreInputEditar, `errorNombre_${clienteId}`);
            }

            // Validación de apellido
            if (apellidoInputEditar && containsNumbers(apellidoInputEditar.value)) {
                isValid = false;
                showValidationMessage(apellidoInputEditar, `errorApellido_${clienteId}`, "El apellido no puede contener números.");
            } else if (apellidoInputEditar) {
                hideValidationMessage(apellidoInputEditar, `errorApellido_${clienteId}`);
            }

            // Validación de dirección
            if (direccionInputEditar && containsInvalidCharacters(direccionInputEditar.value)) {
                isValid = false;
                showValidationMessage(direccionInputEditar, `errorDireccion_${clienteId}`, "La dirección solo puede contener letras, números, espacios y el símbolo °.");
            } else if (direccionInputEditar) {
                hideValidationMessage(direccionInputEditar, `errorDireccion_${clienteId}`);
            }

            // Validación de CUIL/CUIT
            if (cuilInputEditar && (cuilInputEditar.value.length !== 11 || isNaN(cuilInputEditar.value))) {
                isValid = false;
                showValidationMessage(cuilInputEditar, `errorCuitl_${clienteId}`, "El CUIL/CUIT debe tener exactamente 11 dígitos y no puede contener letras.");
            } else if (cuilInputEditar) {
                hideValidationMessage(cuilInputEditar, `errorCuitl_${clienteId}`);
            }

            // Validación de clave
            if (claveInputEditar && (claveInputEditar.value.length !== 8 || isNaN(claveInputEditar.value))) {
                isValid = false;
                showValidationMessage(claveInputEditar, `errorClave_${clienteId}`, "La clave AFIP/AGIP debe tener exactamente 8 dígitos y no puede contener letras.");
            } else if (claveInputEditar) {
                hideValidationMessage(claveInputEditar, `errorClave_${clienteId}`);
            }

            // Validación de matrícula
            if (matriculaInputEditar && (matriculaInputEditar.value.length !== 6 || isNaN(matriculaInputEditar.value))) {
                isValid = false;
                showValidationMessage(matriculaInputEditar, `errorMatricula_${clienteId}`, "La matrícula debe tener exactamente 6 dígitos y no puede contener letras.");
            } else if (matriculaInputEditar) {
                hideValidationMessage(matriculaInputEditar, `errorMatricula_${clienteId}`);
            }

            // Validación de correo
            if (correoInputEditar && !isValidEmail(correoInputEditar.value)) {
                isValid = false;
                showValidationMessage(correoInputEditar, `errorCorreoEditar${clienteId}`, "Por favor, introduce un correo electrónico válido.");
            } else if (correoInputEditar) {
                hideValidationMessage(correoInputEditar, `errorCorreoEditar${clienteId}`);
            }

            // Prevenir el envío si hay errores
            if (!isValid) {
                event.preventDefault();
            }
        });

        // Validaciones en tiempo real
        if (nombreInputEditar) {
            nombreInputEditar.addEventListener("input", function() {
                if (containsNumbers(this.value)) {
                    showValidationMessage(this, `errorNombre_${clienteId}`, "El nombre no puede contener números.");
                } else {
                    hideValidationMessage(this, `errorNombre_${clienteId}`);
                }
            });
        }

        if (apellidoInputEditar) {
            apellidoInputEditar.addEventListener("input", function() {
                if (containsNumbers(this.value)) {
                    showValidationMessage(this, `errorApellido_${clienteId}`, "El apellido no puede contener números.");
                } else {
                    hideValidationMessage(this, `errorApellido_${clienteId}`);
                }
            });
        }

        if (direccionInputEditar) {
            direccionInputEditar.addEventListener("input", function() {
                if (containsInvalidCharacters(this.value)) {
                    showValidationMessage(this, `errorDireccion_${clienteId}`, "La dirección solo puede contener letras, números, espacios y el símbolo °.");
                } else {
                    hideValidationMessage(this, `errorDireccion_${clienteId}`);
                }
            });
        }

        if (cuilInputEditar) {
            cuilInputEditar.addEventListener("input", function() {
                if (this.value.length !== 11 || isNaN(this.value)) {
                    showValidationMessage(this, `errorCuitl_${clienteId}`, "El CUIL/CUIT debe tener exactamente 11 dígitos y no puede contener letras.");
                } else {
                    hideValidationMessage(this, `errorCuitl_${clienteId}`);
                }
            });
        }

        if (claveInputEditar) {
            claveInputEditar.addEventListener("input", function() {
                if (this.value.length !== 8 || isNaN(this.value)) {
                    showValidationMessage(this, `errorClave_${clienteId}`, "La clave AFIP/AGIP debe tener exactamente 8 dígitos y no puede contener letras.");
                } else {
                    hideValidationMessage(this, `errorClave_${clienteId}`);
                }
            });
        }

        if (matriculaInputEditar) {
            matriculaInputEditar.addEventListener("input", function() {
                if (this.value.length !== 6 || isNaN(this.value)) {
                    showValidationMessage(this, `errorMatricula_${clienteId}`, "La matrícula debe tener exactamente 6 dígitos y no puede contener letras.");
                } else {
                    hideValidationMessage(this, `errorMatricula_${clienteId}`);
                }
            });
        }

        // Validación en tiempo real para correo electrónico editar
        if (correoInputEditar) {
            correoInputEditar.addEventListener("input", function() {
                if (!isValidEmail(this.value)) {
                    showValidationMessage(this, `errorCorreoEditar${clienteId}`, "El formato del correo electrónico no es válido.");
                } else {
                    hideValidationMessage(this, `errorCorreoEditar${clienteId}`);
                }
            });
        }
    });

    // Validación para el formulario de agregar edificio
    const agregarEdificioForm = document.querySelector("#agregarEdificioForm");
    if (agregarEdificioForm) {
        const nombreEdificioInput = agregarEdificioForm.querySelector("#nombre_edificio");
        const direccionEdificioInput = agregarEdificioForm.querySelector("#direccion_edificio");
        const cuilEdificioInput = agregarEdificioForm.querySelector("#cuit_edificio");

        agregarEdificioForm.addEventListener("submit", function(event) {
            let isValid = true;

            // Validación en tiempo real para nombre de edificio
            if (containsInvalidCharacters(nombreEdificioInput.value)) {
                isValid = false;
                showValidationMessage(nombreEdificioInput, "errorNombreEdificio", "El nombre del edificio solo puede contener letras, números, espacios y el símbolo °.");
            } else {
                hideValidationMessage(nombreEdificioInput, "errorNombreEdificio");
            }

            // Validación de dirección
            if (containsInvalidCharacters(direccionEdificioInput.value)) {
                isValid = false;
                showValidationMessage(direccionEdificioInput, "errorDireccionEdificio", "La dirección solo puede contener letras, números, espacios y el símbolo °.");
            } else {
                hideValidationMessage(direccionEdificioInput, "errorDireccionEdificio");
            }

            // Validación de CUIL/CUIT
            if (cuilEdificioInput.value.length !== 11 || isNaN(cuilEdificioInput.value)) {
                isValid = false;
                showValidationMessage(cuilEdificioInput, "errorCuitl", "El CUIL/CUIT debe tener exactamente 11 dígitos y no puede contener letras.");
            } else {
                hideValidationMessage(cuilEdificioInput, "errorCuitl");
            }

            // Previene el envío del formulario si hay errores
            if (!isValid) {
                event.preventDefault();
            }
        });

        // Validación en tiempo real para nombre de edificio
        if (nombreEdificioInput) {
            nombreEdificioInput.addEventListener("input", function() {
                console.log("Valor ingresado:", this.value); // Muestra lo que el usuario ingresa
                if (containsInvalidCharacters(this.value)) {
                    showValidationMessage(this, "errorNombreEdificio", "El nombre del edificio solo puede contener letras, números, espacios y el símbolo °.");
                } else {
                    hideValidationMessage(this, "errorNombreEdificio");
                }
            });
        }

        // Validación en tiempo real para dirección de edificio
        if (direccionEdificioInput) {
            direccionEdificioInput.addEventListener("input", function() {
                if (containsInvalidCharacters(this.value)) {
                    showValidationMessage(this, "errorDireccionEdificio", "La dirección solo puede contener letras, números, espacios y el símbolo °.");
                } else {
                    hideValidationMessage(this, "errorDireccionEdificio");
                }
            });
        }

        if (cuilEdificioInput) {
            cuilEdificioInput.addEventListener("input", function() {
                console.log("Valor actual del CUIT:", this.value);
        
                // Validación usando expresión regular
                if (!/^\d{11}$/.test(this.value)) {
                    showValidationMessage(this, "errorCuitl", "El CUIL/CUIT debe tener exactamente 11 dígitos numéricos.");
                } else {
                    hideValidationMessage(this, "errorCuitl");
                }
            });
        }
          
        
    } else {
        console.error("No se encontró el formulario con el id 'agregarEdificioForm'");
    }
        
});
