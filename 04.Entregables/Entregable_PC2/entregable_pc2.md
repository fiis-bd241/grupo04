# 1. Modelo Conceptual

# 2. Modelamiento Lógico

## 2.1 Módelo Lógico

![Módelo Lógico](Modelo_Logico_v1.png)
[Módelo Lógico](Modelo_Logico_v1.png)
## 2.2 Diccionario de Datos

Entidad: Proveedor

Descripción: Empresa o persona que proporciona productos a la empresa
| Atributo | Descripción | Formato | Naturaleza | Valores |
|:----------:|:--------------------------------:|:---------------:|:------------------:|:--------:|
| RUC_proveedor | RUC del proveedor que lo identifica en la empresa | 99999999999 | CHAR(11) | NOT NULL |
| razon_social | Nombre con el que se constituye una empresa | A(100) | VARCHAR(100) | NOT NULL |
| web_proveedor | Sitio web del proveedor  | A(100) | VARCHAR(100) | - |
| rubro | Actividad económica que realiza una empresa | A(100) | VARCHAR(100) | NOT NULL |
| direccion | Ubicacion geográfica donde esta ubicado el proveedor | A(100) | VARCHAR(100) | NOT NULL |
| telefono | Numero de contacto con el proveedor | A(15) | VARCHAR(15) | NOT NULL |
| id_est_proveedor | Identificador único del estado del proveedor | A(10) | VARCHAR(10) | NOT NULL |

Entidad: Tipo_est_proveedor

Descripción: Estado del proveedor en la empresa.
| Atributo | Descripción | Formato | Naturaleza | Valores |
|:----------:|:--------------------------------:|:---------------:|:------------------:|:--------:|
| id_est_proveedor | Identificador único del estado del proveedor | A(10) | VARCHAR(10) | NOT NULL |
| est_proveedor | Estado del proveedor | A(100) | VARCHAR(100) | NOT NULL |

Entidad: Cotización

Descripción: Cotización realizada por el proveedor.
| Atributo | Descripción | Formato | Naturaleza | Valores |
|:----------:|:--------------------------------:|:---------------:|:------------------:|:--------:|
| id_cotizacion |  Identificador único de la cotización | 999999 | Int | >0 |
| monto_total | Cantidad total del dinero que vale la cotizacion | 9999999,99 | NUMERIC(7,2) | NOT NULL |
| RUC_proveedor | RUC del proveedor que lo identifica en la empresa | 99999999999 | CHAR(11) | NOT NULL |
| id_est_cotizacion | Identificador único del estado de la cotizacion | A | CHAR(1) | NOT NULL |

Entidad: Tipo_est_cotizacion

Descripción: Estado de la cotizacion presentada por el proveedor.
| Atributo | Descripción | Formato | Naturaleza | Valores |
|:----------:|:--------------------------------:|:---------------:|:------------------:|:--------:|
| id_est_cotizacion | Identificador único del estado de la cotizacion | A | CHAR(1) | NOT NULL |
| est_cotizacion | Estado de la cotizacion | A(100)| VARCHAR(100) | NOT NULL |

Entidad: Producto

Descripción: Son los bienes que la empresa tiene en venta
| Atributo | Descripción | Formato | Naturaleza | Valores |
|:----------:|:--------------------------------:|:---------------:|:------------------:|:--------:|
| id_producto | Identificador único del producto | 99999 | Int | >0 |
| nombre_producto | Nombre del producto | A(100) | VARCHAR(100) | NOT NULL |
| descripcion_prod | Descripcion de especificaciones del producto | A(100) | VARCHAR(100) | NOT NULL |
| cant_min | Cantidad minima que puede haber de un producto | 99 | Int | >0 |
| cant_max | Cantidad maxima que puede haber de un producto | 999 | Int | >0 |
| precio_unit | Precio unitario que la empresa asigno a un producto | 999 | Int | >0 |
| id_categoria_prod | Identificador unico de la categoria de un producto | 999 | Int | >0 |
| Id_cupón | Identificador unico del cupón aplicado al producto | 9999 | Int | NOT NULL |
| Id_campaña | Identificador unico de la campaña activa que promociona al producto | 999999 | Int | NOT NULL |

Entidad: Categoria_prod

Descripción: Categoria al que pertenece un producto
| Atributo | Descripción | Formato | Naturaleza | Valores |
|:----------:|:--------------------------------:|:---------------:|:------------------:|:--------:|
| id_categoria_prod | Identificador unico de la categoria de un producto | 999 | Int | >0 |
| nombre | Nombre de la categoria del producto | A(100)| VARCHAR(100) | NOT NULL |
| id_tipo_prod | Identificador unico del tipo de producto | 999 | Int | >0 |

Entidad: tipo_prod

Descripción: Tipo de producto al que eertenece un producto
| Atributo | Descripción | Formato | Naturaleza | Valores |
|:----------:|:--------------------------------:|:---------------:|:------------------:|:--------:|
| id_tipo_prod | Identificador unico del tipo de producto | 999 | Int | >0 |
| nombre | Nombre del tipo de producto | A(100)| VARCHAR(100) | NOT NULL |

Entidad: ProveedorXProducto

Descripción: Relacion entre el proveedor y los productos que ofrece en una cotizacion
| Atributo | Descripción | Formato | Naturaleza | Valores |
|:----------:|:--------------------------------:|:---------------:|:------------------:|:--------:|
| id_producto | Identificador único del producto | 99999 | Int | >0 |
| RUC_proveedor | RUC del proveedor que lo identifica en la empresa | 99999999999 | CHAR(11) | NOT NULL |
| precio_prod_prov | Precio unitario que el proveedor asigno a un producto| 999 | Int | >0 |

Entidad: CotizacionXProducto

Descripción: Relacion entre la cotizacion y los productos que nos determina la cantidad de cada producto
| Atributo | Descripción | Formato | Naturaleza | Valores |
|:----------:|:--------------------------------:|:---------------:|:------------------:|:--------:|
| id_cotizacion |  Identificador único de la cotización | 999999 | Int | >0 |
| id_producto | Identificador único del producto | 99999 | Int | >0 |
| cantidad | Cantidad de un producto ofrecido en una cotizacion | 999 | Int | >0 |

Entidad: Distrito

Descripcion: Lugar donde reside la persona

|Atributo|Descripcion|Formato|Naturaleza|Valores|
|---------|-------|-------|----|-----------|
|Id_distrito|Codigo identificador del distrito|99|INT|NOT NULL|
|nombre|Nombre del distrito|A(100)|VARCHAR(100)|NOT NULL|
|ubigeo|Siglas oficiales para el codigo de ubicacion geografica del distrito|AAAAAA|VARCHAR(100)|NOT NULL|
|cod_postal|Codigo numérico que complementa la dirección física y representa una zona geográfica del país. |AA|VARCHAR(100)|NOT NULL|
|id_zona|Codigo identificador de la zona|99|INT|NOT NULL|

Entidad: Repartidor

Descripcion : Persona que realiza la entrega de los pedidos

|Atributo|Descripcion|Formato|Naturaleza|Valores|
|---------|-------|-------|----|-----------|
|Id_repartidor|Codigo identificador del repartidor|9999999|INT|NOT NULL|
|usuario|nombre del usuario de la cuenta del repartidor|A(100)|VARCHAR(100)|NOT NULL|
|contraseña|contraseña de la cuenta del repartidor|A(100)|VARCHAR(100)|NOT NULL|
|Nombre|Nombres del repartidor|A(100)|VARCHAR(100)|NOT NULL|
|Apellido|Apellidos del repartidor|A(100)|VARCHAR(100)|NOT NULL|
|id_zona|zona asignada al repartidor|99|INT|NOT NULL|

Entidad: Zona

Descripcion: Area de agrupamiento para los distritos

|Atributo|Descripcion|Formato|Naturaleza|Valores|
|---------|-------|-------|----|-----------|
|id_zona|Codigo identificador de la zona|99|INT|NOT NULL|
|nombre|Nombre de la zona|A(100)|VARCHAR(100)|NOT NULL|
|cant_distritos|Cantidad de distritos en la zona|99|INT|NOT NULL|

Entidad: Ruta

Descripcion: Metodo de traslado recomendable para la entrega

|Atributo|Descripcion|Formato|Naturaleza|Valores|
|---------|-------|-------|----|-----------|
|id_ruta|Codigo identificador de la ruta|99|INT|NOT NULL|
|distrito_inicial|Distrito inicial de la ruta |A(100)|VARCHAR(100)|NOT NULL|
|distrito_final|Cantidad de distritos en la zona|A(100)|VARCHAR(100)|NOT NULL|
|Tiempo_prom|Tiempo estimado que demora trasladar del primer distrito al otro|AAAAAAAA|VARCHAR(100)|NOT NULL
|medio_transporte|Medio de transporte |Medio de tranporte recomendo para trasladarse|A(100)|VARCHAR(100)|NOT NULL|

Entidad: Pedido 

Descripcion: 

|Atributo|Descripcion|Formato|Naturaleza|Valores|
|---------|-------|-------|----|-----------|
|Id_pedido|Codigo identificador del pedido|9999|INT|NOT NULL|
|fecha_entrega|Fecha que se va a realizar la entrega|DD/MM/AA|DATE|Valido en calendario|
|estado|Estado en que se encuentra el pedido|99|INT|NOT NULL|
|hora_entrega|Hora que se va a realizar la entrega|hh:mm|TIME|NOT NULL|
|Id_ruta|Codigo de la ruta recomendada asignada a la entrega|99|INT|NOT NULL|
|Id_repartidor|Codigo del repartidor encargado de realizar la entrega |9999999|INT|NOT NULL|
|Id_vemta|Codigo de la venta realizada que se va a entregar|9999|INT|NOT NULL|
|Id_persona|Codigo de la persona/cliente que realizó compra|9999999|INT|NOT NULL|

Entidad: Equipo marketing

Descripción: Conjunto de empleados pertenecientes al área de marketing encargados de crear las campañas.
| Atributo | Descripción | Formato | Naturaleza | Valores |
|:----------:|:--------------------------------:|:---------------:|:------------------:|:--------:|
| Id_equipo_mark | Identificador único del equipo de marketing | 99 | INT | NOT NULL |
| nombre_equipo | Nombre perteneciente al equipo de marketing | A(100) | VARCHAR(100) | NOT NULL |
| cant_emp | Cantidad de empleados del equipo de marketing  | 9 | INT | >0 |

Entidad: Cupón

Descripción: Billete que puede ser intercambiado por el descuento de un producto.
| Atributo | Descripción | Formato | Naturaleza | Valores |
|:----------:|:--------------------------------:|:---------------:|:------------------:|:--------:|
| Id_cupón | Identificador único del cupón | 9999 | INT | NOT NULL |
| fecha_ini_cup | Fecha a partir de la cual es válido el cupón | AAAA/MM/DD | DATE | NOT NULL |
| fecha_fin_cup | Fecha hasta la cual es válido el cupón  | AAAA/MM/DD | DATE | NOT NULL |
| desc_cup | Descuento porcentual en forma decimal que aplica el cupón a un producto | 9.99 | FLOAT | >0 |
| esta_activo | Respuesta a, ¿el estado del cupón es válido? | A(5) | BOOLEAN | NOT NULL |

Entidad: Campaña

Descripción: Proyecto de comunicación de los productos y sus promociones en la tienda.
| Atributo | Descripción | Formato | Naturaleza | Valores |
|:----------:|:--------------------------------:|:---------------:|:------------------:|:--------:|
| Id_campaña | Identificador único de la campaña | 999999 | INT | NOT NULL |
| fecha_ini | Fecha a partir de la cual es válida la campaña | AAAA/MM/DD | DATE | NOT NULL |
| fecha_fin | Fecha hasta la cual es válida la campaña  | AAAA/MM/DD | DATE | NOT NULL |
| canal_publi | Red social o página web en la que se transmite la campaña publicitaria | A(100) | VARCHAR(100) | NOT NULL |
| dir_url | Dirección URL a la que se redirige al usuario al precionar en la publicidad | A(100) | VARCHAR(100) | NOT NULL |
| modalidad | Modalidad de publicidad en la red social o página web | A(100) | VARCHAR(100) | NOT NULL |
| archivo | Dirección URL que contiene el archivo jpg o mp4 de la publicidad | A(100) | VARCHAR(100) | NOT NULL |
| desc_campaña | Descuento porcentual en forma decimal que realiza la campaña a los productos que contiene | 9.99 | FLOAT | >0 |
| Id_equipo_mark | Identificador único del equipo de marketing que creó la campaña | 99 | INT | NOT NULL |
| Id_gest_mark | Identificador único del gestor de marketing que gestionó la campaña | 9999999 | INT | NOT NULL |

Entidad: Tipo de Pago

Descripción: Métodos de pago aceptados en el sistema de ventas

| Atributo    | Descripción                                 | Formato     | Naturaleza | Valores    |
|-------------|---------------------------------------------|-------------|------------|------------|
| id_tipo_pago| Código identificador del tipo de pago       | 99          | INT        | NOT NULL   |
| nombre_tipo | Nombre del tipo de pago                     | A(100)      | VARCHAR(100) | NOT NULL |
| nro_tarjeta | Número de tarjeta asociado al tipo de pago | A(50)       | VARCHAR(50)  |     >0   |

Entidad: Detalle de Pago

Descripción: Registro detallado de los pagos realizados en el sistema de ventas

| Atributo       | Descripción                            | Formato     | Naturaleza | Valores    |
|----------------|----------------------------------------|-------------|------------|------------|
| id_detalle_pago| Código identificador del detalle de pago | 9999      | INT        | NOT NULL   |
| fecha_pago     | Fecha en la que se realizó el pago     | DD/MM/AAAA  | DATE       | NOT NULL   |
| hora_pago      | Hora en la que se realizó el pago      | HH:MM       | VARCHAR(10)| NOT NULL   |
| id_tipo_pago   | ID del tipo de pago utilizado          | 99          | INT        | NOT NULL   |

Entidad: Venta

Descripción: Registro de las transacciones comerciales realizadas por los clientes.

| Atributo       | Descripción                                   | Formato     | Naturaleza | Valores    |
|----------------|-----------------------------------------------|-------------|------------|------------|
| id_venta       | Código identificador de la venta              | 9999        | INT        | NOT NULL   |
| Id_persona     | Identificador único del cliente               | 99999999    | INT | NOT NULL   |
| monto_final    | Monto total de la venta                       | 99.99       | FLOAT      | NOT NULL   |
| id_detalle_pago| ID del detalle de pago asociado a la venta    | 9999        | INT        | NOT NULL   |

Entidad: VentaXProd

Descripción: Registro de los productos vendidos en cada transacción.

| Atributo       | Descripción                                         | Formato   | Naturaleza | Valores  |
|----------------|-----------------------------------------------------|-----------|------------|----------|
| id_venta_prod  | Código identificador de la venta del producto       | 999999    | INT        | NOT NULL |
| id_venta       | Identificador único de la venta asociada            | 9999      | INT        | NOT NULL |
| id_producto    | Identificador único del producto vendido            | 9999      | INT        | NOT NULL |
| cant_prod      | Cantidad del producto vendido                       | 9999      | INT        | NOT NULL |
| monto_prod     | Monto total del producto vendido                    | 99.99     | FLOAT      | NOT NULL |


# 3. Creación de tablas

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
  cant_emp INT,
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

CREATE TABLE Transportista
(
  Id_transportista INT NOT NULL,
  nombre_transp VARCHAR(100) NOT NULL,
  nro_licencia VARCHAR(100) NOT NULL,
  PRIMARY KEY (Id_transportista)
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
  PRIMARY KEY (Id_tipo_item_est)
);

CREATE TABLE tipo_asiento_contable
(
  id_tipo_asiento_contable INT NOT NULL,
  nombre_tipo VARCHAR(100) NOT NULL,
  PRIMARY KEY (id_tipo_asiento_contable)
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
  nro_tarjeta VARCHAR(50),
  PRIMARY KEY (id_tipo_pago)
);

CREATE TABLE Cupón
(
  Id_cupón INT NOT NULL,
  fecha_ini_cup DATE NOT NULL,
  fecha_fin_cup DATE NOT NULL,
  desc_cup FLOAT,
  esta_activo BOOLEAN NOT NULL,
  PRIMARY KEY (Id_cupón)
);

CREATE TABLE Persona
(
  Nombre VARCHAR(100) NOT NULL,
  Primer_apell VARCHAR(100) NOT NULL,
  Segundo_apell VARCHAR(100) NOT NULL,
  Correo VARCHAR(100) NOT NULL,
  Telefono INT NOT NULL,
  Id_persona INT NOT NULL,
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
  id_zona INT NOT NULL,
  PRIMARY KEY (Id_repartidor),
  FOREIGN KEY (id_zona) REFERENCES zona(id_zona)
);

CREATE TABLE Campaña
(
  Id_campaña INT NOT NULL,
  fecha_ini DATE NOT NULL,
  fecha_fin DATE NOT NULL,
  canal_publi VARCHAR(100) NOT NULL,
  dir_url VARCHAR(100) NOT NULL,
  modalidad VARCHAR(100) NOT NULL,
  archivo VARCHAR(100) NOT NULL,
  des_campaña FLOAT,
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


CREATE TABLE Factura
(
  nro_factura INT NOT NULL,
  fecha_emision DATE NOT NULL,
  monto FLOAT NOT NULL,
  RUC_proveedor CHAR(11),
  Id_persona INT NOT NULL,
  PRIMARY KEY (nro_factura),
  FOREIGN KEY (RUC_proveedor) REFERENCES Proveedor(RUC_proveedor),
  FOREIGN KEY (Id_persona) REFERENCES Persona(Id_persona)
);


CREATE TABLE Almacen
(
  id_almacen INT NOT NULL,
  Cod_area VARCHAR(100) NOT NULL,
  Id_persona INT NOT NULL,
  Id_tipo_prod INT NOT NULL,
  PRIMARY KEY (id_almacen),
  FOREIGN KEY (Cod_area) REFERENCES Area(Cod_area),
  FOREIGN KEY (Id_persona) REFERENCES Persona(Id_persona),
  FOREIGN KEY (Id_tipo_prod) REFERENCES tipo_prod(Id_tipo_prod)
);

CREATE TABLE Presupuesto
(
  Id_presupuesto INT NOT NULL,
  fecha_elaboracion DATE NOT NULL,
  Id_tipo_presupuesto INT NOT NULL,
  Id_persona INT NOT NULL,
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

CREATE TABLE Item_estado_resultados
(
  Id_item_est__resultados INT NOT NULL,
  Id_asiento_contable INT NOT NULL,
  Id_tipo_item_est INT NOT NULL,
  PRIMARY KEY (Id_item_est__resultados),
  FOREIGN KEY (Id_asiento_contable) REFERENCES Asiento_Contable(Id_asiento_contable),
  FOREIGN KEY (Id_tipo_item_est) REFERENCES Tipo_item_est(Id_tipo_item_est)
);

CREATE TABLE Estado_de_resultado
(
  id_est_resultados INT NOT NULL,
  monto FLOAT NOT NULL,
  Id_item_est__resultados INT NOT NULL,
  PRIMARY KEY (id_est_resultados),
  FOREIGN KEY (Id_item_est__resultados) REFERENCES Item_estado_resultados(Id_item_est__resultados)
);

CREATE TABLE Secciones
(
  id_seccion CHAR(1) NOT NULL,
  id_almacen INT NOT NULL,
  PRIMARY KEY (id_seccion),
  FOREIGN KEY (id_almacen) REFERENCES Almacen(id_almacen)
);

CREATE TABLE Estands
(
  id_estand INT NOT NULL,
  id_almacen INT NOT NULL,
  PRIMARY KEY (id_estand),
  FOREIGN KEY (id_almacen) REFERENCES Almacen(id_almacen)
);

CREATE TABLE Repisas
(
  id_repisas INT NOT NULL,
  id_almacen INT NOT NULL,
  PRIMARY KEY (id_repisas),
  FOREIGN KEY (id_almacen) REFERENCES Almacen(id_almacen)
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
  Id_cupón INT NOT NULL,
  Id_campaña INT NOT NULL,
  PRIMARY KEY (id_producto),
  FOREIGN KEY (Id_categoria_prod) REFERENCES Categoria_prod(Id_categoria_prod),
  FOREIGN KEY (Id_cupón) REFERENCES Cupón(Id_cupón),
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
  Id_persona INT NOT NULL,
  PRIMARY KEY (Id_venta),
  FOREIGN KEY (Id_detalle_pago) REFERENCES Detalle_pago(Id_detalle_pago),
  FOREIGN KEY (Id_persona) REFERENCES Persona(Id_persona)
);

CREATE TABLE VentaXProd
(
  cant_prod INT NOT NULL,
  monto_total FLOAT NOT NULL,
  id_prod_venta INT NOT NULL,
  id_producto INT NOT NULL,
  Id_venta INT NOT NULL,
  PRIMARY KEY (id_prod_venta, id_producto, Id_venta),
  FOREIGN KEY (id_producto) REFERENCES Producto(id_producto),
  FOREIGN KEY (Id_venta) REFERENCES Venta(Id_venta)
);

CREATE TABLE Movimiento
(
  Id_mov INT NOT NULL,
  fecha_mov DATE NOT NULL,
  Id_tipo_mov CHAR(1) NOT NULL,
  id_almacen INT NOT NULL,
  Id_transportista INT NOT NULL,
  PRIMARY KEY (Id_mov),
  FOREIGN KEY (Id_tipo_mov) REFERENCES Tipo_mov(Id_tipo_mov),
  FOREIGN KEY (id_almacen) REFERENCES Almacen(id_almacen),
  FOREIGN KEY (Id_transportista) REFERENCES Transportista(Id_transportista)
);

CREATE TABLE Ubicacion
(
  Id_ubicacion INT NOT NULL,
  id_repisas INT NOT NULL,
  id_estand INT NOT NULL,
  id_seccion CHAR(1) NOT NULL,
  id_almacen INT NOT NULL,
  PRIMARY KEY (Id_ubicacion),
  FOREIGN KEY (id_repisas) REFERENCES Repisas(id_repisas),
  FOREIGN KEY (id_estand) REFERENCES Estands(id_estand),
  FOREIGN KEY (id_seccion) REFERENCES Secciones(id_seccion),
  FOREIGN KEY (id_almacen) REFERENCES Almacen(id_almacen)
);

CREATE TABLE Inventario
(
  id_inventario INT NOT NULL,
  Entradas INT NOT NULL,
  Salidas INT NOT NULL,
  Stock INT NOT NULL,
  id_producto INT NOT NULL,
  Id_ubicacion INT NOT NULL,
  PRIMARY KEY (id_inventario),
  FOREIGN KEY (id_producto) REFERENCES Producto(id_producto),
  FOREIGN KEY (Id_ubicacion) REFERENCES Ubicacion(Id_ubicacion)
);

CREATE TABLE Tipo_est_pedido (
    est_pedido VARCHAR(1) PRIMARY KEY,
    descripcion VARCHAR(50) NOT NULL
);

CREATE TABLE Pedido
(
  Id_pedido INT NOT NULL,
  fecha_entrega DATE NOT NULL,
  est_pedido VARCHAR(100) NOT NULL,
  hora_entrega TIME,
  Id_ruta INT NOT NULL,
  Id_repartidor INT NOT NULL,
  Id_venta INT NOT NULL,
  Id_persona INT NOT NULL,
  PRIMARY KEY (Id_pedido),
  FOREIGN KEY (Id_ruta) REFERENCES Ruta(Id_ruta),
  FOREIGN KEY (Id_repartidor) REFERENCES Repartidor(Id_repartidor),
  FOREIGN KEY (Id_venta) REFERENCES Venta(Id_venta),
  FOREIGN KEY (Id_persona) REFERENCES Persona(Id_persona)
);


CREATE TABLE Tipo_est_formulario
(
  Id_est_formulario VARCHAR(100) NOT NULL,
  est_formulario VARCHAR(100) NOT NULL,
  PRIMARY KEY (Id_est_formulario)
);


CREATE TABLE Alternativa
(
  id_alternativa INT NOT NULL,
  alternativa  NOT NULL,
  PRIMARY KEY (id_alternativa)
);



CREATE TABLE Formulario
(
  Id_formulario INT NOT NULL,
  descrip_formulario VARCHAR(500) NOT NULL,
  fecha_creacion DATE NOT NULL,
  Id_persona VARCHAR(100) NOT NULL,
  Id_est_formulario VARCHAR(100) NOT NULL,
  PRIMARY KEY (Id_formulario),
  FOREIGN KEY (Id_persona) REFERENCES Persona(Id_persona),
  FOREIGN KEY (Id_est_formulario) REFERENCES Tipo_est_formulario(Id_est_formulario)
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

CREATE TABLE Respuesta
(
  Id_respuesta INT NOT NULL,
  respuesta  NOT NULL,
  Id_formulario INT NOT NULL,
  PRIMARY KEY (Id_respuesta),
  FOREIGN KEY (Id_formulario) REFERENCES Formulario(Id_formulario)
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
  Id_persona VARCHAR(100) NOT NULL,
  PRIMARY KEY (Id_comentario),
  FOREIGN KEY (id_producto) REFERENCES Producto(id_producto),
  FOREIGN KEY (Id_persona) REFERENCES Persona(Id_persona)
);



```

# 4. Poblamiento inicial de datos

```sql
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
insert into Proveedor values ('20603302151', 'IMPORT EXPORT JAXU S.A.C','facebook.com/JAXUPERU', 'Papelería', 'Cal. Schell Nro. 255 Com. San  Miguel de Miraflores', '980520529', 'A'),
('20607504149', 'STELLAX S.A.C.','facebook.com/STELLAX', 'Papelería', 'Jr. Ucayali Nro. 738 Int. 102g', '955978789', 'A'),
('20789101234', 'YanbalPapeleríaSAC','facebook.com/Yanbal', 'Papelería', 'Av. Los Pinos 1014', '955978799', 'A'),
('21012345678', 'AtlasBeautySAC','facebook.com/AtlasB', 'Maquillaje', 'Calle Los Olivos 2022', '995978799', 'A'),
('22890123456', 'RuletaCosméticaSAC','facebook.com/RuletaCosmetica', 'Maquillaje', 'Calle Los Álamos 1414', '985978799', 'A');
select * from Proveedor;
-- Tipo_est_cotizacion
insert into Tipo_est_cotizacion values ('A', 'Aceptado'),('N', 'No Aceptado');
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
INSERT INTO Repartidor VALUES (4851677, 'Juan.Martinez', 'Juan123','Martinez',1);
INSERT INTO Repartidor VALUES (7851678, 'David.Suarez', 'David123','Suarez',2);
INSERT INTO Repartidor VALUES (4859677, 'Roman.Reings','Roman123','Reigns',3);
INSERT INTO Repartidor VALUES (7523677, 'Seth.Rollins','Seth123','Rollins',4);
INSERT INTO Repartidor VALUES (9561677, 'Dean.Ambrose','Dean123','Ambrose',5);
INSERT INTO Repartidor VALUES (1564677, 'Cody.Rodhes', 'Cody123','Rodhes',6);
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
INSERT INTO Equipo_Marketing (Id_equipo_mark, nombre_equipo, cant_emp)
VALUES
    (10, 'Equipo A', 4),
    (11, 'Equipo B', 6),
    (12, 'Equipo C', 5),
    (13, 'Equipo D', 5),
    (14, 'Equipo E', 6),
    (15, 'Equipo F', 4),
    (16, 'Equipo G', 5),
    (17, 'Equipo H', 5),
    (18, 'Equipo I', 3),
    (19, 'Equipo J', 4);
select * from Equipo_Marketing;

--Persona
INSERT INTO Persona VALUES 
('María','Gonzales', 'Ramírez', 'maria.gonzales@gmail.com','984562135','10000001','Av. Los Laureles 123','mariagr', 'mmmaaria',8,'CLI',NULL,NULL,'F');
INSERT INTO Persona VALUES 
('Juan','Pérez', 'Flores', 'juan.perez@gmail.com', '984562235','10000002','Jr. Los Cedros 456','juanpr', 'mjuanria',10,'CLI',NULL,NULL,'M'),
('Rosa','Mendoza', 'Díaz', 'rosa.mendoza@gmail.com', '984562335','10000003','Calle Las Flores 789','rosagr', 'mrosaia',11,'CLI',NULL,NULL,'F'),
('Carlos','Torres', 'Chávez', 'carlos.torres@gmail.com', '984562435','10000004','Av. Los Pinos 1011','carlosgr', 'mcarlosa',12,'CLI',NULL,NULL,'M'),
('Patricia','Huamaní', 'Álvarez', 'patricia.huamani@gmail.com', '984862135','10000005','Jr. Las Rosas 1213','patriciagr', 'mpatriciaa',13,'CLI',NULL,NULL,'F'),
('Luis','Sánchez', 'Cruz', 'luis.sanchez@gmail.com', '987456235','10000006','Calle Los Álamos 1415','luisgr', 'mluisr',14,'CLI',NULL,NULL,'M'),
('Ana','Castillo', 'Villanueva', 'ana.castillo@gmail.com', '994562135','10000007','Av. Los Cerezos 1617','anagr', 'anarg',15,'CLI',NULL,NULL,'F'),
('Patricia','Alvarez', 'Valencia', 'patricia.alvarez@gmail.com', '987562135','10000008','r. Las Palmeras 1819','patriciagr', 'patriciarmg',3,'CLI',NULL,NULL,'F'),
('Eduardo','Cruz', 'Salas', 'eduardo.cruz@gmail.com', '984962135','10000009','Calle Los Olivos 2021','eduardogr', 'eeduer',16,'CLI',NULL,NULL,'M'),
('Sandra','Valencia', 'León', 'sandra.valencia@gmail.com', '983562135','10000010','Av. Las Acacias 2223','sandragr', 'sandragr',17,'CLI',NULL,NULL,'F');
INSERT INTO Persona VALUES 
('María','Gonzales', 'Ramírez', 'pilar.gonzales@gmail.com', '989962135','1001','Av. Los Laureles 102','pilargr', 'pilargr',5,'GCM',NULL,'CM','F'),
('Juan','Quispe', 'Villaverde', 'juan.quispe@gmail.com', '997962135','1002','Jr. Los Cedros 425','juanq', 'juanq',1,'GVT',NULL,'VT','M'),
('Camila','Hidalgo', 'Laureano', 'camila.hidalgo@gmail.com', '949962135','1003','Calle Las Flores 748','camilah', 'camilah',2,'GDT',NULL,'DT','F'),
('Steven','Gutierrez', 'Calderon', 'steven.gutierrez@gmail.com', '939962135','1004','Av. Los Pinos 1021','steveng', 'steveng',3,'GFZ',NULL,'FZ','M'),
('Ariana','Del Rio', 'Rojas', 'ariana.delrio@gmail.com', '929962135','1005','Jr. Las Rosas 1022','ariand', 'ariand',4,'GMK',10,'MK','F'),
('Manuel','Ramirez', 'Herberth', 'manuel.ramirez@gmail.com', '919962135','1006','Calle Los Álamos 1082','manuelr', 'manuelr',5,'GAM',NULL,'AM','M'),
('Sandra','Calderon', 'Sosaya', 'sandra.calderon@gmail.com', '990962135','1007','Av. Las Acacias 2102','sandrac', 'sandrac',6,'GCR',NULL,'CRM','F');
select * from Persona;

--Cupón
INSERT INTO Cupón (Id_cupón, fecha_ini_cup, fecha_fin_cup, desc_cup, esta_activo)
VALUES
    (1000, '2022-01-01', '2122-02-01', null, TRUE),
    (1001, '2022-02-01', '2022-03-01', 0.20, FALSE),
    (1002, '2022-03-01', '2022-04-01', 0.50, FALSE),
    (1003, '2022-04-01', '2022-05-01', 0.40, FALSE),
    (1004, '2022-05-01', '2022-06-01', 0.40, FALSE),
    (1005, '2022-06-01', '2022-07-01', 0.30, FALSE),
    (1006, '2022-07-01', '2022-08-01', 0.25, FALSE),
    (1007, '2022-08-01', '2022-09-01', 0.20, FALSE),
    (1008, '2022-09-01', '2022-10-01', 0.15, FALSE),
    (1009, '2022-10-01', '2022-11-01', 0.20, FALSE);
select * from Cupón;

-- Campaña
INSERT INTO Campaña (Id_campaña, fecha_ini, fecha_fin, canal_publi, dir_url, modalidad, archivo, des_campaña, Id_equipo_mark, Id_gest_mark)
VALUES
    (100000, '2022-01-04', '2022-01-11', 'instagram', 'https://linktr.ee/Migni_Store', 'native ad', 'https://marketingmigni.com/campaña100000.mp4', null, 10, 1002),
    (100001, '2022-01-11', '2022-01-18', 'facebook', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100001.jpg', 0.25, 12, 1002),
    (100002, '2022-01-18', '2022-02-18', 'marketplace', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100002.jpg', 0.10, 11, 1002),
    (100003, '2022-02-18', '2022-02-25', 'twitter', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100003.jpg', 0.15, 16, 1002),
    (100004, '2022-02-25', '2022-03-25', 'facebook', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100004.mp4', 0.25, 17, 1002),
    (100005, '2022-03-25', '2022-04-01', 'marketplace', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100005.jpg', 0.30, 17, 1002),
    (100006, '2022-04-01', '2022-04-08', 'marketplace', 'https://linktr.ee/Migni_Store', 'post', 'https://marketingmigni.com/campaña100006.jpg', 0.30, 19, 1002),
    (100007, '2022-04-08', '2022-05-08', 'instagram', 'https://linktr.ee/Migni_Store', 'native ad', 'https://marketingmigni.com/campaña100007.jpg', 0.10, 18, 1002),
    (100008, '2022-05-08', '2022-06-08', 'instagram', 'https://linktr.ee/Migni_Store', 'native ad', 'https://marketingmigni.com/campaña100008.jpg', 0.25, 14, 1002),
    (100009, '2022-06-08', '2022-06-15', 'youtube', 'https://linktr.ee/Migni_Store', 'video ad', 'https://marketingmigni.com/campaña100009.mp4', 0.35, 11, 1002);
select * from Campaña;

--Producto
insert into Producto values (1, 'Cuaderno clear blinder', 'Cuaderno A4 tipo blinder con 60 hojas rayadas', 0, 100, 25.0, 1, 1000,100000);
insert into Producto values (2, 'Bear Notebook B5', 'Cuaderno B5 tipo blinder con 60 hojas rayadas', 0, 100,20.0, 1, 1001,100001);
insert into Producto values (3, 'Diamond pen', 'Incluye protector, Tinta:negra', 0, 100,6.5, 2, 1002,100002);
insert into Producto values (4, 'Releaf Primer', 'Primer de Italia deluxe', 0, 100,28.5, 5, 1003,100003);
insert into Producto values (5, 'Corrector HD Pro', 'Corrector de Italia deluxe, con cobertura media a graduable', 0, 100, 16.0, 10, 1004,100004);
insert into Producto values (6, 'Super Stay Matter Maybelline', 'Labial con efecto matte instransferible por 24h', 0, 100, 45.0, 8, 1005,100005);
insert into Producto values (7, 'Profesional Silicón PROSA', 'Mascara de pestañas que aporta demasiada longitud ', 0, 100, 30.0, 11, 1006,100006);
insert into Producto values (8, 'Gliterally', 'Delineador con glitter extra brillante de Beauty creation', 0, 100,22.0, 6, 1007,100007);
insert into Producto values (9, 'Ultrafine lipliner', 'Delineadores de labios de Italia deluxe', 0, 100, 6.0, 8, 1008,100008);
insert into Producto values (10, 'Fill in thirsty gloss', 'Gloss de Italia deluxe con efecto mentolado', 0, 100, 18.0, 8, 1009,100009);
select * from Producto

--cotizacionxproducto
insert into CotizaciónxProducto values (12, 10, 3);
insert into CotizaciónxProducto values (11, 10, 2);
insert into CotizaciónxProducto values (8, 10, 1);
select * from CotizaciónxProducto

--proveedorxproducto
insert into ProveedorxProducto values (4.8, '3','20603302151');
insert into ProveedorxProducto values (6.0, '2', '20603302151');
insert into ProveedorxProducto values (11.0, '1', '20603302151');
select * from ProveedorxProducto

--Tipos_pago 
INSERT INTO Tipos_pago (id_tipo_pago, nombre_tipo, nro_tarjeta) VALUES
(11, 'Tarjeta de crédito', '12345678'),
(12, 'Tarjeta de débito', '98765432'),
(13, 'Efectivo', NULL),
(14, 'A contra entrega', '11112222'),
(15, 'Yape/Plin', NULL);
select * from Tipos_pago;

--Detalle_pago
INSERT INTO Detalle_pago (Id_detalle_pago, fecha_pago, hora_pago, id_tipo_pago) VALUES
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
INSERT INTO Venta (Id_venta, id_persona, monto_final, Id_detalle_pago) VALUES
(1234, '10000001', 50.0, 2001),
(5678, '10000002', 20.0, 2002),
(9012, '10000003', 6.5, 2003),
(3456, '10000004', 114.0, 2004),
(7890, '10000005', 112.0, 2005),
(2345, '10000006', 45.0, 2006),
(6789, '10000007', 60.0, 2007),
(123, '10000008', 22.0, 2008),
(4567, '10000009', 18.0, 2009),
(8901, '10000010', 72.0, 2010);
select * from Venta;
--VentaXProd
INSERT INTO VentaXProd (id_prod_venta, Id_venta, id_producto, cant_prod, monto_total) VALUES
(12341, 1234, 1, 2, 50.0),
(56782, 5678, 2, 1, 20.0),
(90123, 9012, 3, 1, 6.5),
(34564, 3456, 4, 4, 114.0),
(78905, 7890, 5, 7, 112.0),
(23456, 2345, 6, 1, 45.0),
(67897, 6789, 7, 2, 60.0),
(1238, 123, 8, 1, 22.0),
(45679, 4567, 9, 3, 18.0),
(890110, 8901, 10, 4, 72.0);
select * from VentaXProd;

--Tipo_est_pedido
INSERT INTO Tipo_est_pedido VALUES ('E', 'ENTREGADO'), ('P', 'PENDIENTE');
select * from Tipo_est_pedido;

--Pedido
INSERT INTO Pedido (id_pedido, fecha_entrega, est_pedido, hora_entrega, id_ruta ,id_persona ,id_repartidor,id_venta) VALUES 
(1215,'8/1/2022','E','12:30', 2,'10000001',9561677,1234),
(1365,'19/04/2022','E','12:30', 3,'10000002',9561677,5678),
(1549,'27/08/2022','E','12:30', 4,'10000003',9561677,9012),
(1816,'9/11/2022','E','12:30', 5,'10000004',9561677,3456),
(2465,'8/02/2023','E','12:30', 6,'10000005',7523677,7890),
(2964,'25/06/2023','E','12:30', 7,'10000006',7523677,2345),
(3415,'15/09/2023','E','12:30', 8,'10000007',7851678,6789),
(4315,'29/12/2023','E','12:30', 9,'10000008',9561677,123),
(4516,'11/3/2024','E','12:30', 10,'10000009',7523677,4567),
(4585,'23/07/2024','P','12:30', 11,'10000010',7523677,8901);
select * from Pedido;
```

# 5. Videos individuales
[Quispe Mitma Cesar](../../06.Videos_Individuales/VideosPC2/Quispe_Mitma_Cesar_Fernando-VideoIndividual.md)

[![Video](https://img.youtube.com/vi/ohOmEIjYwds/0.jpg)](https://www.youtube.com/watch?v=ohOmEIjYwds)

[Montes Lozano Diego](../../06.Videos_Individuales/VideosPC2/Montes_Lozano_Diego_Martín_VideoIndividual.md)

# 6. ENTREVISTA
## Link
- [Entrevista1](https://drive.google.com/drive/folders/1TTn2h-Z3sSz5ciMGMDi5mqIKiaWJ94f7?usp=sharing)
[![Video](https://img.youtube.com/vi/9kZT8WSCRc4/0.jpg)](https://www.youtube.com/watch?v=9kZT8WSCRc4)
