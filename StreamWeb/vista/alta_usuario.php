<?php
require_once '../controlador/UsuarioController.php'; //importa el controlador

$controller = new UsuarioController();

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    //datos del formulario
    $nombre = $_POST['nombre'];
    $correo = $_POST['correo'];
    $edad = $_POST['edad'];
    $plan_base = $_POST['plan_base'];
    $duracion = $_POST['duracion'];
    $paquetes = isset($_POST['paquetes']) ? $_POST['paquetes'] : [];

    //registra el usuario con sus paquetes y redirige
    $controller->registrarUsuario($nombre, $correo, $edad, $plan_base, $duracion, $paquetes);
    header("Location: lista_usuarios.php"); 
}
?>

<!DOCTYPE html>
<html lang="es">
<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script> <!-- Sweet alert que utilizaremos más adelnate en el archivo.js !--> 
<head>
    <meta charset="UTF-8">
    <title>Registrar Usuario</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="../public/styles.css">
    <script src="../public/script.js" defer></script> <!-- JavaScript para validaciones -->
</head>
<body>
    <div class="container">
        <h1 class="my-4">Registrar Nuevo Usuario</h1>
        <form id="registroUsuario" method="post">
            <!-- Campo para el nombre -->
            <div class="mb-3">
                <label class="form-label">Nombre</label>
                <input type="text" class="form-control" name="nombre" required>
            </div>

            <!-- Campo para el correo -->
            <div class="mb-3">
                <label class="form-label">Correo</label>
                <input type="email" class="form-control" name="correo" required>
            </div>

            <!-- Campo para la edad -->
            <div class="mb-3">
                <label class="form-label">Edad</label>
                <input type="number" class="form-control" name="edad" id="edad" required>
            </div>

            <!-- Selección del plan base -->
            <div class="mb-3">
                <label class="form-label">Plan Base</label>
                <select class="form-control" name="plan_base" id="plan_base">
                    <option value="Básico">Básico</option>
                    <option value="Estándar">Estándar</option>
                    <option value="Premium">Premium</option>
                </select>
            </div>

            <!-- Selección de paquetes adicionales -->
            <div class="mb-3">
                <label class="form-label">Paquetes</label><br>
                <input type="checkbox" name="paquetes[]" value="Deporte" id="deporte"> Deporte
                <input type="checkbox" name="paquetes[]" value="Cine"> Cine
                <input type="checkbox" name="paquetes[]" value="Infantil"> Infantil
            </div>

            <!-- Selección de la duración de la suscripción -->
            <div class="mb-3">
                <label class="form-label">Duración</label>
                <select class="form-control" name="duracion" id="duracion">
                    <option value="Mensual">Mensual</option>
                    <option value="Anual">Anual</option>
                </select>
            </div>

            <!-- Botón de registro -->
            <button type="submit" class="btn btn-success">Registrar</button>
        </form>
    </div>
</body>
</html>
