<?php
session_start();
if (!isset($_SESSION['usuario'])){
    header("Location: login.php");
    exit();
}
$error = isset($_SESSION['error']) ? $_SESSION['error'] : "";
unset($_SESSION['error']);
$mensaje = isset($_SESSION['mensaje']) ? $_SESSION['mensaje'] : "";
unset($_SESSION['mensaje']);

require_once __DIR__ . '/../modelo/class_tarea.php';
$tareaModel = new Tarea();
$id_usuario = $_SESSION['usuario']['id_usuario'];
$tareas = $tareaModel->obtenerTareasPorUsuario($id_usuario);
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Mis Tareas</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<div class="container mt-5">
    <h1>Mis Tareas</h1>
    <a href="../controlador/LogoutController.php" class="btn btn-danger mb-3">Cerrar Sesión</a>
    
    <?php if($mensaje): ?>
        <div class="alert alert-success"><?= $mensaje ?></div>
    <?php endif; ?>
    <?php if($error): ?>
        <div class="alert alert-danger"><?= $error ?></div>
    <?php endif; ?>
    
    <!-- Formulario para agregar nueva tarea -->
    <form action="../controlador/TareasController.php" method="POST" class="mb-4">
        <div class="mb-3">
            <label for="descripcion" class="form-label">Nueva Tarea:</label>
            <input type="text" name="descripcion" id="descripcion" class="form-control" required>
        </div>
        <button type="submit" name="agregar" class="btn btn-primary">Agregar Tarea</button>
    </form>
    
    <!-- Listado de tareas -->
    <?php if (!empty($tareas)): ?>
    <table class="table table-bordered">
        <thead>
            <tr>
                <th>ID</th>
                <th>Descripción</th>
                <th>Completada</th>
                <th>Acciones</th>
            </tr>
        </thead>
        <tbody>
        <?php foreach ($tareas as $tarea): ?>
            <tr>
                <td><?= $tarea['id_tarea'] ?></td>
                <td><?= $tarea['descripcion'] ?></td>
                <td><?= $tarea['completada'] ? 'Sí' : 'No' ?></td>
                <td>
                    <?php if(!$tarea['completada']): ?>
                    <form action="../controlador/TareasController.php" method="POST" style="display:inline;">
                        <input type="hidden" name="id_tarea" value="<?= $tarea['id_tarea'] ?>">
                        <button type="submit" name="completar" class="btn btn-success btn-sm">Completar</button>
                    </form>
                    <?php endif; ?>
                    <a href="editar_tarea.php?id=<?= $tarea['id_tarea'] ?>" class="btn btn-primary btn-sm">Editar</a>
                    <form action="../controlador/TareasController.php" method="POST" style="display:inline;">
                        <input type="hidden" name="id_tarea" value="<?= $tarea['id_tarea'] ?>">
                        <button type="submit" name="eliminar" class="btn btn-danger btn-sm">Eliminar</button>
                    </form>
                </td>
            </tr>
        <?php endforeach; ?>
        </tbody>
    </table>
    <?php else: ?>
        <p>No tienes tareas registradas.</p>
    <?php endif; ?>
</div>
</body>
</html>
