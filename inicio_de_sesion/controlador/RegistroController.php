<?php
require_once __DIR__ . '/../modelo/class_usuario.php';
session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST'){
    $username = trim($_POST['username']);
    $email = trim($_POST['email']);
    $password = $_POST['password'];
    
    if (empty($username) || empty($email) || empty($password)){
        $_SESSION['error'] = "Todos los campos son obligatorios.";
        header("Location: ../vista/registro.php");
        exit();
    }
    
    $usuarioModel = new Usuario();
    if ($usuarioModel->getUserByEmail($email)){
        $_SESSION['error'] = "El correo electrónico ya está registrado.";
        header("Location: ../vista/registro.php");
        exit();
    }
    
    $resultado = $usuarioModel->registrar($username, $email, $password);
    if ($resultado === true){
        $_SESSION['mensaje'] = "Registro exitoso. Ahora puedes iniciar sesión.";
        header("Location: ../vista/login.php");
        exit();
    } else {
        $_SESSION['error'] = "Error al registrar usuario: " . $resultado;
        header("Location: ../vista/registro.php");
        exit();
    }
}
?>
