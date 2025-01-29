<?php
require_once '../config/conexion.php';

// Clase Usuario para interactuar con la base de datos
class Usuario {
    private $conexion;

    public function __construct() {
        $this->conexion = new Conexion();
    }

    //Agregar un usuario
    public function agregarUsuario($nombre, $correo, $edad, $plan_base, $duracion) {
        if (!filter_var($correo, FILTER_VALIDATE_EMAIL)) {
            return "Correo inválido.";
        }

        $query = "INSERT INTO usuarios (nombre, correo, edad, plan_base, duracion_suscripcion) VALUES (?, ?, ?, ?, ?)";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("ssiss", $nombre, $correo, $edad, $plan_base, $duracion);

        if ($stmt->execute()) {
            return $this->conexion->conexion->insert_id;
        } else {
            return false;
        }
    }

    //Agregar paquetes
    public function agregarPaquete($usuario_id, $paquete) {
        $query = "INSERT INTO paquetes_usuario (usuario_id, paquete) VALUES (?, ?)";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("is", $usuario_id, $paquete);
        return $stmt->execute();
    }

    //Editar usuario
    public function actualizarUsuario($id, $plan_base, $duracion) {
        $query = "UPDATE usuarios SET plan_base = ?, duracion_suscripcion = ? WHERE id = ?";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("ssi", $plan_base, $duracion, $id);
        return $stmt->execute();
    }

    //Eliminar usuario y sus paquetes 
    public function eliminarUsuario($id) {
        $query = "DELETE FROM usuarios WHERE id = ?";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("i", $id);
        return $stmt->execute();
    }

    //Obtener lista de usuarios con sus paquetes
    public function obtenerUsuarios() {
        $query = "SELECT u.*, GROUP_CONCAT(p.paquete SEPARATOR ', ') AS paquetes
                  FROM usuarios u 
                  LEFT JOIN paquetes_usuario p ON u.id = p.usuario_id 
                  GROUP BY u.id";
        $resultado = $this->conexion->conexion->query($query);
        return $resultado->fetch_all(MYSQLI_ASSOC);
    }

    //Obtener usuario por ID
    public function obtenerUsuarioPorId($id) {
        $query = "SELECT * FROM usuarios WHERE id = ?";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("i", $id);
        $stmt->execute();
        return $stmt->get_result()->fetch_assoc();
    }
}
?>
