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
## 3.4 Modulo de Distribucion
### Código Requerimiento : R - 011
### Codigo interfaz : I - 011
### Imagen interfaz : 
![image](../../04.Entregables/Entregable_PC3/Pantallas/ModDistribucion/I0019.png)
### Sentecias SQL:
### Eventos: 
* **Pantalla Visualizar compras: Se mostrará todas las compras que ha realizado el cliente con id = <1>**
```
select fecha_pago,hora_pago
from venta 
inner join detalle_pago on venta.id_detalle_pago = detalle_pago.id_detalle_pago
where id_persona = <1>
```
### Código Requerimiento : R - 012
### Codigo interfaz : I - 012
### Imagen interfaz : 
![image](../../04.Entregables/Entregable_PC3/Pantallas/ModDistribucion/I0020.png)
### Sentecias SQL:
### Eventos: 
* **BOTON ACEPTAR : Se registrará la fecha de entrega de la compra con id = <4> y se creara un nuevo registro de pedido con estado P, sabiendo que el id_pedido es incrementable**
```
INSERT INTO Pedido (fecha_entrega, id_venta,id_est_pedido)
VALUES (TO_DATE(CONCAT(<3>, '-', <2>, '-', <1>), 'YYYY-MM-DD'),<4>,'P');
```
### Código Requerimiento : R - 013
### Codigo interfaz : I - 013
### Imagen interfaz : 
![image](../../04.Entregables/Entregable_PC3/Pantallas/ModDistribucion/I0021.png)
### Sentecias SQL:
### Eventos: 
* **Pantalla Visualizar pedidos: El gestor de distribucion podra visualizar los pedidos pendientes de la zona <A>,en este caso la 1**
```
SELECT 
    p.id_venta,
    p.fecha_entrega,
    pe.Nombre || ' ' || pe.Primer_apell || ' ' || pe.Segundo_apell AS nombre_cliente,
    p.id_est_pedido AS estado_pedido
FROM pedido p
INNER JOIN venta v ON p.id_venta = v.id_venta
INNER JOIN persona pe ON v.id_persona = pe.id_persona
INNER JOIN distrito d ON pe.id_distrito = d.id_distrito
INNER JOIN zona z ON d.id_zona = z.id_zona
WHERE z.id_zona = 1
AND p.id_est_pedido = 'P'
```
### Código Requerimiento : R - 014
### Codigo interfaz : I - 014
### Imagen interfaz : 
![image](../../04.Entregables/Entregable_PC3/Pantallas/ModDistribucion/I0022.png)
### Sentecias SQL:
### Eventos: 
* **Pantalla Asignar: El gestor de distribucion podra visualizar los repartidores disponibles y asignar una fecha y ruta al pedido de codigo <1>**
```
SELECT r.id_repartidor, r.nombre, r.apellido
FROM Repartidor r
INNER JOIN zona z ON r.id_zona = z.id_zona
INNER JOIN distrito d ON z.id_zona = d.id_zona
INNER JOIN persona pe ON pe.id_distrito = d.Id_distrito
INNER JOIN venta v ON v.id_persona = pe.Id_persona
INNER JOIN pedido p ON p.id_venta = v.Id_venta
WHERE p.Id_pedido = <1>;

INSERT INTO pedido(id_repartidor,id_ruta) 
VALUES (<2>,<3>);
WHERE id_pedido = <1>
```
### Código Requerimiento : R - 015
### Codigo interfaz : I - 015
### Imagen interfaz : 
![image](../../04.Entregables/Entregable_PC3/Pantallas/ModDistribucion/I0023.png)
### Sentecias SQL:
### Eventos: 
* **Visualizar historial de pedidos: El gestor de distribucion podra visualizar todos los pedidos que se han registrado**
```
SELECT p.Id_venta, p.fecha_entrega, 
	pe.Nombre || ' ' || pe.Primer_apell || ' ' || pe.Segundo_apell AS nombre_cliente, 
    te.estado_pedido AS estado_pedido
FROM Pedido p
INNER JOIN Venta v ON p.Id_venta = v.Id_venta
INNER JOIN Persona pe ON v.Id_persona = pe.Id_persona
INNER JOIN Tipo_est_pedido te ON p.id_est_pedido = te.id_est_pedido;
```
### Código Requerimiento : R - 016
### Codigo interfaz : I - 016
### Imagen interfaz : 
![image](../../04.Entregables/Entregable_PC3/Pantallas/ModDistribucion/I0024.png)
### Sentecias SQL:
### Eventos: 
* **Visualizar las entregas pendientes: El repartidor de id = <1> podra visualizar todos los pedidos que se encuentran pendientes**
```
SELECT p.Id_venta,p.fecha_entrega,te.estado_pedido
FROM Pedido p
INNER JOIN Repartidor r ON p.Id_repartidor = r.Id_repartidor
INNER JOIN Tipo_est_pedido te ON p.id_est_pedido = te.id_est_pedido
WHERE r.Id_repartidor = <1>
AND p.id_est_pedido = 'P';
```
### Código Requerimiento : R - 017
### Codigo interfaz : I - 017
### Imagen interfaz : 
![image](../../04.Entregables/Entregable_PC3/Pantallas/ModDistribucion/I0025.png)
### Sentecias SQL:
### Eventos: 
* **Boton entregado: El repartidor de id = <1> podra confirmar que se realizó la entrega con exito y actualizara el estado de pedido de codigo <2> a E**
```
UPDATE pedido
SET id_est_pedido = 'E'
WHERE id_repartidor = <1> AND id_pedido = <2>>;
```

### Código Requerimiento : R - 018
### Codigo interfaz : I - 018
### Imagen interfaz : 
![image](../../04.Entregables/Entregable_PC3/Pantallas/ModDistribucion/I0026.png)
### Sentecias SQL:
### Eventos: 
* **Visualizar el historial de pedido: El repartidor de id = <1> podra visualizar todas las entregas que realizó**
```
SELECT p.id_venta,p.fecha_entrega,e.estado_pedido
FROM pedido p
INNER JOIN tipo_est_pedido e on p.id_est_pedido = e.id_est_pedido
WHERE p.id_repartidor = <1>;
```
### Código Requerimiento : R - 019
### Codigo interfaz : I - 019
### Imagen interfaz : 
![image](../../04.Entregables/Entregable_PC3/Pantallas/ModDistribucion/I0027.png)
### Sentecias SQL:
### Eventos: 
* **BOTON VER MAS: El repartidor y el gestor de distribucion podran visualizar los detalles del pedido de id = <1>**
```
SELECT 
    pe.Nombre || ' ' || pe.Primer_apell || ' ' || pe.Segundo_apell AS nombre_cliente,
    p.fecha_entrega,
    p.Id_venta AS codigo_de_compra,
    p.Id_ruta,
    r.nombre AS nombre_repartidor,
    r.Id_repartidor,
    pe.Direccion
FROM Pedido p
INNER JOIN Venta v ON p.Id_venta = v.Id_venta
INNER JOIN Persona pe ON v.Id_persona = pe.Id_persona
INNER JOIN Repartidor r ON p.Id_repartidor = r.Id_repartidor
WHERE p.Id_pedido = <1>;
```

## 3.3 Modulo de Ventas
### Código Requerimiento : R - 020
### Codigo interfaz : I - 020
### Imagen interfaz : 
![image](Pantallas/ModVentas/catalogo.png)
### Sentecias SQL:
### Eventos: 
* **Pantalla Visualizar Catálogo productos: Se mostrará todos los productos al cliente**
```
SELECT id_producto,nombre_producto,precio_unit FROM PRODUCTO;
```

### Código Requerimiento : R - 021
### Codigo interfaz : I - 021
### Imagen interfaz : 
![image](Pantallas/ModVentas/info_prod_catalogo.png)
### Sentecias SQL:
### Eventos: 
* **Pantalla Visualizar información detallada del producto**
```
SELECT P.id_producto,nombre_producto,descripcion_prod,precio_unit,cant_max as cantidad_en_stock,t.nombre as Tipo_Producto,c.nombre as categoria_prod FROM PRODUCTO P
JOIN CATEGORIA_PROD C ON C.ID_CATEGORIA_PROD = P.ID_CATEGORIA_PROD
JOIN TIPO_PROD T ON C.ID_tipo_prod = T.id_tipo_prod;
```
### Código Requerimiento : R - 022
### Codigo interfaz : I - 22
### Imagen interfaz : 
![image](Pantallas/ModVentas/carrito.png)
### Sentecias SQL:
### Eventos: Decidir comprar algo en el carro de compras
* **Pantalla carrito de compras**
```
select nombre_producto,descripcion_prod,cant_prod,cant_prod*precio_unit as precio ,c.esta_activo,direccion,
(select sum(cant_prod*precio_unit) AS PRECIO_FINAL from producto p
 join ventaxprod V ON  p.id_producto = v.id_producto
JOIN venta ve on ve.id_venta=v.id_venta
join persona pe on ve.id_persona = pe.id_persona
join cupón c on c.id_cupón=v.id_cupón
 where ve.id_venta = <900001>
 group by ve.id_venta
 )

from producto p
join ventaxprod V ON  p.id_producto = v.id_producto
JOIN venta ve on ve.id_venta=v.id_venta
join persona pe on ve.id_persona = pe.id_persona
join cupón c on c.id_cupón=v.id_cupón
where ve.id_venta = 900001
```
### Código Requerimiento : R - 023
### Codigo interfaz : I - 023
### Imagen interfaz : 
![image](Pantallas/ModVentas/tipo_pago.png)
### Sentecias SQL:
### Eventos: Elegir método de pago
* **Pantalla Visualizar posibles tipos de pago a elección del cliente**
```
select t.nombre_tipo as tipo_pago,nro_tarjeta from Tipos_pago T
join detalle_pago D on T.ID_TIPO_PAGO = D.ID_TIPO_PAGO
JOIN venta v on v.id_detalle_pago = d.id_detalle_pago
where v.id_venta = <900001>
```
### Código Requerimiento : R - 024
### Codigo interfaz : I - 024
### Imagen interfaz : 
![image](Pantallas/ModVentas/info_despues_comprar.png)
### Sentecias SQL:
### Eventos: Decidir ver información mas detallada mientras esta en el carrito de compras
* **Pantalla Visualizar los detalles del producto que esta comprando en específico**
```
select nombre_producto,descripcion_prod,pe.direccion,cant_prod,(cant_max-cant_prod) as stock_restante,cant_prod*precio_unit as precio,
d.fecha_pago as fecha_en_el_carrito,t.nombre_tipo
from producto p
join ventaxprod V ON  p.id_producto = v.id_producto
JOIN venta ve on ve.id_venta=v.id_venta
join persona pe on ve.id_persona = pe.id_persona
join detalle_pago  d on ve.id_detalle_pago = d.id_detalle_pago
join tipos_pago t on t.id_tipo_pago = d.id_tipo_pago
where ve.id_venta = 900001 and p.id_producto=2
```
### Código Requerimiento : R - 027
### Codigo interfaz : I - 027
### Imagen interfaz : 
![image](Pantallas/ModVentas/cambio_direccion.png)
### Sentecias SQL:
### Eventos: Elegir (si lo desea) cambiar la direccion de envió antes de registrar su compra
* **Pantalla Visualizar cambio de dirección del cliente**
```
Primero actualizamos

UPDATE persona
SET direccion = 'Av. Siempre Viva 123'
WHERE id_persona = 1008

Luego verificamos dicha actualización

select direccion ,d.nombre as nombre_distrito from persona P
JOIN DISTRITO D ON P.ID_DISTRITO=D.ID_DISTRITO
WHERE id_persona = 1008
```
### Código Requerimiento : R - 025
### Codigo interfaz : I - 025
### Imagen interfaz : 
![image](Pantallas/ModVentas/historial_ventas_gestor.png)
### Sentecias SQL:
### Eventos: Decidir ver el historial de ventas de la empresa para dar seguimiento
* **Pantalla Visualizar historial de ventas**
```
select vp.id_venta,p.nombre,sum(vp.monto_total) as monto_final,t.nombre_tipo,d.fecha_pago,d.hora_pago from VentaXProd  vp
JOIN venta v on vp.id_venta=v.id_venta
join persona p on p.id_persona=v.id_persona
join detalle_pago  d on v.id_detalle_pago = d.id_detalle_pago
join tipos_pago t on t.id_tipo_pago = d.id_tipo_pago
group by vp.id_venta,p.nombre,t.nombre_tipo,d.fecha_pago,d.hora_pago
order by d.fecha_pago desc
```

### Código Requerimiento : R - 026
### Codigo interfaz : I - 026
### Imagen interfaz : 
![image](Pantallas/ModVentas/historial_cliente.png)
### Sentecias SQL:
### Eventos: Decidir ver el historial de ventas de algun cliente en especifico
* **Pantalla Visualizar historial de ventas de clientes**
```

select vp.id_venta,pr.id_producto,pr.nombre_producto,vp.cant_prod as cantidad,pr.precio_unit as precio_unitario,
vp.cant_prod*pr.precio_unit as sub_total,c.esta_activo,vp.cant_prod*pr.precio_unit as monto,
t.nombre_tipo as tipo_pago from VentaXProd  vp
JOIN venta v on vp.id_venta=v.id_venta
join producto pr on pr.id_producto=vp.id_producto
join persona p on p.id_persona=v.id_persona
join cupón c on c.id_cupón=vp.id_cupón
join detalle_pago  d on v.id_detalle_pago = d.id_detalle_pago
join tipos_pago t on t.id_tipo_pago = d.id_tipo_pago
where p.nombre = 'Brittney'

```

### Módulo de CRM


### Código Requerimiento : R - 028
### Codigo interfaz : I - 028
### Imagen interfaz : 
![image](../../04.Entregables/Entregable_PC3/Pantallas/ModCRM2/analisis.png)

Sectencia SQL:
Eventos:Visualizar análisis de datos de productos:
```
SELECT p.nombre_producto, COUNT(vp.id_producto) AS cantidad_vendida, SUM(vp.precio_total) AS ingreso_total
FROM Producto p
LEFT JOIN VentaXProd vp ON p.id_producto = vp.id_producto
GROUP BY p.nombre_producto
ORDER BY cantidad_vendida ASC;

```


### Código Requerimiento : R - 029
### Codigo interfaz : I - 029
### Imagen interfaz : 
![image](../../04.Entregables/Entregable_PC3/Pantallas/ModCRM2/comentarios.png)

Sectencia SQL:

Eventos: Visualizar, guardar y eliminar comentarios de clientes.

Visualizar comentarios:

```
SELECT p.Nombre || ' ' || p.Primer_apell || ' ' || p.Segundo_apell, 
       prod.nombre_producto, c.descrip_comentario, c.hora_comentario, c.fecha_comentario, c.Id_comentario
FROM Comentario c
JOIN Persona p ON c.Id_persona = p.Id_persona
JOIN Producto prod ON c.id_producto = prod.id_producto;

```

Guardar en revisión:


```
INSERT INTO Revision (id_comentario, puntos) 
VALUES (%s, %s);

```


Eliminar comentario:


```
DELETE FROM Comentario 
WHERE Id_comentario = %s;

```


Visualizar revisiones:


```
SELECT p.Nombre || ' ' || p.Primer_apell || ' ' || p.Segundo_apell, 
       prod.nombre_producto, r.puntos, c.Id_comentario, c.descrip_comentario, prod.descripcion_prod
FROM Revision r 
JOIN Comentario c ON r.id_comentario = c.Id_comentario
JOIN Persona p ON c.Id_persona = p.Id_persona
JOIN Producto prod ON c.id_producto = prod.id_producto;

```
Eliminar revisión:


```
DELETE FROM Revision 
WHERE id_comentario = %s;

```



### Código Requerimiento : R - 030
### Codigo interfaz : I - 030
### Imagen interfaz : 
![image](../../04.Entregables/Entregable_PC3/Pantallas/ModCRM2/correo.png)

Sectencia SQL:

Eventos: Visualizar, enviar y eliminar correos electrónicos.

Visualizar correos:

```
SELECT Id_persona, Nombre, Correo FROM Persona;

```

Cargar correos enviados:


```
SELECT email_name, FechaHora FROM EmailSend ORDER BY FechaHora DESC;

```

Guardar correo enviado:

```
INSERT INTO EmailSend (email_name, enviados, email_content, FechaHora) 
VALUES (%s, %s::text[], %s, %s);

```

Eliminar correo enviado:

```
DELETE FROM EmailSend 
WHERE email_name = %s;

```

Cargar detalles del correo enviado:

```
SELECT email_name, email_content, enviados 
FROM EmailSend 
WHERE email_name = %s;

```


### Código Requerimiento : R - 031
### Codigo interfaz : I - 031
### Imagen interfaz : 
![image](../../04.Entregables/Entregable_PC3/Pantallas/ModCRM2/formularios.png)

Sentencia SQL:

Eventos: Crear, enviar y gestionar formularios.

Cargar formularios creados:

```
SELECT Id_formulario, descrip_formulario 
FROM Formulario 
ORDER BY descrip_formulario;

```

Recuperar emails:

```
SELECT Id_persona, Nombre, Correo 
FROM Persona;

```

Insertar nuevo formulario:


```
INSERT INTO Formulario (descrip_formulario, fecha_creacion, Id_est_formulario) 
VALUES (%s, CURRENT_DATE, %s) 
RETURNING Id_formulario;

```

Insertar pregunta de formulario:

```
INSERT INTO Pregunta (pregunta, tipo_preg) 
VALUES (%s, %s) 
RETURNING Id_pregunta;

```

Vincular pregunta con formulario:


```
INSERT INTO FormularioxPregunta (Id_formulario, Id_pregunta) 
VALUES (%s, %s);

```

Eliminar formulario:

```
DELETE FROM Respuesta 
WHERE Id_pregunta IN (SELECT Id_pregunta FROM FormularioxPregunta WHERE Id_formulario = %s);

DELETE FROM FormularioxPregunta 
WHERE Id_formulario = %s;

DELETE FROM Formulario 
WHERE Id_formulario = %s;

```

Mostrar detalles del formulario:

```
SELECT pregunta 
FROM Pregunta 
INNER JOIN FormularioxPregunta 
ON Pregunta.Id_pregunta = FormularioxPregunta.Id_pregunta 
WHERE FormularioxPregunta.Id_formulario = %s;


```


Mostrar detalles de los encuestados:


```
SELECT Persona.Id_persona, Persona.Nombre 
FROM Persona 
INNER JOIN Respuesta 
ON Persona.Id_persona = Respuesta.Id_persona 
INNER JOIN Pregunta 
ON Respuesta.Id_pregunta = Pregunta.Id_pregunta 
INNER JOIN FormularioxPregunta 
ON Pregunta.Id_pregunta = FormularioxPregunta.Id_pregunta 
WHERE FormularioxPregunta.Id_formulario = %s;


```

Mostrar respuestas del encuestado:


```
SELECT Pregunta.pregunta, Respuesta.respuesta 
FROM Respuesta 
INNER JOIN Pregunta 
ON Respuesta.Id_pregunta = Pregunta.Id_pregunta 
INNER JOIN FormularioxPregunta 
ON Pregunta.Id_pregunta = FormularioxPregunta.Id_pregunta 
WHERE FormularioxPregunta.Id_formulario = %s 
AND Respuesta.Id_persona = %s;

```

### Código Requerimiento : R - 032
### Codigo interfaz : I - 032
### Imagen interfaz : 
![image](../../04.Entregables/Entregable_PC3/Pantallas/ModCRM2/home.png)

Sentencia :

Eventos: presiona un boton y enviar .

Wattsapp: Ejecuta enviar_wats5.py:

```
os.system('python c:/Users/Administrador/Desktop/pythonproyects/apli_escri/enviar_wats5.py')

```

Comentarios: Ejecuta revisar_comentario8.py:

```
os.system('python c:/Users/Administrador/Desktop/pythonproyects/apli_escri/revisar_comentario8.py')

```

Crear Formulario: Ejecuta crear_formularios14.py:

```
os.system('python c:/Users/Administrador/Desktop/pythonproyects/apli_escri/crear_formularios14.py')

```

Crear Email: Ejecuta correos_enviar8.py:

```
os.system('python c:/Users/Administrador/Desktop/pythonproyects/apli_escri/correos_enviar8.py')

```

Mis Clientes Potenciales: Ejecuta analisis4.py:

```
os.system('python c:/Users/Administrador/Desktop/pythonproyects/apli_escri/analisis4.py')

```

Ver Datos: Ejecuta verinfo.py

```
os.system('python c:/Users/Administrador/Desktop/pythonproyects/apli_escri/verinfo.py')

```

Abrir Pipeline: Ejecuta Pipelinefino3.py

```
os.system('python c:/Users/Administrador/Desktop/pythonproyects/apli_escri/Pipelinefino3.py')

```


### Código Requerimiento : R - 033
### Codigo interfaz : I - 033
### Imagen interfaz : 
![image](../../04.Entregables/Entregable_PC3/Pantallas/ModCRM2/pipeline.png)

Sentencia SQL:

Evento: Actualizar el estado del pipeline

Acción: Actualiza el estado del usuario en la base de datos y en la interfaz gráfica.

```
INSERT INTO Pipeline (Id_persona, estado) 
VALUES (%s, %s) 
ON CONFLICT (Id_persona) 
DO UPDATE SET estado = EXCLUDED.estado;

```

Evento: Enviar Email

Acción: Abre una ventana para redactar y enviar un correo electrónico al usuario seleccionado. Guarda el correo enviado en la base de datos.

```
INSERT INTO EmailSend (email_name, enviados, email_content, fechahora, Id_persona) 
VALUES (%s, %s::text[], %s, %s, %s)

```

Evento: Enviar WhatsApp

Acción: Abre una ventana para redactar y enviar un mensaje de WhatsApp al usuario seleccionado. Guarda el mensaje enviado en la base de datos.

```
INSERT INTO MensajeSend (mensaje_name, enviados, mensaje_content, fechahora, Id_persona) 
VALUES (%s, %s::text[], %s, %s, %s)

```


### Código Requerimiento : R - 034
### Codigo interfaz : I - 034
### Imagen interfaz : 
![image](../../04.Entregables/Entregable_PC3/Pantallas/ModCRM2/watsapp.png)

Sentencia SQL:

Evento: Cargar Contactos

Acción: Cargar y mostrar los contactos desde la base de datos en una lista.

```
SELECT Id_persona, Nombre, Telefono FROM Persona;

```

Evento: Agregar Destinatarios

Acción: Agregar los contactos seleccionados a la lista de destinatarios.

Evento: Enviar y Guardar Mensaje

Acción: Enviar un mensaje de WhatsApp a los contactos seleccionados y guardar el mensaje enviado en la base de datos.

```
INSERT INTO MensajeSend (mensaje_name, enviados, mensaje_content, FechaHora, Id_persona) 
VALUES (%s, %s::text[], %s, %s, %s)


```
Evento: Cargar Detalles del Mensaje Enviado

Acción: Cargar y mostrar los detalles del mensaje enviado seleccionado desde la base de datos.

```
SELECT mensaje_name, mensaje_content, enviados FROM MensajeSend WHERE mensaje_name = %s

```

Evento: Eliminar Mensaje Enviado

Acción: Eliminar el mensaje enviado seleccionado de la base de datos y de la lista.

```
DELETE FROM MensajeSend WHERE mensaje_name = %s

```

### Código Requerimiento : R - 035
### Codigo interfaz : I - 035
### Imagen interfaz : 
![image](../../04.Entregables/Entregable_PC3/Pantallas/ModCRM2/usuario.png)

Sentencia SQL:

Evento: Cargar Preferencias del Usuario

Acción: Cargar y mostrar las preferencias y datos recopilados del usuario desde la base de datos.

```
SELECT p.Nombre, f.descrip_formulario, r.respuesta 
FROM Respuesta r
JOIN Persona p ON r.Id_persona = p.Id_persona
JOIN Pregunta q ON r.Id_pregunta = q.Id_pregunta
JOIN FormularioxPregunta fp ON q.Id_pregunta = fp.Id_pregunta
JOIN Formulario f ON fp.Id_formulario = f.Id_formulario
WHERE p.Id_persona = %s;

```

Evento: Enviar Mensaje de WhatsApp Basado en Preferencias

Acción: Enviar un mensaje de WhatsApp al usuario basado en sus preferencias.

```
INSERT INTO MensajeSend (mensaje_name, enviados, mensaje_content, FechaHora, Id_persona) 
VALUES (%s, %s::text[], %s, %s, %s)

```


### Código Requerimiento : R - 036
### Codigo interfaz : I - 036
### Imagen interfaz : 
![image](../../04.Entregables/Entregable_PC3/Pantallas/ModCRM2/contacto.png)

Sentencia SQL:

Evento: Enviar Comentario

Acción: Insertar el comentario del usuario en la base de datos.

```
INSERT INTO Comentario (Id_persona, Id_producto, descrip_comentario, fecha_comentario, hora_comentario) 
VALUES (%s, %s, %s, CURRENT_DATE, CURRENT_TIME)

```


| Código | R036 |
|----------|----------|
|Nombre  | 	Envío de Comentarios por Parte del Usuario |
| Objetivo | <p align="left"> Permitir a los usuarios enviar comentarios sobre productos y servicios.</p> | 
| Descripción | Facilitar a los usuarios la capacidad de enviar comentarios y opiniones sobre productos y servicios, para que el gestor de CRM pueda revisarlos y actuar en consecuencia. | 
| Actor primario   | Usuario | 
|Actor secundario| Gestor de CRM|
|Precondiciones |El usuario ha accedido a su cuenta en la plataforma |


| Código Interfaz | I036 |
|----------|----------|
|Imagen interfaz||



##3.6. Módulo de finanzas

### Código Requerimiento : R - 037
### Codigo interfaz : I - 037
### Imagen interfaz : 
![image](https://github.com/fiis-bd241/grupo04/blob/main/04.Entregables/Entregable_PC3/Pantallas/VerFactura.PNG)
Sectencia SQL:
Eventos: Hacer click a una factura y visualiza la factura escogida:
```
select f.nro_factura, f.fecha_emision,dp.hora_pago,
concat (p.nombre, ' ', p.primer_apell,' ', p.segundo_apell) as Nombre,
p.direccion, tp.nombre_tipo as metodo_pago, 
tif.tipo_fac, prod.nombre_producto , vp.cant_prod, f.monto, e.nom_estado
from factura f
inner join Persona p on p.id_persona = f.id_persona
inner join Tipo_Factura tif on f.id_tip_fac = tif.id_tip_fac
inner join Estado e on f.id_estado = e.id_estado
inner join venta v on v.id_persona = f.id_persona
inner join detalle_pago dp on dp.id_detalle_pago = v.id_detalle_pago
inner join tipos_pago tp on tp.id_tipo_pago = dp.id_tipo_pago
inner join ventaxprod vp on vp.id_venta = v.id_venta
inner join producto prod on prod.id_producto = vp.id_producto
where f.nro_factura = 2022001;
```
### Código Requerimiento : R - 038
### Codigo interfaz : I - 038
### Imagen interfaz : 
![image](https://github.com/fiis-bd241/grupo04/blob/main/04.Entregables/Entregable_PC3/Pantallas/HistorialFactura.PNG)
Eventos: Visualizar todas las facturas, y poder filtrarlo por el año, etc.

--Todas las fcaturas sin filtro:
```
select f.nro_factura, f.fecha_emision,
f.monto,f.id_persona, f.ruc_proveedor,  tif.tipo_fac, e.nom_estado
from factura f
inner join Tipo_Factura tif on f.id_tip_fac = tif.id_tip_fac
inner join Estado e on f.id_estado = e.id_estado
order by f.nro_factura; 
```
-Facturas de un año en espcifico:
```
select f.nro_factura, f.fecha_emision,dp.hora_pago,
concat (p.nombre, ' ', p.primer_apell,' ', p.segundo_apell) as Nombre,
p.direccion, tp.nombre_tipo as metodo_pago, 
tif.tipo_fac, prod.nombre_producto , vp.cant_prod, f.monto, e.nom_estado
from factura f
inner join Persona p on p.id_persona = f.id_persona
inner join Tipo_Factura tif on f.id_tip_fac = tif.id_tip_fac
inner join Estado e on f.id_estado = e.id_estado
inner join venta v on v.id_persona = f.id_persona
inner join detalle_pago dp on dp.id_detalle_pago = v.id_detalle_pago
inner join tipos_pago tp on tp.id_tipo_pago = dp.id_tipo_pago
inner join ventaxprod vp on vp.id_venta = v.id_venta
inner join producto prod on prod.id_producto = vp.id_producto
where extract(year from fecha_emision) = 2022;
```
### ![image](https://github.com/fiis-bd241/grupo04/blob/main/04.Entregables/Entregable_PC3/Pantallas/A%C3%B1adirFactura.PNG)
--Para llenar la factura:
```
select f.nro_factura, f.fecha_emision,dp.hora_pago,p.nombre,
concat (p.nombre, ' ', p.primer_apell,' ', p.segundo_apell) as Nombre,
p.direccion, tp.nombre_tipo as metodo_pago, 
tif.tipo_fac, prod.nombre_producto , vp.cant_prod, f.monto
from factura f
inner join Persona p on p.id_persona = f.id_persona
inner join Tipo_Factura tif on f.id_tip_fac = tif.id_tip_fac
inner join Estado e on f.id_estado = e.id_estado
inner join venta v on v.id_persona = f.id_persona
inner join detalle_pago dp on dp.id_detalle_pago = v.id_detalle_pago
inner join tipos_pago tp on tp.id_tipo_pago = dp.id_tipo_pago
inner join ventaxprod vp on vp.id_venta = v.id_venta
inner join producto prod on prod.id_producto = vp.id_producto;
```
### Código Requerimiento : R - 039
### Codigo interfaz : I - 039
### Imagen interfaz : 
![image](https://github.com/fiis-bd241/grupo04/blob/main/04.Entregables/Entregable_PC3/Pantallas/Factura%20Estados.PNG)
eventos: Podemos ver las facturas que faltan pagar, etc:

--Facturas que faltan pgar hasta hoy
```
select f.nro_factura, f.fecha_emision,
f.monto,f.id_persona, f.ruc_proveedor,  tif.tipo_fac, e.nom_estado
from factura f
inner join Tipo_Factura tif on f.id_tip_fac = tif.id_tip_fac
inner join Estado e on f.id_estado = e.id_estado
where e.nom_estado IN ('Falta Pagar', 'No Pagado')
  AND f.fecha_emision <= CURRENT_DATE;
```
--Facturas que faltan pagar la semana actual
```
select f.nro_factura, f.fecha_emision,
f.monto,f.id_persona, f.ruc_proveedor,  tif.tipo_fac, e.nom_estado
from factura f
inner join Tipo_Factura tif on f.id_tip_fac = tif.id_tip_fac
inner join Estado e on f.id_estado = e.id_estado
where e.nom_estado IN ('Falta Pagar', 'No Pagado')
  and extract(week from f.fecha_emision) = extract(week from current_date)
  and extract(year from f.fecha_emision) = extract(year from current_date);
```
--Faltan mes actual 
```
select f.nro_factura, f.fecha_emision,
f.monto,f.id_persona, f.ruc_proveedor,  tif.tipo_fac, e.nom_estado
from factura f
inner join Tipo_Factura tif on f.id_tip_fac = tif.id_tip_fac
inner join Estado e on f.id_estado = e.id_estado
where e.nom_estado IN ('Falta Pagar', 'No Pagado')
  and extract(month from f.fecha_emision) = extract(month from current_date)-1
  and extract(year from f.fecha_emision) = extract(year from current_date);
```  

### Código Requerimiento : R - 040
### Codigo interfaz : I - 040
### Imagen interfaz : 
![image](https://github.com/fiis-bd241/grupo04/blob/main/04.Entregables/Entregable_PC3/Pantallas/HistorialdeAsientos.PNG)

-Eventos: Ver los asientos contables así como su estado y el tipo.
```
select a.id_asiento_contable,ta.nombre_tipo_as as tipo_asientocontable, a.cant_debe, a.cant_haber, 
f.monto, e.nom_estado 
from asiento_contable a
inner join tipo_asiento_contable ta on ta.id_tipo_asiento_contable = a.id_tipo_asiento_contable
inner join factura f on f.nro_factura = a.nro_factura
inner join Persona p on p.id_persona = f.id_persona
inner join Estado e on f.id_estado = e.id_estado
order by a.id_asiento_contable;
```

### Código Requerimiento : R - 041
### Codigo interfaz : I - 041
### Imagen interfaz : 
![image](https://github.com/fiis-bd241/grupo04/blob/main/04.Entregables/Entregable_PC3/Pantallas/EstadodeResultados.PNG)

-Eventos: Ver el estado de Resultados:
```
select ite.id_item_est__resultados, tie.nombre_tipo_item, f.monto, tv.nom_val,  
top.nom_operacion, er.periodo, er.mes 
from item_estado_resultados ite
inner join asiento_contable a on a.id_asiento_contable = ite.id_asiento_contable
inner join factura f on f.nro_factura = a.nro_factura
inner join estadoxitem ei on ei.id_item_est__resultados= ite.id_item_est__resultados
inner join estado_de_Resultados er on er.id_estad_result = ei.id_estad_result
inner join tipo_item_est tie on tie.id_tipo_item_est = ite.id_tipo_item_est
inner join Tip_valor tv on tv.id_tip_valor = tie.id_tip_valor
inner join Tip_operación top on top.id_tip_op = tie.id_tip_op ;
```
