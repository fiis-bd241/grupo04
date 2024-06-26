CREATE TABLE Pelicula(id INT,nombre VARCHAR(100),duracion VARCHAR(100),genero VARCHAR(100),PRIMARY KEY (id));

INSERT INTO Pelicula(id, nombre, duracion, genero) VALUES (2, 'Marvel', '2.5','Accion');
INSERT INTO Pelicula(id, nombre, duracion, genero) VALUES (3, 'Mars', '2.5','Sci');
select * from Pelicula;