# Capítulo 08: Creación de tablas
```sql
CREATE TABLE tipo_prod
(
  Id_tipo_prod INT NOT NULL,
  Nombre VARCHAR(100) NOT NULL,
  PRIMARY KEY (Id_tipo_prod)
);

CREATE TABLE Categoria_prod
(
  Nombre VARCHAR(100) NOT NULL,
  Id_categoria_prod INT NOT NULL,
  Id_tipo_prod INT NOT NULL,
  PRIMARY KEY (Id_categoria_prod),
  FOREIGN KEY (Id_tipo_prod) REFERENCES tipo_prod(Id_tipo_prod)
);

CREATE TABLE Area
(
  Cod_area VARCHAR(100) NOT NULL,
  Tipo_area VARCHAR(100) NOT NULL,
  Descripcion VARCHAR(100) NOT NULL,
  PRIMARY KEY (Cod_area)
);

CREATE TABLE zona
(
  id_zona INT NOT NULL,
  nombre VARCHAR(100) NOT NULL,
  cant_distritos INT NOT NULL,
  PRIMARY KEY (id_zona)
);

CREATE TABLE distrito
(
  Id_distrito INT NOT NULL,
  nombre VARCHAR(100) NOT NULL,
  ubigeo CHAR(6) NOT NULL,
  cod_postal CHAR(2) NOT NULL,
  id_zona INT NOT NULL,
  PRIMARY KEY (Id_distrito),
  FOREIGN KEY (id_zona) REFERENCES zona(id_zona)
);

CREATE TABLE Equipo_Marketing
(
  Id_equipo_mark INT NOT NULL,
  nombre_equipo VARCHAR(100) NOT NULL,
  PRIMARY KEY (Id_equipo_mark)
);

CREATE TABLE Rol
(
  Id_rol VARCHAR(20) NOT NULL,
  nombre_rol VARCHAR(100) NOT NULL,
  PRIMARY KEY (Id_rol)
);

CREATE TABLE Ruta
(
  Id_ruta INT NOT NULL,
  distrito_inicial VARCHAR(100) NOT NULL,
  distrito_final VARCHAR(100) NOT NULL,
  Tiempo_prom VARCHAR(100) NOT NULL,
  medio_transporte VARCHAR(100) NOT NULL,
  PRIMARY KEY (Id_ruta)
);


CREATE TABLE Tipo_mov
(
  Id_tipo_mov CHAR(1) NOT NULL,
  nombre_tipo_mov VARCHAR(100) NOT NULL,
  PRIMARY KEY (Id_tipo_mov)
);

CREATE TABLE Tipo_Genero
(
  Id_tipo_genero CHAR(1) NOT NULL,
  tipo_genero VARCHAR(100) NOT NULL,
  PRIMARY KEY (Id_tipo_genero)
);

CREATE TABLE Tipo_est_cotizacion
(
  Id_est_cotizacion CHAR(1) NOT NULL,
  est_cotizacion VARCHAR(100) NOT NULL,
  PRIMARY KEY (Id_est_cotizacion)
);

CREATE TABLE Tipo_est_proveedor
(
  Id_est_proveedor VARCHAR(10) NOT NULL,
  est_proveedor VARCHAR(100) NOT NULL,
  PRIMARY KEY (Id_est_proveedor)
);

CREATE TABLE Tipos_pago
(
  id_tipo_pago INT NOT NULL,
  nombre_tipo VARCHAR(100) NOT NULL,
  PRIMARY KEY (id_tipo_pago)
);

CREATE TABLE Persona
(
  Id_persona INT,
  Nombre VARCHAR(100) NOT NULL,
  Primer_apell VARCHAR(100) NOT NULL,
  Segundo_apell VARCHAR(100) NOT NULL,
  Correo VARCHAR(100) NOT NULL,
  Telefono INT NOT NULL,
  Direccion VARCHAR(200) NOT NULL,
  Usuario VARCHAR(100),
  Contraseña VARCHAR(100),
  Id_distrito INT,
  Id_cargo VARCHAR(20),
  Id_equipo_mark INT,
  Cod_area VARCHAR(100),
  Id_tipo_genero CHAR(1) NOT NULL,
  PRIMARY KEY (Id_persona),
  FOREIGN KEY (Id_distrito) REFERENCES distrito(Id_distrito),
  FOREIGN KEY (Id_cargo) REFERENCES Rol(Id_rol),
  FOREIGN KEY (Id_equipo_mark) REFERENCES Equipo_Marketing(Id_equipo_mark),
  FOREIGN KEY (Cod_area) REFERENCES Area(Cod_area),
  FOREIGN KEY (Id_tipo_genero) REFERENCES Tipo_Genero(Id_tipo_genero)
);

CREATE TABLE Proveedor
(
  RUC_proveedor CHAR(11) NOT NULL,
  Razon_social VARCHAR(100) NOT NULL,
  web_proveedor VARCHAR(100),
  Rubro VARCHAR(100) NOT NULL,
  Direccion VARCHAR(100) NOT NULL,
  Telefono VARCHAR(15) NOT NULL,
  Id_est_proveedor VARCHAR(10) NOT NULL,
  PRIMARY KEY (RUC_proveedor),
  FOREIGN KEY (Id_est_proveedor) REFERENCES Tipo_est_proveedor(Id_est_proveedor)
);

CREATE TABLE Cotizacion
(
  id_cotizacion INT NOT NULL,
  Monto_total NUMERIC(7,2) NOT NULL,
  RUC_proveedor CHAR(11) NOT NULL,
  Id_est_cotizacion CHAR(1) NOT NULL,
  PRIMARY KEY (id_cotizacion),
  FOREIGN KEY (RUC_proveedor) REFERENCES Proveedor(RUC_proveedor),
  FOREIGN KEY (Id_est_cotizacion) REFERENCES Tipo_est_cotizacion(Id_est_cotizacion)
);

CREATE TABLE Repartidor
(
  Id_repartidor INT NOT NULL,
  usuario VARCHAR(100) NOT NULL,
  contraseña VARCHAR(100) NOT NULL,
  apellido VARCHAR(100) NOT NULL,
  nombre VARCHAR(100) NOT NULL,
  id_zona INT NOT NULL,
  PRIMARY KEY (Id_repartidor),
  FOREIGN KEY (id_zona) REFERENCES zona(id_zona)
);

CREATE TABLE Campaña
(
  Id_campaña INT NOT NULL,
  nom_campaña VARCHAR(100) NOT NULL,
  fecha_ini DATE NOT NULL,
  fecha_fin DATE NOT NULL,
  dir_url VARCHAR(100) NOT NULL,
  modalidad VARCHAR(100) NOT NULL,
  archivo VARCHAR(100) NOT NULL,
  desc_campaña FLOAT NOT NULL,
  Id_equipo_mark INT NOT NULL,
  Id_gest_mark INT NOT NULL,
  PRIMARY KEY (Id_campaña),
  FOREIGN KEY (Id_equipo_mark) REFERENCES Equipo_Marketing(Id_equipo_mark),
  FOREIGN KEY (Id_gest_mark) REFERENCES Persona(Id_persona)
);

CREATE TABLE Detalle_pago
(
  Id_detalle_pago INT NOT NULL,
  fecha_pago DATE NOT NULL,
  hora_pago VARCHAR(10) NOT NULL,
  id_tipo_pago INT NOT NULL,
  PRIMARY KEY (Id_detalle_pago),
  FOREIGN KEY (id_tipo_pago) REFERENCES Tipos_pago(id_tipo_pago)
);

CREATE TABLE Producto
(
  id_producto INT NOT NULL,
  nombre_producto VARCHAR(100) NOT NULL,
  descripcion_prod VARCHAR(100) NOT NULL,
  Cant_min INT NOT NULL,
  Cant_max INT NOT NULL,
  Precio_unit FLOAT NOT NULL,
  Id_categoria_prod INT NOT NULL,
  PRIMARY KEY (id_producto),
  FOREIGN KEY (Id_categoria_prod) REFERENCES Categoria_prod(Id_categoria_prod)
);

CREATE TABLE CampañaXProd
(
  id_producto INT NOT NULL,
  Id_campaña INT NOT NULL,
  PRIMARY KEY (id_producto, Id_campaña),
  FOREIGN KEY (id_producto) REFERENCES Producto(id_producto),
  FOREIGN KEY (Id_campaña) REFERENCES Campaña(Id_campaña)
);

CREATE TABLE Canal
(
  Id_canal INT NOT NULL,
  nombre_canal VARCHAR(100) NOT NULL,
  PRIMARY KEY (Id_canal)
);


CREATE TABLE CampañaXCanal
(
  Id_campaña INT NOT NULL,
  Id_canal INT NOT NULL,
  PRIMARY KEY (Id_campaña, Id_canal),
  FOREIGN KEY (Id_campaña) REFERENCES Campaña(Id_campaña),
  FOREIGN KEY (Id_canal) REFERENCES Canal(Id_canal)
);


CREATE TABLE Observacion
(
  Id_observacion INT NOT NULL,
  descripcion VARCHAR(100) NOT NULL,
  Id_campaña INT NOT NULL,
  estado_atendido BOOLEAN NOT NULL,
  PRIMARY KEY (Id_observacion),
  FOREIGN KEY (Id_campaña) REFERENCES Campaña(Id_campaña)
);


CREATE TABLE CotizaciónxProducto
(
  Cantidad INT NOT NULL,
  id_cotizacion INT NOT NULL,
  id_producto INT NOT NULL,
  PRIMARY KEY (id_cotizacion, id_producto),
  FOREIGN KEY (id_cotizacion) REFERENCES Cotizacion(id_cotizacion),
  FOREIGN KEY (id_producto) REFERENCES Producto(id_producto)
);

CREATE TABLE ProveedorxProducto
(
  Precio_prod_prov FLOAT NOT NULL,
  id_producto INT NOT NULL,
  RUC_proveedor CHAR(11) NOT NULL,
  PRIMARY KEY (id_producto, RUC_proveedor),
  FOREIGN KEY (id_producto) REFERENCES Producto(id_producto),
  FOREIGN KEY (RUC_proveedor) REFERENCES Proveedor(RUC_proveedor)
);

CREATE TABLE Venta
(
  Id_venta INT NOT NULL,
  monto_final FLOAT NOT NULL,
  Id_detalle_pago INT NOT NULL,
  Id_persona INT,
  Nro_Tarjeta VARCHAR(20),
  PRIMARY KEY (Id_venta),
  FOREIGN KEY (Id_detalle_pago) REFERENCES Detalle_pago(Id_detalle_pago),
  FOREIGN KEY (Id_persona) REFERENCES Persona(Id_persona)
);

CREATE TABLE Cupón
(
  Id_cupón INT NOT NULL,
  fecha_ini_cup DATE NOT NULL,
  fecha_fin_cup DATE NOT NULL,
  desc_cup FLOAT NOT NULL,
  esta_activo BOOLEAN NOT NULL,
  PRIMARY KEY (Id_cupón)
);

CREATE TABLE VentaXProd
(
  cant_prod INT NOT NULL,
  monto_total FLOAT NOT NULL,
  id_prod_venta INT NOT NULL,
  id_producto INT NOT NULL,
  Id_venta INT NOT NULL,
  Id_cupón INT,
  PRIMARY KEY (id_prod_venta, id_producto, Id_venta),
  FOREIGN KEY (id_producto) REFERENCES Producto(id_producto),
  FOREIGN KEY (Id_venta) REFERENCES Venta(Id_venta)
);

CREATE TABLE Tipo_est_pedido (
    est_pedido VARCHAR(1) PRIMARY KEY,
    descripcion VARCHAR(50) NOT NULL
);

CREATE TABLE Pedido
(
  Id_pedido SERIAL NOT NULL,
  fecha_entrega DATE NOT NULL,
  est_pedido VARCHAR(100) NOT NULL,
  hora_entrega TIME,
  Id_ruta INT NOT NULL,
  Id_repartidor INT NOT NULL,
  Id_venta INT NOT NULL,
  PRIMARY KEY (Id_pedido),
  FOREIGN KEY (Id_ruta) REFERENCES Ruta(Id_ruta),
  FOREIGN KEY (Id_repartidor) REFERENCES Repartidor(Id_repartidor),
  FOREIGN KEY (Id_venta) REFERENCES Venta(Id_venta)
);


CREATE TABLE Alternativa
(
  id_alternativa INT NOT NULL,
  alternativa VARCHAR[]  NOT NULL,
  PRIMARY KEY (id_alternativa)
);

CREATE TABLE Pregunta
(
  Id_pregunta INT NOT NULL,
  pregunta VARCHAR(200) NOT NULL,
  tipo_preg VARCHAR(100) NOT NULL,
  id_alternativa INT,
  PRIMARY KEY (Id_pregunta),
  FOREIGN KEY (id_alternativa) REFERENCES Alternativa(id_alternativa)
);

CREATE TABLE Tipo_est_formulario
(
  Id_est_formulario INT NOT NULL,
  est_formulario VARCHAR(100) NOT NULL,
  PRIMARY KEY (Id_est_formulario)
);

CREATE TABLE Formulario
(
  Id_formulario INT NOT NULL,
  descrip_formulario VARCHAR(500) NOT NULL,
  fecha_creacion DATE NOT NULL,
  Id_persona INT,
  Id_est_formulario INT NOT NULL,
  PRIMARY KEY (Id_formulario),
  FOREIGN KEY (Id_persona) REFERENCES Persona(Id_persona),
  FOREIGN KEY (Id_est_formulario) REFERENCES Tipo_est_formulario(Id_est_formulario)
);

CREATE TABLE Respuesta
(
  Id_respuesta INT NOT NULL,
  respuesta VARCHAR(200) NOT NULL,
  Id_pregunta INT NOT NULL,
  PRIMARY KEY (Id_respuesta),
  FOREIGN KEY (Id_pregunta) REFERENCES Pregunta(Id_pregunta)
);

CREATE TABLE FormularioxPregunta
(
  Id_formulario INT NOT NULL,
  Id_pregunta INT NOT NULL,
  PRIMARY KEY (Id_formulario, Id_pregunta),
  FOREIGN KEY (Id_formulario) REFERENCES Formulario(Id_formulario),
  FOREIGN KEY (Id_pregunta) REFERENCES Pregunta(Id_pregunta)
);
CREATE TABLE PreguntaxRespuesta
(
  Id_pregunta INT NOT NULL,
  Id_respuesta INT NOT NULL,
  PRIMARY KEY (Id_pregunta, Id_respuesta),
  FOREIGN KEY (Id_pregunta) REFERENCES Pregunta(Id_pregunta),
  FOREIGN KEY (Id_respuesta) REFERENCES Respuesta(Id_respuesta)
);
CREATE TABLE Comentario
(
  Id_comentario INT NOT NULL,
  descrip_comentario VARCHAR(200) NOT NULL,
  fecha_comentario DATE NOT NULL,
  hora_comentario VARCHAR(10) NOT NULL,
  id_producto INT NOT NULL,
  Id_persona INT,
  PRIMARY KEY (Id_comentario),
  FOREIGN KEY (id_producto) REFERENCES Producto(id_producto),
  FOREIGN KEY (Id_persona) REFERENCES Persona(Id_persona)
);

CREATE TABLE Almacen
(
  Id_Almacen INT NOT NULL,
  Tipo_Almacen VARCHAR(30) NOT NULL,
  Descrip_Almacen VARCHAR(259) NOT NULL,
  PRIMARY KEY (Id_Almacen)
);

CREATE TABLE Secciones
(
  Seccion CHAR(1) NOT NULL,
  Id_Almacen INT NOT NULL,
  PRIMARY KEY (Seccion),
  FOREIGN KEY (Id_Almacen) REFERENCES Almacen(Id_Almacen)
);

CREATE TABLE Estands
(
  Estand VARCHAR(2) NOT NULL,
  Id_Almacen INT NOT NULL,
  Seccion CHAR(1) NOT NULL,
  PRIMARY KEY (Estand),
  FOREIGN KEY (Id_Almacen) REFERENCES Almacen(Id_Almacen),
  FOREIGN KEY (Seccion) REFERENCES Secciones(Seccion)
);

CREATE TABLE Repisas
(
  Repisa VARCHAR(2) NOT NULL,
  Id_Almacen INT NOT NULL,
  Seccion CHAR(1) NOT NULL,
  PRIMARY KEY (Repisa),
  FOREIGN KEY (Id_Almacen) REFERENCES Almacen(Id_Almacen),
  FOREIGN KEY (Seccion) REFERENCES Secciones(Seccion)
);

CREATE TABLE Ubicacion
(
  Ubicacion_Prod VARCHAR(10) NOT NULL,
  Seccion CHAR(1) NOT NULL,
  Estand VARCHAR(2) NOT NULL,
  Repisa VARCHAR(2) NOT NULL,
  Id_Almacen INT NOT NULL,
  PRIMARY KEY (Ubicacion_Prod),
  FOREIGN KEY (Id_Almacen) REFERENCES Almacen(Id_Almacen),
  FOREIGN KEY (Seccion) REFERENCES Secciones(Seccion),
  FOREIGN KEY (Estand) REFERENCES Estands(Estand),
  FOREIGN KEY (Repisa) REFERENCES Repisas(Repisa)
);

CREATE TABLE Transportista
(
  Id_Transportista INT NOT NULL,
  Nombre_Transp CHAR(30) NOT NULL,
  Estado CHAR(20) NOT NULL,
  PRIMARY KEY (Id_Transportista)
);

CREATE TABLE Orden_Almacen
(
  Id_Orden_Almacen VARCHAR(20) NOT NULL,
  Cod_Area VARCHAR(100),
  Id_Persona INT,
  Id_Tipo_Prod INT NOT NULL,
  Id_Pedido INT,
  ID_Almacen INT NOT NULL,
  PRIMARY KEY (Id_Orden_Almacen),
  FOREIGN KEY (Cod_Area) REFERENCES Area(Cod_Area),
  FOREIGN KEY (Id_Persona) REFERENCES Persona(Id_Persona),
  FOREIGN KEY (Id_Pedido) REFERENCES Pedido(Id_Pedido),
  FOREIGN KEY (Id_Tipo_Prod) REFERENCES Tipo_Prod(Id_Tipo_Prod)
);

CREATE TABLE Movimiento
(
  Id_Mov INT NOT NULL,
  Fecha_Mov DATE NOT NULL,
  Id_Tipo_Mov CHAR(1) NOT NULL,
  Id_Almacen INT NOT NULL,
  Id_Transportista INT,
  Id_Orden_Almacen VARCHAR(20) NOT NULL,
  PRIMARY KEY (Id_Mov),
  FOREIGN KEY (Id_Tipo_Mov) REFERENCES Tipo_Mov(Id_Tipo_Mov),
  FOREIGN KEY (Id_Almacen) REFERENCES Almacen(Id_Almacen),
  FOREIGN KEY (Id_Transportista) REFERENCES Transportista(Id_Transportista),
  FOREIGN KEY (Id_Orden_Almacen) REFERENCES Orden_Almacen(Id_Orden_Almacen)
);

CREATE TABLE Inventario
(
  Cod_Barra_Prod INT NOT NULL,
  Descrip_Presentacion CHAR(20) NOT NULL,
  Entradas INT NOT NULL,
  Salidas INT,
  Stock INT,
  Id_Producto INT NOT NULL,
  Importe_Invent DECIMAL,
  Ubicacion_Prod VARCHAR(10) NOT NULL,
  PRIMARY KEY (Cod_Barra_Prod),
  FOREIGN KEY (Id_Producto) REFERENCES Producto(Id_Producto),
  FOREIGN KEY (Ubicacion_Prod) REFERENCES Ubicacion(Ubicacion_Prod)
);
CREATE TABLE Tipo_Factura
(
  id_tip_Fac INT NOT NULL,
  tipo_fac VARCHAR(100) NOT NULL,
  PRIMARY KEY (id_tip_Fac)
);
CREATE TABLE Estado
(
  id_estado INT NOT NULL,
  nom_estado VARCHAR(100) NOT NULL,
  PRIMARY KEY (id_estado)
);

CREATE TABLE Tip_valor
(
  id_tip_valor INT NOT NULL,
  nom_val VARCHAR(100) NOT NULL,
  PRIMARY KEY (id_tip_valor)
);

CREATE TABLE Tip_operación
(
  id_tip_op INT NOT NULL,
  nom_operacion VARCHAR(100) NOT NULL,
  PRIMARY KEY (id_tip_op)
);


CREATE TABLE Tipo_presupuesto
(
  Id_tipo_presupuesto INT NOT NULL,
  nombre_tipo VARCHAR(100) NOT NULL,
  PRIMARY KEY (Id_tipo_presupuesto)
);

CREATE TABLE Tipo_item_est
(
  Id_tipo_item_est INT NOT NULL,
  nombre_tipo_item VARCHAR(100) NOT NULL,
  id_tip_op INT NOT NULL,
  id_tip_valor INT NOT NULL,
  PRIMARY KEY (Id_tipo_item_est),
  FOREIGN KEY (id_tip_op) REFERENCES Tip_operación(id_tip_op),
  FOREIGN KEY (id_tip_valor) REFERENCES Tip_valor(id_tip_valor)
);

CREATE TABLE tipo_asiento_contable
(
  id_tipo_asiento_contable INT NOT NULL,
  nombre_tipo_as VARCHAR(100) NOT NULL,
  PRIMARY KEY (id_tipo_asiento_contable)
);   
CREATE TABLE Estado_de_Resultados
(
  id_estad_result INT NOT NULL,
  periodo INT NOT NULL,
  mes INT NOT NULL,
  PRIMARY KEY (id_estad_result)
); 
CREATE TABLE Factura
(
  nro_factura INT NOT NULL,
  fecha_emision DATE NOT NULL,
  monto FLOAT NOT NULL,
  Id_persona INT,
  RUC_proveedor CHAR(11),
  id_tip_Fac INT NOT NULL,
  id_estado INT NOT NULL,
  PRIMARY KEY (nro_factura),
  FOREIGN KEY (RUC_proveedor) REFERENCES Proveedor(RUC_proveedor),
  FOREIGN KEY (Id_persona) REFERENCES Persona(Id_persona),
  FOREIGN KEY (id_tip_Fac) REFERENCES Tipo_Factura(id_tip_Fac),
  FOREIGN KEY (id_estado) REFERENCES Estado(id_estado)
); 

CREATE TABLE Presupuesto
(
  Id_presupuesto INT NOT NULL,
  fecha_elaboracion DATE NOT NULL,
  periodo VARCHAR(100) NOT NULL,
  Id_tipo_presupuesto INT NOT NULL,
  Id_persona INT,
  PRIMARY KEY (Id_presupuesto),
  FOREIGN KEY (Id_tipo_presupuesto) REFERENCES Tipo_presupuesto(Id_tipo_presupuesto),
  FOREIGN KEY (Id_persona) REFERENCES Persona(Id_persona)
);

CREATE TABLE Asiento_Contable
(
  Id_asiento_contable INT NOT NULL,
  cant_debe FLOAT NOT NULL,
  cant_haber FLOAT NOT NULL,
  nro_factura INT NOT NULL,
  id_tipo_asiento_contable INT NOT NULL,
  PRIMARY KEY (Id_asiento_contable),
  FOREIGN KEY (nro_factura) REFERENCES Factura(nro_factura),
  FOREIGN KEY (id_tipo_asiento_contable) REFERENCES tipo_asiento_contable(id_tipo_asiento_contable)
);

CREATE TABLE Item_estado_resultados(
  Id_item_est__resultados INT NOT NULL,
  Id_asiento_contable INT NOT NULL,
  Id_tipo_item_est INT NOT NULL,
  PRIMARY KEY (Id_item_est__resultados),
  FOREIGN KEY (Id_asiento_contable) REFERENCES Asiento_Contable(Id_asiento_contable),
  FOREIGN KEY (Id_tipo_item_est) REFERENCES Tipo_item_est(Id_tipo_item_est)
);  
CREATE TABLE EstadoxItem
(
  monto FLOAT NOT NULL,
  Id_item_est__resultados INT NOT NULL,
  id_estad_result INT NOT NULL,
  PRIMARY KEY (Id_item_est__resultados, id_estad_result),
  FOREIGN KEY (Id_item_est__resultados) REFERENCES Item_estado_resultados(Id_item_est__resultados),
  FOREIGN KEY (id_estad_result) REFERENCES Estado_de_Resultados(id_estad_result)
);

-- tipo_prod
insert into tipo_prod values ('1', 'Maquillaje');
insert into tipo_prod values ('2', 'Papelería');
select * from tipo_prod;
-- Categoria_prod
insert into Categoria_prod (Id_categoria_prod, Nombre, Id_tipo_prod)
values ('1', 'Cuadernos', '2'),('2', 'Lapiceros', '2');
insert into Categoria_prod values ('Paletas', '3', '1');
insert into Categoria_prod values ('Rubores', '4', '1');
insert into Categoria_prod values ('Primers', '5', '1');
insert into Categoria_prod values ('Glitter', '6', '1');
insert into Categoria_prod values ('Máscara de pestañas', '7', '1');
insert into Categoria_prod values ('Labiales', '8', '1');
insert into Categoria_prod values ('Polvos', '9', '1');
insert into Categoria_prod values ('Correctores', '10', '1');
insert into Categoria_prod values ('Delineador', '11', '1');
select * from Categoria_prod;
-- Tipo_est_proveedor
insert into Tipo_est_proveedor values ('A', 'Activo'),('N', 'No Activo');
select * from Tipo_est_proveedor;
-- Proveedor
insert into Proveedor values ('20603302151', 'IMPORT EXPORT JAXU S.A.C','facebook.com/JAXUPERU', 'Papelería', 'Cal. Schell Nro. 255 Com. San Miguel de Miraflores', '980520529', 'A'),
('20607504149', 'STELLAX S.A.C.','facebook.com/STELLAX', 'Papelería', 'Jr. Ucayali Nro. 738 Int. 102g', '955978789', 'A'),
('20789101234', 'YanbalPapeleríaSAC','facebook.com/Yanbal', 'Papelería', 'Av. Los Pinos 1014', '955978799', 'A'),
('21012345678', 'AtlasBeautySAC','facebook.com/AtlasB', 'Maquillaje', 'Calle Los Olivos 2022', '995978799', 'A'),
('22890123456', 'RuletaCosméticaSAC','facebook.com/RuletaCosmetica', 'Maquillaje', 'Calle Los Álamos 1414', '985978799', 'A');
select * from Proveedor;
-- Tipo_est_cotizacion
insert into Tipo_est_cotizacion values ('A', 'Aceptado'),('N', 'No Aceptado'), ('P', 'Pendiente');
select * from Tipo_est_cotizacion;

-- Cotizacion
insert into Cotizacion values (10, '276.40','20603302151', 'A'),
(11, '300.40','20607504149', 'N'),
(12, '227.10','21012345678', 'A'),
(13, '341.40','22890123456', 'N'),
(14, '249.40','20789101234', 'A'),
(15, '246.40','20603302151', 'A'),
(16, '271.50','20607504149', 'N'),
(17, '216.70','20789101234', 'A'),
(18, '246.40','21012345678', 'A'),
(19, '226.40','22890123456', 'A');
select * from Cotizacion;

-- Area
insert into Area values ('CM','Compras','Area que realiza compra a proveedores'),
('VT','Ventas','Area que gestiona las ventas'),
('DT','Distribucion','Area que gestiona el envio de pedidos'),
('FZ','Finanzas','Area que gestiona las finanzas'),
('MK','Marketing','Area que gestiona las campañas de marketing'),
('AM','Almacen','Area que recepciona las compras de la empresa'),
('CRM','CRM','Area que gestiona la fidelizacion de los clientes');
select * from Area;
--Rol
insert into Rol values ('GCM', 'Gestor de compras'),
('GVT', 'Gestor de ventas'),
('GMK', 'Gestor de marketing'),
('GFZ', 'Gestor de finanzas'),
('GDT', 'Gestor de distribucion'),
('GAM', 'Gestor de almacen'),
('GCR', 'Gestor de CRM'),
('CLI', 'Cliente'),
('EMP', 'Empleado');
select * from Rol;
--zona
INSERT INTO zona VALUES (1, 'Norte', 8);
INSERT INTO zona VALUES (2, 'Este', 8);
INSERT INTO zona VALUES (3, 'Sur', 5);
INSERT INTO zona VALUES (4, 'Central', 10);
INSERT INTO zona VALUES (5, 'Central Sur', 7);
INSERT INTO zona VALUES (6, 'Balnearios del sur', 5);
select * from zona;
--distrito
INSERT INTO distrito VALUES (1, 'Ancon', '150102', '02', 1);
INSERT INTO distrito VALUES (2, 'Ate', '150103', '03', 2);
INSERT INTO distrito VALUES (3, 'Barranco', '150104', '04', 5);
INSERT INTO distrito VALUES (4, 'Independencia', '150102', '02', 1);
INSERT INTO distrito VALUES (5, 'Comas', '150110', '03', 1);
INSERT INTO distrito VALUES (6, 'San Martin de Porres', '150112', '04', 1);
INSERT INTO distrito VALUES (7, 'San Juan de Lurigancho', '150132', '04', 2);
INSERT INTO distrito VALUES (8, 'Miraflores', '150122', '18', 5);
INSERT INTO distrito VALUES (9, 'La Victoria', '150115', '13', 4);
INSERT INTO distrito VALUES (10,'San Isidro', '150131', '27', 5);
INSERT INTO distrito VALUES (11,'San Borja', '150130', '41', 5);
INSERT INTO distrito VALUES (12,'Surco', '150140', '33', 5);
INSERT INTO distrito VALUES (13,'San Miguel', '150136', '32', 4);
INSERT INTO distrito VALUES (14,'Magdalena del Mar', '150120', '17', 4);
INSERT INTO distrito VALUES (15,'La Molina', '150114', '12', 2);
INSERT INTO distrito VALUES (16,'Lince', '150116', '14', 4);
INSERT INTO distrito VALUES (17,'Pueblo Libre', '150121', '21', 4);
select * from distrito;
--Repartidor
INSERT INTO Repartidor VALUES (4851677, 'Juan.Martinez', 'Juan123','Martinez','Juan',1);
INSERT INTO Repartidor VALUES (7851678, 'David.Suarez', 'David123','Suarez','David',2);
INSERT INTO Repartidor VALUES (4859677, 'Roman.Reings','Roman123','Reigns','Roman',3);
INSERT INTO Repartidor VALUES (7523677, 'Seth.Rollins','Seth123','Rollins','Seth',4);
INSERT INTO Repartidor VALUES (9561677, 'Dean.Ambrose','Dean123','Ambrose','Dean',5);
INSERT INTO Repartidor VALUES (1564677, 'Cody.Rodhes', 'Cody123','Rodhes','Cody',6);
select * from Repartidor;
--RUTA
INSERT INTO Ruta VALUES (1, 'San Juan de Lurigancho','La Victoria','00:30:00','Tren electrico');
INSERT INTO Ruta VALUES (2, 'San Juan de Lurigancho','Miraflores','01:30:00','Metropolitano');
INSERT INTO Ruta VALUES (3, 'San Juan de Lurigancho','San Isidro','01:15:00','Metropolitano');
INSERT INTO Ruta VALUES (4, 'San Juan de Lurigancho','San Borja','00:45:00','Tren electrico');
INSERT INTO Ruta VALUES (5, 'San Juan de Lurigancho','Surco','01:00:00','Tren electrico');
INSERT INTO Ruta VALUES (6, 'San Juan de Lurigancho','San Miguel','01:15:00','Metropolitano');
INSERT INTO Ruta VALUES (7, 'San Juan de Lurigancho','Magdalena del Mar','01:15:00','Metropolitano');
INSERT INTO Ruta VALUES (8, 'San Juan de Lurigancho','La Molina','01:10:00','Tren electrico');
INSERT INTO Ruta VALUES (9, 'San Juan de Lurigancho','Barranco','02:00:00','Metropolitano');
INSERT INTO Ruta VALUES (10,'San Juan de Lurigancho','Lince','01:05:00','Metropolitano');
INSERT INTO Ruta VALUES (11,'San Juan de Lurigancho','Pueblo Libre','01:15:00','Metropolitano');
INSERT INTO Ruta VALUES (12,'San Juan de Lurigancho','San Juan de Lurigancho','00:25:00','Motocicleta');
select * from Ruta;

--Tipo_Genero
INSERT INTO Tipo_Genero VALUES ('M', 'Masculino'),('F', 'Femenino');
select * from Tipo_Genero;

--Equipo_Marketing
INSERT INTO Equipo_Marketing (Id_equipo_mark, nombre_equipo)
VALUES
    (10, 'Equipo A'),
    (11, 'Equipo B'),
    (12, 'Equipo C'),
    (13, 'Equipo D'),
    (14, 'Equipo E'),
    (15, 'Equipo F'),
    (16, 'Equipo G'),
    (17, 'Equipo H'),
    (18, 'Equipo I'),
    (19, 'Equipo J');
select * from Equipo_Marketing;

--Persona
INSERT INTO Persona VALUES 
('10000001','María','Gonzales', 'Ramírez', 'maria.gonzales@gmail.com','984562135','Av. Los Laureles 123','mariagr', 'mmmaaria',8,'CLI',NULL,NULL,'F');
INSERT INTO Persona VALUES 
('10000002','Juan','Pérez', 'Flores', 'juan.perez@gmail.com', '984562235','Jr. Los Cedros 456','juanpr', 'mjuanria',10,'CLI',NULL,NULL,'M'),
('10000003','Rosa','Mendoza', 'Díaz', 'rosa.mendoza@gmail.com', '984562335','Calle Las Flores 789','rosagr', 'mrosaia',11,'CLI',NULL,NULL,'F'),
('10000004','Carlos','Torres', 'Chávez', 'carlos.torres@gmail.com', '984562435','Av. Los Pinos 1011','carlosgr', 'mcarlosa',12,'CLI',NULL,NULL,'M'),
('10000005','Patricia','Huamaní', 'Álvarez', 'patricia.huamani@gmail.com', '984862135','Jr. Las Rosas 1213','patriciagr', 'mpatriciaa',13,'CLI',NULL,NULL,'F'),
('10000006','Luis','Sánchez', 'Cruz', 'luis.sanchez@gmail.com', '987456235','Calle Los Álamos 1415','luisgr', 'mluisr',14,'CLI',NULL,NULL,'M'),
('10000007','Ana','Castillo', 'Villanueva', 'ana.castillo@gmail.com', '994562135','Av. Los Cerezos 1617','anagr', 'anarg',15,'CLI',NULL,NULL,'F'),
('10000008','Patricia','Alvarez', 'Valencia', 'patricia.alvarez@gmail.com', '987562135','Jr. Las Palmeras 1819','patriciagr', 'patriciarmg',3,'CLI',NULL,NULL,'F'),
('10000009','Eduardo','Cruz', 'Salas', 'eduardo.cruz@gmail.com', '984962135','Calle Los Olivos 2021','eduardogr', 'eeduer',16,'CLI',NULL,NULL,'M'),
('10000010','Sandra','Valencia', 'León', 'sandra.valencia@gmail.com', '983562135','Av. Las Acacias 2223','sandragr', 'sandragr',17,'CLI',NULL,NULL,'F');
INSERT INTO Persona VALUES 
('1001','María','Gonzales', 'Ramírez', 'pilar.gonzales@gmail.com', '989962135','Av. Los Laureles 102','pilargr', 'pilargr',5,'GCM',NULL,'CM','F'),
('1002','Juan','Quispe', 'Villaverde', 'juan.quispe@gmail.com', '997962135','Jr. Los Cedros 425','juanq', 'juanq',1,'GVT',NULL,'VT','M'),
('1003','Camila','Hidalgo', 'Laureano', 'camila.hidalgo@gmail.com', '949962135','Calle Las Flores 748','camilah', 'camilah',2,'GDT',NULL,'DT','F'),
('1004','Steven','Gutierrez', 'Calderon', 'steven.gutierrez@gmail.com', '939962135','Av. Los Pinos 1021','steveng', 'steveng',3,'GFZ',NULL,'FZ','M'),
('1005','Ariana','Del Rio', 'Rojas', 'ariana.delrio@gmail.com', '929962135','Jr. Las Rosas 1022','ariand', 'ariand',4,'GMK',10,'MK','F'),
('1006','Manuel','Ramirez', 'Herberth', 'manuel.ramirez@gmail.com', '919962135','Calle Los Álamos 1082','manuelr', 'manuelr',5,'GAM',NULL,'AM','M'),
('1007','Sandra','Calderon', 'Sosaya', 'sandra.calderon@gmail.com', '990962135','Av. Las Acacias 2102','sandrac', 'sandrac',6,'GCR',NULL,'CRM','F');
select * from Persona;

--Cupón
INSERT INTO Cupón (Id_cupón, fecha_ini_cup, fecha_fin_cup, desc_cup, esta_activo)
VALUES
    (1000, '2022-01-01', '2022-02-01', 0.10, FALSE),
    (1001, '2022-02-01', '2022-03-01', 0.20, FALSE),
    (1002, '2022-03-01', '2022-04-01', 0.50, FALSE),
    (1003, '2022-04-01', '2022-05-01', 0.40, FALSE),
    (1004, '2022-05-01', '2022-06-01', 0.40, FALSE),
    (1005, '2022-06-01', '2022-07-01', 0.30, FALSE),
    (1006, '2022-07-01', '2022-08-01', 0.25, FALSE),
    (1007, '2022-08-01', '2022-09-01', 0.20, FALSE),
    (1008, '2022-09-01', '2022-10-01', 0.15, FALSE),
    (1009, '2022-10-01', '2022-11-01', 0.20, FALSE),
	(1010, '2022-11-01', '2022-12-01', 0.30, FALSE),
    (1011, '2022-11-01', '2022-12-01', 0.45, FALSE),
    (1012, '2022-11-01', '2022-12-01', 0.35, FALSE),
    (1013, '2022-12-01', '2023-01-01', 0.25, FALSE),
    (1014, '2022-12-01', '2023-01-01', 0.15, FALSE),
    (1015, '2022-12-01', '2023-01-01', 0.10, FALSE),
    (1016, '2023-01-01', '2023-02-01', 0.50, FALSE),
    (1017, '2023-01-01', '2023-02-01', 0.40, FALSE),
    (1018, '2023-01-01', '2023-02-01', 0.60, FALSE),
    (1019, '2023-02-01', '2023-03-01', 0.20, FALSE),
    (1020, '2023-02-01', '2023-03-01', 0.55, FALSE),
    (1021, '2023-02-01', '2023-03-01', 0.25, FALSE),
    (1022, '2023-02-01', '2023-03-01', 0.35, FALSE),
    (1023, '2023-03-01', '2023-04-01', 0.45, FALSE),
    (1024, '2023-03-01', '2023-04-01', 0.50, FALSE),
    (1025, '2023-03-01', '2023-04-01', 0.30, FALSE),
    (1026, '2023-04-01', '2023-05-01', 0.20, FALSE),
    (1027, '2023-04-01', '2023-05-01', 0.15, FALSE),
    (1028, '2023-04-01', '2023-05-01', 0.40, FALSE),
    (1029, '2023-05-01', '2023-06-01', 0.60, FALSE),
    (1030, '2023-05-01', '2023-06-01', 0.55, FALSE),
    (1031, '2023-05-01', '2023-06-01', 0.25, FALSE),
    (1032, '2023-05-01', '2023-06-01', 0.35, FALSE),
    (1033, '2023-06-01', '2023-07-01', 0.45, FALSE),
    (1034, '2023-06-01', '2023-07-01', 0.50, FALSE),
    (1035, '2023-06-01', '2023-07-01', 0.30, FALSE),
    (1036, '2023-07-01', '2023-08-01', 0.20, FALSE),
    (1037, '2023-07-01', '2023-08-01', 0.15, FALSE),
    (1038, '2023-07-01', '2023-08-01', 0.40, FALSE),
    (1039, '2023-08-01', '2023-09-01', 0.60, FALSE),
    (1040, '2023-08-01', '2023-09-01', 0.55, FALSE),
    (1041, '2023-08-01', '2023-09-01', 0.25, FALSE),
    (1042, '2023-08-01', '2023-09-01', 0.35, FALSE),
    (1043, '2023-09-01', '2023-10-01', 0.45, FALSE),
    (1044, '2023-09-01', '2023-10-01', 0.50, FALSE),
    (1045, '2023-09-01', '2023-10-01', 0.30, FALSE),
    (1046, '2023-10-01', '2023-11-01', 0.20, FALSE),
    (1047, '2023-10-01', '2023-11-01', 0.15, FALSE),
    (1048, '2023-10-01', '2023-11-01', 0.40, FALSE),
    (1049, '2023-11-01', '2023-12-01', 0.60, FALSE),
    (1050, '2023-11-01', '2023-12-01', 0.55, FALSE),
    (1051, '2023-11-01', '2023-12-01', 0.25, FALSE),
    (1052, '2023-11-01', '2023-12-01', 0.35, FALSE),
    (1053, '2023-12-01', '2024-01-01', 0.45, FALSE),
    (1054, '2023-12-01', '2024-01-01', 0.50, FALSE),
    (1055, '2023-12-01', '2024-01-01', 0.30, FALSE),
    (1056, '2024-01-01', '2024-02-01', 0.20, FALSE),
    (1057, '2024-01-01', '2024-02-01', 0.15, FALSE),
    (1058, '2024-01-01', '2024-02-01', 0.40, FALSE),
    (1059, '2024-02-01', '2024-03-01', 0.60, FALSE),
    (1060, '2024-02-01', '2024-03-01', 0.55, FALSE),
    (1061, '2024-02-01', '2024-03-01', 0.25, FALSE),
    (1062, '2024-02-01', '2024-03-01', 0.35, FALSE),
    (1063, '2024-03-01', '2024-04-01', 0.45, FALSE),
    (1064, '2024-03-01', '2024-04-01', 0.50, FALSE),
    (1065, '2024-03-01', '2024-04-01', 0.30, FALSE),
    (1066, '2024-04-01', '2024-05-01', 0.20, FALSE),
    (1067, '2024-04-01', '2024-05-01', 0.15, FALSE),
    (1068, '2024-04-01', '2024-05-01', 0.40, FALSE),
    (1069, '2024-05-01', '2024-06-01', 0.60, FALSE),
    (1070, '2024-05-01', '2024-06-01', 0.55, FALSE),
    (1071, '2024-05-01', '2024-06-01', 0.25, FALSE),
    (1072, '2024-05-01', '2024-06-01', 0.35, FALSE),
    (1073, '2024-06-01', '2024-07-01', 0.45, TRUE),
    (1074, '2024-06-01', '2024-07-01', 0.50, FALSE),
    (1075, '2024-06-01', '2024-07-01', 0.30, TRUE),
    (1076, '2024-07-01', '2024-08-01', 0.20, FALSE),
    (1077, '2024-07-01', '2024-08-01', 0.15, FALSE),
    (1078, '2024-07-01', '2024-08-01', 0.40, FALSE),
    (1079, '2024-08-01', '2024-09-01', 0.60, FALSE),
    (1080, '2024-08-01', '2024-09-01', 0.55, FALSE),
    (1081, '2024-08-01', '2024-09-01', 0.25, FALSE),
    (1082, '2024-08-01', '2024-09-01', 0.35, FALSE),
    (1083, '2024-09-01', '2024-10-01', 0.45, FALSE),
    (1084, '2024-09-01', '2024-10-01', 0.50, FALSE),
    (1085, '2024-09-01', '2024-10-01', 0.30, FALSE),
    (1086, '2024-10-01', '2024-11-01', 0.20, FALSE),
    (1087, '2024-10-01', '2024-11-01', 0.15, FALSE),
    (1088, '2024-10-01', '2024-11-01', 0.40, FALSE),
    (1089, '2024-11-01', '2024-12-01', 0.60, FALSE),
    (1090, '2024-11-01', '2024-12-01', 0.55, FALSE),
    (1091, '2024-11-01', '2024-12-01', 0.25, FALSE),
    (1092, '2024-11-01', '2024-12-01', 0.35, FALSE),
    (1093, '2024-12-01', '2025-01-01', 0.45, FALSE),
    (1094, '2024-12-01', '2025-01-01', 0.50, FALSE),
    (1095, '2024-12-01', '2025-01-01', 0.30, FALSE),
    (1096, '2025-01-01', '2025-02-01', 0.20, FALSE),
    (1097, '2025-01-01', '2025-02-01', 0.15, FALSE),
    (1098, '2025-01-01', '2025-02-01', 0.40, FALSE),
    (1099, '2025-02-01', '2025-03-01', 0.60, FALSE);
select * from Cupón;

-- Campaña
INSERT INTO Campaña (Id_campaña, nom_campaña, fecha_ini, fecha_fin, dir_url, modalidad, archivo, desc_campaña, Id_equipo_mark, Id_gest_mark)
VALUES
    (100000, 'campaña enero 1', '2022-01-04', '2022-01-11', 'https://linktr.ee/Migni_Store', 'native ad', 'https://marketingmigni.com/campaña100000.mp4', 0.10, 10, 1005),
    (100001, 'campaña enero 2', '2022-01-11', '2022-01-18', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100001.jpg', 0.25, 12, 1005),
    (100002, 'campaña enero 3', '2022-01-18', '2022-02-18', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100002.jpg', 0.10, 11, 1005),
    (100003, 'campaña escolar 1', '2022-02-18', '2022-02-25', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100003.jpg', 0.15, 16, 1005),
    (100004, 'campaña escolar 2', '2022-02-25', '2022-03-25', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100004.mp4', 0.25, 17, 1005),
    (100005, 'campaña escolar 3', '2022-03-25', '2022-04-01', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100005.jpg', 0.30, 17, 1005),
    (100006, 'campaña abril 1', '2022-04-01', '2022-04-08', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100006.jpg', 0.30, 19, 1005),
    (100007, 'campaña abril 2', '2022-04-08', '2022-05-08', 'https://linktr.ee/Migni_Store', 'native ad', 'https://marketingmigni.com/campaña100007.jpg', 0.10, 18, 1005),
    (100008, 'campaña dia de la madre 2022', '2022-05-08', '2022-06-08', 'https://linktr.ee/Migni_Store', 'native ad', 'https://marketingmigni.com/campaña100008.jpg', 0.25, 14, 1005),
    (100009, 'campaña dia del padre 2022', '2022-06-08', '2022-06-15', 'https://linktr.ee/Migni_Store', 'video ad', 'https://marketingmigni.com/campaña100009.mp4', 0.35, 11, 1005),
	(100010, 'campaña junio 2022', '2022-06-15', '2022-06-22', 'https://linktr.ee/Migni_Store', 'video ad', 'https://marketingmigni.com/campaña100010.mp4', 0.20, 14, 1005),
    (100011, 'campaña san juan 2022', '2022-06-22', '2022-06-29', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100011.jpg', 0.30, 12, 1005),
    (100012, 'campaña escolar 2022', '2022-06-29', '2022-07-29', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100012.mp4', 0.40, 15, 1005),
    (100013, 'campaña independencia peruana 2022', '2022-07-29', '2022-08-05', 'https://linktr.ee/Migni_Store', 'native ad', 'https://marketingmigni.com/campaña100013.mp4', 0.25, 11, 1005),
    (100014, 'campaña agosto 2022', '2022-08-05', '2022-08-12', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100014.jpg', 0.35, 18, 1005),
    (100015, 'campaña día de la madre 2022', '2022-08-12', '2022-09-12', 'https://linktr.ee/Migni_Store', 'video ad', 'https://marketingmigni.com/campaña100015.jpg', 0.15, 17, 1005),
    (100016, 'campaña regreso a clases 2022', '2022-09-12', '2022-09-19', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100016.jpg', 0.50, 13, 1005),
    (100017, 'campaña septiembre 2022', '2022-09-19', '2022-09-26', 'https://linktr.ee/Migni_Store', 'native ad', 'https://marketingmigni.com/campaña100017.mp4', 0.30, 15, 1005),
    (100018, 'campaña halloween 2022', '2022-09-26', '2022-10-31', 'https://linktr.ee/Migni_Store', 'video ad', 'https://marketingmigni.com/campaña100018.jpg', 0.45, 12, 1005),
    (100019, 'campaña inicio noviembre 2022', '2022-10-31', '2022-11-07', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100019.jpg', 0.40, 19, 1005),
    (100020, 'campaña noviembre 2022', '2022-11-07', '2022-11-14', 'https://linktr.ee/Migni_Store', 'native ad', 'https://marketingmigni.com/campaña100020.mp4', 0.35, 16, 1005),
    (100021, 'campaña black friday 2022', '2022-11-14', '2022-11-21', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100021.jpg', 0.20, 18, 1005),
    (100022, 'campaña fin de año 2022', '2022-11-21', '2022-12-19', 'https://linktr.ee/Migni_Store', 'video ad', 'https://marketingmigni.com/campaña100022.mp4', 0.45, 15, 1005),
    (100023, 'campaña navidad 2022', '2022-12-19', '2022-12-26', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100023.jpg', 0.30, 17, 1005),
    (100024, 'campaña año nuevo 2022', '2022-12-26', '2023-01-02', 'https://linktr.ee/Migni_Store', 'native ad', 'https://marketingmigni.com/campaña100024.mp4', 0.25, 13, 1005),
    (100025, 'campaña inicio año 2023', '2023-01-02', '2023-01-09', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100025.jpg', 0.40, 14, 1005),
    (100026, 'campaña enero 2023', '2023-01-09', '2023-01-16', 'https://linktr.ee/Migni_Store', 'video ad', 'https://marketingmigni.com/campaña100026.mp4', 0.35, 15, 1005),
    (100027, 'campaña inicio febrero 2023', '2023-01-16', '2023-02-06', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100027.jpg', 0.20, 12, 1005),
    (100028, 'campaña amor y amistad 2023', '2023-02-06', '2023-02-14', 'https://linktr.ee/Migni_Store', 'native ad', 'https://marketingmigni.com/campaña100028.jpg', 0.30, 18, 1005),
    (100029, 'campaña febrero 2023', '2023-02-14', '2023-02-21', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100029.mp4', 0.45, 16, 1005),
    (100030, 'campaña marzo 2023', '2023-02-21', '2023-02-28', 'https://linktr.ee/Migni_Store', 'video ad', 'https://marketingmigni.com/campaña100030.mp4', 0.25, 13, 1005),
    (100031, 'campaña inicio marzo 2023', '2023-02-28', '2023-03-07', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100031.jpg', 0.40, 19, 1005),
    (100032, 'campaña día de la mujer 2023', '2023-03-07', '2023-03-14', 'https://linktr.ee/Migni_Store', 'native ad', 'https://marketingmigni.com/campaña100032.mp4', 0.35, 15, 1005),
    (100033, 'campaña marzo 2 2023', '2023-03-14', '2023-03-21', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100033.jpg', 0.20, 14, 1005),
    (100034, 'campaña fin de marzo 2023', '2023-03-21', '2023-03-28', 'https://linktr.ee/Migni_Store', 'video ad', 'https://marketingmigni.com/campaña100034.mp4', 0.30, 16, 1005),
    (100035, 'campaña abril 2023', '2023-03-28', '2023-04-04', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100035.jpg', 0.45, 18, 1005),
    (100036, 'campaña semana santa 2023', '2023-04-04', '2023-04-11', 'https://linktr.ee/Migni_Store', 'native ad', 'https://marketingmigni.com/campaña100036.jpg', 0.40, 17, 1005),
    (100037, 'campaña abril 2 2023', '2023-04-11', '2023-04-18', 'https://linktr.ee/Migni_Store', 'video ad', 'https://marketingmigni.com/campaña100037.mp4', 0.25, 12, 1005),
    (100038, 'campaña abril 3 2023', '2023-04-18', '2023-04-25', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100038.jpg', 0.30, 13, 1005),
    (100039, 'campaña abril 4 2023', '2023-04-25', '2023-05-02', 'https://linktr.ee/Migni_Store', 'native ad', 'https://marketingmigni.com/campaña100039.mp4', 0.20, 16, 1005),
    (100040, 'campaña inicio mayo 2023', '2023-05-02', '2023-05-09', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100040.jpg', 0.35, 18, 1005),
    (100041, 'campaña día de la madre 2023', '2023-05-09', '2023-05-16', 'https://linktr.ee/Migni_Store', 'video ad', 'https://marketingmigni.com/campaña100041.mp4', 0.25, 14, 1005),
    (100042, 'campaña mayo 2023', '2023-05-16', '2023-05-23', 'https://linktr.ee/Migni_Store', 'native ad', 'https://marketingmigni.com/campaña100042.jpg', 0.40, 17, 1005),
    (100043, 'campaña fin de mayo 2023', '2023-05-23', '2023-05-30', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100043.jpg', 0.30, 15, 1005),
    (100044, 'campaña junio 2023', '2023-05-30', '2023-06-06', 'https://linktr.ee/Migni_Store', 'video ad', 'https://marketingmigni.com/campaña100044.mp4', 0.45, 12, 1005),
    (100045, 'campaña día del padre 2023', '2023-06-06', '2023-06-13', 'https://linktr.ee/Migni_Store', 'native ad', 'https://marketingmigni.com/campaña100045.jpg', 0.20, 19, 1005),
    (100046, 'campaña inicio verano 2023', '2023-06-13', '2023-06-20', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100046.jpg', 0.30, 16, 1005),
    (100047, 'campaña junio 2 2023', '2023-06-20', '2023-06-27', 'https://linktr.ee/Migni_Store', 'video ad', 'https://marketingmigni.com/campaña100047.mp4', 0.25, 13, 1005),
    (100048, 'campaña fin de junio 2023', '2023-06-27', '2023-07-04', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100048.jpg', 0.35, 14, 1005),
    (100049, 'campaña julio 2023', '2023-07-04', '2023-07-11', 'https://linktr.ee/Migni_Store', 'native ad', 'https://marketingmigni.com/campaña100049.mp4', 0.40, 17, 1005),
    (100050, 'campaña mitad de año 2023', '2023-07-11', '2023-07-18', 'https://linktr.ee/Migni_Store', 'video ad', 'https://marketingmigni.com/campaña100050.mp4', 0.25, 15, 1005),
    (100051, 'campaña julio 2 2023', '2023-07-18', '2023-07-25', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100051.jpg', 0.30, 16, 1005),
    (100052, 'campaña fin de julio 2023', '2023-07-25', '2023-08-01', 'https://linktr.ee/Migni_Store', 'native ad', 'https://marketingmigni.com/campaña100052.jpg', 0.45, 18, 1005),
    (100053, 'campaña agosto 2023', '2023-08-01', '2023-08-08', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100053.mp4', 0.40, 17, 1005),
    (100054, 'campaña vuelta a clases 2023', '2023-08-08', '2023-08-15', 'https://linktr.ee/Migni_Store', 'video ad', 'https://marketingmigni.com/campaña100054.jpg', 0.35, 14, 1005),
    (100055, 'campaña agosto 2 2023', '2023-08-15', '2023-08-22', 'https://linktr.ee/Migni_Store', 'native ad', 'https://marketingmigni.com/campaña100055.mp4', 0.20, 13, 1005),
    (100056, 'campaña fin de agosto 2023', '2023-08-22', '2023-08-29', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100056.jpg', 0.30, 12, 1005),
    (100057, 'campaña septiembre 2023', '2023-08-29', '2023-09-05', 'https://linktr.ee/Migni_Store', 'video ad', 'https://marketingmigni.com/campaña100057.mp4', 0.25, 19, 1005),
    (100058, 'campaña inicio septiembre 2023', '2023-09-05', '2023-09-12', 'https://linktr.ee/Migni_Store', 'native ad', 'https://marketingmigni.com/campaña100058.jpg', 0.35, 16, 1005),
    (100059, 'campaña día del niño 2023', '2023-09-12', '2023-09-19', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100059.mp4', 0.40, 18, 1005),
    (100060, 'campaña septiembre 2 2023', '2023-09-19', '2023-09-26', 'https://linktr.ee/Migni_Store', 'video ad', 'https://marketingmigni.com/campaña100060.mp4', 0.45, 15, 1005),
    (100061, 'campaña fin de septiembre 2023', '2023-09-26', '2023-10-03', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100061.jpg', 0.25, 14, 1005),
    (100062, 'campaña octubre 2023', '2023-10-03', '2023-10-10', 'https://linktr.ee/Migni_Store', 'native ad', 'https://marketingmigni.com/campaña100062.mp4', 0.30, 17, 1005),
    (100063, 'campaña día de la raza 2023', '2023-10-10', '2023-10-17', 'https://linktr.ee/Migni_Store', 'video ad', 'https://marketingmigni.com/campaña100063.jpg', 0.35, 16, 1005),
    (100064, 'campaña octubre 2 2023', '2023-10-17', '2023-10-24', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100064.mp4', 0.20, 13, 1005),
    (100065, 'campaña fin de octubre 2023', '2023-10-24', '2023-10-31', 'https://linktr.ee/Migni_Store', 'native ad', 'https://marketingmigni.com/campaña100065.jpg', 0.40, 18, 1005),
    (100066, 'campaña noviembre 2023', '2023-10-31', '2023-11-07', 'https://linktr.ee/Migni_Store', 'video ad', 'https://marketingmigni.com/campaña100066.mp4', 0.25, 15, 1005),
    (100067, 'campaña inicio noviembre 2023', '2023-11-07', '2023-11-14', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100067.jpg', 0.30, 16, 1005),
    (100068, 'campaña black friday 2023', '2023-11-14', '2023-11-21', 'https://linktr.ee/Migni_Store', 'native ad', 'https://marketingmigni.com/campaña100068.mp4', 0.45, 17, 1005),
    (100069, 'campaña fin de noviembre 2023', '2023-11-21', '2023-11-28', 'https://linktr.ee/Migni_Store', 'video ad', 'https://marketingmigni.com/campaña100069.jpg', 0.35, 18, 1005),
    (100070, 'campaña inicio diciembre 2023', '2023-11-28', '2023-12-05', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100070.jpg', 0.30, 16, 1005),
    (100071, 'campaña navidad 2023', '2023-12-05', '2023-12-12', 'https://linktr.ee/Migni_Store', 'native ad', 'https://marketingmigni.com/campaña100071.mp4', 0.25, 14, 1005),
    (100072, 'campaña diciembre 2 2023', '2023-12-12', '2023-12-19', 'https://linktr.ee/Migni_Store', 'video ad', 'https://marketingmigni.com/campaña100072.jpg', 0.35, 17, 1005),
    (100073, 'campaña fin de diciembre 2023', '2023-12-19', '2023-12-26', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100073.jpg', 0.40, 18, 1005),
    (100074, 'campaña inicio año nuevo 2024', '2023-12-26', '2024-01-02', 'https://linktr.ee/Migni_Store', 'native ad', 'https://marketingmigni.com/campaña100074.jpg', 0.45, 15, 1005),
    (100075, 'campaña enero 2024', '2024-01-02', '2024-01-09', 'https://linktr.ee/Migni_Store', 'video ad', 'https://marketingmigni.com/campaña100075.mp4', 0.30, 16, 1005),
    (100076, 'campaña inicio enero 2024', '2024-01-09', '2024-01-16', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100076.jpg', 0.25, 14, 1005),
    (100077, 'campaña año nuevo chino 2024', '2024-01-16', '2024-01-23', 'https://linktr.ee/Migni_Store', 'native ad', 'https://marketingmigni.com/campaña100077.mp4', 0.20, 13, 1005),
    (100078, 'campaña fin de enero 2024', '2024-01-23', '2024-01-30', 'https://linktr.ee/Migni_Store', 'video ad', 'https://marketingmigni.com/campaña100078.jpg', 0.35, 15, 1005),
    (100079, 'campaña inicio febrero 2024', '2024-01-30', '2024-02-06', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100079.jpg', 0.40, 17, 1005),
    (100080, 'campaña día de la amistad 2024', '2024-02-06', '2024-02-13', 'https://linktr.ee/Migni_Store', 'native ad', 'https://marketingmigni.com/campaña100080.mp4', 0.45, 18, 1005),
    (100081, 'campaña febrero 2024', '2024-02-13', '2024-02-20', 'https://linktr.ee/Migni_Store', 'video ad', 'https://marketingmigni.com/campaña100081.jpg', 0.30, 16, 1005),
    (100082, 'campaña fin de febrero 2024', '2024-02-20', '2024-02-27', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100082.jpg', 0.25, 14, 1005),
    (100083, 'campaña marzo 2024', '2024-02-27', '2024-03-05', 'https://linktr.ee/Migni_Store', 'native ad', 'https://marketingmigni.com/campaña100083.mp4', 0.20, 13, 1005),
    (100084, 'campaña inicio marzo 2024', '2024-03-05', '2024-03-12', 'https://linktr.ee/Migni_Store', 'video ad', 'https://marketingmigni.com/campaña100084.jpg', 0.35, 15, 1005),
    (100085, 'campaña día de la mujer 2024', '2024-03-12', '2024-03-19', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100085.mp4', 0.40, 17, 1005),
    (100086, 'campaña marzo 2 2024', '2024-03-19', '2024-03-26', 'https://linktr.ee/Migni_Store', 'native ad', 'https://marketingmigni.com/campaña100086.jpg', 0.45, 18, 1005),
    (100087, 'campaña fin de marzo 2024', '2024-03-26', '2024-04-02', 'https://linktr.ee/Migni_Store', 'video ad', 'https://marketingmigni.com/campaña100087.mp4', 0.30, 16, 1005),
    (100088, 'campaña abril 2024', '2024-04-02', '2024-04-09', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100088.jpg', 0.25, 14, 1005),
    (100089, 'campaña inicio abril 2024', '2024-04-09', '2024-04-16', 'https://linktr.ee/Migni_Store', 'native ad', 'https://marketingmigni.com/campaña100089.mp4', 0.20, 13, 1005),
    (100090, 'campaña semana santa 2024', '2024-04-16', '2024-04-23', 'https://linktr.ee/Migni_Store', 'video ad', 'https://marketingmigni.com/campaña100090.jpg', 0.35, 15, 1005),
    (100091, 'campaña abril 2 2024', '2024-04-23', '2024-04-30', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100091.mp4', 0.40, 16, 1005),
    (100092, 'campaña fin de abril 2024', '2024-04-30', '2024-05-07', 'https://linktr.ee/Migni_Store', 'native ad', 'https://marketingmigni.com/campaña100092.jpg', 0.45, 17, 1005),
    (100093, 'campaña mayo 2024', '2024-05-07', '2024-05-14', 'https://linktr.ee/Migni_Store', 'video ad', 'https://marketingmigni.com/campaña100093.mp4', 0.30, 18, 1005),
    (100094, 'campaña inicio mayo 2024', '2024-05-14', '2024-05-21', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100094.jpg', 0.25, 14, 1005),
    (100095, 'campaña día de la madre 2024', '2024-05-21', '2024-06-28', 'https://linktr.ee/Migni_Store', 'native ad', 'https://marketingmigni.com/campaña100095.mp4', 0.20, 13, 1005),
    (100096, 'campaña mayo 2 2024', '2024-06-28', '2024-07-04', 'https://linktr.ee/Migni_Store', 'video ad', 'https://marketingmigni.com/campaña100096.jpg', 0.35, 10, 1005),
    (100097, 'campaña fin de mayo 2024', '2024-07-04', '2024-08-11', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100097.mp4', 0.40, 10, 1005),
    (100098, 'campaña junio 2024', '2024-08-11', '2024-09-18', 'https://linktr.ee/Migni_Store', 'native ad', 'https://marketingmigni.com/campaña100098.jpg', 0.45, 10, 1005),
    (100099, 'campaña inicio junio 2024', '2024-09-18', '2024-10-25', 'https://linktr.ee/Migni_Store', 'video ad', 'https://marketingmigni.com/campaña100099.mp4', 0.30, 10, 1005);


select * from Campaña;

--Producto
insert into Producto values (1, 'Cuaderno clear blinder', 'Cuaderno A4 tipo blinder con 60 hojas rayadas', 0, 100, 25.0, 1);
insert into Producto values (2, 'Bear Notebook B5', 'Cuaderno B5 tipo blinder con 60 hojas rayadas', 0, 100,20.0, 1);
insert into Producto values (3, 'Diamond pen', 'Incluye protector, Tinta:negra', 0, 100,6.5, 2);
insert into Producto values (4, 'Releaf Primer', 'Primer de Italia deluxe', 0, 100,28.5, 5);
insert into Producto values (5, 'Corrector HD Pro', 'Corrector de Italia deluxe, con cobertura media a graduable', 0, 100, 16.0, 10);
insert into Producto values (6, 'Super Stay Matter Maybelline', 'Labial con efecto matte instransferible por 24h', 0, 100, 45.0, 8);
insert into Producto values (7, 'Profesional Silicón PROSA', 'Mascara de pestañas que aporta demasiada longitud ', 0, 100, 30.0, 11);
insert into Producto values (8, 'Gliterally', 'Delineador con glitter extra brillante de Beauty creation', 0, 100,22.0, 6);
insert into Producto values (9, 'Ultrafine lipliner', 'Delineadores de labios de Italia deluxe', 0, 100, 6.0, 8);
insert into Producto values (10, 'Fill in thirsty gloss', 'Gloss de Italia deluxe con efecto mentolado', 0, 100, 18.0, 8);
select * from Producto;

--CampañaXProd
INSERT INTO CampañaXProd (id_producto, Id_campaña)
VALUES
    (1, 100000),
    (2, 100001),
    (5, 100002),
    (7, 100003),
    (7, 100004),
    (2, 100005),
    (8, 100006),
    (9, 100007),
    (10, 100008),
    (2, 100009),
	(10, 100010),
    (4, 100011),
    (10, 100012),
    (6, 100013),
    (5, 100014),
    (8, 100015),
    (1, 100016),
    (7, 100017),
    (3, 100018),
    (4, 100019),
    (9, 100020),
    (1, 100021),
    (2, 100022),
    (3, 100023),
    (4, 100024),
    (6, 100025),
    (7, 100026),
    (8, 100027),
    (9, 100028),
    (10, 100029),
    (1, 100030),
    (2, 100031),
    (3, 100032),
    (4, 100033),
    (6, 100034),
    (1, 100035),
    (8, 100036),
    (5, 100037),
    (2, 100038),
    (10, 100039),
    (9, 100040),
    (1, 100041),
    (2, 100042),
    (5, 100043),
    (10, 100044),
    (5, 100045),
    (9, 100046),
    (4, 100047),
    (7, 100048),
    (3, 100049),
    (3, 100050),
    (8, 100051),
    (1, 100052),
    (2, 100053),
    (4, 100054),
    (2, 100055),
    (4, 100056),
    (6, 100057),
    (7, 100058),
    (3, 100059),
    (9, 100060),
    (3, 100061),
    (8, 100062),
    (1, 100063),
    (5, 100064),
    (6, 100065),
    (1, 100066),
    (2, 100067),
    (7, 100068),
    (9, 100069),
    (2, 100070),
    (1, 100071),
    (1, 100072),
    (4, 100073),
    (3, 100074),
    (8, 100075),
    (3, 100076),
    (6, 100077),
    (8, 100078),
    (5, 100079),
    (2, 100080),
    (3, 100081),
    (3, 100082),
    (5, 100083),
    (1, 100084),
    (4, 100085),
    (6, 100086),
    (2, 100087),
    (7, 100088),
    (10, 100089),
    (9, 100090),
    (4, 100091),
    (3, 100092),
    (1, 100093),
    (4, 100094),
    (5, 100095),
    (7, 100096),
    (5, 100097),
    (9, 100098),
    (8, 100099);
select * from CampañaXProd;

--Canal
INSERT INTO Canal (Id_canal, nombre_canal)
VALUES
    (100, 'youtube'),
    (101, 'twitter'),
    (102, 'marketplace'),
    (103, 'instagram'),
    (104, 'facebook'),
	(105, 'google ads'),
    (106, 'linkedin'),
    (107, 'pinterest'),
    (108, 'snapchat'),
    (109, 'tiktok'),
    (110, 'reddit');
select * from Canal;

--CampañaXCanal
INSERT INTO CampañaXCanal (Id_campaña, Id_canal)
VALUES
    (100000, 102),
    (100001, 101),
    (100002, 103),
    (100003, 101),
    (100004, 100),
    (100005, 100),
    (100006, 102),
    (100007, 101),
    (100008, 104),
    (100009, 103),
	(100010, 105),
    (100011, 108),
    (100012, 106),
    (100013, 110),
    (100014, 107),
    (100015, 104),
    (100016, 109),
    (100017, 100),
    (100018, 101),
    (100019, 102),
    (100020, 105),
    (100021, 108),
    (100022, 106),
    (100023, 110),
    (100024, 107),
    (100025, 104),
    (100026, 109),
    (100027, 100),
    (100028, 101),
    (100029, 102),
    (100030, 105),
    (100031, 108),
    (100032, 106),
    (100033, 110),
    (100034, 107),
    (100035, 104),
    (100036, 109),
    (100037, 100),
    (100038, 101),
    (100039, 102),
    (100040, 105),
    (100041, 108),
    (100042, 106),
    (100043, 110),
    (100044, 107),
    (100045, 104),
    (100046, 109),
    (100047, 100),
    (100048, 101),
    (100049, 102),
    (100050, 105),
    (100051, 108),
    (100052, 106),
    (100053, 110),
    (100054, 107),
    (100055, 104),
    (100056, 109),
    (100057, 100),
    (100058, 101),
    (100059, 102),
    (100060, 105),
    (100061, 108),
    (100062, 106),
    (100063, 110),
    (100064, 107),
    (100065, 104),
    (100066, 109),
    (100067, 100),
    (100068, 101),
    (100069, 102),
    (100070, 105),
    (100071, 108),
    (100072, 106),
    (100073, 110),
    (100074, 107),
    (100075, 104),
    (100076, 109),
    (100077, 100),
    (100078, 101),
    (100079, 102),
    (100080, 105),
    (100081, 108),
    (100082, 106),
    (100083, 110),
    (100084, 107),
    (100085, 104),
    (100086, 109),
    (100087, 100),
    (100088, 101),
    (100089, 102),
    (100090, 105),
    (100091, 108),
    (100092, 106),
    (100093, 110),
    (100094, 107),
    (100095, 104),
    (100096, 109),
    (100097, 100),
    (100098, 101),
    (100099, 102);
select * from CampañaXCanal;

--Observacion
INSERT INTO Observacion (Id_observacion, descripcion, Id_campaña, estado_atendido)
VALUES
    (10000, 'aumentar en una semana la duracion de la campaña y agregar un producto más', 100000, TRUE),
    (10001, 'Lanzar una nueva campaña de marketing para el producto 2', 100001, TRUE),
    (10002, 'Reducir el descuento en un 10%', 100002, TRUE),
    (10003, 'Lanzar una nueva campaña de marketing para el producto 7', 100003, TRUE),
    (10004, 'Extender la fecha de inicio de la campaña en tres días', 100004, TRUE),
    (10005, 'Ofrecer un descuento del 15%', 100005, TRUE),
    (10006, 'Actualizar las fechas de la campaña', 100006, TRUE),
    (10007, 'Cambiar a una promoción especial', 100007, TRUE),
    (10008, 'Incluir un regalo con la compra del producto durante la campaña', 100008, TRUE),
    (10009, 'Extender la campaña hasta fin de mes y aumentar el presupuesto publicitario', 100009, TRUE),
	(10010, 'Realizar un evento de lanzamiento en línea para el nuevo producto', 100010, TRUE),
    (10011, 'Implementar una estrategia de redes sociales para aumentar la visibilidad', 100011, TRUE),
    (10012, 'Ofrecer envío gratuito durante toda la campaña', 100012, TRUE),
    (10013, 'Aumentar la duración de la campaña en una semana y agregar un producto más', 100013, TRUE),
    (10014, 'Reducir el precio del producto en un 5% durante la campaña', 100014, TRUE),
    (10015, 'Lanzar una nueva campaña de marketing para el producto 4', 100015, TRUE),
    (10016, 'Extender la fecha de inicio de la campaña en cinco días', 100016, TRUE),
    (10017, 'Ofrecer un descuento del 20% para los primeros 50 compradores', 100017, TRUE),
    (10018, 'Actualizar las fechas de la campaña según el calendario de marketing', 100018, TRUE),
    (10019, 'Agregar una promoción especial para nuevos clientes', 100019, TRUE),
    (10020, 'Incluir una oferta 2x1 en productos seleccionados durante la campaña', 100020, TRUE),
    (10021, 'Extender la campaña hasta fin de mes y aumentar el presupuesto publicitario', 100021, TRUE),
    (10022, 'Realizar un evento de lanzamiento en línea para el nuevo producto', 100022, TRUE),
    (10023, 'Implementar una estrategia de redes sociales para aumentar la visibilidad', 100023, TRUE),
    (10024, 'Ofrecer envío gratuito durante toda la campaña', 100024, TRUE),
    (10025, 'Aumentar la duración de la campaña en una semana y agregar un producto más', 100025, TRUE),
    (10026, 'Reducir el precio del producto en un 15% durante la campaña', 100026, TRUE),
    (10027, 'Lanzar una nueva campaña de marketing para el producto 1', 100027, TRUE),
    (10028, 'Extender la fecha de inicio de la campaña en tres días', 100028, TRUE),
    (10029, 'Ofrecer un descuento del 10% para los primeros 100 compradores', 100029, TRUE),
    (10030, 'Actualizar las fechas de la campaña según el calendario de marketing', 100030, TRUE),
    (10031, 'Agregar una promoción especial para clientes frecuentes', 100031, TRUE),
    (10032, 'Incluir un regalo con la compra del producto durante la campaña', 100032, TRUE),
    (10033, 'Extender la campaña hasta fin de mes y aumentar el presupuesto publicitario', 100033, TRUE),
    (10034, 'Realizar un evento de lanzamiento en línea para el nuevo producto', 100034, TRUE),
    (10035, 'Implementar una estrategia de redes sociales para aumentar la visibilidad', 100035, TRUE),
    (10036, 'Ofrecer envío gratuito durante toda la campaña', 100036, TRUE),
    (10037, 'Aumentar la duración de la campaña en una semana y agregar un producto más', 100037, TRUE),
    (10038, 'Reducir el precio del producto en un 5% durante la primera semana', 100038, TRUE),
    (10039, 'Lanzar una nueva campaña de marketing para el producto 17', 100039, TRUE),
    (10040, 'Extender la fecha de inicio de la campaña en dos días', 100040, TRUE),
    (10041, 'Ofrecer un descuento del 20% para los primeros 50 compradores', 100041, TRUE),
    (10042, 'Actualizar las fechas de la campaña según el calendario de marketing', 100042, TRUE),
    (10043, 'Agregar una promoción especial para nuevos clientes', 100043, TRUE),
    (10044, 'Incluir una oferta 2x1 en productos seleccionados durante la campaña', 100044, TRUE),
    (10045, 'Extender la campaña hasta fin de mes y aumentar el presupuesto publicitario', 100045, TRUE),
    (10046, 'Realizar un evento de lanzamiento en línea para el nuevo producto', 100046, TRUE),
    (10047, 'Implementar una estrategia de redes sociales para aumentar la visibilidad', 100047, TRUE),
    (10048, 'Ofrecer envío gratuito durante toda la campaña', 100048, TRUE),
    (10049, 'Aumentar la duración de la campaña en una semana y agregar un producto más', 100049, TRUE),
    (10050, 'Reducir el precio del producto en un 15% durante la primera semana', 100050, TRUE),
    (10051, 'Lanzar una nueva campaña de marketing para el producto 3', 100051, TRUE),
    (10052, 'Extender la fecha de inicio de la campaña en cinco días', 100052, TRUE),
    (10053, 'Ofrecer un descuento del 20% para los primeros 100 compradores', 100053, TRUE),
    (10054, 'Actualizar las fechas de la campaña según el calendario de marketing', 100054, TRUE),
    (10055, 'Agregar una promoción especial para clientes frecuentes', 100055, TRUE),
    (10056, 'Incluir un regalo con la compra del producto durante la campaña', 100056, TRUE),
    (10057, 'Extender la campaña hasta fin de mes y aumentar el presupuesto publicitario', 100057, TRUE),
    (10058, 'Realizar un evento de lanzamiento en línea para el nuevo producto', 100058, TRUE),
    (10059, 'Implementar una estrategia de redes sociales para aumentar la visibilidad', 100059, TRUE),
    (10060, 'Ofrecer envío gratuito durante toda la campaña', 100060, TRUE),
    (10061, 'Aumentar la duración de la campaña en una semana y agregar un producto más', 100061, TRUE),
    (10062, 'Reducir el precio del producto en un 10% durante la campaña', 100062, TRUE),
    (10063, 'Lanzar una nueva campaña de marketing para el producto 5', 100063, TRUE),
    (10064, 'Extender la fecha de inicio de la campaña en tres días', 100064, TRUE),
    (10065, 'Ofrecer un descuento del 15% para los primeros 50 compradores', 100065, TRUE),
    (10066, 'Actualizar las fechas de la campaña según el calendario de marketing', 100066, TRUE),
    (10067, 'Agregar una promoción especial para nuevos clientes', 100067, TRUE),
    (10068, 'Incluir una oferta 2x1 en productos seleccionados durante la campaña', 100070, TRUE),
    (10069, 'Extender la campaña hasta fin de mes y aumentar el presupuesto publicitario', 100071, TRUE),
    (10070, 'Realizar un evento de lanzamiento en línea para el nuevo producto', 100072, TRUE),
    (10071, 'Implementar una estrategia de redes sociales para aumentar la visibilidad', 100073, TRUE),
    (10072, 'Ofrecer envío gratuito durante toda la campaña', 100074, TRUE),
    (10073, 'Aumentar la duración de la campaña en una semana y agregar un producto más', 100075, TRUE),
    (10074, 'Reducir el precio del producto en un 10% durante la primera semana', 100076, TRUE),
    (10075, 'Lanzar una nueva campaña de marketing para el producto 10', 100077, TRUE),
    (10076, 'Extender la fecha de inicio de la campaña en dos días', 100078, TRUE),
    (10077, 'Ofrecer un descuento del 20% para los primeros 100 compradores', 100079, TRUE),
    (10078, 'Actualizar las fechas de la campaña según el calendario de marketing', 100080, FALSE),
    (10079, 'Agregar una promoción especial para nuevos clientes', 100081, TRUE),
    (10080, 'Incluir una oferta 2x1 en productos seleccionados durante la campaña', 100082, FALSE),
    (10081, 'Extender la campaña hasta fin de mes y aumentar el presupuesto publicitario', 100083, FALSE),
    (10082, 'Realizar un evento de lanzamiento en línea para el nuevo producto', 100084, FALSE),
    (10083, 'Implementar una estrategia de redes sociales para aumentar la visibilidad', 100085, FALSE),
    (10084, 'Ofrecer envío gratuito durante toda la campaña', 100086, FALSE),
    (10085, 'Aumentar la duración de la campaña en una semana y agregar un producto más', 100087, FALSE),
    (10086, 'Reducir el precio del producto en un 5% durante la campaña', 100088, FALSE),
    (10087, 'Lanzar una nueva campaña de marketing para el producto 2', 100089, FALSE),
    (10088, 'Extender la fecha de inicio de la campaña en cinco días', 100090, FALSE),
    (10089, 'Ofrecer un descuento del 20% para los primeros 50 compradores', 100091, FALSE),
    (10090, 'Actualizar las fechas de la campaña según el calendario de marketing', 100091, FALSE),
    (10091, 'Agregar una promoción especial para clientes frecuentes', 100092, FALSE),
    (10092, 'Incluir un regalo con la compra del producto durante la campaña', 100093, FALSE),
    (10093, 'Extender la campaña hasta fin de mes y aumentar el presupuesto publicitario', 100093, FALSE),
    (10094, 'Realizar un evento de lanzamiento en línea para el nuevo producto', 100096, FALSE),
    (10095, 'Implementar una estrategia de redes sociales para aumentar la visibilidad', 100096, FALSE),
    (10096, 'Ofrecer envío gratuito durante toda la campaña', 100097, FALSE),
    (10097, 'Aumentar la duración de la campaña en una semana y agregar un producto más', 100098, FALSE),
    (10098, 'Reducir el precio del producto en un 15% durante la primera semana', 100098, FALSE),
    (10099, 'Extender la duración de la campaña en dos semanas y añadir un producto adicional', 100099, FALSE);

select * from Observacion;

--cotizacionxproducto
insert into CotizaciónxProducto values (12, 10, 3);
insert into CotizaciónxProducto values (11, 10, 2);
insert into CotizaciónxProducto values (8, 10, 1);
insert into CotizaciónxProducto values (12, 11, 3);
insert into CotizaciónxProducto values (12, 11, 2);
insert into CotizaciónxProducto values (8, 11, 1);
insert into CotizaciónxProducto values (15, 13, 3);
insert into CotizaciónxProducto values (15, 13, 2);
insert into CotizaciónxProducto values (00, 13, 1);
select * from CotizaciónxProducto;

--proveedorxproducto
insert into ProveedorxProducto values (4.8, '3','20603302151');
insert into ProveedorxProducto values (6.0, '2', '20603302151');
insert into ProveedorxProducto values (11.0, '1', '20603302151');
insert into ProveedorxProducto values (5.1, '3','20607504149');
insert into ProveedorxProducto values (6.2, '2', '20607504149');
insert into ProveedorxProducto values (12.0, '1', '20607504149');
insert into ProveedorxProducto values (5.5, '3','20789101234');
insert into ProveedorxProducto values (6.3, '2', '20789101234');
insert into ProveedorxProducto values (12.2, '1', '20789101234');
select * from ProveedorxProducto;

--Tipos_pago 
INSERT INTO Tipos_pago (id_tipo_pago, nombre_tipo) VALUES
(11, 'Tarjeta de crédito'),
(12, 'Tarjeta de débito'),
(13, 'Efectivo'),
(14, 'A contra entrega'),
(15, 'Yape/Plin');
select * from Tipos_pago;

--Detalle_pago
INSERT INTO Detalle_pago (Id_detalle_pago  , fecha_pago , hora_pago  , id_tipo_pago  ) VALUES
(2001, '2022-01-01', '09:15', 11), 
(2002, '2022-04-15', '10:30', 12), 
(2003, '2022-08-22', '11:45', 13),
(2004, '2022-11-05', '13:20', 14), 
(2005, '2023-02-03', '14:50', 15),
(2006, '2023-06-18', '15:55', 14),
(2007, '2023-09-09', '16:10', 11), 
(2008, '2023-12-25', '17:25', 12), 
(2009, '2024-03-07', '18:40', 11), 
(2010, '2024-07-12', '19:55', 13);
select * from Detalle_pago;
--Venta
INSERT INTO Venta (Id_venta, id_persona, monto_final , Id_detalle_pago , nro_tarjeta ) VALUES
(1234, '10000001', 50.0, 2001,12345678),
(5678, '10000002', 20.0, 2002,12345679),
(9012, '10000003', 6.5, 2003,NULL ),
(3456, '10000004', 114.0, 2004,12335679),
(7890, '10000005', 112.0, 2005,NULL),
(2345, '10000006', 45.0, 2006, NULL),
(6789, '10000007', 60.0, 2007,23456809),
(123, '10000008', 22.0, 2008, 34561238),
(4567, '10000009', 18.0, 2009,72891500),
(8901, '10000010', 72.0, 2010,NULL);
select * from Venta;
--VentaXProd
INSERT INTO VentaXProd (id_prod_venta, Id_venta, id_producto, cant_prod, monto_total, Id_cupón) VALUES
(12341, 1234, 1, 2, 50.0, 1000),
(56782, 5678, 2, 1, 20.0, 1001),
(90123, 9012, 3, 1, 6.5, NULL),
(34564, 3456, 4, 4, 114.0, NULL),
(78905, 7890, 5, 7, 112.0, 1003),
(23456, 2345, 6, 1, 45.0, 1002),
(67897, 6789, 7, 2, 60.0, 1009),
(1238, 123, 8, 1, 22.0, 1006),
(45679, 4567, 9, 3, 18.0, 1007),
(890110, 8901, 10, 4, 72.0, NULL);
select * from VentaXProd;

INSERT INTO Tipo_est_formulario (Id_est_formulario, est_formulario) VALUES
(1, 'Activo'),
(2, 'Inactivo');

--Tipo_est_pedido
INSERT INTO Tipo_est_pedido VALUES ('E', 'ENTREGADO'), ('P', 'PENDIENTE');
select * from Tipo_est_pedido;

--Pedido
INSERT INTO Pedido (id_pedido, fecha_entrega, est_pedido, hora_entrega, id_ruta ,id_repartidor,id_venta) VALUES 
(1215,'8/1/2022','E','12:30', 2,9561677,1234),
(1365,'19/04/2022','E','12:30', 3,9561677,5678),
(1549,'27/08/2022','E','12:30', 4,9561677,9012),
(1816,'9/11/2022','E','12:30', 5,9561677,3456),
(2465,'8/02/2023','E','12:30', 6,7523677,7890),
(2964,'25/06/2023','E','12:30', 7,7523677,2345),
(3415,'15/09/2023','E','12:30', 8,7851678,6789),
(4315,'29/12/2023','E','12:30', 9,9561677,123),
(4516,'11/3/2024','E','12:30', 10,7523677,4567),
(4585,'23/07/2024','P','12:30', 11,7523677,8901);

select * from Pedido;

INSERT INTO Formulario (Id_formulario, descrip_formulario, fecha_creacion, Id_persona, Id_est_formulario) VALUES
(1, 'Encuesta de satisfacción', '2024-04-25', '1007', 1),
(2, 'Encuesta de preferencias', '2024-04-26', '1007', 2),
(3, 'Encuesta de productos', '2024-04-27', '1007', 1),
(4, 'Encuesta de opiniones', '2024-05-28', '1007', 2),
(5, 'Encuesta de experiencia', '2024-05-01', '1007', 1);

INSERT INTO Alternativa (id_alternativa, alternativa) VALUES
(1, ARRAY['Sí', 'No']),
(2, ARRAY['Excelente', 'Bueno', 'Regular', 'Malo', 'Muy malo']),
(3, ARRAY['Rojo', 'Azul', 'Verde', 'Negro', 'Blanco', 'Amarillo', 'Naranja', 'Morado']),
(4, ARRAY['Pequeño', 'Mediano', 'Grande', 'Extra grande']),
(5, ARRAY['Lápiz', 'Bolígrafo', 'Pluma', 'Marcador', 'Goma de borrar']),
(6, ARRAY['Seco', 'Graso', 'Mixto']),
(7, ARRAY['Líquido', 'Crema', 'Gel', 'Spray', 'Polvo']),
(8, ARRAY['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']),
(9, ARRAY['Extremadamente insatisfecho', 'Muy insatisfecho', 'Insatisfecho', 'Neutral', 'Satisfecho', 'Muy satisfecho', 'Extremadamente satisfecho']);

INSERT INTO Pregunta (Id_pregunta, pregunta, tipo_preg, id_alternativa) VALUES
(1, '¿Está satisfecho con su compra?', 'Opción única', 1),
(2, '¿Qué tal le pareció la calidad del producto?', 'Opción única', 2),
(3, '¿Cuál es su color favorito?', 'Opción única', 3),
(4, '¿Prefiere tamaños pequeños, medianos, grandes o extra grandes?', 'Opción múltiple', 4),
(5, '¿Cuál es su artículo de papelería favorito?', 'Opción única', 5),
(6, '¿Cómo describiría su tipo de piel?', 'Libre', NULL),
(7, '¿Qué tipo de producto cosmético prefiere?', 'Opción múltiple', 7),
(8, 'Por favor, califique del 1 al 10 la calidad del producto', 'Opción única', 8),
(9, '¿Cómo calificaría su satisfacción general con el servicio?', 'Opción única', 9);

INSERT INTO Respuesta (Id_respuesta, respuesta, Id_pregunta) VALUES
(1, 'Sí, estoy muy satisfecho con mi compra', 1),
(2, 'No, el producto no cumplió mis expectativas', 1),
(3, 'Excelente', 2),
(4, 'Regular', 2),
(5, 'Azul, siempre me ha gustado ese color', 3),
(6, 'Grande, necesito espacio para tomar apuntes', 4),
(7, 'Bolígrafo, es versátil y fácil de usar', 5),
(8, 'Tengo la piel mixta, algunas zonas son grasas y otras secas', 6),
(9, 'Prefiero cremas para el cuidado facial', 7),
(10, '8', 1),
(11, '3', 2),
(12, 'Rojo', 3),
(13, 'Pequeño', 4),
(14, 'Pluma', 5),
(15, 'Mi piel es grasa en la zona T y mixta en el resto', 6),
(16, 'Gel', 7),
(17, '9', 1),
(18, 'Satisfecho', 1),
(19, 'Neutral', 1),
(20, 'Insatisfecho', 1),
(21, '5', 2),
(22, 'Amarillo', 3),
(23, 'Extra grande', 4),
(24, 'Goma de borrar', 5),
(25, 'Mixto', 6),
(26, 'Polvo', 7),
(27, '7', 1),
(28, 'satisfecho', 1);

INSERT INTO PreguntaxRespuesta (Id_pregunta, Id_respuesta) VALUES
(1, 1),
(1, 2),
(2, 3),
(2, 4),
(3, 5),
(4, 6),
(4, 7),
(5, 8),
(6, 9),
(8, 10),
(8, 11),
(8, 12),
(8, 13),
(8, 14),
(8, 15),
(8, 16),
(8, 17),
(9, 18),
(9, 19),
(9, 20),
(9, 21),
(9, 22),
(9, 23),
(9, 24),
(9, 25),
(9, 26),
(9, 27),
(9, 28);

INSERT INTO FormularioxPregunta (Id_formulario, Id_pregunta) VALUES
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(1, 5),
(2, 6),
(2, 7),
(2, 8),
(2, 9);

INSERT INTO Comentario (Id_comentario, descrip_comentario, fecha_comentario, hora_comentario, id_producto, Id_persona) VALUES
(1, 'El servicio al cliente fue excepcional, y el producto llegó antes de lo esperado. ¡Muy satisfecho!', '2024-04-01', '09:30', 1, '10000001'),
(2, 'La calidad del producto es regular. Creo que podrían mejorar en ese aspecto', '2024-04-01', '14:00', 2, '10000003'),
(3, 'El color azul es mi favorito desde siempre. ¡Me encanta!', '2024-05-02', '10:15', 3, '10000005'),
(4, 'El tamaño grande es perfecto para mí, ya que me gusta tener mucho espacio para escribir', '2024-04-02', '15:45', 1, '10000007'),
(5, 'Siempre he sido fanático de los bolígrafos. Son prácticos y versátiles', '2024-04-03', '11:30', 4, '10000001'),
(6, 'Mi piel es mixta, así que necesito productos específicos para controlar las zonas grasas', '2024-04-04', '08:00', 3, '10000003'),
(7, 'Excelente atención al cliente. El personal fue muy amable y servicial', '2024-04-05', '16:20', 5, '10000004'),
(8, 'El producto llegó en malas condiciones. Estoy muy insatisfecho con el servicio', '2024-04-06', '13:45', 6, '10000009'),
(9, 'La crema que compré es de muy buena calidad. Definitivamente volveré a comprarla', '2024-04-07', '10:10', 7, '10000008');



--Tipo_Mov
INSERT INTO Tipo_Mov VALUES ('E', 'Entrada de Productos'), ('R', 'Salida de Productos a Clientes'),('S','Salida de Productos a Áreas de la Empresa');
select * from Tipo_Mov;

--Almacen
INSERT INTO Almacen VALUES (1,'Papeleria', 'Artículos de oficina, librería, útiles de escritorio'), (2,'Maquillaje', 'Artículos de belleza para damas y caballeros');
select * from Almacen;

--Secciones
INSERT INTO Secciones VALUES ('A', 1),('B', 1),('C', 2),('D', 2) ;
select * from Secciones;

--Estands
INSERT INTO Estands VALUES ('E1', 1,'A'),('E2', 1,'A'),('E3', 1,'A'),('E4', 1,'B') ;
select * from Estands;

--Repisas
INSERT INTO Repisas VALUES ('R1', 1,'A'),('R2', 1,'A'),('R3', 1,'B'),('R4', 1,'B') ;
select * from Repisas;

--Ubicacion
INSERT INTO Ubicacion VALUES ('A-E1-R11','A','E1','R1',1);
select * from Ubicacion;

--Transportista
INSERT INTO Transportista VALUES (1001,'Juan Carlos Ramirez','Disponible');
select * from Transportista;


--Inventario
INSERT INTO Inventario VALUES (1242300021,'Forrado',20,10,10,2,200.00,'A-E1-R11');
select * from Inventario;


--Tipo_presupuesto
insert into Tipo_presupuesto values (1,'presupuesto compras');
insert into Tipo_presupuesto values (2,'presupuesto inversiones');
insert into Tipo_presupuesto values (3,'presupuesto ventas');
insert into Tipo_presupuesto values (4,'presupuesto distribución');
select * from Tipo_presupuesto;

--Tipo_asiento_contable
insert into tipo_asiento_contable values (401,'apertura');
insert into tipo_asiento_contable values (402,'cierre');
insert into tipo_asiento_contable values (403, 'ajuste');
insert into tipo_asiento_contable values (404,'ingreso');
insert into tipo_asiento_contable values (405,'gasto');
insert into tipo_asiento_contable values (406,'gasto');
insert into tipo_asiento_contable values (407,'cobro');
insert into tipo_asiento_contable values (408,'compras');
insert into tipo_asiento_contable values (409,'ventas');
insert into tipo_asiento_contable values (410,'provision');
select * from tipo_asiento_contable;
--Tipo_Factura
insert into Tipo_Factura values (111, 'compras');
insert into Tipo_Factura values (112, 'ventas');
insert into Tipo_Factura values (113, 'gastos');
--Tipo_estado
insert into Estado values (71,'Pagado');
insert into Estado values (72,'No Pagado');
insert into Estado values (73,'Falta Pagar');
--Tipo_valor
insert into Tip_valor values (41, 'Positivo');
insert into Tip_valor values (42, 'Negativo');
--Tipo_operacion
insert into Tip_operación values (21, 'Operacion Simple');
insert into Tip_operación values (22, 'Operacion Calculada');

--Tipo_item_est
insert into Tipo_item_est values (301,'ventas',21, 41);
insert into Tipo_item_est values (302,'compras',21, 42);
insert into Tipo_item_est values (303,'costos de producción',21, 42);
insert into Tipo_item_est values (304,'costos de ventas',21, 42);
insert into Tipo_item_est values (305,'utilidad bruta',22, 41);
insert into Tipo_item_est values (306,'gastos de operación',21, 42);
insert into Tipo_item_est values (307,'utilidad operativa',22, 41);
insert into Tipo_item_est values (308,'gastos financieros',21, 42);
insert into Tipo_item_est values (309,'utilidad antes de impuesto',22, 41);
insert into Tipo_item_est values (310,'impuesto',21, 42);
insert into Tipo_item_est values (311,'utilidad neta',22, 41);
select * from Tipo_item_est;
--Factura
insert into Factura values (2022001,'01-01-2022',100.05,'10000001',null,111, 71);
insert into Factura values (2022002,'02-08-2022',250.75,null,'20603302151', 112, 71);
insert into Factura values (2022003,'23-11-2022',500,'10000002',null, 113, 72);
insert into Factura values (2022004,'12-04-2023',20.05,'10000003',null, 112, 73);
insert into Factura values (2022005,'17-07-2021',660,null,'22890123456', 112, 72);
insert into Factura values (2022006,'05-09-2022',13.05,'10000004',null, 111, 73);
insert into Factura values (2022007,'01-01-2023',123.56,'10000005',null, 111, 71);
insert into Factura values (2022008,'13-10-2021',1000,null,'20607504149', 112, 72);
insert into Factura values (2022009,'04-06-2023',200.65,null,'20789101234', 112, 71);
insert into Factura values (2022010,'01-01-2024',134.78,'10000006',null, 113, 73);
select * from Factura;

--Presupuesto
insert into Presupuesto values (601,'01-01-2022','may-2023', 1,'1007');
insert into Presupuesto values (602,'15-01-2022','jun-2023', 2,'1005');
insert into Presupuesto values (603,'01-01-2023','dic-2023', 3,'1006');
insert into Presupuesto values (604,'22-01-2022','oct-2023', 4,'1003');
insert into Presupuesto values (605,'04-01-2021','jul-2022', 3,'1002');
insert into Presupuesto values (606,'01-01-2022','nov-2023', 2,'1001');
insert into Presupuesto values (607,'06-01-2021','oct-2022', 1,'1004');
insert into Presupuesto values (608,'11-01-2022','agos-2023', 2,'1002');
insert into Presupuesto values (609,'13-10-2023','ene-2024', 2,'1001');
insert into Presupuesto values (610,'02-10-2022','febr-2023', 4,'1007');
select * from Presupuesto;
--Asiento-contable
insert into Asiento_Contable values (101,100.5, 0,2022001,401);
insert into Asiento_Contable values (102,0,250.75,2022002,404);
insert into Asiento_Contable values (103,500,0,2022003,403);
insert into Asiento_Contable values (104,0,730.25,2022004,406);
insert into Asiento_Contable values (105,0 , 567,2022005,403);
insert into Asiento_Contable values (106,1067.5,0,2022006,408);
insert into Asiento_Contable values (107,1200,0,2022007,405);
insert into Asiento_Contable values (108,0,1000.2,2022008,410);
insert into Asiento_Contable values (109,300.5,0,2022009,403);
insert into Asiento_Contable values (110, 12500.25, 0,2022010,401);
select * from Asiento_Contable;

---Item_estado_resultado
insert into Item_estado_resultados values (81,101,301);
insert into Item_estado_resultados values (82,102,302);
insert into Item_estado_resultados values (83,103,303);
insert into Item_estado_resultados values (84,103,304);
insert into Item_estado_resultados values (85,101,305);
insert into Item_estado_resultados values (86,102,306);
insert into Item_estado_resultados values (87,102,307);
insert into Item_estado_resultados values (88,101,303);
insert into Item_estado_resultados values (89,109,302);
insert into Item_estado_resultados values (90,103,305);
select * from Item_estado_resultados;

--Estado de resultados
insert into Estado_de_resultados values (201, 2004,1);
insert into Estado_de_resultados values (202, 2000,2);
insert into Estado_de_resultados values (203, 2003,3);
insert into Estado_de_resultados values (204, 2018,4);
select * from Estado_de_resultados;
 
--Estadoxitem
insert into EstadoxItem values (1000, 81, 203);
insert into EstadoxItem values (10670, 83, 202);
select * from EstadoxItem;


--Almacen
INSERT INTO Orden_Almacen VALUES ('OT-001','AM','1006',2,1215,2);
select * from Orden_Almacen;

--Movimiento
INSERT INTO Movimiento VALUES (101,'2/03/2024','S',1,1001,'OT-001');
select * from Movimiento;


SELECT * FROM VENTA;
SELECT * from detalle_pago;
select * from tipos_pago;
select * from factura;

```
