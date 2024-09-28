document.addEventListener('DOMContentLoaded', function() {
    // Obtiene todos los botones de filtro
    const botonesFiltro = document.querySelectorAll('.btn-filtro');

    // Itera sobre cada botón y añade un evento de clic
    botonesFiltro.forEach(function(boton) {
        boton.addEventListener('click', function() {
            const filtro = this.getAttribute('data-filtro'); // Obtiene el filtro del botón
            filtrarTabla(filtro);
        });
    });

    function filtrarTabla(filtro) {
        // Obtiene todas las filas de la tabla
        const filas = document.querySelectorAll('#tabla-resultados tr');

        filas.forEach(function(fila) {
            const tipoActividad = fila.getAttribute('data-tipo'); // Obtiene el tipo de actividad de cada fila
            
            // Mostrar todas las filas si el filtro es 'todos'
            if (filtro === 'Todos') {
                fila.style.display = ''; // Muestra la fila
            } else {
                // Mostrar solo las filas que coincidan con el filtro
                if (tipoActividad === filtro) {
                    fila.style.display = ''; // Muestra la fila
                } else {
                    fila.style.display = 'none'; // Oculta la fila
                }
            }
        });
    }
});