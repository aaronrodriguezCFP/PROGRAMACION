<?php
require_once __DIR__ . '/../config/conexion.php';

class Usuario {
    private $conexion;
    
    public function __construct(){
        $this->conexion = new Conexion();
    }
    
    // Registrar un nuevo usuario (almacena el hash de la contraseña)
    public function registrar($username, $email, $password){
        $hash = password_hash($password, PASSWORD_DEFAULT);
        $query = "INSERT INTO usuarios (username, email, password) VALUES (?, ?, ?)";
        $stmt = $this->conexion->conexion->prepare($query);
        if (!$stmt) {
            return "Error en la preparación: " . $this->conexion->conexion->error;
        }
        $stmt->bind_param("sss", $username, $email, $hash);
        if($stmt->execute()){
            $stmt->close();
            return true;
        } else {
            $error = $stmt->error;
            $stmt->close();
            return $error;
        }
    }
    
    // Obtener un usuario por correo electrónico
    public function getUserByEmail($email){
        $query = "SELECT * FROM usuarios WHERE email = ?";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("s", $email);
        $stmt->execute();
        $result = $stmt->get_result();
        $usuario = $result->fetch_assoc();
        $stmt->close();
        return $usuario;
    }
    
    // Obtener un usuario por su ID
    public function getUserById($id_usuario){
        $query = "SELECT * FROM usuarios WHERE id_usuario = ?";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("i", $id_usuario);
        $stmt->execute();
        $result = $stmt->get_result();
        $usuario = $result->fetch_assoc();
        $stmt->close();
        return $usuario;
    }
}
?>
