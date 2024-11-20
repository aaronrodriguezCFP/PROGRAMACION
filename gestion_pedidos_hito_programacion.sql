-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS gestion_pedidos;
USE gestion_pedidos;

-- Crear la tabla 'clientes'
CREATE TABLE IF NOT EXISTS clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    direccion VARCHAR(255),
    email VARCHAR(100) UNIQUE,
    telefono VARCHAR(15)
);

-- Crear la tabla 'productos'
CREATE TABLE IF NOT EXISTS productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    descripcion VARCHAR(255),
    precio DECIMAL(10, 2),
    stock INT
);

-- Crear la tabla 'pedidos'
CREATE TABLE IF NOT EXISTS pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT,
    total DECIMAL(10, 2),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE CASCADE
);

-- Crear la tabla 'detalles_pedido'
CREATE TABLE IF NOT EXISTS detalles_pedido (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pedido_id INT,
    producto_id INT,
    cantidad INT,
    subtotal DECIMAL(10, 2),
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id) ON DELETE CASCADE,
    FOREIGN KEY (producto_id) REFERENCES productos(id) ON DELETE CASCADE
);

-- Insertar datos iniciales en 'clientes'
INSERT INTO clientes (nombre, direccion, email, telefono) VALUES
('Juan Pérez', 'Calle Mayor 123', 'juan.perez@example.com', '123456789'),
('Ana López', 'Avenida de la Paz 45', 'ana.lopez@example.com', '987654321'),
('Luis Gómez', 'Calle Falsa 123', 'luis.gomez@example.com', '654321987'),
('Maria Sánchez', 'Plaza del Sol 12', 'maria.sanchez@example.com', '321987654');

-- Insertar datos iniciales en 'productos'
INSERT INTO productos (nombre, descripcion, precio, stock) VALUES
('PS5', 'Consola de videojuegos', 500.00, 5),
('iPhone 16', 'Smartphone de alta gama', 1200.00, 3),
('Gafas Filtro Azul', 'Protegen la vista al usar pantallas', 25.00, 10),
('Botas Doc Martens', 'Botas de cuero de calidad', 150.00, 15);

-- Insertar pedidos de ejemplo
INSERT INTO pedidos (cliente_id, total) VALUES
(1, 50.25),
(2, 35.75),
(3, 10.50);

-- Insertar detalles de pedido de ejemplo
INSERT INTO detalles_pedido (pedido_id, producto_id, cantidad, subtotal) VALUES
(1, 1, 1, 500.00), -- Juan compró 1 PS5
(1, 3, 2, 50.00),  -- Juan compró 2 gafas filtro azul
(2, 2, 1, 1200.00), -- Ana compró 1 iPhone 16
(2, 4, 1, 150.00),  -- Ana compró 1 par de botas Doc Martens
(3, 3, 2, 50.00);   -- Luis compró 2 gafas filtro azul

-- Verificar los datos
SELECT * FROM clientes;
SELECT * FROM productos;
SELECT * FROM pedidos;
SELECT * FROM detalles_pedido;
