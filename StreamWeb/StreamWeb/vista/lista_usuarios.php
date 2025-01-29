<?php
require_once '../controlador/UsuarioController.php'; //importa el controlador

$controller = new UsuarioController();
$usuarios = $controller->listarUsuarios(); //obtiene la lista de usuarios

//definir precios de los planes base
$precios_planes = [
    "Básico" => 9.99,
    "Estándar" => 13.99,
    "Premium" => 17.99
];

//definir precios de los paquetes adicionales
$precios_paquetes = [
    "Deporte" => 6.99,
    "Cine" => 7.99,
    "Infantil" => 4.99
];

//función para calcular el costo mensual total del usuario
function calcularCosto($usuario, $precios_planes, $precios_paquetes) {
    $costo = $precios_planes[$usuario['plan_base']]; // Precio del plan base

    //sumar el costo de los paquetes adicionales si existen
    if (!empty($usuario['paquetes'])) {
        $paquetes = explode(", ", $usuario['paquetes']);
        foreach ($paquetes as $paquete) {
            if (isset($precios_paquetes[$paquete])) {
                $costo += $precios_paquetes[$paquete];
            }
        }
    }

    return number_format($costo, 2) . " €"; 
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Usuarios Registrados</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="../public/styles.css"> <!-- Archivo de estilos -->
</head>
<body>
    <div class="container">
        <h1 class="my-4">Usuarios Registrados</h1>
        <table class="table table-striped"> <!-- Tabla con estilos Bootstrap -->
            <thead>
                <tr>
                    <th>Nombre</th>
                    <th>Correo</th>
                    <th>Edad</th>
                    <th>Plan Base</th>
                    <th>Duración</th>
                    <th>Paquetes</th>
                    <th>Costo Mensual</th>
                    <th>Acciones</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($usuarios as $usuario): ?>
                <tr>
                    <td><?= $usuario['nombre'] ?></td>
                    <td><?= $usuario['correo'] ?></td>
                    <td><?= $usuario['edad'] ?></td>
                    <td><?= $usuario['plan_base'] ?></td>
                    <td><?= $usuario['duracion_suscripcion'] ?></td>
                    <td><?= $usuario['paquetes'] ?: 'Ninguno' ?></td> <!-- Si no tiene paquetes, muestra Ninguno -->
                    <td><?= calcularCosto($usuario, $precios_planes, $precios_paquetes) ?></td> <!-- muestra el costo mensual -->
                    <td>
                        <a href="editar_usuario.php?id=<?= $usuario['id'] ?>" class="btn btn-warning btn-sm">Editar</a>
                        <a href="eliminar_usuario.php?id=<?= $usuario['id'] ?>" class="btn btn-danger btn-sm">Eliminar</a>
                    </td>
                </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
        <a href="alta_usuario.php" class="btn btn-primary">Registrar Usuario</a> <!-- Botón para registrar nuevos usuarios -->
    </div>
</body>
</html>
