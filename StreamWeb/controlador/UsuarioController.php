<?php
require_once '../modelo/Usuario.php';

class UsuarioController {
    private $modelo;

    public function __construct() {
        $this->modelo = new Usuario();
    }

    //registrar un usuario
    public function registrarUsuario($nombre, $correo, $edad, $plan_base, $duracion, $paquetes) {
        $usuario_id = $this->modelo->agregarUsuario($nombre, $correo, $edad, $plan_base, $duracion);
        
        if ($usuario_id) {
            foreach ($paquetes as $paquete) {
                $this->modelo->agregarPaquete($usuario_id, $paquete);
            }
            echo "Usuario registrado con éxito.";
        }
    }

    //editar usuario
    public function actualizarUsuario($id, $plan_base, $duracion) {
        return $this->modelo->actualizarUsuario($id, $plan_base, $duracion);
    }

    //eliminar usuario
    public function eliminarUsuario($id) {
        return $this->modelo->eliminarUsuario($id);
    }

    //listar usuarios
    public function listarUsuarios() {
        return $this->modelo->obtenerUsuarios();
    }

    //obtener usuario por ID
    public function obtenerUsuarioPorId($id) {
        return $this->modelo->obtenerUsuarioPorId($id);
    }
}
?>
