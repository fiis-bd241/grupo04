# 1. Ajustes al Modelamiento
## Módulo de Compras
El módulo no fue alterado, se mantuvieron las tablas ya presentadas anteriormente de Proveedor, Cotizacion, CotizacionxProducto, tipo_est_proveedor, tipo_est_cotizacion estas serán las tablas definitivas que se usaran en el módulo de compras.

## Módulo de Marketing
Se agregaron más tablas en coordinación con el módulo de marketing, se hicieron cambios en el modelo conceptual y lógico, afectando a las tablas y consecuentemente al códigl generador de las tablas en nuestra base de datos (Postgresql), se trastocaron funcionamientos en el figma y se agregaron funciones faltantes para el equipo de marketing y el gestor de marketing.

## Módulo de Ventas
Se configuro una lookup table para identificar a los diferentes tipos de pago que puede realizar el cliente. Estos pagos pueden realizarse mediante tarjetas de crédito o débito, efectivo,a contraentrega, yaple/plin. Por lo demas,se mantienen las relaciones y tablas que se vieron en anteriores informes: Venta, VentaxProd,detalle_pago(se le agregó el atributo nro_tarjeta y puede ser null en casos de que que el pago sea en efectivo), tipos_pago(lookup table)

![image](MODLOG2.png)

## Módulo de Distribucion
El módulo tuvo que alterarse,los pedidos se reasignan por zonas y cada repartidor entrega en una zona especifica,se ubica la ruta por el distrito del cliente.El gerente de distribucion aun sigue asignando los repartidores pero se reducen la cantidad disponible al trabajar solo por zonas.


## Módulo de Almacén
Se configuraron y se agregaron tablas para poder identificar mejor las categorías, los colores, las clases de cada producto (como sub productos), la marca; para poder filtrar con palabras claves y agilizar la búsqueda y hacerla más general, se agregaron sub tipos de productos para poder compararlo con los sub tipos existentes en el mercado y así se pueda alcanzar a más necesidades de clientes con productos nuevos. Se agregaron tablas para saber la ubicación de cada producto y calcular el espacio disponible para nuevas compras. Modificar la tabla inventario para tener en tiempo real (con una variable Timestamp) el stock disponible y el área de ventas puede ofrecer el stock real. Y se agregó una tabla imágenes para poder saber la cantidad aproximada de memoria, en la carga de imágenes, que se utilizará en el aplicativo.

![image](AlmacenER.png)
![image](AlmacenRS.png) 

## Módulo de Finanzas
Se modificó tanto el modelo conceptual con el modelo E-R ya que para la Entidad Item de Estados de Resultados se tiene un atributo que es compuesto que se refiere al tipo de Estado de Resultado en el que se considera ademas del nombre del tipo se considera que tipo de operación será en el Estado de Resultados ya que las Utilidades harán operaciones compuestas mientras que ventas, costo de ventas serán operaciones simples además se tiene un atributo que es tipo_valor que hace referencia a que puede sumar o restar que se representa con positivo o negativo respectivamente.

![image](https://github.com/fiis-bd241/grupo04/blob/main/04.Entregables/Entregable_PC3/Pantallas/Modelo%20Conceptual.PNG) 

Por otro lado, en el modelo E-R se modificaron los atributos nuevos considerados del modelo E-R además que se normalizó hasta la 3 f, entonces tenemos para factura dos atributos nuevos que son el estado, tipo_factura ya que era importane considerar que tipo de factura es y el estado que es si lo ha pagado, si falta pagar o si no pagó nada por lo que se consideraron tablas que son Estado, Tipo_Factura además para los atributos del Estado de Resultados se consideró dos tablas que indican el tipo_valor con valores si es negativo o positivo y el tipo_operacion si es operación compuesta o simple.
![image](https://github.com/fiis-bd241/grupo04/blob/main/04.Entregables/Entregable_PC3/Pantallas/ModeloE-R.PNG) 



# 2. Asignación de Códigos por Requerimientos y Prototipos de Interfaces de Usuario

## 2.1. Codificacion de Requerimientos
### 2.1.1. Modulo de Compras

| Código | R001  |
|----------|----------|
|Nombre  |Visualizar proveedores|
|Objetivo  |Permitir a los gestores poder visualizar los proveedores que estan registrados.|
| Descripción   | Proceso mediante el cual los gestores pueden acceder a la visualización de todos los proveedores dentro de los registros|
| Actor primario    | Gestor de compras |
| Actor secundario    | -  |
| Precondiciones    | El proveedor ya debe haber contactado con la empresa previamente |

| Código | R002  |
|----------|----------|
|Nombre  |Añadir proveedor|
|Objetivo  |Permitir que el Gestor de compras pueda añadir proveedores a la página de Migni Store|
| Descripción   | Proceso de registro de proveedores en la aplicación, con datos de empresa ya sea ruc, razon social, dirección, telefono, rubro, correo y sitio web|
| Actor primario    | Gestor de compras |
| Actor secundario    | -  |
| Precondiciones    | El proveedor ya debe haber contactado con la empresa previamente |

| Código | R003  |
|----------|----------|
|Nombre  |Detalle proveedores|
|Objetivo  |Permitir a los gestores poder acceder y visualizar de un proveedor específico dentro de los registros|
| Descripción   | Proceso mediante el cual los gestores pueden acceder a la visualización de un proveedor específico dentro de los registros |
| Actor primario    | Gestor de compras|
| Actor secundario    | -  |
| Precondiciones    | El proveedor ya debe haber contactado con la empresa previamente |

| Código | R004  |
|----------|----------|
|Nombre  |Historial cotizaciones|
| Objetivo  |Permitir a los gestores poder acceder y visualizar las cotizaciones realizadas por un proveedor|
| Descripción   |Proceso mediante el cual los gestores pueden acceder a la visualización de las cotizaciones, con sus respectivos datos|
| Actor primario    | Gestor de compras|
| Actor secundario    | -  |
| Precondiciones    | El proveedor ya debe haber contactado con la empresa previamente |

| Código | R005  |
|----------|----------|
|Nombre  |Detalle Cotizaciones|
|Objetivo  |Permitir a los gestores poder acceder y visualizar de una cotizacion específica dentro del historial|
| Descripción   | Proceso mediante el cual los gestores pueden acceder a la visualización de una cotizacion específica dentro del historial|
| Actor primario    | Gestor de compras|
| Actor secundario    | -  |
| Precondiciones    | El proveedor ya debe haber contactado con la empresa previamente|

| Código | R006  |
|----------|----------|
|Nombre  |Aceptar/Rechazar cotizacion del proveedor|
|Objetivo  |Permitir que el gestor de compras pueda aceptar o rechazar la cotizacion realizada por el proveedor |
| Descripción   | Proceso en el cual se puede visualizar la cotizacion, con estado pendiente y aceptar o rechazar dicha cotizacion|
| Actor primario    | Gestor de compras |
| Actor secundario    | -  |
| Precondiciones    | El proveedor debe haber sido registrado por el gestor de compras |

### 2.1.2. Módulo de Marketing

| Código | R007  |
|----------|----------|
|Nombre  | Proponer Campaña |
| Objetivo | <p align="left"> Permitir que el Equipo de marketing proponga una campaña.</p> | 
| Descripción | Proceso mediante el cual el Equipo de marketing puede proponer una campaña para su posterior revisión de parte del Gestor de marketing. | 
| Actor primario   | Equipo de marketing | 
|Actor secundario| Gestor de marketing |
|Precondiciones | - |

| Código | R008  |
|----------|----------|
|Nombre  | Revisar campañas |
| Objetivo | <p align="left"> Permitir que el Gestor de marketing revise la campaña brindada por el equipo de marketing correspondiente.</p> | 
| Descripción | Proceso mediante el cual el Gestor de marketing puede revisar las campañas propuestas por el equipo de marketing, su criterio definirá si la campaña será aceptada o rechazada, en el caso de ser rechazada se enviarán las observaciones al equipo de marketing.  | 
| Actor primario   | Gestor de marketing | 
|Actor secundario| Equipo de marketing |
|Precondiciones | El equipo de marketing debe haber propuesto una campaña. |

| Código | R009  |
|----------|----------|
|Nombre  | Observar campaña |
| Objetivo | <p align="left"> Enviar observaciones de una campaña es específico al equipo de marketing que la diseño.</p> | 
| Descripción | Proceso mediante el cual el Gestor de marketing envía las observaciones de campañas propuestas al equipo de amrketing correspondiente. | 
| Actor primario   | Gestor de marketing | 
|Actor secundario| Equipo de marketing |
|Precondiciones | El equipo de marketing debe haber propuesto una campaña |

| Código | R010  |
|----------|----------|
|Nombre  | Atender Observaciones |
| Objetivo | <p align="left"> Permitir que el Equipo de marketing realice las correcciones de una campaña.</p> | 
| Descripción | Proceso mediante el cual el Equipo de marketing puede realizar las correcciones de campañas que les corresponda, siguiendo las observaciones realizadas por el Gestor de marketing. | 
| Actor primario   | Equipo de marketing | 
|Actor secundario| Gestor de marketing |
|Precondiciones | El Gestor de marketing debe haber realizado una observación a la campaña. |

| Código | R011  |
|----------|----------|
|Nombre  | Editar campañas vigentes |
| Objetivo | <p align="left"> Permitir que el Gestor de marketing edite las campañas vigentes.</p> | 
| Descripción | Proceso mediante el cual el Gestor de marketing puede editar las campañas que ya están vigentes, se limita a los datos necesarios y posibles de editar. | 
| Actor primario   | Gestor de marketing | 
|Actor secundario| - |
|Precondiciones | Debe existir al menos una campaña vigente. |

### 2.1.3. Módulo de Ventas

| Código | R012 |
|----------|----------|
|Nombre  | Ver Catálogo de Productos|
| Objetivo | <p align="left"> Permitir que el cliente visualice el catálogo completo de productos disponibles en la plataforma de ventas.</p> | 
| Descripción |  Facilitar al cliente la exploración de todos los productos disponibles para su compra, mostrando información básica de cada producto. | 
| Actor primario   | Cliente | 
|Actor secundario| Plataforma de Ventas|
|Precondiciones |El cliente ha accedido a la plataforma de ventas|

| Código | R013 |
|----------|----------|
|Nombre  | Ver Detalle de Producto desde el Catálogo|
| Objetivo | <p align="left"> Permitir que el cliente acceda a una vista detallada de un producto mientras navega por el catálogo en la plataforma de ventas.</p>| 
| Descripción | Facilitar al cliente la visualización de información detallada sobre un producto específico mientras navega por el catálogo de la plataforma de ventas, brindando detalles como descripción, código, marca, tipo de producto, precio y disponibilidad en stock.| 
| Actor primario   | Cliente | 
|Actor secundario| Plataforma de Ventas|
|Precondiciones |El cliente ha iniciado sesión en la plataforma de ventas |

| Código | R014 |
|----------|----------|
|Nombre  | Realizar una compra (carrito de compras)|
| Objetivo | <p align="left"> Permitir que el cliente realice una compra en la plataforma de ventas y pueda cambiar su dirección de envío antes de finalizar la transacción si lo desea.</p> | 
| Descripción | Facilitar el proceso de compra para el cliente, desde la selección de productos hasta la finalización de la transacción. | 
| Actor primario   | Cliente | 
|Actor secundario| Plataforma de Ventas|
|Precondiciones |El cliente ha accedido a la plataforma de ventas y ha agregado productos al carrito de compras. |

| Código | R015 |
|----------|----------|
|Nombre  | Elegir Método de Pago|
| Objetivo | <p align="left"> Permitir que el cliente elija el método de pago al realizar una compra en la plataforma de ventas.</p> | 
| Descripción | Facilitar al cliente la selección de su método de pago preferido durante el proceso de compra, limitando las opciones a tarjeta de débito o crédito. | 
| Actor primario   | Cliente | 
|Actor secundario| Plataforma de Ventas|
|Precondiciones |El cliente ha accedido a la plataforma de ventas y ha agregado productos al carrito de compras|

| Código | R016 |
|----------|----------|
|Nombre  | Ver Detalles del Producto|
| Objetivo | <p align="left"> Permitir que el cliente acceda a una vista detallada del producto en la plataforma de ventas después de elegir su método de pago correspondiente.</p> | 
| Descripción | Facilitar al cliente la visualización de información detallada sobre un producto seleccionado. | 
| Actor primario   | Cliente | 
|Actor secundario| Plataforma de Ventas|
|Precondiciones |El cliente ha iniciado el proceso de pago y ha ingresado los datos de su tarjeta|

| Código | R017 |
|----------|----------|
|Nombre  | Añadir Nueva Dirección de Envío|
| Objetivo | <p align="left"> Permitir que el cliente agregue una nueva dirección de envío para recibir sus productos comprados en la plataforma de ventas.</p> | 
| Descripción | Facilitar al cliente la posibilidad de registrar una dirección adicional donde desee recibir sus pedidos, aumentando la flexibilidad en la entrega de productos. | 
| Actor primario   | Cliente | 
|Actor secundario| Plataforma de Ventas|
|Precondiciones |El cliente ha iniciado sesión en su cuenta en la plataforma de ventas|


| Código | R018 |
|----------|----------|
|Nombre  | Consultar Historial de Ventas de la Empresa|
| Objetivo | <p align="left"> Permitir que el gestor acceda al historial de ventas de la empresa en la plataforma de ventas.</p> | 
| Descripción | Facilitar al gestor el acceso a información detallada sobre las ventas realizadas por la empresa, incluyendo datos como fechas, productos vendidos, montos y clientes. | 
| Actor primario   | Gestor de Ventas | 
|Actor secundario| Plataforma de Ventas|
|Precondiciones |El gestor ha accedido a la plataforma de ventas|


| Código | R019 |
|----------|----------|
|Nombre  | Consultar Historial de ventas de algun cliente|
| Objetivo | <p align="left"> Permitir que el gestor acceda al historial de ventas del cliente para realizar seguimientos.</p> | 
| Descripción | Facilitar al gestor el acceso a información detallada sobre las ventas realizadas por el cliente. | 
| Actor primario   | Gestor de Ventas | 
|Actor secundario| Plataforma de Ventas|
|Precondiciones |El gestor ha accedido a la plataforma de ventas|

### 2.1.4. Modulo de distribucion

| Código | R020  |
|----------|----------|
|Nombre  |Visualizar compras|
|Objetivo  |Permitir a los clientes poder ver sus compras y entregas pendientes.|
| Descripción   | Proceso mediante el cual los clientes pueden acceder a la visualización de todas sus compras sin entregar|
| Actor primario    | Cliente |
| Actor secundario    | -  |
| Precondiciones    | El cliente debe haber realizado una compra previamente |

| Código | R021  |
|----------|----------|
|Nombre  |Establecer fecha de la entrega|
|Objetivo  |Permitir a los clientes definir la fecha que desean que se le entregue su compra.|
| Descripción   | Proceso mediante el cual los clientes pueden establecer la fecha de su entrega y ademas se crea el pedido|
| Actor primario    | Cliente |
| Actor secundario    | -  |
| Precondiciones    | El cliente debe haber realizado una compra previamente |

| Código | R022  |
|----------|----------|
|Nombre  |Visualizar pedidos|
|Objetivo  |Permitir al gestor de distribucion visualizar los pedidos pendientes.|
| Descripción   | Proceso mediante el cual el gestor de distribucion pueden ver los pedidos que se encuentran pendientes|
| Actor primario    | Gestor de distribucion |
| Actor secundario    | -  |
| Precondiciones    | El cliente debe haber establecido una fecha de entrega previamente |

| Código | R023  |
|----------|----------|
|Nombre  |Asignar|
|Objetivo  |Permitir al gestor de distribucion asignar un repartidor a un pedido  y una ruta segun la zona establecida.|
| Descripción   | Proceso mediante el cual el gestor de distribucion pueden establecer los repartidores y las rutas a cada pedido|
| Actor primario    | Gestor de distribucion |
| Actor secundario    | -  |
| Precondiciones    | El cliente debe haber establecido una fecha de entrega previamente y los pedidos debe estar pendientes |

| Código | R024  |
|----------|----------|
|Nombre  |Visualizar el historial de pedidos|
|Objetivo  |Permitir al gestor de distribucion visualizar todas los pedidos y entregas realizadas.|
| Descripción   | Proceso mediante el cual el gestor de distribucion pueden visualizar todos los pedidos y entregas realizadas en un lapso de tiempo|
| Actor primario    | Gestor de distribucion |
| Actor secundario    | -  |
| Precondiciones    | Deben haber existido entregas realizadas con exito |

| Código | R025  |
|----------|----------|
|Nombre  |Visualizar las entregas pendientes|
|Objetivo  |Permitir al repartidor visualizar todos los pedidos pendientes.|
| Descripción   | Proceso mediante el cual el repartidor pueden visualizar todos los pedidos que se encuentra aun pendientes|
| Actor primario    | Repartidor |
| Actor secundario    | -  |
| Precondiciones    | El repartidor se le debe haber asignado pedidos |

| Código | R026  |
|----------|----------|
|Nombre  |Entregado|
|Objetivo  |Permitir al repartidor confirmar que la entrega se realizó con exito.|
| Descripción   | Proceso el cual el repartidor confirma que ha realizado la entrega y actualiza el estado del pedido |
| Actor primario    | Repartidor |
| Actor secundario    | -  |
| Precondiciones    | El repartidor debe haber aceptado el pedido |

| Código | R027  |
|----------|----------|
|Nombre  |Visualizar el historial de pedidos|
|Objetivo  |Permitir al repartidor visualizar sus pedidos y entregas realizadas.|
| Descripción   | Proceso mediante el cual el repartidor puede visualizar todos los sus pedidos y entregas realizadas en un lapso de tiempo|
| Actor primario    | Gestor de distribucion |
| Actor secundario    | -  |
| Precondiciones    | Deben haber existido entregas realizadas con exito |

| Código | R028  |
|----------|----------|
|Nombre  |Ver detalles/ver mas|
|Objetivo  |Permitir al gestor de distribucion y el repartidor ver los detalles del pedido.|
| Descripción   | Proceso mediante el cual el gerente de distribucion y el repartidor pueden visualizar mas detalles acerca del pedido
| Actor primario    | Gestor de distribucion y repartidor |
| Actor secundario    | -  |
| Precondiciones    | Debe existir el pedido, con la fecha establecidad previamente |

### 2.2.5. Módulo de Finanzas

| Código             | R037 |
|--------------------|----------|
| Nombre             | Añadir Factura |
| Objetivo           | Permitir al contador ingresar facturas. |
| Descripción        | PRoceso mediante el contador agrega una factura según la transacciones que tiene la Empresa. |
| Actor primario | Contador |
| Actor secundario | - |
| *Precondiciones* | - El usuario ha iniciado sesión en el sistema.<br>- El usuario tiene permisos para añadir facturas. |
| *Flujo Alternativo* | - Si hay errores en los datos ingresados, el sistema muestra mensajes de error y permite al usuario corregir la información. |

| Código             | R038 |
|--------------------|------|
| Nombre             | Ver Historial de Facturas |
| Objetivo           | Permitir al contador general y al gerente general consultar el historial de facturas. |
| Descripción        | Proceso mediante el cual se muestra el historial completo de facturas de la empresa. |
| Actor primario     | Contador General, Gerente General |
| Actor secundario   | - |
| *Precondiciones*   | - El usuario ha iniciado sesión en el sistema.<br>- El usuario tiene permisos para ver el historial de facturas. |
| *Flujo Alternativo*| - Si no hay facturas registradas, el sistema muestra un mensaje indicando la ausencia de facturas. |

| Código             | R039 |
|--------------------|------|
| Nombre             | Ver estado de Facturas |
| Objetivo           | Permitir al contador general y al gerente general consultar el estado de las facturas. |
| Descripción        | Proceso mediante el cual se muestra el estado actual de las facturas (pendientes, pagadas, vencidas, etc.). |
| Actor primario     | Contador General, Gerente General |
| Actor secundario   | - |
| *Precondiciones*   | - El usuario ha iniciado sesión en el sistema.<br>- El usuario tiene permisos para ver el estado de las facturas. |
| *Flujo Alternativo*| - Si no hay facturas con el estado seleccionado, el sistema muestra un mensaje indicando la ausencia de facturas en ese estado. |

| Código             | R040 |
|--------------------|------|
| Nombre             | Ver asientos contables |
| Objetivo           | Permitir al contador general y al gerente general consultar los asientos contables. |
| Descripción        | Proceso mediante el cual se muestran los asientos contables registrados en el sistema. |
| Actor primario     | Contador General, Gerente General |
| Actor secundario   | - |
| *Precondiciones*   | - El usuario ha iniciado sesión en el sistema.<br>- El usuario tiene permisos para ver los asientos contables. |
| *Flujo Alternativo*| - Si no hay asientos contables registrados, el sistema muestra un mensaje indicando la ausencia de asientos contables. |

| Código             | R041 |
|--------------------|------|
| Nombre             | Ver estado de resultados |
| Objetivo           | Permitir al contador general y al gerente general consultar el estado de resultados de la empresa. |
| Descripción        | Proceso mediante el cual se muestra el estado de resultados, incluyendo ingresos, gastos y utilidades de la empresa. |
| Actor primario     | Contador General, Gerente General |
| Actor secundario   | - |
| *Precondiciones*   | - El usuario ha iniciado sesión en el sistema.<br>- El usuario tiene permisos para ver el estado de resultados. |
| *Flujo Alternativo*| - Si no hay datos disponibles para el estado de resultados, el sistema muestra un mensaje indicando la ausencia de información. |


### 2.1.5. Modulo de CRM

| Código | R029  |
|----------|----------|
|Nombre  |Agregar comentario usuario|
|Objetivo  |Permite al usuario ingresar un comentario|
| Descripción   | importante recalcar que esta subida de informacion es hecha solo desde que el usuario se registro anteriormente , ademas es relacionado a un producto en especifico
| Actor primario    | usuario|
| Actor secundario    | -  |
| Precondiciones    | debe haber un inicio de sesion anteriormente|


| Código | R030  |
|----------|----------|
|Nombre  |Comentario general|
|Objetivo  |permite a las personas ingresar un comentario|
| Descripción   | este ingreso de informacion a modo de comentario es hecho ingresando informacion personal y referente a un producto en especifico
| Actor primario    |usuario |
| Actor secundario    | -  |
| Precondiciones    | - |


| Código | R031  |
|----------|----------|
|Nombre  |Formularios|
|Objetivo  |Permitir al gestor de CRM enviar formularios a los usuarios |
| Descripción   | Proceso mediante el cual el gestor de CRM entrega los formularios a grupos de usuarios respectivos en el cual califican determinados productos o calidad de servicio entre otros
| Actor primario    | Gestor de CRM
| Actor secundario    | -  |
| Precondiciones    | Debe existir los usuarios registrados con su correo email |

| Código | R032  |
|----------|----------|
|Nombre  |Correos personalizados|
|Objetivo  |Permitir al gestor de CRM enviar correos personalizados |
| Descripción   | Proceso mediante el cual el gestor de CRM informa a los usuarios sobre los productos , pudiendo entregar determinados cupones que el area de Marketing asigno
| Actor primario    | Gestor de CRM |
| Actor secundario    | -  |
| Precondiciones    | Debe existir los usuarios registrados con su correo email|

| Código | R033  |
|----------|----------|
|Nombre  |Registro de llamadas |
|Objetivo  |Permitir al gestor de CRM poder atender determinadas llamadas que no han sido respondidas , para evitar la salida de potenciales compradores |
| Descripción   | Proceso mediante el gestor de CRM  puede atender llamadas que los de venta no han podido responder 
| Actor primario    | Gestor de CRM |
| Actor secundario    | Gestor de ventas  |
| Precondiciones    | Debe existir un registro de llamadas |

| Código | R034  |
|----------|----------|
|Nombre  |Clasificacion de comentarios|
|Objetivo  |Permitir al gestor de CRM poder clasificar comentarios|
| Descripción   | Proceso mediante el cual el gestor de CRM clasifica sus potenciales clientes , haciendo que tenga una venta asegurada o los cuales estan aprobados a un seguimientos por record de compras, asi como comentarios SPAM
| Actor primario    | Gestor de CRM |
| Actor secundario    | -  |
| Precondiciones    |debe existir un registro de usuarios ademas de sus respectivos comentarios |

| Código | R035  |
|----------|----------|
|Nombre  |Dashboards y reportes|
|Objetivo  |Permitir al gestor de CRM poder orientarse |
| Descripción   | Proceso mediante el cual el gestor de CRM hacer analisis , se puede orientar para ofrecer determinado producto para incentivar a su compra o para poder darle mas visibilidad 
| Actor primario    | Gestor de CRM |
| Actor secundario    | -  |
| Precondiciones    | Debe existir la carga de informacion de los usuarios y ventas |

| Código | R036  |
|----------|----------|
|Nombre  |Pantalla de inicio|
|Objetivo  |Permitir al gestor de CRM localizar los diferentes modulos|
| Descripción   | Es la pantalla de inicio el cual se visualiza todas las opciones que puede realizar el gestor de CRM , asi como un pequeño modulo donde puede ver sus dashboards hechos y cargados 
| Actor primario    | Gestor de CRM |
| Actor secundario    | -  |
| Precondiciones    | Debe existir la cuenta del gestor de CRM ademas para poder visualizar los datos del dashboard haber cargado informacion con anterioridad |

## 2.2. Codificación de prototipos de interfaz
### 2.2.1. Modulo de Compras

| Código Interfaz | I001 |
|----------|----------|
|Imagen interfaz|![image](Pantallas/ModCompras/MP6-.png)|

| Código Interfaz | I002 |
|----------|----------|
|Imagen interfaz|![image](Pantallas/ModCompras/MP1.png)|

| Código Interfaz | I003  |
|----------|----------|
|Imagen interfaz|![image](Pantallas/ModCompras/MP2.png)|

| Código Interfaz | I004  |
|----------|----------|
|Imagen interfaz|![image](Pantallas/ModCompras/MP3-.png)|

| Código Interfaz | I005  |
|----------|----------|
|Imagen interfaz|![image](Pantallas/ModCompras/MP4.png)|

| Código Interfaz | I006  |
|----------|----------|
|Imagen interfaz|![image](Pantallas/ModCompras/MP5.png)|

| Código Interfaz | I007  |
|----------|----------|
|Imagen interfaz|![image](Pantallas/ModMarketing/I007.png)|

| Código Interfaz | I008  |
|----------|----------|
|Imagen interfaz|![image](Pantallas/ModMarketing/I008.png)|

| Código Interfaz | I009  |
|----------|----------|
|Imagen interfaz|![image](Pantallas/ModMarketing/I009.png)|

| Código Interfaz | I010  |
|----------|----------|
|Imagen interfaz|![image](Pantallas/ModMarketing/I010.png)|

| Código Interfaz | I011  |
|----------|----------|
|Imagen interfaz|![image](Pantallas/ModMarketing/I011.png)|

### 2.2.3. Modulo de Ventas

| Código Interfaz | I012 |
|----------|----------|
|Imagen interfaz|![image](Pantallas/ModVentas/catalogo.png)|

| Código Interfaz | I013 |
|----------|----------|
|Imagen interfaz|![image](Pantallas/ModVentas/info_prod_catalogo.png)|

| Código Interfaz | I014 |
|----------|----------|
|Imagen interfaz|![image](Pantallas/ModVentas/carrito.png)|

| Código Interfaz | I015 |
|----------|----------|
|Imagen interfaz|![image](Pantallas/ModVentas/tipo_pago.png)|

| Código Interfaz | I016 |
|----------|----------|
|Imagen interfaz|![image](Pantallas/ModVentas/info_despues_comprar.png)|

| Código Interfaz | I017 |
|----------|----------|
|Imagen interfaz|![image](Pantallas/ModVentas/cambio_direccion.png)|

| Código Interfaz | I018 |
|----------|----------|
|Imagen interfaz|![image](Pantallas/ModVentas/historial_ventas_gestor.png)|

| Código Interfaz | I018 |
|----------|----------|
|Imagen interfaz|![image](Pantallas/ModVentas/historial_cliente.png)|

### 2.2.4. Modulo de distribucion

| Código Interfaz | I020 |
|----------|----------|
|Imagen interfaz|![image](Pantallas/ModDistribucion/I0019.png)|

| Código Interfaz | I021 |
|----------|----------|
|Imagen interfaz|![image](Pantallas/ModDistribucion/I0020.png)|

| Código Interfaz | I022 |
|----------|----------|
|Imagen interfaz|![image](Pantallas/ModDistribucion/I0021.png)|

| Código Interfaz | I023 |
|----------|----------|
|Imagen interfaz|![image](Pantallas/ModDistribucion/I0022.png)|

| Código Interfaz | I024 |
|----------|----------|
|Imagen interfaz|![image](Pantallas/ModDistribucion/I0023.png)|

| Código Interfaz | I025 |
|----------|----------|
|Imagen interfaz|![image](Pantallas/ModDistribucion/I0024.png)|

| Código Interfaz | I026 |
|----------|----------|
|Imagen interfaz|![image](Pantallas/ModDistribucion/I0025.png)|

| Código Interfaz | I027 |
|----------|----------|
|Imagen interfaz|![image](Pantallas/ModDistribucion/I0026.png)|

| Código Interfaz | I028 |
|----------|----------|
|Imagen interfaz|![image](Pantallas/ModDistribucion/I0027.png)|

### 2.2.5. Modulo de CRM

| Código Interfaz | I029 |
|----------|----------|
|Imagen interfaz|![image](Pantallas/ModCRM/1.png)|

| Código Interfaz | I030 |
|----------|----------|
|Imagen interfaz|![image](Pantallas/ModCRM/2.png)|

| Código Interfaz | I031 |
|----------|----------|
|Imagen interfaz|![image](Pantallas/ModCRM/3.png)|

| Código Interfaz | I032 |
|----------|----------|
|Imagen interfaz|![image](Pantallas/ModCRM/4.png)|

| Código Interfaz | I033 |
|----------|----------|
|Imagen interfaz|![image](Pantallas/ModCRM/5.png)|

| Código Interfaz | I034 |
|----------|----------|
|Imagen interfaz|![image](Pantallas/ModCRM/6.png)|

| Código Interfaz | I035 |
|----------|----------|
|Imagen interfaz|![image](Pantallas/ModCRM/7.png)|

| Código Interfaz | I036 |
|----------|----------|
|Imagen interfaz|![image](Pantallas/ModCRM/8.png)|

### 2.2.6. Modulo de Finanzas
| Código Interfaz | I037 |
|-----------------|------|
|Imagen interfaz|![image](Pantallas/Home_Contador.PNG)|

| Código Interfaz | I038 |
|-----------------|------|
|Imagen interfaz|![image](https://github.com/fiis-bd241/grupo04/blob/main/04.Entregables/Entregable_PC3/Pantallas/Factura%20Estados.PNG)|

| Código Interfaz | I039 |
|-----------------|------|
|Imagen interfaz|![image](https://github.com/fiis-bd241/grupo04/blob/main/04.Entregables/Entregable_PC3/Pantallas/HistorialFactura.PNG)|

| Código Interfaz | I040 |
|-----------------|------|
|Imagen interfaz|![image](https://github.com/fiis-bd241/grupo04/blob/main/04.Entregables/Entregable_PC3/Pantallas/VerFactura.PNG)|

| Código Interfaz | I041 |
|-----------------|------|
|Imagen interfaz|![image](https://github.com/fiis-bd241/grupo04/blob/main/04.Entregables/Entregable_PC3/Pantallas/A%C3%B1adirFactura.PNG)|

| Código Interfaz | I042 |
|-----------------|------|
|Imagen interfaz|![image](https://github.com/fiis-bd241/grupo04/blob/main/04.Entregables/Entregable_PC3/Pantallas/HistorialdeAsientos.PNG)|

| Código Interfaz | I043 |
|-----------------|------|
|Imagen interfaz|![image](https://github.com/fiis-bd241/grupo04/blob/main/04.Entregables/Entregable_PC3/Pantallas/EstadodeResultados.PNG)|



# 3. Sentencias SQL por cada prototipo
## 3.1 Modulo de Compras
### Código Requerimiento : R - 001
### Codigo interfaz : I - 001
### Imagen interfaz : 
![image](Pantallas/ModCompras/MP6-.png)
### Sentecias SQL:
### Eventos: 
* **Pantalla Visualizar Proveedores: Se mostrará todos los proveedores dentro de la empresa con un estado de activo**
```
SELECT razon_social 
FROM proveedor
WHERE id_est_proveedor = 'A'
```

### Código Requerimiento : R - 002
### Codigo interfaz : I - 002
### Imagen interfaz : 
![image](Pantallas/ModCompras/MP1.png)
### Sentecias SQL:
### Eventos: 
* **Boton Añadir Proveedor: Nos permite ingresar los datos de un proveedor para ser guardado en la base de datos** 
```
INSERT INTO proveedor(ruc_proveedor, razon_social, web_proveedor, rubro, direccion, telefono, id_est_proveedor)
VALUES (<1>, <2>, <3>, <4>, <5>, <6>, 'A');
```

### Código Requerimiento : R - 003
### Codigo interfaz : I - 003
### Imagen interfaz : 
![image](Pantallas/ModCompras/MP2.png)
### Sentecias SQL:
### Eventos: 
* **Pantalla Detalle Proveedores: Se mostrará todos los datos de los proveedores activos en la empresa**
```
SELECT ruc_proveedor, razon_social, web_proveedor, rubro, direccion, telefono, id_est_proveedor
FROM proveedor
WHERE ruc_proveedor = <1>;
```

### Código Requerimiento : R - 004
### Codigo interfaz : I - 004
### Imagen interfaz : 
![image](Pantallas/ModCompras/MP3-.png)
### Sentecias SQL:
### Eventos: 
* **Pantalla Historial Cotizaciones: Se mostrará el historial de todas las cotizaciones aceptadas, no aceptadas y pendientes** 
```
SELECT id_cotizacion, id_est_cotizacion, monto_total, ruc_proveedor
FROM cotizacion
WHERE id_cotizacion = <1> OR id_cotizacion = <2> OR id_cotizacion = <3> OR id_cotizacion = <4> OR id_cotizacion = <5> OR id_cotizacion = <6>
```

### Código Requerimiento : R - 005
### Codigo interfaz : I - 005
### Imagen interfaz : 
![image](Pantallas/ModCompras/MP4.png)
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

### Código Requerimiento : R - 006
### Codigo interfaz : I - 006
### Imagen interfaz : 
![image](Pantallas/ModCompras/MP5.png)
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

### Código Requerimiento : R - 007
### Codigo interfaz : I - 007
### Imagen interfaz : 
![image](Pantallas/ModMarketing/I007.png)
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

### Código Requerimiento : R - 008
### Codigo interfaz : I - 008
### Imagen interfaz : 
![image](Pantallas/ModMarketing/I008.png)
### Sentecias SQL:
### Eventos: 
* **Carga de pantalla: La pantalla se llena con los datos correspondientes a la campaña a revisar**
* **Botón Aceptar: No se realizan cambios en las tablas**
* **Botón Rechazar: No se realizan cambios en las tablas, pero se abre la pantalla de envío de observaciones**
```
--CARGA:
SELECT Id_campaña, nom_campaña, fecha_ini, fecha_fin, dir_url, modalidad, archivo, desc_campaña, Id_equipo_mark
FROM Campaña
WHERE Id_campaña = <1>;

SELECT id_producto
FROM CampañaXProd
WHERE Id_campaña = <1>;

SELECT Id_canal
FROM CampañaXCanal
WHERE Id_campaña = <1>;
```

### Código Requerimiento : R - 009
### Codigo interfaz : I - 009
### Imagen interfaz : 
![image](Pantallas/ModMarketing/I009.png)
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

### Código Requerimiento : R - 010
### Codigo interfaz : I - 010
### Imagen interfaz : 
![image](Pantallas/ModMarketing/I010.png)
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

### Código Requerimiento : R - 011
### Codigo interfaz : I - 011
### Imagen interfaz : 
![image](Pantallas/ModMarketing/I011.png)
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
## 3.3 Modulo de Ventas
### Código Requerimiento : R - 012
### Codigo interfaz : I - 012
### Imagen interfaz : 
![image](Pantallas/ModVentas/catalogo.png)
### Sentecias SQL:
### Eventos: 
* **Pantalla Visualizar Catálogo productos: Se mostrará todos los productos al cliente**
```
SELECT id_producto,nombre_producto,precio_unit FROM PRODUCTO;
```

### Código Requerimiento : R - 013
### Codigo interfaz : I - 013
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
### Código Requerimiento : R - 014
### Codigo interfaz : I - 014
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
### Código Requerimiento : R - 015
### Codigo interfaz : I - 015
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
### Código Requerimiento : R - 016
### Codigo interfaz : I - 016
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
### Código Requerimiento : R - 017
### Codigo interfaz : I - 017
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
### Código Requerimiento : R - 018
### Codigo interfaz : I - 018
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

### Código Requerimiento : R - 019
### Codigo interfaz : I - 019
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
## 3.4 Modulo de Distribucion
### Código Requerimiento : R - 020
### Codigo interfaz : I - 020
### Imagen interfaz : 
![image](Pantallas/ModDistribucion/I0019.png)
### Sentecias SQL:
### Eventos: 
* **Pantalla Visualizar compras: Se mostrará todas las compras que ha realizado el cliente con id = <1>**
```
select fecha_pago,hora_pago
from venta 
inner join detalle_pago on venta.id_detalle_pago = detalle_pago.id_detalle_pago
where id_persona = <1>
```
### Código Requerimiento : R - 021
### Codigo interfaz : I - 021
### Imagen interfaz : 
![image](Pantallas/ModDistribucion/I0020.png)
### Sentecias SQL:
### Eventos: 
* **BOTON ACEPTAR : Se registrará la fecha de entrega de la compra con id = <4> y se creara un nuevo registro de pedido con estado P, sabiendo que el id_pedido es incrementable**
```
INSERT INTO pedido (fecha_entrega,id_venta,id_est_pedido)
VALUES (1216,TO_DATE(CONCAT('<3>-', '<2>-', '<1>'), 'YYYY-MM-DD'),<4>,'P');
```
### Código Requerimiento : R - 022
### Codigo interfaz : I - 022
### Imagen interfaz : 
![image](Pantallas/ModDistribucion/I0021.png)
### Sentecias SQL:
### Eventos: 
* **Pantalla Visualizar pedidos: El gestor de distribucion podra visualizar los pedidos pendientes**
```
SELECT pedido.id_venta,pedido.fecha_entrega, persona.CONCAT(nombre, ' ', primer_apell),tipo_est_pedido.estado_pedido
FROM pedido 
INNER JOIN venta ON pedido.id_venta = venta.id_venta
INNER JOIN persona  ON venta.id_persona = persona.id_persona
INNER JOIN tipo_est_pedido ON pedido.id_est_pedido = tipo_est_pedido.id_est_pedido
WHERE id_persona = <1> AND id_est_pedido = 'P';
```
### Código Requerimiento : R - 023
### Codigo interfaz : I - 023
### Imagen interfaz : 
![image](Pantallas/ModDistribucion/I0022.png)
### Sentecias SQL:
### Eventos: 
* **Pantalla Asignar: El gestor de distribucion podra visualizar los repartidores disponibles y asignar una fecha y ruta al pedido de codigo <1>**
```
SELECT id_repartidor , nombre;
from repartidor
INSERT INTO pedido(id_repartidor,id_ruta) 
VALUES (<2>,<3>);
WHERE id_pedido = <1>
```
### Código Requerimiento : R - 024
### Codigo interfaz : I - 024
### Imagen interfaz : 
![image](Pantallas/ModDistribucion/I0023.png)
### Sentecias SQL:
### Eventos: 
* **Visualizar historial de pedidos: El gestor de distribucion podra visualizar todos los pedidos que se han registrado**
```
SELECT p.id_venta,p.fecha_entrega,persona.CONCAT(nombre, ' ', primer_apell),tipo_est_pedido.estado_pedido
from pedido p
INNER JOIN venta ON pedido.id_venta = venta.id_venta
INNER JOIN persona  ON venta.id_persona = persona.id_persona
```
### Código Requerimiento : R - 025
### Codigo interfaz : I - 025
### Imagen interfaz : 
![image](Pantallas/ModDistribucion/I0024.png)
### Sentecias SQL:
### Eventos: 
* **Visualizar las entregas pendientes: El repartidor de id = <1> podra visualizar todos los pedidos que se encuentran pendientes**
```
SELECT p.id_venta,p.fecha_entrega,e.estado_pedido
FROM pedido p
INNER JOIN tipo_est_pedido e on pedido.id_est_pedido = tipo_est_pedido.id_est_pedido
WHERE id_repartidor = <1> AND  id_est_pedido = 'P';
```
### Código Requerimiento : R - 026
### Codigo interfaz : I - 026
### Imagen interfaz : 
![image](Pantallas/ModDistribucion/I0025.png)
### Sentecias SQL:
### Eventos: 
* **Boton entregado: El repartidor de id = <1> podra confirmar que se realizó la entrega con exito y actualizara el estado de pedido de codigo <2> a E**
```
UPDATE pedido
SET id_est_pedido = 'E'
WHERE id_repartidor = <1> AND id_pedido = <2>>;
```

### Código Requerimiento : R - 027
### Codigo interfaz : I - 027
### Imagen interfaz : 
![image](Pantallas/ModDistribucion/I0026.png)
### Sentecias SQL:
### Eventos: 
* **Visualizar el historial de pedido: El repartidor de id = <1> podra visualizar todas las entregas que realizó**
```
SELECT id_venta,fecha_entrega,e.estado_pedido
FROM pedido
INNER JOIN tipo_est_pedido e on pedido.id_est_pedido = tipo_est_pedido.id_est_pedido
WHERE id_repartidor = <1>;
```
### Código Requerimiento : R - 028
### Codigo interfaz : I - 028
### Imagen interfaz : 
![image](Pantallas/ModDistribucion/I0027.png)
### Sentecias SQL:
### Eventos: 
* **BOTON VER MAS: El repartidor y el gestor de distribucion podran visualizar los detalles del pedido de id = <1>**
```
SELECT per.nombre,ped.fecha_entrega,ped.id_venta,ven.monto_final,ped.id_ruta,rep.nombre,rep.id_repartidor,per.direccion
FROM pedido ped
INNER JOIN venta ven on ven.id_venta = ped.id_venta
INNER JOIN persona per on per.id_persona = ven.id_persona
INNER JOIN repartidor rep on rep.id_repartidor = ped.id_repartidor
WHERE id_pedido = <1>
```
## 3.5 Modulo de Alamcén
### Sentecias SQL:

--Mostrar el Stock, el precio unitario y el Valor en el inventario de cada producto
SELECT pr.Nombre_Producto,pr.Precio_Unitario_Producto,
       SUM(i.Entradas - COALESCE(i.Salidas, 0)) AS Stock_Disponible,
		(( SUM(i.Entradas - COALESCE(i.Salidas, 0)))*pr.Precio_Unitario_Producto) AS Importe_Inventario
FROM Inventario i
JOIN Producto pr ON i.Id_Producto = pr.Id_Producto
GROUP BY pr.Nombre_Producto,pr.Precio_Unitario_Producto
ORDER BY pr.Nombre_Producto;

--Mostrar la Ubicación vacía dentro del almacén y su Volumen Disponible en cm3
SELECT 
    CONCAT(A.Seccion,'-',A.Id_Stand,'-',A.Id_Repisas) AS Ubicacion,
    (E.Largo*E.Ancho*R.Altura) AS Volumen_Disponible
FROM 
    Acopla A
JOIN Estands E ON A.Id_Stand = E.Id_Stand
JOIN Repisas R ON A.Id_Repisas = R.Id_Repisas
LEFT JOIN 
    Inventario I ON A.Id_Stand = I.Id_Stand 
                    AND A.Id_Repisas = I.Id_Repisas 
                    AND A.Seccion = I.Seccion
WHERE I.Id_Inventario IS NULL
ORDER BY A.Seccion;

--Mostrar el Volumen Restante por cada Ubicación que se haya ingresado un producto
SELECT 
    CONCAT(A.Seccion,'-',A.Id_Stand,'-',A.Id_Repisas) AS Ubicacion,
    (E.Largo * E.Ancho * R.Altura) AS Volumen_Total,
    (E.Largo * E.Ancho * R.Altura) - COALESCE(SUM(I.Entradas - I.Salidas), 0) AS Volumen_Restante
FROM 
    Acopla AS A
INNER JOIN 
    Estands AS E ON A.Id_Stand = E.Id_Stand
INNER JOIN 
    Repisas AS R ON A.Id_Repisas = R.Id_Repisas
LEFT JOIN 
    Inventario AS I ON A.Id_Stand = I.Id_Stand 
                    AND A.Id_Repisas = I.Id_Repisas 
                    AND A.Seccion = I.Seccion
GROUP BY 
    A.Id_Stand, A.Id_Repisas, A.Seccion, E.Largo, E.Ancho, R.Altura;

--Mostrar los productos que se aplican en el rostro, como busqueda con palabra clave
SELECT p.Nombre_Producto,  
       (i.Entradas - COALESCE(i.Salidas, 0)) AS Stock_Disponible,
		m.Id_Marca
FROM Producto p
JOIN Produce pr ON p.Id_Producto = pr.Id_Producto
JOIN Marca m ON pr.Id_Marca = m.Id_Marca
JOIN Inventario i ON p.Id_Producto = i.Id_Producto
WHERE p.Zona_Uso = 'Rostro';

--Mostrar productos que son labiales con características de colores, marca, subtipos y clases
SELECT 
    p.Nombre_Producto AS Producto,
    STRING_AGG(DISTINCT c.Nombre_Color, ', ') AS Colores_Disponibles,
    m.Id_Marca AS Marca,
    STRING_AGG(DISTINCT st.Nombre_Sub_Tipo, ', ') AS Subtipos,
    STRING_AGG(DISTINCT cm.Nombre_Clase_Maquillaje, ', ') AS Clases_Maquillaje
FROM 
    Producto p
JOIN 
    Categoria_Producto cp ON p.Nombre_Categoria = cp.Nombre_Categoria
JOIN 
    Disponible d ON p.Id_Producto = d.Id_Producto
JOIN 
    Colores c ON d.Id_Color = c.Id_Color
JOIN 
    Produce pr ON p.Id_Producto = pr.Id_Producto
JOIN 
    Marca m ON pr.Id_Marca = m.Id_Marca
JOIN 
    Presenta pre ON p.Id_Producto = pre.Id_Producto
JOIN 
    Sub_Tipo st ON pre.Id_Sub_Tipo = st.Id_Sub_Tipo
LEFT JOIN 
    Clase_Maquillaje cm ON p.Id_Producto = cm.Id_Producto
WHERE 
    cp.Nombre_Categoria = 'Labiales'
GROUP BY 
    p.Nombre_Producto, m.Id_Marca;

--Mostrar dónde se ubican los Rimels y su stock
SELECT CONCAT(a.Seccion, '-', a.Id_Stand, '-', a.Id_Repisas) AS Ubicacion,
		p.Nombre_Producto,
       (i.Entradas - COALESCE(i.Salidas, 0)) AS Stock_Disponible
FROM Producto p
JOIN Inventario i ON p.Id_Producto = i.Id_Producto
JOIN Acopla a ON a.Id_Stand = i.Id_Stand AND a.Seccion = i.Seccion AND a.Id_Repisas = i.Id_Repisas
JOIN Categoria_Producto cp ON p.Nombre_Categoria = cp.Nombre_Categoria
WHERE cp.Nombre_Categoria = 'Rimels';

--Mostrar el peso que soporta cada seccion de mis almacenes
SELECT s.Seccion,a.Id_Almacen,s.Peso_Soporta
FROM Almacen a
JOIN Secciones s ON a.Id_Almacen = s.Id_Almacen;

--Mostrar el peso y volumen unitario de cada producto, para la distribución
SELECT
	pr.Nombre_Producto,pr.Peso_Unitario_Producto,
	(pr.Ancho_Present*pr.Largo_Present*pr.Alto_Present) AS Volumen_Unitario
FROM Producto pr;

--Mostrar el peso que se puede adicionar todavía a una sección
SELECT s.Seccion,
       s.Peso_Soporta - COALESCE(SUM(p.Peso_Unitario_Producto * i.Entradas), 0) AS Peso_Restante,
       COALESCE(SUM(p.Peso_Unitario_Producto * i.Entradas), 0) AS Peso_Soportado_Actualmente
FROM Secciones s
LEFT JOIN Inventario i ON s.Seccion = i.Seccion
LEFT JOIN Producto p ON i.Id_Producto = p.Id_Producto
GROUP BY s.Seccion, s.Peso_Soporta
ORDER BY s.Seccion;

--Mostrar la ubicación donde el volumen sea menor o igual a un volumen dado en cm3
--Cuando llega nueva mercancia
SELECT CONCAT(a.Seccion,'-',a.Id_Stand,'-',a.Id_Repisas) AS Ubicacion,
	(e.Largo*e.Ancho*r.Altura) AS Volumen
FROM Acopla a
JOIN Estands e ON a.Id_Stand=e.Id_Stand
JOIN Repisas r ON a.Seccion=r.Seccion AND a.Id_Repisas=r.Id_Repisas
WHERE (e.Largo * e.Ancho * r.Altura)<=200000.0;

--Mostrar las zonas en donde aplica cada categoría (en especial de maquillaje)
SELECT c.Nombre_Categoria, string_agg(cz.Zona,', ') AS Zonas
FROM Categoria_Producto c
JOIN Categoria_Producto_Zona cz ON c.Nombre_Categoria=cz.Nombre_Categoria
GROUP BY c.Nombre_Categoria;

--Mostrar los Sub Tipos que existen en el mercado por cada categoría
SELECT c.Nombre_Categoria, string_agg(cs.Sub_Tipo_Existe,', ') AS Sub_Tipo_Existen
FROM Categoria_Producto c
JOIN Categoria_Producto_Sub_Tipo_Existe cs ON c.Nombre_Categoria=cs.Nombre_Categoria
GROUP BY c.Nombre_Categoria;

--Mostrar el tamaño en KB de cada imagen subido por cada producto
SELECT p.Nombre_Producto, 
       ROUND(SUM((i.Largo_Imagen * i.Alto_Imagen * i.Profundidad_Bits) / 8192.0), 2) AS Tamaño_Imagen_KB
FROM Producto p
JOIN Imagenes i ON p.Id_Producto = i.Id_Producto
GROUP BY p.Nombre_Producto;

--Mostrar el tamaño en KB de cada imagen subido por cada clase de maquillaje
SELECT cm.Nombre_Clase_Maquillaje, 
       ROUND(SUM((i.Largo_Imagen * i.Alto_Imagen * i.Profundidad_Bits) / 8192.0), 2) AS Tamaño_Imagen_KB
FROM Clase_Maquillaje cm
JOIN Imagenes i ON cm.Id_Producto = i.Id_Producto AND cm.Id_Clase_Maquillaje = i.Id_Clase_Maquillaje
GROUP BY cm.Nombre_Clase_Maquillaje;

--Mostrar el total de memoria de todas las imagenes
SELECT 
    ROUND(SUM((i.Largo_Imagen * i.Alto_Imagen * i.Profundidad_Bits) / 8192.0), 2) AS Suma_Total_Imagenes_KB
FROM 
    Imagenes i
JOIN 
    Producto p ON i.Id_Producto = p.Id_Producto
JOIN 
    Clase_Maquillaje cm ON i.Id_Producto = cm.Id_Producto AND i.Id_Clase_Maquillaje = cm.Id_Clase_Maquillaje;

# 4. Carga de Datos
La carga de datos se ha hecho mediante archivos .csv

[Tabla tipo_est_cotizacion](ArchivosCSV/tipo_est_cotizacion.csv)

[Tabla tipo_est_proveedor](ArchivosCSV/tipo_est_proveedor.csv)

[Tabla Proveedores](ArchivosCSV/Proveedores.csv)

[Tabla Cotizaciones](ArchivosCSV/Cotizaciones.csv)

[Tabla CotizacionxProducto](ArchivosCSV/CotizacionxProducto.csv)

[Tabla Almacen](ArchivosCSV/Almacen.csv)

[Tabla Secciones](ArchivosCSV/Secciones.csv)

[Tabla Estands](ArchivosCSV/Estands.csv)

[Tabla Repisas](ArchivosCSV/Repisas.csv)

[Tabla Acopla](ArchivosCSV/Acopla.csv)

[Tabla Tipo_Movimiento](ArchivosCSV/Tipo_Movimiento.csv)

[Tabla Tipo_Producto](ArchivosCSV/Tipo_Producto.csv)

[Tabla Categoria_Producto](ArchivosCSV/Categoria_Producto.csv)

[Tabla Funciones_Categoria](ArchivosCSV/Funciones_Categoria.csv)

[Tabla Caracteriza](ArchivosCSV/Caracteriza.csv)

[Tabla Categoria_Producto_Zona](ArchivosCSV/Categoria_Producto_Zona.csv)

[Tabla Categoria_Producto_Sub_Tipo_Existe](ArchivosCSV/Categoria_Producto_Sub_Tipo_Existe.csv)

[Tabla Sub_Tipo](ArchivosCSV/Sub_Tipo.csv)

[Tabla Producto](ArchivosCSV/Producto.csv)

[Tabla Persona](ArchivosCSV/Personas.csv)

[Tabla Equipo de marketing](ArchivosCSV/Equipo_Marketing.csv)

[Tabla Cupón](ArchivosCSV/Cupón.csv)

[Tabla Campaña](ArchivosCSV/Campaña.csv)

[Tabla CampañaXProd](ArchivosCSV/CampañaXProd.csv)

[Tabla Canal](ArchivosCSV/Canal.csv)

[Tabla CampañaXCanal](ArchivosCSV/CampañaXCanal.csv)

[Tabla Observacion](ArchivosCSV/Observacion.csv)

[Tabla detalle_pago](ArchivosCSV/detalle_pago.csv)

[Tabla tipos_pago](ArchivosCSV/tipos_pago.csv)

[Tabla Venta](ArchivosCSV/venta.csv)

[Tabla VentaxProd](ArchivosCSV/ventaxprod.csv)

[Tabla ruta](ArchivosCSV/ruta.csv)

[Tabla pedido](ArchivosCSV/pedido.csv)

[Tabla repartidor](ArchivosCSV/repartidor.csv)

[Tabla zona](ArchivosCSV/zona.csv)

[Tabla distrito](ArchivosCSV/distrito.csv)


# 5. Funcionalidad Primaria Elegida (por módulo)

## MÓDULO : COMPRAS
**Funcionalidad primaria elegida:** Gestionar todas las cotizaciones hechas por los proveedores<br>
**Sustentación:** La gestión de cotizaciones en una empresa de venta de productos es una funcionalidad importante debido a que se requiere un análisis de la viabilidad de la cantidad de productos entregados y los precios de cada uno.<br>

Esta funcionalidad permitirá cumplir con los requerimientos de las pantallas relacionadas a Cotizaciones Historial cotizaciones (R004), Detalle Cotizaciones (R005), Aceptar/Rechazar cotización del proveedor (R006) los cuales se encuentran relacionados con las interfaces I-004, I-005, I-006.

| Actividad     | Descripción        | 
|:-------------:|:---------------:|
| 1       | Al ingresar en la opción de cotizaciones en el sistema (desde un correo autotizado), se podrá verificar el historial de cotizaciones que tenemos, dentro de este podemos ver en primer lugar los que están en estado pendiente, entonces el gestor de compras le dará en el botón de ver más, para poder ver el detalle de la cotización.<br>![image](Pantallas/ModCompras/HOMEC.png) ![image](Pantallas/ModCompras/MP3-.png) | 
| 2    | En el caso que le dé en ver más en una cotización que ya tiene un estado de aceptado o no aceptado, no aparecerán los botones (botones deshabilitados), de aceptar o rechazar oferta <br> ![image]( Pantallas/ModCompras/MP4.png) | 
| 3 | En el caso que le dé en ver más en una cotización que tiene un estado de pendiente, tendrá habilitado los botones de aceptar o rechazar oferta, al presionar el botón de aceptar la cotizacion cambia a estado de aceptado y le mostrara una pantalla de oferta aceptada, en el otro caso que rechace la cotizacion, la cotizacion cambiara a estado de no aceptado y saldrá una ventana de oferta rechazada.<br> ![image](Pantallas/ModCompras/MP5.png) ![image](Pantallas/ModCompras/MP5-1.png) ![image](Pantallas/ModCompras/MP5-2.png) |

## MÓDULO : MARKETING
**Funcionalidad primaria elegida:** Flujo de creación de campañas de marketing<br>
**Sustentación:** Para el área de marketing o para el negocio en general, es indispensable que las campañas de marketing tengan un nivel de calidad alto, es por ello que pasan por revisiones a cargo del gestor de marketing y modificaciones hechas por el equipo de marketing al que se le encargó.<br>

Esta funcionalidad permitirá cumplir con los requerimientos Proponer campaña (R007), Revisar campañas (R008), Observar campañas (R009) y atender observaciones (RO1O), estas tienen como interfaces a I007, I008, I009 e I010 respectivamente.

| Actividad     | Descripción        | 
|:-------------:|:---------------:|
| 1       | Un empleado ingresa a la página principal de los equipos de marketing (con un correo autorizado), tendrá la opción de crear propuesta y atender observaciones, para empezar con la funcionalidad elegida, se escoge en crear propuesta.<br>![image](Pantallas/ModMarketing/HomeEquipoMarketing.png) | 
| 2    | Ya en la pantalla de crear propuesta, el usuario del equipo de marketing genera una nueva campaña asociada a un id_campaña autogenerado, un id_equipo_marketing correspondiente y los datos que este ingrese, esto se dá al momento de presionar el botón enviar. Si se presiona el botón cancelar no se produce cambio alguno y se vuelve a la pantalla anterior. <br> ![image]( Pantallas/ModMarketing/I007.png) | 
| 3 | Con la campaña ya creada, el Gestor de marketing puede revisarla, para ello primero tiene que ingresar a la página principal del Gestor de amrketing en donde tiene las opciones de ver las campañas vigentes y las campañas propuestas, en este caso, vamos a revisar las campañas propuestas. ![image](Pantallas/ModMarketing/HomeGestorMarketing.png) |
| 4    | Ya en la pantalla de campañas propuestas, el Gestor de marketing puede visualizar todas aquellas campañas generadas por el equipo de marketing, se les dice propuestas ya que aún no han tenido revisión y tampoco han sido publicadas pues aún no se llega a la fecha de inicio, el Gestor de marketing presiona en el botón "Ver más" para revisar los datos de la respectiva campaña. <br> ![image]( Pantallas/ModMarketing/CampañaProp.png) | 
| 5    | Ya revisando los datos de la campaña, el Gestor de marketing toma una desición, si encuentra correcto los datos, presionará en enviar y no se realizarán cambios en el sistema, pero si encuentra alguna observacion que realizar, presionará en rechazar y se dirigira al apartado de observaciones. <br> ![image]( Pantallas/ModMarketing/I008.png) | 
| 6    | Ya en la pantalla de observaciones, el Gestor de marketing hará una descripción de aquellas observaciones que tiene la campaña generada por el equipo de marketing, se registrará al momento de presionar en enviar, pero si se da en cancelar, no se hará ningún cambio y se regresará a la pantalla anterior. <br> ![image]( Pantallas/ModMarketing/I009.png) |
| 7    | Un empleado de un equipo de marketing ingresa al Home del equipo de marketing y presiona en atender observaciones. <br> ![image]( Pantallas/ModMarketing/HomeEquipoMarketing.png) | 
| 8    | Ya en la pantalla de atender observaciones, el equipo de marketing puede visualizar todas aquellas observaciones que ha realizado el Gestor de marketing y que aún no han sido atendidas, el equipo de marketing presionará en una de ellas para visualizar los detalles y corregir la campaña. <br> ![image]( Pantallas/ModMarketing/Observaciones.png) | 
| 9    | El equipo de marketing lee las observaciones realizadas a la campaña y realiza las correcciones respectivas, al presionar en enviar se actualizarán aquellos datos de la campaña que han sido cambiados, además de actualizar el estado de la observación a atendido, en el caso de presionar en cancelar, no se realiza ningún cambio y se regresa a la pantalla anterior . <br> ![image]( Pantallas/ModMarketing/I010.png) | 

## MÓDULO : Distribucion
**Funcionalidad primaria elegida:** Flujo de entrega de pedido <br>
**Sustentación:** Para la empresa, el área de distribucion  es indispensable puesto que es una necesidad hacer llegar los productos a los cliente, es por ello que estara area se encargara de la gestion de distribucion desde la creacion del pedido hasta la entrega.<br>

Esta funcionalidad permitirá cumplir con los requerimientos Establecer fecha de entrega (R021), asignar repartidor y ruta (R023), visualizar el historial de pedidos (R024 y R027) y confirmar la entrega (RO26), estas tienen como interfaces a I021, I023, I024,I027 e I026 respectivamente.

| Actividad     | Descripción        | 
|:-------------:|:---------------:|
| 1       | El cliente ingresa a la página principal con una cuenta autorizada y se dirige al apartado de "ver mis pedidos".<br>![image](Pantallas/ModDistribucion/I0019.png) | 
| 2    | Ya en la pantalla de "ver mis pedidos", el cliente escoge uno de los pedidos que le faltan entregar y selecciona la fecha de entrega. <br> ![image]( Pantallas/ModDistribucion/I0020.png) | 
| 3 | Una vez seleccionada la fecha de entrega,esto creara el pedido y aparecera en el apartado de gestionar pedidos del gestor de distribucion. <br>![image](Pantallas/ModDistribucion/I0021.png) |
| 4    |El gestor de distribucion accede al apartado de gestionar pedidos y escoge uno de los pedidos para asignarle un repartidor y una ruta <br> ![image]( Pantallas/ModDistribucion/I0022.png) | 
| 5    | Cuando es seleccionado el repartidor este pedido aparecera en el apartado de "gestionar pedidos" del repartidor. <br> ![image]( Pantallas/ModDistribucion/I0024.png) | 
| 6    | El repartidor acepta el pedido cuando este realizar la entrega puede confirmarlo,y asi actualizar el estado del pedido <br> ![image](  Pantallas/ModDistribucion/I0025.png) |
| 7    |  Tanto el gerente de distribucion como el repartidor pueden ver los detalles del pedido <br> ![image](  Pantallas/ModDistribucion/I0027.png) | 


## MÓDULO : VENTAS
**Funcionalidad primaria elegida:** Gestionar el flujo de compra de prodcutos por parte de cliente<br>
**Sustentación:** Como se trata de una página web que permite ventas online, es muy importante manejar y controlar el flujo de ventas que al dia recibe la empresa por parte de numerosos clientes.<br>

Esta funcionalidad permitirá cumplir con los requerimientos de las pantallas relacionadas a Ver Cátalogo de productos(R012), Realizar una compra (R014), Elegir método de pago (R015) y consultar el historial de ventas y de cliente (R018 Y R019).Dichas funcionalidades  se encuentran relacionados con las interfaces I-0012, I-014, I-0015, I-018, I-019

| Actividad     | Descripción        | 
|:-------------:|:---------------:|
| 1       | Al ingresar a la web el cliente podra ver todo el arsenal de productos con los que cuenta la empresa para que pueda encontrar el que desee comprar.<br>![image](Pantallas/ModVentas/catalogo.png)| 
| 2    | Luego de escojer sus productos, el cliente pasa a la seccion del carrito de compras donde puede configurar ciertos aspectos de los porductos que esta comprando. Se le detalla los precios que va a tener que pagar y  tambien se le informa que prosiga con el proceso de pago con un método de pago permitido.<br> ![image]( Pantallas/ModVentas/carrito.png) | 
| 3 | Se procede a elegir un método de pago y luego rellenar los datos correpsondientes a dicho pago.entonces ya podria procesarse y registrarse la compra en los historiales de venta de la empresa.<br> ![image](Pantallas/ModVentas/tipo_pago.png) ! |
| 4 | Despues de la venta, se puede visualizar tanto los historiales de venta del cliente y de la empresa en general.Lo que permite visualizar los registros de venta de algún periodo en la empresa y asi poder darles seguimiento.<br> ![image](Pantallas/ModVentas/historial_ventas_gestor.png) ![image](Pantallas/ModVentas/historial_cliente.png) |




# 6. Stack Tecnológico elegido para su aplicación

## 6.1 Stack Tecnológico
| Stack                         | Detalle                                               |
|-------------------------------|-------------------------------------------------------|
| Lenguaje de programación      | Python <br>![Python](https://img.shields.io/badge/Python-3.9-yellow.svg?style=for-the-badge&logo=python&logoColor=white)|
| Librería GUI                  | Tkinter <br> ![Tkinter](https://img.shields.io/badge/Tkinter-blue.svg?style=for-the-badge&logo=python&logoColor=white)|
| Editor de código              | Visual Studio Code <br> ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-1.89.0-skyblue.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)|
| Base de datos                 | PostgreSQL <br> ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14.0-skyblue.svg?style=for-the-badge&logo=postgresql&logoColor=white)|
| Controlador de base de datos  | pgAdmin <br> ![pgadmin](https://img.shields.io/badge/pgAdmin-4-blue.svg?style=for-the-badge&logo=pgadmin)|

## 6.2 Diagrama de componentes

![image](DIAGCOMP.png)

# 7. Primera Versión de su Aplicación (BONUS)

![image](APLICATIVOMC.png)

[Aplicativo](AplicativoV1/Proveedores/prueba/client/gui_app.py)

# 8. Videos individuales

[Quispe Mitma Cesar](../../06.Videos_Individuales/VideosPC3/Quispe_Mitma_Cesar_Fernando-VideoIndividual.md)

[Taipe Sicha Ronny Andy](../../06.Videos_Individuales/VideosPC3/VideoIndividualPC3TaipeSichaRonnyAndy.md)

[Montes Lozano Diego Martín](../../06.Videos_Individuales/VideosPC3/Montes_Lozano_Diego_VideoIndividual.md)
