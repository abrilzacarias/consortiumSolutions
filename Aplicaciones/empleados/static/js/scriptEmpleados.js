document.addEventListener('DOMContentLoaded', function() {
    console.log('Script iniciado');
    
    // Manejar la apertura del modal
    const editButtons = document.querySelectorAll('[data-modal-target^="editarEmpleadoModal_"]');
    console.log('Botones encontrados:', editButtons.length);
    
    editButtons.forEach(button => {
        const modalId = button.getAttribute('data-modal-target');
        console.log('Buscando modal:', modalId);
        const modal = document.getElementById(modalId);
        
        if (modal) {
            console.log('Modal encontrado:', modalId);
            const modalInstance = new Modal(modal);
            
            button.addEventListener('click', () => {
                console.log('Botón clickeado para modal:', modalId);
                modalInstance.show();
            });
            
            // Manejar el cierre del modal
            const closeButton = modal.querySelector('[data-modal-hide]');
            if (closeButton) {
                closeButton.addEventListener('click', () => {
                    console.log('Botón de cierre clickeado para modal:', modalId);
                    modalInstance.hide();
                });
            }
        }
    });
});
