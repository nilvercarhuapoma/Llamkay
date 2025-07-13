// ==== Modal de edición ====
function editProfile() {
    openEditProfileModal();
}
window.editProfile = editProfile;

function openEditProfileModal() {
    const modal = document.getElementById('editProfileModal');
    if (modal) {
        modal.style.display = 'flex';
        modal.classList.add('show');
    } else {
        console.error('❌ No se encontró el modal de edición');
    }
}

function cerrarModalEdicion() {
    const modal = document.getElementById('editProfileModal');
    if (modal) {
        modal.style.display = 'none';
        modal.classList.remove('show');
    }
}

// ==== Validar campos antes de enviar ====
function validateForm(form) {
    const telefono = form.querySelector('[name="telefono"]').value.trim();
    if (telefono && !/^\d{9}$/.test(telefono)) {
        showNotification('❌ El teléfono debe tener 9 dígitos', 'error');
        return false;
    }

    const precioHora = form.querySelector('[name="precio_hora"]').value;
    if (precioHora && (isNaN(precioHora) || parseFloat(precioHora) < 0)) {
        showNotification('❌ El precio por hora debe ser un número válido', 'error');
        return false;
    }

    return true;
}

// ==== Previsualizar imagen ====
function setupImagePreview() {
    const fileInput = document.querySelector('input[name="foto"]');
    if (fileInput) {
        fileInput.addEventListener('change', function (e) {
            const file = e.target.files[0];
            if (file) {
                if (!file.type.startsWith('image/')) {
                    showNotification('❌ Por favor selecciona una imagen válida', 'error');
                    this.value = '';
                    return;
                }

                if (file.size > 5 * 1024 * 1024) {
                    showNotification('❌ La imagen no debe superar los 5MB', 'error');
                    this.value = '';
                    return;
                }

                console.log('📸 Imagen válida seleccionada');
            }
        });
    }
}

// ==== Mostrar notificación ====
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;

    // Colores consistentes con perfil.css
    let backgroundColor, boxShadow;
    switch(type) {
        case 'success':
            backgroundColor = '#07734B'; // Verde principal del tema
            boxShadow = '0 4px 12px rgba(7, 115, 75, 0.3)';
            break;
        case 'error':
            backgroundColor = '#dc2626'; // Rojo de error
            boxShadow = '0 4px 12px rgba(220, 38, 38, 0.3)';
            break;
        default:
            backgroundColor = '#024959'; // Azul principal del tema
            boxShadow = '0 4px 12px rgba(2, 73, 89, 0.3)';
    }

    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: ${backgroundColor};
        color: white;
        padding: 12px 24px;
        border-radius: 20px;
        box-shadow: ${boxShadow};
        z-index: 10000;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
        font-size: 14px;
        font-weight: 500;
        max-width: 300px;
        transform: translateX(100%);
        transition: transform 0.3s ease;
        border: 1px solid rgba(255,255,255,0.2);
    `;

    document.body.appendChild(notification);
    setTimeout(() => { notification.style.transform = 'translateX(0)' }, 100);
    setTimeout(() => {
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => notification.remove(), 300);
    }, 4000);
}

// ==== Manejar envío del formulario ====
document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('form-editar-perfil');
    if (!form) {
        console.warn('⚠️ No se encontró el formulario de edición');
        return;
    }

    const modal = document.getElementById('editProfileModal');

    // Cerrar modal al hacer clic fuera
    if (modal) {
        modal.addEventListener('click', function (e) {
            if (e.target === modal) cerrarModalEdicion();
        });
    }

    // Cerrar modal con Escape
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && modal?.style.display === 'flex') {
            cerrarModalEdicion();
        }
    });

    setupImagePreview();

    form.addEventListener('submit', function (e) {
        e.preventDefault();

        if (!validateForm(form)) return;

        const submitBtn = form.querySelector('button[type="submit"]');
        const originalText = submitBtn.textContent;
        submitBtn.textContent = 'Guardando...';
        submitBtn.disabled = true;

        // Agregar estilos de carga al botón
        submitBtn.style.background = '#9CDBA6';
        submitBtn.style.cursor = 'not-allowed';

        const formData = new FormData(form);
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        fetch('/usuarios/actualizar_perfil/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken
            },
            body: formData
        })
        .then(res => res.json().then(data => ({ ok: res.ok, status: res.status, data })))
        .then(({ ok, data, status }) => {
            submitBtn.textContent = originalText;
            submitBtn.disabled = false;
            submitBtn.style.background = ''; // Restaurar estilo original
            submitBtn.style.cursor = '';

            if (ok && data.status === 'ok') {
                showNotification('✅ Perfil actualizado correctamente', 'success');
                cerrarModalEdicion();
                setTimeout(() => location.reload(), 1000);
            } else {
                const msg = data.message || `Error desconocido. Código ${status}`;
                showNotification('❌ ' + msg, 'error');
            }
        })
        .catch(err => {
            console.error('❌ Error en fetch:', err);
            submitBtn.textContent = originalText;
            submitBtn.disabled = false;
            submitBtn.style.background = '';
            submitBtn.style.cursor = '';
            showNotification('❌ Error de conexión con el servidor.', 'error');
        });
    });

    console.log('✅ guardarPerfil.js listo');
});

// ==== Funciones globales ====
window.openEditProfileModal = openEditProfileModal;
window.cerrarModalEdicion = cerrarModalEdicion;