document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("registroUsuario");

    form.addEventListener("submit", function(event) {
        const edad = parseInt(document.getElementById("edad").value);
        const paquetes = document.querySelectorAll('input[name="paquetes[]"]:checked');
        const planBase = document.getElementById("plan_base").value;
        const duracion = document.getElementById("duracion").value;

        let errores = [];

        // Restricción de menores de 18 años
        if (edad < 18) {
            for (let paquete of paquetes) {
                if (paquete.value !== "Infantil") {
                    errores.push("⚠️ Los menores de 18 años solo pueden contratar el <b>Pack Infantil</b>.");
                }
            }
        }

        // Restricción del Plan Básico
        if (planBase === "Básico" && paquetes.length > 1) {
            errores.push("⚠️ El <b>Plan Básico</b> solo permite seleccionar un paquete adicional.");
        }

        // Restricción del Pack Deporte
        for (let paquete of paquetes) {
            if (paquete.value === "Deporte" && duracion !== "Anual") {
                errores.push("⚠️ El <b>Pack Deporte</b> solo puede ser contratado si la suscripción es <b>Anual</b>.");
            }
        }

        if (errores.length > 0) {
            event.preventDefault(); // Evita que el formulario se envíe
            
            // Mostrar alertas con SweetAlert2
            Swal.fire({
                title: "Error en el registro",
                html: errores.join("<br>"), // Muestra los errores en formato HTML
                icon: "error",
                confirmButtonText: "Aceptar"
            });
        }
    });
});
