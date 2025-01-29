<?php
require_once '../controlador/UsuarioController.php';

$controller = new UsuarioController();
$controller->eliminarUsuario($_GET['id']);
header("Location: lista_usuarios.php");
?>
