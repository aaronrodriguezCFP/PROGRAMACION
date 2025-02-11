<?php
require_once __DIR__ . '/../config/conexion.php';

class Tarea {
    private $conexion;
    
    public function __construct(){
        $this->conexion = new Conexion();
    }
    
    // Agregar una nueva tarea para un usuario
    public function agregarTarea($id_usuario, $descripcion){
        $query = "INSERT INTO tareas (id_usuario, descripcion) VALUES (?, ?)";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("is", $id_usuario, $descripcion);
        if ($stmt->execute()){
            $stmt->close();
            return true;
        } else {
            $error = $stmt->error;
            $stmt->close();
            return $error;
        }
    }
    
    // Obtener todas las tareas de un usuario
    public function obtenerTareasPorUsuario($id_usuario){
        $query = "SELECT * FROM tareas WHERE id_usuario = ?";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("i", $id_usuario);
        $stmt->execute();
        $resultado = $stmt->get_result();
        $tareas = [];
        while ($fila = $resultado->fetch_assoc()){
            $tareas[] = $fila;
        }
        $stmt->close();
        return $tareas;
    }
    
    // Marcar una tarea como completada
    public function completarTarea($id_tarea){
        $query = "UPDATE tareas SET completada = 1 WHERE id_tarea = ?";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("i", $id_tarea);
        if ($stmt->execute()){
            $stmt->close();
            return true;
        } else {
            $error = $stmt->error;
            $stmt->close();
            return $error;
        }
    }
    
    // Editar la descripción de una tarea
    public function editarTarea($id_tarea, $descripcion){
        $query = "UPDATE tareas SET descripcion = ? WHERE id_tarea = ?";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("si", $descripcion, $id_tarea);
        if ($stmt->execute()){
            $stmt->close();
            return true;
        } else {
            $error = $stmt->error;
            $stmt->close();
            return $error;
        }
    }
    
    // Eliminar una tarea
    public function eliminarTarea($id_tarea){
        $query = "DELETE FROM tareas WHERE id_tarea = ?";
        $stmt = $this->conexion->conexion->prepare($query);
        $stmt->bind_param("i", $id_tarea);
        if ($stmt->execute()){
            $stmt->close();
            return true;
        } else {
            $error = $stmt->error;
            $stmt->close();
            return $error;
        }
    }
}
?>
