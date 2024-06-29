# Capítulo 02: Requerimientos
## Requerimientos Funcionales
## - Casos de uso para Marketing
**Caso de uso: Editar campaña vigente**

| Objetivo | <p align="left"> Permitir que el Gestor de marketing edite las campañas vigentes.</p> | 
|:--------------:|--------------|
| Descripción | Proceso mediante el cual el Gestor de marketing puede editar las campañas que ya están vigentes, se limita a los datos necesarios y posibles de editar. | 
| Actor primario   | Gestor de marketing | 
|Actor secundario| - |
|Precondiciones | Debe existir al menos una campaña vigente. |
| Paso | <p align="center"> Acción </p> |
| 1 | El gestor de marketing inicia sesión en su cuenta de la página web de Migni Store. |
| 2 | El gestor de marketing accede a la sección "Mostrar campañas vigentes". |
| 3 | La página muestra la vista de campañas vigentes y un histograma que muestra la cantidad de clientes que han ingresado a travez de los medios de publicidad. |
| 4 | El gestor de marketing accede a la opción de "editar" de la respectiva campaña.|
| 5 | El gestor de marketing puede eliminar la campaña. |
| 6 | El gestor de marketing procede a editar los datos necesarios y posibles de editar. |
| 7 | En caso de querer guardar los cambios realizados, el gestor de marketing accede a la opción de "guardar" y la campaña será guardada. |
| 8 | El caso termina |

**Caso de uso: Revisar campaña propuesta**

| Objetivo | <p align="left"> Permitir que el Gestor de marketing revise la campaña brindada por el equipo de marketing correspondiente.</p> | 
|:--------------:|--------------|
| Descripción | Proceso mediante el cual el Gestor de marketing puede revisar las campañas propuestas por el equipo de marketing, su criterio definirá si la campaña será aceptada o rechazada, en el caso de ser rechazada se enviarán las observaciones al equipo de marketing.  | 
| Actor primario   | Gestor de marketing | 
|Actor secundario| - |
|Precondiciones | El equipo de marketing debe haber propuesto una campaña. |
| Paso | <p align="center"> Acción </p> |
| 1 | El gestor de marketing inicia sesión en su cuenta de la página web de Migni Store. |
| 2 | El gestor de marketing accede a la sección "Mostrar campañas propuestas". |
| 3 | La página muestra la vista de campañas propuestas. |
| 4 | El gestor de marketing analiza los datos presentados y toma decisiones estratégicas basadas en la información proporcionada. |
| 5 | Si el gestor de marketing considera incorrectos los datos de la campaña seleccionada, accede a la opción de "observacion" de la respectiva campaña a observar. |
| 6 | El gerente de marketing relizará las observaciones y se las enviará al equipo de marketing. |
| 7 | El caso termina |

**Caso de uso: Proponer campaña**

| Objetivo | <p align="left"> Permitir que el Gestor de marketing genere una campaña y la asigne a un equipo de marketing.</p> | 
|:--------------:|--------------|
| Descripción | Proceso mediante el cual el equipo de marketing enviará una propuesta de campaña, esta debe ser futura para que el gestor pueda revisarla. | 
| Actor primario   | Equipo de marketing | 
|Actor secundario| - |
|Precondiciones | - |
| Paso | <p align="center"> Acción </p> |
| 1 | El equipo de marketing inicia sesión en su cuenta de la página web de Migni Store. |
| 2 | El equipo de marketing accede a la sección "generar propuesta". |
| 3 | La página muestra la vista de proponer campaña. |
| 5 | El equipo de marketing ingresa los datos correspondientes a la campaña, la unica condicion es que la fecha ini_sea despues de la fecha actual, aunque si se puede generar antes de ello, pues existen casos especiales. |
| 6 | El equipo de marketing envia la campaña propuesta al gestor de marketing con la opción enviar. |
| 7 | El caso termina |

**Caso de uso: Atender observación**

| Objetivo | <p align="left"> Permitir que el equipo de marketing corrija las observaciones realizadas por el Gestor de Marketing.</p> | 
|:--------------:|--------------|
| Descripción | Proceso mediante el cual el equipo de marketing selecciona una observacion y hace las correcciones brindadas por el gestor de marketing correspondientes a los datos de la campaña asociada. | 
| Actor primario   | Equipo de marketing | 
|Actor secundario| - |
|Precondiciones | el gestor de marketing debe de haber observado al menos una campaña propuesta por el equipo de marketing |
| Paso | <p align="center"> Acción </p> |
| 1 | El equipo de marketing inicia sesión en su cuenta de la página web de Migni Store. |
| 2 | El equipo de marketing accede a la sección "atender observaciones". |
| 3 | La página muestra la vista de observaciones realizadas. |
| 4 | El equipo de marketing selecciona una observacion.|
| 5 | El equipo de marketing presiona el boton "atender". |
| 6 | El equipo de marketing envia los datos de campaña corregidos con respecto a la observacion realizada por el gestor de marketing. |
| 7 | El caso termina |

## -  Casos de uso para Compras
**Caso de uso : Añadir proveedor**

| Objetivo | <p align="left">Permitir que el Gestor de compras pueda añadir proveedores a la página de Migni Store.</p> | 
|:--------------:|--------------|
| Descripción | Proceso de registro de proveedores en la aplicación, con datos de empresa ya sea nombre, dirección, numero, rubro, correo y sitio web.  | 
| Actor primario   | Gestor de compras | 
|Actor secundario| - |
|Precondiciones | El proveedor ya debe haber contactado con la empresa previamente |
| Paso | <p align="center"> Acción </p> |
| 1 | El gestor de compras accede a la pagina web |
| 2 | El gestor de compras ingresa sus datos de inicio de sesión |
| 3 | El gestor de compras se dirige al apartado de proveedores |
| 4 | El gestor de compras se dirige a “añadir proveedores”|
| 5 | El gestor de compras registra el nombre, teléfono, dirección, correo electrónico, rubro, sitio web y foto del proveedor |
| 6 | El sistema guarda los datos del proveedor |
| 7 | El sistema confirma de la creación de un nuevo proveedor |
| 8 | El caso termina |

**Caso de uso : Aceptar/Rechazar oferta del proveedor**

| Objetivo | <p align="left"> Permitir que el gestor de compras pueda aceptar o rechazar la oferta realizada por el proveedor d</p> | 
|:--------------:|--------------|
| Descripción | Proceso en el cual se puede visualizar la oferta, con estado pendiente y aceptar o rechazar dicha oferta| 
| Actor primario   | Gestor de compras | 
|Actor secundario| - |
|Precondiciones | El proveedor debe haber sido registrado por el gestor de compras |
| Paso | <p align="center"> Acción </p> |
| 1  | El gestor de compras ingresa a la plataforma web con su correo y contraseña|
| 2  | El gestor de compras se dirige a la sección de proveedores |
| 3  | El gestor de compras selecciona el proveedor que desee verificar su historial |
| 4  | El gestor de compras accede a la parte de registros del proveedor elegido |
| 5  | El gestor de compras revisa las solicitudes pendientes |
| 6  | El gestor de compras ingresa a la solicitud pendiente|
| 7  | El gestor de compras acepta o rechaza la oferta del proveedor |
| 8  | Se actualiza el estado de la oferta  |
| 9 | El caso se termina |

**Caso de uso : Visualizar proveedores/historial**

| Objetivo | <p align="left">  Permitir a los gestores poder acceder  y visualizar los proveedores y registros, con sus datos. </p> | 
|:--------------:|--------------|
| Descripción | Proceso mediante el cual los gestores pueden acceder a la visualización de proveedores y sus registros de compras.  | 
| Actor primario | Gestor de compras | 
|Actor secundario| - |
|Precondiciones | El proveedor debe haber sido registrado por el gestor de compras |
| Paso | <p align="center"> Acción </p> |
| 1 | El gestor de compras ingresa a la plataforma web con su correo y contraseña. |
| 2 | El gestor de compras ingresa a la sección de Proveedores |
| 3 | El sistema muestra la sección de Proveedores que fueron registrados|
| 4 | El gestor de compras elige de que proveedor va a revisar la información |
| 5 | El gestor de compras selecciona la opción de registros |
| 6 | El sistema muestra el historial de ofertas que fueron subidas a la pagina web y su estado|
| 7 | El caso termina |

## -  Casos de uso para Almacen
**Caso de uso : Visualizar Inventario**

| Objetivo | <p align="left"> Permite que el Gestor de Almacén pueda gestionar el inventario, analizar, filtrar y hacer toma de decisiones respecto al stock y ubicación </p> | 
|:--------------:|--------------|
| Descripción | Proceso de visualización del inventario de cada producto recepcionado | 
| Actor primario | Gestor de almacén | 
|Actor secundario|-|
|Precondiciones | El producto debe ser ingresado a algún almacén |
| Paso | <p align="center"> Acción </p> |
| 1 | Inicio de login del gestor de almacén, cuyo correo se mostrará en la parte superior derecho|
| 2 | Ingresa a la opción de Inventario en el marco izquierdo |
| 3 | El sistema le mostrará en un tabla el id producto, nombre, presentación, color, stock, ubicación|
| 4 | Se podrá seleccionar una fila de la tabla, lo cual el sistema mostrará en el marco derecho la imagen, importe total y volumen del producto seleccionado |

**Caso de uso : Filtrar Inventario**

| Objetivo | <p align="left"> Permite al Gestor de Almacén o algún trabajador filtrar los campos de mi tabla productos para mostrar lo que se requiere buscar </p> | 
|:--------------:|--------------|
| Descripción | Proceso de búsqueda o filtración con parámetros (botones o labels) para mis productos| 
| Actor primario | Gestor de almacén | 
|Actor secundario| Trabajador de almacén|
|Precondiciones |Ingresar un dato o dar clic en algún filtro|
| Paso | <p align="center"> Acción </p> |
| 1 | En el marco superior se puede dar clic en el botón 'Maquillaje' y se mostrará en la tabla solo los productos de mi almacén maquillaje, del mismo modo, al dar clic en el botón 'Papelería', me mostrará los productos de mi almacén papelería |
| 2 | Al dar clic en el botón 'Sin Stock' me mostrará los productos que no cuento con stock para posteriormente realizar una compra |
| 3 | El label 'Ingresar Código Producto' se puede filtrar por el ID Producto ya sea con el código completo o con las iniciales del ID Producto al darle clic en 'Buscar'|
| 4 | El label 'Ingresar Marca Produco' mostrará un combo box con las marcas registradas de los productos y al seleccionar una marca y darle clic en buscar se mostrará los productos que sean de la marca ingresada |
| 5 | El label 'Ingresar Stock Minimo' permite ingresar un número para filtrar los producto que tengan como stock igual o mayor que el número ingresado|
| 6 | El label 'Ingresar Categoría' mostrará un combo box con las categorías registradas para poder filtrar los productos de acuerdo a su tipo de categoría|

**Caso de uso : Visualizar Pedidos**

| Objetivo | <p align="left"> Permite al Gestor de Almacén ver los pedidos que faltan por procesar o que ya han sido procesados y/o completados </p> | 
|:--------------:|--------------|
| Descripción | Ver y gestionar los pedidos de las ventas efectuadas en el sistema para registrar un kardex| 
| Actor primario | Gestor de almacén | 
|Actor secundario| Trabajador de almacén|
|Precondiciones |La venta deben estar en estado 'C' (Canceladas) para que el pedido pase automático y esté en estado 'L' (Leído)|
| Paso | <p align="center"> Acción </p> |
| 1 |En el marco izquierdo ingresar a la sección 'Pedidos' que mostrará en un inicio todos los pedidos que están en estado 'L' para su registro más rápido |
| 2 | En la tabla pedidos se mostrará los campos: ID Pedido, Tipo Entrega, Fecha Entrega, Dias Faltantes, Cod Venta, Repartidor (asignado automático por la zona de la dirección del cliente, si el repartidor está disponible y si el tipo de entrega es en domicilio) |
| 3 | Al dar clic en una fila de la tabla pedidos, en el marco derecho se mostrará una tabla con los campos: ID Producto, Nombre, Cantidad, Ubicación; que vendría a ser el detalle del pedido para poder preparar los respectivos productos|

**Caso de uso : Filtrar Pedido**

| Objetivo | <p align="left"> Permite al Gestor de Almacén o algún trabajador filtrar los campos de mi tabla pedidos para mostrar lo que se requiere buscar </p> | 
|:--------------:|--------------|
| Descripción | Proceso de búsqueda o filtración con parámetros (botones o labels) para mis pedidos| 
| Actor primario | Gestor de almacén | 
|Actor secundario| Trabajador de almacén|
|Precondiciones |Ingresar un dato o dar clic en algún filtro|
| Paso | <p align="center"> Acción </p> |
| 1 | El label 'Tipo Entrega' mostrará un combo box con los diferentes tipos de entrega que el cliente haya seleccionado en su venta que puede ser a Domicilio, Recojo o Envío|
| 2 | El label 'Estado Pedido' mostrará un combo box con los diferentes estados que se le asigna a un pedido que puede ser, Leído, En Preparación, Despachado y Retornado|
| 3 | El botón 'Actualizar' mostrará en la tabla pedidos solo aquellos ID Pedido que faltan por procesar como en la pantalla de inicio|

**Caso de uso : Registrar**

| Objetivo | <p align="left"> Permite ingresar los detalles del pedido a mi tabla Kardex </p> | 
|:--------------:|--------------|
| Descripción | los ID Producto con sus cantidades respectivas y el tipo de movimiento se agregan de manera automática mi sección Kardex| 
| Actor primario | Gestor de almacén | 
|Actor secundario|-|
|Precondiciones |Que un pedido seleccionado esté en estado 'L'|
| Paso | <p align="center"> Acción </p> |
| 1 | Al dar clic en el botón registrar que aparecerá en el marco derecho, se actualizará el estado de la venta a 'P' (En Proceso) y el estado del pedido a 'P' (En Preparación), y se agregarán los ítems de los productos con su cantidad a las tablas Kardex y KardexxProducto|

**Caso de uso : Visualizar Kardex**

| Objetivo | <p align="left"> Permite al Gestor de Almacén ver los detalles de los pedidos despachados con tu tipo de movimiento </p> | 
|:--------------:|--------------|
| Descripción | Se podrá los detalles del movimiento de los productos de mi almacén| 
| Actor primario | Gestor de almacén | 
|Actor secundario|-|
|Precondiciones |El pedido ha sido recogido de almacén y está en estado 'P'|
| Paso | <p align="center"> Acción </p> |
| 1 |En el marco izquierdo ingresar a la sección 'Kardex' que mostrarála tabla Kardex con los campos: ID Kardex, Fecha, Movimiento, Pedido, Tipo entreg|
| 2 | Al dar clic en una fila de la tabla kardex, en el marco derecho se mostrará una tabla con los campos: Producto, Cantidad que indicarán a qué productos se ha efectuado ese movimiento en almacén|

## -  Casos de uso para Distribucion

**Caso de uso : Establecer fecha de entrega del pedido**

| Objetivo | <p align="left">Permitir que el cliente establezca la entrega de pedido .</p> | 
|:--------------:|--------------|
| Descripción | Proceso de asignacion de la fecha de la entrega del pedido,con actualizaciones de estado en el apartado del cliente y la lista de pedidos del gestor de ventas.  | 
| Actor primario   | Cliente | 
|Actor secundario| - |
|Precondiciones | El cliente realizo el pedido y el pago respectivo |
| Paso | <p align="center"> Acción </p> |
| 1 | El cliente accede a la pagina web |
| 2 | El cliente ingresa sus datos de inicio de sesión |
| 3 | El cliente se dirige al apartado de mis pedidos |
| 4 | El cliente selecciona "Establecer fecha de entrega" de la seccion de uno de sus pedidos|
| 5 | El cliente asigna la fecha y hora de entrega |
| 6 | El sistema actualiza la base de datos con la fecha asignada de entrega |
| 7 | El sistema actualiza la seccion del pedido del cliente,quitando la seleccion "Establecer fecha de entrega" y añadiendo la opcion "Reprogramar fecha" |
| 8 | El sistemas actualiza la base de datos de la lista de "gestionar pedidos" del apartado del gestor de ventas y añade el pedido |
|9|El sistema asigna el estado del pedido en la lista de "Gestionar pedidos" del apartado del gestor de ventas a "PENDIENTE" |
|10|El caso termina|

**Caso de uso : Asignar repartidor**

| Objetivo | <p align="left">Permitir que el Gestor de ventas pueda asignar un repartidor a cada pedido.</p> | 
|:--------------:|--------------|
| Descripción | Proceso de eleccion de repartidores disponibles para cada entrega de un pedido.  | 
| Actor primario   | Gestor de ventas | 
|Actor secundario| - |
|Precondiciones | El pedido deberia tener una direccion,fecha y hora establecida de entrega |
| Paso | <p align="center"> Acción </p> |
| 1 | El gestor de ventas accede a la pagina web |
| 2 | El gestor de ventas ingresa sus datos de inicio de sesión |
| 3 | El gestor de ventas se dirige al apartado de gestionar pedidos |
| 4 | El gestor de ventas presiona la parte “ASIGNAR” en la columna de repartidor,de cualquier pedido |
| 5 | El gestor de ventas escoge al repartidor entre todos los disponibles |
| 6 | El sistema actualiza el pedido con los datos del repartidor asignado |
| 7 | El sistema actualiza la base de datos del repartidor asignado |
| 8 | El pedido aparece en la lista de pendientes del repartidor |
|9|El pedido se actualiza en la columna de repartidor a "ASIGNADO"|
|10|El caso termina|


**Caso de uso : Actualizar estado de pedido a ENTREGADO**

| Objetivo | <p align="left">Permitir que el repartidor logre la entrega de pedido y actualice el estado .</p> | 
|:--------------:|--------------|
| Descripción | Proceso de entrega del pedido,con actualizaciones de estado en el apartado del cliente y la lista de pedidos del gestor de ventas.  | 
| Actor primario   | Repartidor | 
|Actor secundario| - |
|Precondiciones | El pedido fue asignado a un repartidor |
| Paso | <p align="center"> Acción </p> |
| 1 | El repartidor accede a la pagina web |
| 2 | El repartidor ingresa sus datos de inicio de sesión |
| 3 | El repartidor se dirige al apartado de pedidos pendientes |
| 4 | El repartidor acepta el pedido|
| 5 | El sistema actualiza el estado del pedido en el apartado de "mis pedidos" del cliente a "SU PEDIDO ESTA EN CAMINO" |
| 6 | El repartidor realiza la entrega |
| 7 | El repartidor vuelve a ingresar a la pagina web y se dirige a su apartado |
| 8 | El repartidor confirma que se ha entregado el pedido |
|9|El sistema quita el pedido del la seccion de "Pedidos pendientes" del repartidor |
|10|El sistema agrega el pedido entregado y actualiza la base de datos del historial de pedidos del repartidor |
|11|El sistema actualiza el estado del pedido a "ENTREGADO" en la seccion de gestionar pedidos del gestor de ventas|
|12|El caso termina|

## - Casos de uso para Finanzas
**Caso de uso : Añadir factura**

| **Objetivo**       | <p align="left"> Permitir al usuario añadir una factura al sistema.</p>  |
|:--------------:|--------------|
| **Descripción**    | Proceso de creación y registro de una facturas de los diferentes tipos existentes para considerar el monto y clasificarlos como asientos contables. |
| **Actor Primario** | Contador General |
| **Precondiciones** | El usuario ha iniciado sesión y tiene permisos para añadir facturas. |
| **Paso**           | <p align="center"> Acción </p>|
| 1 | El usuario selecciona "Añadir Factura" en el menú principal. |
| 2 | El sistema presenta un formulario para ingresar detalles de la factura. |
| 3 | El usuario completa el formulario con la información requerida así como el tipo. |
| 4 | El usuario revisa y confirma la creación de la factura. |
| 5 | El sistema valida la información ingresada y guarda la factura en la base de datos. |
| 6 | El sistema genera automáticamente el asiento contable correspondiente. |
| **Flujo Alternativo** | - Si hay errores en los datos, el sistema muestra mensajes de error y permite correcciones. |

**Caso de Uso: Ver Estado de Facturas**
|  **Objetivo** | <p align="left">Permitir al usuario consultar y gestionar el estado de las facturas en el sistema, incluyendo el pago.</p>|
|:--------------:|--------------|
|Descripción	| Proceso de visualización y gestión de las facturas registradas, permitiendo su edición, aprobación o rechazo según el estado de cada factura.|
|Actor Primario	| Contador General, Gestor de Costos, Gerente General. |
| Precondiciones|	El usuario ha iniciado sesión y tiene permisos para acceder al módulo de Finanzas.|
| Paso | <p align="center">Acción</p>|
| 1 | El usuario selecciona "Facturas" en el menú principal. |
| 2 | El usuario elige "Ver Estado de Facturas" en el menú del módulo de Finanzas. |
| 3 | El sistema muestra una lista de todas las facturas registradas con su estado actual (VIGENTE, PROPUESTA, ACEPTADA, RECHAZADA) y estado de pago (Pagada, No Pagada, Parcialmente Pagada). |
| 4 | El usuario puede filtrar las facturas por criterios específicos (fecha, proveedor, cliente, estado, estado de pago, etc.). |
| 5 | El usuario selecciona una factura de la lista para ver más detalles. |
| 6 | El sistema muestra una vista detallada de la factura seleccionada, incluyendo: fecha de emisión, proveedor, importe total, productos/servicios, estado actual, estado de pago, historial de modificaciones. |
| 7 | Dependiendo del estado de la factura, el usuario puede realizar las siguientes acciones: |
| 7.1 | Editar (VIGENTE): Modificar fecha y modalidad de pago, agregar o quitar productos/servicios. |
| 7.2 | Revisar (PROPUESTA): Aprobar o rechazar la factura, añadiendo observaciones si es rechazada. |
| 7.3 | Registrar (ACEPTADA): Registrar la factura en los sistemas contables. |
| 7.4 | Ver Observaciones (RECHAZADA): Ver las observaciones realizadas por el contador general. |
| 7.5 | Actualizar Estado de Pago: Marcar la factura como pagada, no pagada o parcialmente pagada según corresponda. |
| 8 | El usuario guarda cualquier cambio realizado. |
| 9 | El sistema confirma que los cambios han sido guardados exitosamente y envía notificaciones pertinentes. |
| Flujo Alternativo | - Si el usuario no tiene permisos, el sistema muestra un mensaje de error y redirige a la pantalla principal. |
| | - Si la factura buscada no se encuentra, el sistema muestra un mensaje indicando que no hay resultados y ofrece opciones de búsqueda avanzada. |

**Caso de Uso: Ver Asientos Contables**

| **Objetivo**       | <p align="left"> Facilitar al usuario la consulta de asientos contables. </p>  |
|:--------------:|--------------|
| **Descripción**    | Mostrar una lista de asientos contables con opciones para ver detalles, filtrar, buscar además de editar e ingresar.|
| **Actor Primario** | Contador General, Gerente General|
| **Precondiciones** | El usuario ha iniciado sesión y según su rol tiene permisos para ver los asientos contables o para editar e ingresar. |
| **Paso**           | <p align="center"> Acción </p> |
| 1 | El usuario selecciona "Ver Asientos Contables" en el menú principal. |
| 2 | El sistema muestra una lista de asientos contables ordenados por fecha. |
| 3 | El usuario puede seleccionar un asiento para ver detalles adicionales. |
| 4 | El usuario puede filtrar y buscar asientos por fecha, número o tipo además de ingresar o editar según el rol que tenga. |
| 5 | El caso termina. |
| **Flujo Alternativo** | - Si el usuario no tiene permisos, el sistema muestra un mensaje de error. |

**Caso de Uso: Ver Estado de Resultados**

| **Objetivo**       |  <p align="left">  Permitir al usuario consultar el estado de resultados.</p>  |
|:--------------:|--------------|
| **Descripción**    | Mostrar el estado de resultados con ingresos, costos de ventas, gastos operativos y beneficios netos así como poder editar en caso lo necesita considerando su rol. |
| **Actor Primario** | Gerente General, Contador General |
| **Precondiciones** | - El usuario ha iniciado sesión y tiene permisos según sea el caso para ver, editar el estado de resultados. |
| **Paso**           | <p align="center"> Acción </p>|
| 1 | El usuario selecciona "Ver Estado de Resultados" en el menú principal. |
| 2 | El sistema muestra el estado de resultados con los datos correspondientes. |
| 3 | El sistema calcula automáticamente los valores basados en las transacciones registradas. |
| 4 | El usuario puede filtrar y buscar transacciones específicas. |
| 5 | El caso termina. |
| **Flujo Alternativo** | - Si el usuario no tiene permisos, el sistema muestra un mensaje de error. |

**Caso de Uso: Ver Reporte Contable**

| **Objetivo**       |  <p align="left">Permitir al usuario descargar el reporte contable. </p> |
|:--------------:|--------------|
| **Descripción**    | Generar y  ver un reporte contable.|
| **Actor Primario** | Gerente General, Contador General |
| **Precondiciones** | El usuario ha iniciado sesión  y tiene permisos para ver reportes contables o para editar según sea el caso. |
| **Paso**           |  <p align="center"> Acción </p>  |
| 1 | El usuario selecciona la opción de "Ver Reporte Contable" en el menú principal. |
| 2 | El sistema genera el reporte según el periodo. |
| 2 | El sistema muestra un resumen contable con el total de ingresos, gastos, activos, pasivos y patrimonio así como una análisis detallado. |
| 3 | El sistema presenta un desglose detallado de cada categoría contable. |
| 4 | El usuario puede filtrar y buscar transacciones específicas dentro del resumen. |
| 5 | El usuario puede dejar algunas acotaciones específicas dentro del resumen. |
| 4 | El caso termina. |
| **Flujo Alternativo** | - Si el usuario no tiene permisos para acceder al resumen contable, el sistema muestra un mensaje de error. |

**Caso de Uso: Asignar Presupuesto**

| **Objetivo**       |  <p align="left"> Permitir al usuario asignar un presupuesto a diferentes departamentos o proyectos. </p> |
|:--------------:|--------------|
| **Descripción**    | Asignar y distribuir fondos según las necesidades de cada departamento o proyecto. |
| **Actor Primario** | Contador General, Gerente General |
| **Precondiciones** | - El usuario ha iniciado sesión y el usuario tiene permisos para asignar presupuestos. |
| **Paso**           |  <p align="center"> Acción </p>  |
| 1 | El usuario selecciona "Asignar Presupuesto" en el menú principal. |
| 2 | El sistema muestra una lista de departamentos o proyectos. |
| 3 | El usuario selecciona el departamento o proyecto y el monto a asignar. |
| 4 | El sistema registra la asignación y actualiza el presupuesto total. |
| 5 | El caso termina. |
| **Flujo Alternativo** | - Si el usuario no tiene permisos, el sistema muestra un mensaje de error. |

**Caso de Uso: Gestión de Presupuesto**

| **Objetivo**       |  <p align="left"> Permitir al usuario gestionar presupuestos financieros. </p>  |
|:--------------:|--------------|
| **Descripción**    | Crear, editar y revisar presupuestos, con opciones para ajustar partidas y comparar con datos reales. |
| **Actor Primario** | Contador General, Gerente General |
| **Precondiciones** | - El usuario ha iniciado sesión y tiene permisos para gestionar presupuestos. |
| **Paso**           |  <p align="center"> Acción </p>  |
| 1 | El usuario selecciona "Gestión de Presupuestos" en el menú principal. |
| 2 | El sistema muestra una lista de presupuestos existentes. |
| 3 | El usuario puede crear un nuevo presupuesto o editar uno existente. |
| 4 | El sistema permite ajustar partidas y comparar con datos reales. |
| 5 | El caso termina. |
| **Flujo Alternativo** | - Si el usuario no tiene permisos, el sistema muestra un mensaje de error. |

## Requerimientos de atributos de Calidad


   **Simplicidad y Facilidad de Uso:**
   - La página web debe ser intuitiva y fácil de usar, especialmente para usuarios nuevos. Se deben evitar interfaces complicadas que puedan confundir a los 
     usuarios.

   **Rendimiento:**
   - La página web debe cargar rápidamente y proporcionar una experiencia de usuario fluida en todos los dispositivos y conexiones a internet. Se debe minimizar 
     el tiempo de carga de las páginas y optimizar el rendimiento del sitio.
     
  **Seguridad:**
   - La página controlará el acceso solo de las personas que cuenten con una cuenta en el sistema, ya que dependiendo del rol podrá editar, ver así como registrar en el 
     aplicativo.
     
   **Usabilidad:**
   - La usabilidad es esencial para que tanto los administradores, trabajadores como los clientes interactúen facilmente con el sistema, y permita optimizar el proceso de 
     obtención de información necesaria especialmente para los clientes al momento de buscar sus productos.
     
   **Escalabilidad:**
   -  La página será capaz de soportar una gran cantidad de usuarios y operaciones.

## Restricciones:

   **Compatibilidad con Navegadores:**
   - La página web debe ser compatible con una variedad de navegadores web modernos, incluidos Chrome, Firefox, Safari y Edge, para garantizar una experiencia de 
     usuario consistente.

   **Cumplimiento Legal Básico:**
   - Se deben cumplir con las leyes y regulaciones básicas relacionadas con la protección de datos y la privacidad en línea, pero considerando la capacidad 
     limitada de recursos para cumplir con estándares más complejos desde el principio.
