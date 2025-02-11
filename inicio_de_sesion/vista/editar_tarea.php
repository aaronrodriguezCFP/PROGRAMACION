<?php
session_start();
if (!isset($_SESSION['usuario'])){
    header("Location: login.php");
    exit();
}

if(!isset($_GET['id'])){
    $_SESSION['error'] = "No se especificó la tarea a editar.";
    header("Location: tareas.php");
    exit();
}

$id_tarea = $_GET['id'];

require_once __DIR__ . '/../modelo/class_tarea.php';
$tareaModel = new Tarea();
$tarea = null;
$tareas = $tareaModel->obtenerTareasPorUsuario($_SESSION['usuario']['id_usuario']);
foreach($tareas as $t){
    if($t['id_tarea'] == $id_tarea){
        $tarea = $t;
        break;
    }
}

if(!$tarea){
    $_SESSION['error'] = "Tarea no encontrada.";
    header("Location: tareas.php");
    exit();
}
$error = isset($_SESSION['error']) ? $_SESSION['error'] : "";
unset($_SESSION['error']);
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Editar Tarea</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<div class="container mt-5">
    <h1>Editar Tarea</h1>
    <?php if($error): ?>
        <div class="alert alert-danger"><?= $error ?></div>
    <?php endif; ?>
    <form action="../controlador/TareasController.php" method="POST">
        <input type="hidden" name="id_tarea" value="<?= $tarea['id_tarea'] ?>">
        <div class="mb-3">
            <label for="descripcion" class="form-label">Descripción:</label>
            <input type="text" name="descripcion" id="descripcion" class="form-control" value="<?= $tarea['descripcion'] ?>" required>
        </div>
        <button type="submit" name="editar" class="btn btn-primary">Actualizar Tarea</button>
        <a href="tareas.php" class="btn btn-secondary">Cancelar</a>
    </form>
</div>
</body>
</html>
