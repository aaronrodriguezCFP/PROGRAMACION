<?php
require_once __DIR__ . '/../modelo/class_tarea.php';
session_start();

if (!isset($_SESSION['usuario'])) {
    header("Location: login.php");
    exit();
}

$tareaModel = new Tarea();

if ($_SERVER['REQUEST_METHOD'] === 'POST'){
    if (isset($_POST['agregar'])) {
        $descripcion = trim($_POST['descripcion']);
        $id_usuario = $_SESSION['usuario']['id_usuario'];
        if(empty($descripcion)){
            $_SESSION['error'] = "La descripción no puede estar vacía.";
            header("Location: ../vista/tareas.php");
            exit();
        }
        $resultado = $tareaModel->agregarTarea($id_usuario, $descripcion);
        if($resultado === true){
            $_SESSION['mensaje'] = "Tarea agregada correctamente.";
        } else {
            $_SESSION['error'] = "Error al agregar tarea: " . $resultado;
        }
        header("Location: ../vista/tareas.php");
        exit();
    } elseif (isset($_POST['completar'])) {
        $id_tarea = $_POST['id_tarea'];
        $resultado = $tareaModel->completarTarea($id_tarea);
        if($resultado === true){
            $_SESSION['mensaje'] = "Tarea marcada como completada.";
        } else {
            $_SESSION['error'] = "Error al completar tarea: " . $resultado;
        }
        header("Location: ../vista/tareas.php");
        exit();
    } elseif (isset($_POST['editar'])) {
        $id_tarea = $_POST['id_tarea'];
        $descripcion = trim($_POST['descripcion']);
        if(empty($descripcion)){
            $_SESSION['error'] = "La descripción no puede estar vacía.";
            header("Location: ../vista/editar_tarea.php?id=".$id_tarea);
            exit();
        }
        $resultado = $tareaModel->editarTarea($id_tarea, $descripcion);
        if($resultado === true){
            $_SESSION['mensaje'] = "Tarea actualizada correctamente.";
        } else {
            $_SESSION['error'] = "Error al actualizar tarea: " . $resultado;
        }
        header("Location: ../vista/tareas.php");
        exit();
    } elseif (isset($_POST['eliminar'])) {
        $id_tarea = $_POST['id_tarea'];
        $resultado = $tareaModel->eliminarTarea($id_tarea);
        if($resultado === true){
            $_SESSION['mensaje'] = "Tarea eliminada correctamente.";
        } else {
            $_SESSION['error'] = "Error al eliminar tarea: " . $resultado;
        }
        header("Location: ../vista/tareas.php");
        exit();
    }
}
?>
