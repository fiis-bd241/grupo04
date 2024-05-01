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
  cant_emp INT NOT NULL,
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
  Tiempo_prom  NOT NULL,
  medio_transporte VARCHAR(100) NOT NULL,
  PRIMARY KEY (Id_ruta)
);

CREATE TABLE Pregunta
(
  Id_pregunta INT NOT NULL,
  pregunta VARCHAR(200) NOT NULL,
  tipo_preg VARCHAR(100) NOT NULL,
  PRIMARY KEY (Id_pregunta)
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

CREATE TABLE Tipo_est_formulario
(
  Id_est_formulario VARCHAR(100) NOT NULL,
  est_formulario VARCHAR(100) NOT NULL,
  PRIMARY KEY (Id_est_formulario)
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
  desc_cup FLOAT NOT NULL,
  esta_activo BOOLEAN NOT NULL NOT NULL,
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
  des_campaña FLOAT NOT NULL,
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

CREATE TABLE Formulario
(
  Id_formulario INT NOT NULL,
  descrip_formulario VARCHAR(500) NOT NULL,
  fecha_creacion DATE NOT NULL,
  Id_persona INT NOT NULL,
  Id_est_formulario VARCHAR(100) NOT NULL,
  PRIMARY KEY (Id_formulario),
  FOREIGN KEY (Id_persona) REFERENCES Persona(Id_persona),
  FOREIGN KEY (Id_est_formulario) REFERENCES Tipo_est_formulario(Id_est_formulario)
);

CREATE TABLE Respuesta
(
  Id_respuesta INT NOT NULL,
  respuesta VARCHAR(300) NOT NULL,
  Id_formulario INT NOT NULL,
  PRIMARY KEY (Id_respuesta),
  FOREIGN KEY (Id_formulario) REFERENCES Formulario(Id_formulario)
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

CREATE TABLE FormularioxPregunta
(
  Id_formulario INT NOT NULL,
  Id_pregunta INT NOT NULL,
  PRIMARY KEY (Id_formulario, Id_pregunta),
  FOREIGN KEY (Id_formulario) REFERENCES Formulario(Id_formulario),
  FOREIGN KEY (Id_pregunta) REFERENCES Pregunta(Id_pregunta)
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

CREATE TABLE PreguntaxRespuesta
(
  Id_pregunta INT NOT NULL,
  Id_respuesta INT NOT NULL,
  PRIMARY KEY (Id_pregunta, Id_respuesta),
  FOREIGN KEY (Id_pregunta) REFERENCES Pregunta(Id_pregunta),
  FOREIGN KEY (Id_respuesta) REFERENCES Respuesta(Id_respuesta)
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
  descuento FLOAT NOT NULL,
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

CREATE TABLE Comentario
(
  Id_comentario INT NOT NULL,
  descrip_comentario VARCHAR(200) NOT NULL,
  fecha_comentario DATE NOT NULL,
  hora_comentario VARCHAR(10) NOT NULL,
  id_producto INT NOT NULL,
  Id_persona INT NOT NULL,
  PRIMARY KEY (Id_comentario),
  FOREIGN KEY (id_producto) REFERENCES Producto(id_producto),
  FOREIGN KEY (Id_persona) REFERENCES Persona(Id_persona)
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

CREATE TABLE Pedido
(
  Id_pedido INT NOT NULL,
  fecha_entrega DATE NOT NULL,
  est_pedido VARCHAR(100) NOT NULL,
  hora_entrega INT NOT NULL,
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
```

# 4. Poblamiento inicial de datos

# 5. Videos individuales


