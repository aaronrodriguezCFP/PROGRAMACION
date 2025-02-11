<?php
require_once __DIR__ . '/../modelo/class_usuario.php';
session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST'){
    $email = trim($_POST['email']);
    $password = $_POST['password'];
    
    if(empty($email) || empty($password)){
        $_SESSION['error'] = "Por favor ingresa tu correo y contraseña.";
        header("Location: ../vista/login.php");
        exit();
    }
    
    $usuarioModel = new Usuario();
    $usuario = $usuarioModel->getUserByEmail($email);
    
    if($usuario){
        if (password_verify($password, $usuario['password'])){
            session_regenerate_id(true); // Regenera el ID de la sesión por seguridad
            $_SESSION['usuario'] = $usuario;  // Se guarda el array del usuario en la sesión
            header("Location: ../vista/tareas.php");
            exit();
        } else {
            $_SESSION['error'] = "Contraseña incorrecta.";
            header("Location: ../vista/login.php");
            exit();
        }
    } else {
        $_SESSION['error'] = "Usuario no encontrado.";
        header("Location: ../vista/login.php");
        exit();
    }
}
?>
