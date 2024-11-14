document.addEventListener("DOMContentLoaded", function() {
    function containsNumbers(str) {
        return /\d/.test(str);
    }

    function containsInvalidCharacters(str) {
        // Permite solo letras, números, espacios y el símbolo °
        const regex = /^[a-zA-Z0-9°\s]*$/;
        return !regex.test(str); // Si contiene caracteres no permitidos, devuelve true
    }

    function containsOnlyLettersAndAccents(value) {
        // Expresión regular que permite únicamente letras (con tildes) y espacios
        const regex = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$/;
        return regex.test(value);
    }

    // Función para mostrar el mensaje de validación
    function showValidationMessage(inputElement, errorElementId, message) {
        const errorElement = document.getElementById(errorElementId);
        if (errorElement) {
            errorElement.textContent = message;
            errorElement.classList.remove("hidden");  // Muestra el mensaje de error
            inputElement.classList.add("border-red-500"); // Agrega un borde rojo al campo
        }
    }

    // Función para ocultar el mensaje de validación
    function hideValidationMessage(inputElement, errorElementId) {
        const errorElement = document.getElementById(errorElementId);
        if (errorElement) {
            errorElement.textContent = "";
            errorElement.classList.add("hidden"); // Oculta el mensaje de error
            inputElement.classList.remove("border-red-500"); // Remueve el borde rojo del campo
        }
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
            // Validación del campo de nombre
            if (!containsOnlyLettersAndAccents(nombreInput.value)) {
                isValid = false;
                showValidationMessage(nombreInput, "errorNombre", "El nombre solo puede contener letras y tildes.");
            } else {
                hideValidationMessage(nombreInput, "errorNombre");
            }

            // Validación de apellido
            if (!containsOnlyLettersAndAccents(apellidoInput.value)) {
                isValid = false;
                showValidationMessage(apellidoInput, "errorApellido", "El apellido solo puede contener letras y tildes.");
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
        nombreInput.addEventListener('input', function() {
            if (!containsOnlyLettersAndAccents(this.value.trim())) {
                showValidationMessage(this, "errorNombre", "El nombre solo puede contener letras y tildes.");
            } else {
                hideValidationMessage(this, "errorNombre");
            }
        });

        // Validación en tiempo real para el apellido
        apellidoInput.addEventListener("input", function() {
            if (!containsOnlyLettersAndAccents(apellidoInput.value)) {
                showValidationMessage(apellidoInput, "errorApellido", "El apellido solo puede contener letras y tildes.");
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
            if (nombreInputEditar && !containsOnlyLettersAndAccents(nombreInputEditar.value)) {
                isValid = false;
                showValidationMessage(nombreInputEditar, `errorNombre_${clienteId}`, "El nombre solo puede contener letras y tildes.");
            } else if (nombreInputEditar) {
                hideValidationMessage(nombreInputEditar, `errorNombre_${clienteId}`);
            }

            // Validación de apellido
            if (apellidoInputEditar && !containsOnlyLettersAndAccents(apellidoInputEditar.value)) {
                isValid = false;
                showValidationMessage(apellidoInputEditar, `errorApellido_${clienteId}`, "El solo puede contener letras y tildes.");
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
                if (!containsOnlyLettersAndAccents(this.value)) {
                    showValidationMessage(this, `errorNombre_${clienteId}`, "El nombre solo puede contener letras y tildes.");
                } else {
                    hideValidationMessage(this, `errorNombre_${clienteId}`);
                }
            });
        }

        if (apellidoInputEditar) {
            apellidoInputEditar.addEventListener("input", function() {
                if (!containsOnlyLettersAndAccents(this.value)) {
                    showValidationMessage(this, `errorApellido_${clienteId}`, "El apellido solo puede contener letras y tildes.");
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
            if (cuilEdificioInput.value.length !== 11 || isNaN(cuilInput.value)) {
                isValid = false;
                showValidationMessage(cuilInput, "errorCuitlEdificio", "El CUIL/CUIT debe tener exactamente 11 dígitos y no puede contener letras.");
            } else {
                hideValidationMessage(cuilInput, "errorCuitlEdificio");
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
        
                // Validación usando expresión regular para solo números y longitud de 11 caracteres
                if (cuilEdificioInput.value.length !== 11 || isNaN(cuilEdificioInput.value)) {
                    showValidationMessage(cuilEdificioInput, "errorCuitlEdificio", "El CUIL/CUIT debe tener exactamente 11 dígitos y no puede contener letras.");
                } else {
                    hideValidationMessage(cuilEdificioInput, "errorCuitlEdificio");
                }
            });
        }
        
    } else {
        console.error("No se encontró el formulario con el id 'agregarEdificioForm'");
    }
        
    const editarEdificioForms = document.querySelectorAll('form[id^="editarEdificioModal_"]');

    editarEdificioForms.forEach(function(editarForm) {
        const edificioId = editarForm.id.replace('editarEdificioModal_', '');
        
        const nombreEdificioInput = editarForm.querySelector(`#nombre_edificio_${edificioId}`);
        const direccionEdificioInput = editarForm.querySelector(`#direccion_edificio_${edificioId}`);
        const cuitEdificioInput = editarForm.querySelector(`#cuit_edificio_${edificioId}`);
    
        // Validación cuando se envía el formulario
        editarForm.addEventListener("submit", function(event) {
            let isValid = true;
    
            // Validación en tiempo real para nombre de edificio
            if (containsInvalidCharacters(nombreEdificioInput.value)) {
                isValid = false;
                showValidationMessage(nombreEdificioInput, `errorNombre_${edificioId}`, "El nombre del edificio solo puede contener letras, números, espacios y el símbolo °.");
            } else {
                hideValidationMessage(nombreEdificioInput, `errorNombre_${edificioId}`);
            }
    
            // Validación de dirección
            if (containsInvalidCharacters(direccionEdificioInput.value)) {
                isValid = false;
                showValidationMessage(direccionEdificioInput, `errorDirecion_${edificioId}`, "La dirección solo puede contener letras, números, espacios y el símbolo °.");
            } else {
                hideValidationMessage(direccionEdificioInput, `errorDirecion_${edificioId}`);
            }
    
            // Validación de CUIL/CUIT
            if (cuitEdificioInput.value.length !== 11 || isNaN(cuitEdificioInput.value)) {
                isValid = false;
                showValidationMessage(cuitEdificioInput, `errorCuit_${edificioId}`, "El CUIL/CUIT debe tener exactamente 11 dígitos y no puede contener letras.");
            } else {
                hideValidationMessage(cuitEdificioInput, `errorCuit_${edificioId}`);
            }
    
            // Previene el envío del formulario si hay errores
            if (!isValid) {
                event.preventDefault();
            }
        });
    
        // Validación en tiempo real para el nombre de edificio
        nombreEdificioInput.addEventListener("input", function() {
            if (containsInvalidCharacters(this.value)) {
                showValidationMessage(this, `errorNombre_${edificioId}`, "El nombre del edificio solo puede contener letras, números, espacios y el símbolo °.");
            } else {
                hideValidationMessage(this, `errorNombre_${edificioId}`);
            }
        });
    
        // Validación en tiempo real para la dirección de edificio
        direccionEdificioInput.addEventListener("input", function() {
            if (containsInvalidCharacters(this.value)) {
                showValidationMessage(this, `errorDirecion_${edificioId}`, "La dirección solo puede contener letras, números, espacios y el símbolo °.");
            } else {
                hideValidationMessage(this, `errorDirecion_${edificioId}`);
            }
        });
    
        // Validación en tiempo real para el CUIL/CUIT
        cuitEdificioInput.addEventListener("input", function() {
            if (cuitEdificioInput.value.length !== 11 || isNaN(cuitEdificioInput.value)) {
                showValidationMessage(cuitEdificioInput, `errorCuit_${edificioId}`, "El CUIL/CUIT debe tener exactamente 11 dígitos y no puede contener letras.");
            } else {
                hideValidationMessage(cuitEdificioInput, `errorCuit_${edificioId}`);
            }
        });
    
    });
    
});
