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


# 3. Creación de tablas

# 4. Poblamiento inicial de datos

# 5. Videos individuales


