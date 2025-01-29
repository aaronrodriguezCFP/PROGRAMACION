DROP DATABASE IF EXISTS streamweb;
CREATE DATABASE streamweb;
USE streamweb;

-- Tabla de usuarios
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL UNIQUE,
    edad INT NOT NULL CHECK (edad >= 0),  
    plan_base ENUM('Básico', 'Estándar', 'Premium') NOT NULL,
    duracion_suscripcion ENUM('Mensual', 'Anual') NOT NULL
);

-- Tabla de paquetes contratados por cada usuario
CREATE TABLE paquetes_usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    paquete ENUM('Deporte', 'Cine', 'Infantil') NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
);

-- Insertar usuarios de prueba
INSERT INTO usuarios (nombre, correo, edad, plan_base, duracion_suscripcion)
VALUES
('Juan Pérez', 'juan.perez@email.com', 25, 'Estándar', 'Mensual'),
('Ana García', 'ana.garcia@email.com', 17, 'Básico', 'Anual');

-- Insertar paquetes de prueba
INSERT INTO paquetes_usuario (usuario_id, paquete)
VALUES
(1, 'Cine'),   -- Juan Pérez puede elegir cualquier paquete
(2, 'Infantil'); -- Ana García (menor de 18) solo puede elegir el Pack Infantil