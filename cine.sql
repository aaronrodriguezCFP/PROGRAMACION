CREATE DATABASE cine;
USE cine;

CREATE TABLE genero (
    id_genero CHAR(3) PRIMARY KEY,
    nombre VARCHAR(50)
);

CREATE TABLE pelicula (
    id_pelicula CHAR(5) PRIMARY KEY,
    titulo VARCHAR(100),
    director VARCHAR(100),
    duracion INT,
    clasificacion VARCHAR(10),
    id_genero CHAR(3),
    FOREIGN KEY (id_genero) REFERENCES genero(id_genero)
);

INSERT INTO genero VALUES ('ACC', 'Acción'), ('COM', 'Comedia'), ('DRA', 'Drama');

INSERT INTO pelicula VALUES 
('Peli1', 'John Wick', 'Chad Stahelski', 110, '+18', 'ACC'),
('Peli2', 'American Psycho', 'Mary Harron', 102, '+18', 'DRA');
