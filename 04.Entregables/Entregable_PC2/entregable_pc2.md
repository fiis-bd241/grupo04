# 1. Modelo Conceptual

# 2. Modelamiento Lógico

## 2.1 Módelo Lógico

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

Entidad: Tipo_est_cotizacion

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


# 3. Creación de tablas

# 4. Poblamiento inicial de datos

# 5. Videos individuales


