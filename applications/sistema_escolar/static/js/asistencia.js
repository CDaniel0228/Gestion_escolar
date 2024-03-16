function registrarCambioAsistencia(nuevoEstado, rowId) {
    // Aquí puedes realizar una llamada a tu API para registrar el cambio de asistencia
    // por ejemplo, utilizando XMLHttpRequest, Fetch API o jQuery.ajax

    // Ejemplo con Fetch API
    fetch('/sistema_escolar/default/accion', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ estado: nuevoEstado, rowId: rowId }),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Registro de asistencia exitoso:', data);
        // Puedes realizar acciones adicionales si es necesario
    })
    .catch(error => {
        console.error('Error al registrar asistencia:', error);
    });
}