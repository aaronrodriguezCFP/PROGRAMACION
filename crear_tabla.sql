-- Crear la base de datos y la tabla "producto"
CREATE DATABASE IF NOT EXISTS akihabara_db;
USE akihabara_db;

CREATE TABLE IF NOT EXISTS producto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    categoria VARCHAR(100),
    precio DECIMAL(10,2),
    stock INT
);

-- Crear el usuario 'userAkihabara' con permisos sobre la base de datos
CREATE USER IF NOT EXISTS 'userAkihabara'@'localhost' IDENTIFIED BY 'Akihabara2025!';
GRANT ALL PRIVILEGES ON akihabara_db.* TO 'userAkihabara'@'localhost';
FLUSH PRIVILEGES;

-- Insertar muchos productos de prueba
INSERT INTO producto (nombre, categoria, precio, stock) VALUES
('Figura de Anya Forger', 'Figura', 59.95, 8),
('Manga Chainsaw Man Vol.1', 'Manga', 9.99, 20),
('Póster Studio Ghibli Colección', 'Póster', 15.50, 15),
('Llavero Pikachu 3D', 'Llavero', 6.99, 25),
('Camiseta One Piece Luffy', 'Ropa', 19.90, 12),
('Figura de Tanjiro Kamado', 'Figura', 39.95, 10),
('Manga Jujutsu Kaisen Vol.3', 'Manga', 8.50, 17),
('Póster Attack on Titan', 'Póster', 12.00, 20),
('Llavero Totoro', 'Llavero', 5.50, 30),
('Sudadera Naruto', 'Ropa', 34.99, 6),
('Figura de Goku Ultra Instinct', 'Figura', 79.99, 5),
('Manga Naruto Vol.10', 'Manga', 7.95, 22),
('Póster Evangelion Asuka', 'Póster', 11.99, 18),
('Llavero Nezuko', 'Llavero', 6.50, 27),
('Camiseta Tokyo Revengers', 'Ropa', 21.00, 14);
