<?php
//conexión con la base de datos
class Conexion {
    private $servidor = 'localhost';
    private $usuario = 'root';
    private $password = 'curso';
    private $base_datos = 'streamweb';
    private $port = '3306';
    public $conexion;

    //establecer conexión con la base de datos
    public function __construct() {
        $this->conexion = new mysqli($this->servidor, $this->usuario, $this->password, $this->base_datos);
        
        //verifica si hay un error en la conexión
        if ($this->conexion->connect_error) {
            die("Error de conexión: " . $this->conexion->connect_error);
        }
    }

    //cerrar la conexión
    public function cerrar() {
        $this->conexion->close();
    }
}
?>
