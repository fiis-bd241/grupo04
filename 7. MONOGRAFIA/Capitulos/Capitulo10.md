# Capítulo 10: Sentencias SQL por prototipo


## Módulo marketing
### Código Requerimiento : R - 001
### Codigo interfaz : I - 001
### Imagen interfaz : 
![image](imagenes_cap_9/modulo_mark/I007.png)
### Sentecias SQL:
### Eventos: 
* **Carga de pantalla: la pantalla se llena con el Id_campaña siguiente al último registro y con el Id_equipo_mark con el que se entró a la página**
* **BOTON Enviar: Inserta una nueva fila en la tabla Campaña, además de insertar nuevas filas en la tabla CampañaXProd y CampañaXCanal**
* **BOTON Cancelar: No se realizan cambios en la tabla** 
```
--CARGA:
SELECT MAX(Id_campaña) + 1 AS nuevo_Id_campaña
FROM Campaña;

SELECT id_equipo_mark
FROM persona
WHERE usuario=<12>
AND contraseña=<13>;

-- BOTON Enviar
INSERT INTO Campaña (Id_campaña, nom_campaña, fecha_ini, fecha_fin, dir_url, modalidad, archivo, desc_campaña, Id_equipo_mark, Id_gest_mark)
VALUES
    (<1>, <2>, <3>, <4>, <5>, <6>, <7>, <8>, <9>, 1005);

INSERT INTO CampañaXProd (id_producto, Id_campaña)
VALUES
    (<10>, <1>);

INSERT INTO CampañaXCanal (Id_campaña, Id_canal)
VALUES
    (<1>, <11>);
    
```

### Código Requerimiento : R - 002
### Codigo interfaz : I - 002
### Imagen interfaz : 
![image](imagenes_cap_9/modulo_mark/I009.png)
### Sentecias SQL:
### Eventos: 
* **Carga de pantalla: La pantalla se llena con el Id_observacion siguiente al último registro en la tabla observaciones y con el Id de la campaña asociada**
* **BOTON Enviar: Se inserta una nueva fila en la tabla Observacion, el estado_atendido estará en FALSE porque aun no se atiende**
* **BOTON Cancelar:No se realiza ningun cambio a las tablas, se vuelve a la pantalla anterior** 
```
--CARGA:
SELECT MAX(Id_observacion) + 1 AS nuevo_Id_observacion
FROM Observacion;

SELECT Id_campaña
FROM Campaña
WHERE Id_campaña = <2>;

--BOTÓN ENVIAR:
INSERT INTO Observacion (Id_observacion, descripcion, Id_campaña, estado_atendido)
VALUES
    (<1>,<3> , <2>, FALSE);
```

### Código Requerimiento : R - 003
### Codigo interfaz : I - 003
### Imagen interfaz : 
![image](imagenes_cap_9/modulo_mark/I010.png)
### Sentecias SQL:
### Eventos: 
* **Carga de pantalla: La pantalla se llena con el Id_observacion con, el Id_campaña relacionado con sus datos correspondientes, el Id_equipo_marketing que propuso la campaña**
* **BOTON Enviar: Se registran los cambios realizados en la pantalla, además de actualizar el estado_atendido de la observacion a TRUE**
* **BOTON Cancelar: No se realizan cambios en las tablas** 
```
--CARGA
SELECT 
    o.Id_observacion,
    o.descripcion,
    o.Id_campaña,
    c.Id_equipo_mark,
    c.nom_campaña,
    c.fecha_ini,
    c.fecha_fin,
    c.dir_url,
    c.modalidad,
    c.archivo,
    c.desc_campaña
FROM 
    Observacion o
JOIN 
    Campaña c ON o.Id_campaña = c.Id_campaña
WHERE Id_observacion= <1>;

SELECT 
    cxp.id_producto
FROM 
    Observacion o
JOIN 
    Campaña c ON o.Id_campaña = c.Id_campaña
JOIN 
    CampañaXProd cxp ON c.Id_campaña = cxp.Id_campaña
WHERE 
    o.Id_observacion = <1>;

SELECT 
    cxc.id_canal
FROM 
    Observacion o
JOIN 
    Campaña c ON o.Id_campaña = c.Id_campaña
JOIN 
    CampañaXCanal cxc ON c.Id_campaña = cxc.Id_campaña
WHERE 
    o.Id_observacion = <1>;

--BOTON ENVIAR
UPDATE Campaña
SET 
 nom_campaña= <2>,
 fecha_ini= <3>,
 fecha_fin= <4>,
 dir_url= <5>,
 modalidad= <6>,
 archivo= <7>,
 desc_campaña <8>
WHERE Id_campaña = (SELECT Id_campaña FROM Observacion WHERE Id_observacion = <1>);

UPDATE CampañaXProd
SET
 id_producto= <9>
WHERE Id_campaña = (SELECT Id_campaña FROM Observacion WHERE Id_observacion = <1>)
AND id_producto= (SELECT 
    cxp.id_producto
FROM 
    Observacion o
JOIN 
    Campaña c ON o.Id_campaña = c.Id_campaña
JOIN 
    CampañaXProd cxp ON c.Id_campaña = cxp.Id_campaña
WHERE 
    o.Id_observacion = <1>);

UPDATE CampañaXCanal
SET
 Id_canal =<10>
WHERE Id_campaña = (SELECT Id_campaña FROM Observacion WHERE Id_observacion = <1>)
AND id_canal = (SELECT 
    cxc.id_canal
FROM 
    Observacion o
JOIN 
    Campaña c ON o.Id_campaña = c.Id_campaña
JOIN 
    CampañaXCanal cxc ON c.Id_campaña = cxc.Id_campaña
WHERE 
    o.Id_observacion = <1>);

UPDATE Observacion
SET
 estado_atendido =TRUE
WHERE
 Id_observacion=<1>;
```

### Código Requerimiento : R - 004
### Codigo interfaz : I - 004
### Imagen interfaz : 
![image](imagenes_cap_9/modulo_mark/I011.png)
### Sentecias SQL:
### Eventos: 
* **Carga de pantalla: La pantalla se carga con el id_campaña correspondiente a la campaña a editar y tambien se cargan los datos asociados a esta**
* **BOTON Guardar: Se actualizan los datos de las tablas según los cambios realizados**
* **BOTON Cancelar: No se realizan cambios en las tablas**
* **BOTON Eliminar: Se elimina la campaña y todas las filas de lastablas asociadas que contangan este id_campaña**
```
--CARGA
SELECT
    Id_campaña,
    nom_campaña,
    fecha_ini,
    fecha_fin,
    dir_url,
    modalidad,
    archivo,
    desc_campaña
FROM Campaña
WHERE Id_campaña=<1>;

SELECT id_producto
FROM CampañaXProd
WHERE Id_campaña=<1>;

SELECT Id_canal
FROM CampañaXCanal
WHERE Id_campaña=<1>;

--BOTON ENVIAR
UPDATE Campaña
SET 
 nom_campaña= <2>,
 fecha_ini= <3>,
 fecha_fin= <4>,
 dir_url= <5>,
 modalidad= <6>,
 archivo= <7>,
 desc_campaña <8>
WHERE Id_campaña = <1>;

UPDATE CampañaXProd
SET
 id_producto= <9>
WHERE Id_campaña = <1>
AND id_producto= (SELECT id_producto
FROM CampañaXProd
WHERE Id_campaña=<1>);

UPDATE CampañaXCanal
SET
 id_canal=<10>
WHERE Id_campaña= <1>
AND Id_canal=(SELECT Id_canal
FROM CampañaXCanal
WHERE Id_campaña=<1>);

--BOTON ELIMINAR
DELETE FROM CampañaXProd WHERE Id_campaña=<1>;
DELETE FROM CampañaXCanal WHERE Id_campaña=<1>;
DELETE FROM Observacion WHERE Id_campaña=<1>;
DELETE FROM Campaña WHERE Id_campaña =<1>; 
```

## Modulo de Compras
### Código Requerimiento : R - 005
### Codigo interfaz : I - 005
### Imagen interfaz : 
![image](../../04.Entregables/Entregable_PC3/Pantallas/ModCompras/MP6-.png)
### Sentecias SQL:
### Eventos: 
* **Pantalla Visualizar Proveedores: Se mostrará todos los proveedores dentro de la empresa con un estado de activo**
```
SELECT razon_social 
FROM proveedor
WHERE id_est_proveedor = 'A'
```

### Código Requerimiento : R - 006
### Codigo interfaz : I - 006
### Imagen interfaz : 
![image](../../04.Entregables/Entregable_PC3/Pantallas/ModCompras/MP1.png)
### Sentecias SQL:
### Eventos: 
* **Boton Añadir Proveedor: Nos permite ingresar los datos de un proveedor para ser guardado en la base de datos** 
```
INSERT INTO proveedor(ruc_proveedor, razon_social, web_proveedor, rubro, direccion, telefono, id_est_proveedor)
VALUES (<1>, <2>, <3>, <4>, <5>, <6>, 'A');
```

### Código Requerimiento : R - 007
### Codigo interfaz : I - 007
### Imagen interfaz : 
![image](../../04.Entregables/Entregable_PC3/Pantallas/ModCompras/MP2.png)
### Sentecias SQL:
### Eventos: 
* **Pantalla Detalle Proveedores: Se mostrará todos los datos de los proveedores activos en la empresa**
```
SELECT ruc_proveedor, razon_social, web_proveedor, rubro, direccion, telefono, id_est_proveedor
FROM proveedor
WHERE ruc_proveedor = <1>;
```

### Código Requerimiento : R - 008
### Codigo interfaz : I - 008
### Imagen interfaz : 
![image](../../04.Entregables/Entregable_PC3/Pantallas/ModCompras/MP3-.png)
### Sentecias SQL:
### Eventos: 
* **Pantalla Historial Cotizaciones: Se mostrará el historial de todas las cotizaciones aceptadas, no aceptadas y pendientes** 
```
SELECT id_cotizacion, id_est_cotizacion, monto_total, ruc_proveedor
FROM cotizacion
WHERE id_cotizacion = <1> OR id_cotizacion = <2> OR id_cotizacion = <3> OR id_cotizacion = <4> OR id_cotizacion = <5> OR id_cotizacion = <6>
```

### Código Requerimiento : R - 009
### Codigo interfaz : I - 009
### Imagen interfaz : 
![image](../../04.Entregables/Entregable_PC3/Pantallas/ModCompras/MP4.png)
### Sentecias SQL:
### Eventos: 
* **Pantalla Detalle Cotización: Nos permite visualizar todos los datos de una cotizacion, los productos y sus cantidades, ademas de los datos del proveedor.** 
```
SELECT p.ruc_proveedor, p.razon_social, p.rubro, p.direccion, p.telefono, p.web_proveedor, c.monto_total
FROM proveedor p
INNER JOIN cotizacion c ON c.ruc_proveedor = p.ruc_proveedor
WHERE c.id_cotizacion = <1>;

SELECT pd.nombre_producto, cx.cantidad
FROM proveedor p
INNER JOIN cotizacion c ON c.ruc_proveedor = p.ruc_proveedor
INNER JOIN cotizaciónxproducto cx ON cx.id_cotizacion = c.id_cotizacion
INNER JOIN producto pd ON pd.id_producto = cx.id_producto
WHERE c.id_cotizacion = <1>;
```

### Código Requerimiento : R - 010
### Codigo interfaz : I - 010
### Imagen interfaz : 
![image](../../04.Entregables/Entregable_PC3/Pantallas/ModCompras/MP5.png)
### Sentecias SQL:
### Eventos: 
* **BOTON Aceptar Oferta: Actualiza el estado de una cotizacion pendiente a un estado de Aceptado**
* **BOTON Rechazar Oferta: Actualiza el estado de una cotizacion pendiente a un estado de No Aceptado** 
```
-- BOTON Aceptar Oferta
UPDATE cotizacion 
SET id_est_cotizacion = 'A'
WHERE id_cotizacion = <1>;

-- BOTON Rechazar Oferta
UPDATE cotizacion 
SET id_est_cotizacion = 'N'
WHERE id_cotizacion = <1>;
```



