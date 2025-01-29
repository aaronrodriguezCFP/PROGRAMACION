<?php
require_once '../controlador/UsuarioController.php'; // Importa el controlador

$controller = new UsuarioController();
$usuario = $controller->obtenerUsuarioPorId($_GET['id']); // Obtiene el usuario a editar

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Actualiza el usuario con los datos del formulario
    $controller->actualizarUsuario($_POST['id'], $_POST['plan_base'], $_POST['duracion']);
    header("Location: lista_usuarios.php"); // Redirige a la lista de usuarios
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Editar Usuario</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="../public/styles.css"> <!-- Archivo de estilos -->
</head>
<body>
    <div class="container mt-5">
        <div class="card shadow-lg p-4"> <!-- Tarjeta con sombra para mejor presentación -->
            <h2 class="text-center mb-4">Editar Usuario</h2>
            <form method="post">
                <input type="hidden" name="id" value="<?= $usuario['id'] ?>"> <!-- ID oculto -->

                <!-- Selección del Plan Base -->
                <div class="mb-3">
                    <label class="form-label">Plan Base</label>
                    <select class="form-select" name="plan_base">
                        <option value="Básico" <?= ($usuario['plan_base'] == 'Básico') ? 'selected' : '' ?>>Básico</option>
                        <option value="Estándar" <?= ($usuario['plan_base'] == 'Estándar') ? 'selected' : '' ?>>Estándar</option>
                        <option value="Premium" <?= ($usuario['plan_base'] == 'Premium') ? 'selected' : '' ?>>Premium</option>
                    </select>
                </div>

                <!-- Selección de la Duración -->
                <div class="mb-3">
                    <label class="form-label">Duración</label>
                    <select class="form-select" name="duracion">
                        <option value="Mensual" <?= ($usuario['duracion_suscripcion'] == 'Mensual') ? 'selected' : '' ?>>Mensual</option>
                        <option value="Anual" <?= ($usuario['duracion_suscripcion'] == 'Anual') ? 'selected' : '' ?>>Anual</option>
                    </select>
                </div>

                <!-- Botones de acción -->
                <div class="text-center">
                    <button type="submit" class="btn btn-success">Actualizar</button>
                    <a href="lista_usuarios.php" class="btn btn-secondary">Cancelar</a>
                </div>
            </form>
        </div>
    </div>
</body>
</html>
