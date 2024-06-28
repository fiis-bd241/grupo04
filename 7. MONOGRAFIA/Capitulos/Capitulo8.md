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

```
