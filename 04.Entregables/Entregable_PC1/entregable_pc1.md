## 1. Descripción de la Empresa, del Proceso de Negocio Elegido y Motivación
### 1.1 Datos de la empresa
- Descripción de la empresa: Es una microempresa que vende maquillaje y papelería que busca traer productos de buena calidad y buen precio, sus principales productos son maquillaje, lapiceros, cuadernos.

- RUC:
- Razón social:
- Dirección:
- Teléfono:
- Misión: Nuestra misión es ser un referente en el mercado por la diversidad y calidad de nuestros productos en papelería y maquillaje. Buscamos ofrecer una orientación personalizada a nuestros clientes para encontrar los productos que mejor se adapten a sus gustos con la única finalidad de satisfacerlos.💗✨
- Visión: Nuestra visión es ser reconocidos como el espacio preferido para aquellos que buscan una experiencia de compra excepcional en el mundo del maquillaje y la papelería por lo que nos esforzamos por crear un ambiente acogedor y emocionante, donde los clientes puedan explorar una amplia diversidad de productos y recibir asesoramiento personalizado por parte de nuestro equipo capacitado. Es así que aspiramos establecer relaciones sólidas y duraderas con nuestros clientes, basadas en la confianza, la satisfacción y la lealtad hacia nuestro servicio por eso es que nos innovaremos constantemente para mantenernos a la vanguardia de las tendencias y necesidades de nuestros público, sin descuidar la dedicación y calidad procurada. 💗
- Productos ofrecidos:
  - Papelería:
    - Cuadernos
    - Lapiceros
  - Maquillaje
    - Paletas
    - Rubores
    - Primers
    - Polvos y correctores
    - Glitter
    - Delineadores de ojos y labios
    - Labiales y glosses
    - Máscaras de pestañas
### 1.2 Descripción del proceso de negocio

- Proceso de compra - Este proceso se refiere a las compras de los diversos productos mediante la aceptación de ofertas realizadas por los proveedores, estos productos posteriormente irán al almacén de la empresa.
- Proceso de venta - Este proceso es acerca de los procesos de venta en la empresa que inicia desde que el cliente nos contacta para venderle el producto.
- Proceso de almacen - Este proceso se refiere a cómo se gestiona el almacén de manera que constatemente se verifica el stock de los productos.
- Proceso de distribucion - Este proceso se refiere a las actividades que abarcan llevar el producto hasta el cliente.
- Proceso de marketing - Este proceso es acerca de las actividades que realizan para llamar al cliente.
- Proceso de finanzas - Este proceso abarca las diversas actividades en que se gestionan las ganancias y perdidas en base a las compras, los gastos y las ventas.
- Proceso de CRM - Este proceso abarca las actividades para mapear a los clientes y saber mejor sus necesidades.

### PROCESO AS IS

- Proceso de Compra
![Proceso de Compra](../Entregable2/ProcesosASIS/BPMN_CompraASIS.png)

|Secuencia | Actividad | Descripción | Responsable |
|:----:|:----------------:|:--------------------------:|:-----------:|
| 1 | Solicitud del área de almacén para realizar una compra | El área de almacén solicitó realizar una compra porque ya no quedan existencias de algún producto. | Gestor de almacén |
| 2 | Aprobación para solicitar una compra | El área de compra recibe la solicitud de falta de productos y procede a aprobarla | Gestor de compras |
| 3 | Elección de productos a comprar | El área de compra revisa los productos faltantes emitidos en la solicitud y procede a revisar la cantidad que comprara de dichos productos | Gestor de compras |
| 4 | Evaluación del proveedor | El área de compra revisa todas las ofertas realizadas por los proveedores y decide aceptarlas o rechazarlas en función al precio que ofrezcan | Gestor de compras |
| 5 | Emisión de solicitud de compra | El área de compra se acepta una propuesta del proveedor y procede a emitir una solicitud de compra hacia dicho proveedor | Gestor de compras |
| 6 | Recepción de la solicitud por parte del proveedor| El proveedor recepciona la solicitud emitida por el área de compras. | Proveedor |
| 7 | Realización del pago | El área de compra realiza el pago acordado hacia el proveedor | Gestor de compras |
| 8 | Recepción del comprobante de pago del Proveedor | El área de compras recepciona el comprobante de pago que realizo hacia el proveedor | Gestor de compras |
| 9 | Validación de la Factura | Se valida la factura emitida hacia la empresa| Contador |
| 10 | Almacenar Documento | Se almacena la factura que fue emitida | Contador | 
| 11 | Registrar la compra en Excel | Se registran los productos comprados en un Excel | Gestor de Compra |
| 12 | Recepción de productos | La empresa recepciona los productos que fueron entregados | Gestor de compra |
| 13 | Envió al almacén | Se envía al almacén todos los productos recepcionados para su posterior revisión | Gestor de compra |
| 14 | Recepción en almacén | En el almacén recepciona todos los productos y serán revisados para asegurarse que llegaron en correcto estado | Gestor de almacén |


- Proceso de Venta

![Proceso de Venta](../Entregable2/ProcesosASIS/ProcesoVentaBPMN.png)

- Proceso de Almacén

![Proceso de Almacén](../Entregable2/ProcesosASIS/AsIs%20Almacen.png)

- Proceso de Distribución
  
![Proceso de Distribución](../Entregable2/ProcesosASIS/DistribucionAsis.jpeg)

|Secuencia|Proceso|Descripcion|Responsable|
|---------|-------|-----------|-----------|
|1        |Preparacion del pedido solicitado|Se separan los productos que se van a entregar.|Gestor de ventas|
|2|Coordinacion del lugar|El cliente y el gestor de ventas coordinan el lugar de entrega del producto|Gestor de ventas y cliente|
|3|Cotizacion de delivery|Si el lugar de entrega no se encuentra dentro de los puntos de encuentro disponibles, se cotiza el transporte realizado de acuerdo al lugar|Gestor de ventas|
|4|Coordinar la fecha y hora|Escogido el lugar de encuentro, se establece la hora y fecha de entrega|Gestor de ventas y cliente|
|5|Actualizacion del pedido|Se actualiza el estado del pedido en PENDIENTE|Gestor de ventas|
|6|Cancelacion de entrega|El cliente ha cancelado la entrega y el proceso termina|Cliente|
|7|Preparacion del pedido|Se empaqueta los productos para su respectiva entrega|Gestor de ventas |
|8|Eleccion del personal disponible para la entrega|Se elige al personal que se encuentra disponible y listo para la entrega|Repartidor|
|9|Personal en el punto de entrega|El personal llega al punto de entrega|Repartidor|
|10|Emision de nueva fecha de entrega|Si el cliente tiene demora en el punto de encuentro|Gestor de ventas |
|11|Verificacion de código de compra|Se verifica si el código de compra que presenta el cliente es correcto|Repartidor|
|12|Recepcion del producto por el cliente|Si el código es correcto,el cliente recibe el producto |Repartidor|
|13|Actualizar el estado de productos de almacen|Si la entrega se realiza con éxito,se actualiza el estado del pedido a ENTREGADO|Repartidor|

- Proceso de Marketing

![Proceso de Marketing](../Entregable2/ProcesosASIS/BPMN_marketing.jpeg)

- Proceso de CRM

![Proceso de CRM](../Entregable2/ProcesosASIS/Proceso-CRM.png)

- Proceso de Finanzas

![Proceso de Finanzas](../Entregable2/ProcesosASIS/ProcesosFinanzas.png)

### PROCESO TO BE

- Proceso de Compra
![Proceso de Compra](../Entregable2/ProcesosTOBE/BPMN_CompraTOBE.png)

|Secuencia | Actividad | Descripción | Responsable |
|:----:|:----------------:|:--------------------------:|:-----------:|
| 1 | Solicitud del área de almacén para realizar una compra | El área de almacén solicitó realizar una compra porque ya no quedan existencias de algún producto. | Gestor de almacén |
| 2 | Aprobar solicitud para la compra | El área de compra recibe la solicitud del área del almacén y luego de revisarlo se acepta | Gestor de compras |
| 3 | Elección de productos a comprar | El área de compra revisa los productos faltantes emitidos en la solicitud y procede a revisar la cantidad que comprara de dichos productos | Gestor de compras |
| 4 | Enviar solicitud de compra a los proveedores | El área de compra envía solicitudes a los proveedores de los productos que les hacen falta | Gestor de compras |
| 5 | Registrar oferta en la web | El gestor de compras registra su oferta en la web para posteriormente poder visualizarlo en la pestaña de historial | Gestor de compras|
| 6 | Evaluar ofertas del proveedor | El área de compra revisa todas las ofertas realizadas por los proveedores y decide aceptarlas o rechazarlas | Gestor de compras |
| 7 | Emisión de solicitud de compra | El área de compras envía una solicitud de compra al proveedor que fue aceptado su oferta | Gestor de compras |
| 8 | Recepción de la solicitud por parte del proveedor| El proveedor recepciona la solicitud emitida por el área de compras. | Proveedor |
| 9 | Realización del pago | El área de compra realiza el pago acordado hacia el proveedor | Gestor de compras |
| 10 | Recepción del comprobante de pago del Proveedor | El área de compras recepciona el comprobante de pago que realizo hacia el proveedor | Gestor de compras |
| 11 | Validación de la Factura | Se valida la factura emitida hacia la empresa| Gestor de compras |
| 12 | Almacenar Factura | Se almacena la factura en una base de datos que luego revisara el contador | Gestor de compras | 
| 13 | Recepción de productos | La empresa recepciona los productos que fueron entregados | Gestor de compra |
| 14 | Enviar al almacén | Se envía al almacén todos los productos recepcionados para su posterior revisión | Gestor de compra |
| 15 | Recepción en almacén | En el almacén recepciona todos los productos y serán revisados para asegurarse que llegaron en correcto estado | Gestor de almacén |

- Proceso de Venta

![Proceso de Venta](../Entregable2/ProcesosTOBE/BPMN_VENTATOBE.png)

- Proceso de Almacén

![Proceso de Almacén](../Entregable2/ProcesosTOBE/ToBeAlmacen.jpg)

- Proceso de Distribución
  
![Proceso de Distribución](../Entregable2/ProcesosTOBE/DistribucionTobe.jpeg)

|Secuencia|Proceso|Descripcion|Responsable|
|---------|-------|-----------|-----------|
|1        |Actualizacion de pedido en la lista de "mis pedidos"|El pedido aparece en la lista de "mis pedidos" del cliente|Cliente|
|2|Coordinar la fecha y hora|En la vista de "mis pedidos" el cliente establece la hora y fecha de entrega|Cliente|
|3|Actualizacion del pedido en la lista de pedidos|Se actualiza el estado del pedido en PENDIENTE y aparece en la vista del gestor de ventas|Gestor de ventas|
|4|Asignacion del repartidor disponible para la entrega|Se elige al repartidor que se encuentra disponible para la entrega|Gestor de ventas|
|5|Actualizacion del pedido en la lista del repartidor|El pedido aparece en la lista del repartidor al que se ha asignado|Repartidor|
|6|Cancelacion de entrega|El cliente cancela la entrega y se reprograma una nueva fecha|Cliente|
|7|Actualizacion de pedido a "CANCELADO"|El pedido se actualiza en "CANCELADO" en la lista de pedidos del gestor de ventas y de pedidos pendientes del repartidor si es que ya se le habia asignado|Gestor de ventas y repartidor|
|8|Preparacion del pedido|Se empaqueta los productos para su respectiva entrega|Gestor de ventas |
|9|Repartidor acepta el pedido|El repartidor entra en la lista de sus pedidos pendientes y acepta el pedido que va a entregar|Repartidor|
|10|Actualizacion de estado de pedido "SU PEDIDO ESTA EN CAMINO"|El pedido se actualiza en la lista de "mis pedidos" del cliente a "SU PEDIDO ESTA EN CAMINO"|Cliente|
|11|El repartidor llega al punto de encuentro|El repartidor se dirige al lugar de entrega hasta llegar al punto|Repartidor|
|12|Verificacion de código de compra|El repartidor se encuentra con el cliente y verifica si el código de compra que presenta el cliente es correcto|Repartidor y cliente|
|13|Recepcion del producto por el cliente|Verificado que el código es correcto,el cliente recibe el producto |Cliente|
|14|Actualizar el estado del pedido a "ENTREGADO"|El repartidor entra a la lista de sus pedidos y confirma que se ha entregado el pedido ,lo que actualiza el estado del pedido a ENTREGADO automaticamente en la lista del gestor de ventas|Repartidor|
|15|Reprogramar pedido|El pedido por alguna razon,como que el cliente no llegó al punto de encuentro,el codigo de compra era incorrecto, no se pudo entregar,el repartidor oprime la opcion de reprogramar pedido y el cliente debe establecer nueva fecha|Repartidor|

- Proceso de Marketing

![Proceso de Marketing](../Entregable2/ProcesosTOBE/BPMN_MARKETINGTOBE.jpeg)

- Proceso de Finanzas

![Proceso de Finanzas](../Entregable2/ProcesosTOBE/ProcesoFinanzasTOBE.png)

- Proceso de CRM

![Proceso de CRM](../Entregable2/ProcesosTOBE/Proceso-CRM-BPMN.png)

### 1.3 Motivación
-
## 2. Módulos
### 2.1 Módulo Compra-Proveedores
- Descripción: Este módulo de compra-proveedores permite al gestor de compras añadir nuevos proveedores a la base de datos de la empresa, así como también facilita la gestión de las ofertas recibidas de dichos proveedores. Desde aceptar hasta rechazar ofertas, además permite la visualización completa de los datos del proveedor, desde sus datos hasta el historial de ofertas que han realizado a la empresa, este modulo tiene el fin de poder optimizar el proceso de gestión de compras realizadas a los proveedores.

- Responsabilidades: Gestionar el proceso de compra, elección de proveedores, añadir nuevos proveedores, subir los archivos de la cotizacion que el proveedor le ofrece y confirmar o rechazar las ofertas del proveedor.

- Interacción: Con el módulo de almacen y finanzas.

- Funcionalidad:

  **- Home Gestor Compra**
    - Responsabilidades: Permite al gestor de compras tener su propia vista de las partes que constituyen su módulo, como son la visualizacion de proveedores, acceso al stock y acceso a finanzas.

  **- Proveedores Actuales**
    - Responsabilidades: Permite al gestor visualizar y acceder al historial de todos los proveedores con las que la empresa esta trabajando.

  **- Añadir proveedores**
    - Responsabilidades: Permite al gestor de compras añadir nuevos proveedores con los que va a trabajar.

  **- Perfil del proveedor**
    - Responsabilidades: Permite al gestor de compras visualizar, gestionar y actualizar la información de los proveedores con los que está trabajando.

  **- Historial del proveedor**
    - Responsabilidades: Muestra al gestor de compras un registro detallado de las ofertas no aceptadas, aceptadas y pendientes por aceptar/rechazar, dentro de la plataforma a lo largo del tiempo. Además permite que el gestor pueda realizar un seguimiento de sus ofertas pasadas.

  **- Datos de cotización**
    - Responsabilidades: Permite visualizar el detalle de la cotización de productos que ha realizado el proveedor a la empresa.

  **- Confirmar Oferta**
    - Responsabilidades: Permite al gestor de compras aceptar o rechazar la oferta final que ha realizado el proveedor hacia la empresa.

### 2.2 Módulo Venta
### 2.3 Módulo Almacén
### 2.4 Módulo Distribución

- Descripcion: Este modulo de distribucion permite al cliente ver el estado de sus pedidos,al gestor de ventas acceder a la base de datos de los pedidos para ver los detalles de las entregas y asignarles un repartidor,y este ultimo podra visualizar la lista de pedidos pendientes que se les asigno accediendo a la base datos y actualizar los estados de los pedidos.

- Responsabilidades: Gestionar las entregas de los pedidos,asignarles una fecha,elegir el repartidor,ver detalles de la entrega,actualizar los estados de entrega,y notificarle al cliente la llegada de su pedido.

- Interacción: Con el módulo de ventas y almacen.

- Detalles de estado:

  - CANCELADO: El pedido ha sido reprogramado,el cliente cambió la fecha,por lo que se cancela la entrega del pedido en la fecha pre-establecida.
  - PENDIENTE: El pedido aun no ha sido entregado.
  - ENTREGADO: El pedido fue entregado al cliente con exito.

- Funcionalidad:

  **- Home Gestor Ventas**
    - Responsabilidades: Permite al gestor de ventas tener su propia vista de las partes que constituyen su módulo, como son el acceso al historial de ventas, pedidos y gestion de los pedidos .

  **- Gestionar pedidos**
    - Responsabilidades: Permite al gestor de ventas vizualizar los pedidos,su estado y si hay asignado o no un repartidor para cada entrega.

  **- Asignar repartidor**
    - Responsabilidades: Permite al gestor de ventas asignar un repartidor a cada pedido para su respectiva entrega.

  **- Ver mas**
    - Responsabilidades: Permite al gestor de ventas y el repartidor visualizar los detalles de la entrega,nombre del cliente,fecha,hora,dirrecion,y los detalles del repartidor.

  **- Eliminar X-gestor de ventas**
    - Responsabilidades: Permite al gestor de ventas eliminar pedidos cancelados o entregados de la lista de gestion de pedidos,estos pasan automaticamente al historial de pedidos.

  **- Historial de pedidos-gestor de ventas**
    - Responsabilidades: Permite al gestor de ventas visualizar todos los pedidos,entregados o cancelados, que se realizaron en el mes.

  **- Home Repartidor**
    - Responsabilidades: Permite al repartidor tener su propia vista de las partes que constituyen su módulo, como son el acceso al la lista de sus pedidos pendientes y el historial de sus entregas .

  **- Pedidos pendientes**
    - Responsabilidades: Permite al repartidor visualizar los pedidos que se le asignaron,sus detalles y estado.

  **- Aceptar-repartidor**
    - Responsabilidades: Permite al repartidor,que esta listo con el pedido para la entrega,aceptar el pedido para dirigirse a la direccion dada,lo cual actualiza y notifica al cliente con "SU PEDIDO ESTA EN CAMINO".

  **- Entregado-repartidor**
    - Responsabilidades: Permite al repartidor,que ya hizo la entrega, actualizar el estado del pedido de "PENDIENTE" a "ENTREGADO",tanto para la lista del gestor de ventas y para el historial del repartidor.

  **- Eliminar X-repartidor**
    - Responsabilidades: Permite al repartidor eliminar pedidos cancelados de su lista de pedidos pendientes,estos pasan automaticamente a su historial de pedidos.    

  **- Reprogramar-repartidor**
    - Responsabilidades: Permite al repartidor,que no logro entregar el pedido,por codigo incorrecto o ausencia del cliente,hacer una reprogramacion de la fecha.

  **- Ver mis pedidos**
    - Responsabilidades: Permite al cliente visualizar el estado de sus pedidos y sus detalles.

  **- Ver detalles de su compra**
    - Responsabilidades: Permite al cliente ver los detalles de la compra que realizó,como la fecha,hora,los productos que compró,su precio y el monto total .

  **- Establecer la fecha y hora de entrega**
    - Responsabilidades: Permite al cliente establecer la hora y la fecha en la que se va a realizar la entrega.

  **- Reprogramar fecha**
    - Responsabilidades: Permite al cliente reprogramar la fecha de la entrega de su producto,dado el caso que ocurra un imprevisto,lo cual cancela la entrega del pedido con la antigua fecha.

  **- Ver detalles de la entrega**
    - Responsabilidades: Permite al cliente ver los detalles de la entrega,como la fecha,hora,el perfil del repartidor que fue asignado.


### 2.5 Módulo Marketing
### 2.6 Módulo Finanzas
### 2.7 Módulo CRM

## 3. Requerimientos
### 3.1 Requerimientos Funcionales

**Caso de uso N°1: Añadir proveedor**

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

**Caso de uso N°2: Aceptar/Rechazar oferta del proveedor**

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

**Caso de uso N°3: Visualizar proveedores/historial**

| Objetivo | <p align="left">  Permitir a los gestores poder acceder  y visualizar los proveedores y registros, con sus datos. </p> | 
|:--------------:|--------------|
| Descripción | Proceso mediante el cual los administradores pueden acceder a las finanzas y datos relevantes para evaluar la utlización de los recursos. | 
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

## 4. Prototipo
- Para ver el prototipo debe ingresar al siguiente enlace:

[Figma](https://www.figma.com/file/JaEtbwPTFhxpp8rVLio8Lc/Proyecto-Migni-Store?type=design&node-id=56-105&mode=design&t=6vRNAXtGiQCHDJhl-0)

## 5. Modelado Conceptual
### 5.1 Diagrama de entidad relación
- Modelo Conceptual

![Modelo Conceptual](Modelo%20conceptualv1.png)


## 6. Modelado Relacional
### 6.1 Modelo Lógico
![Modelo Lógico](Modelo_Logico.png)
[Modelo Lógico](https://drive.google.com/file/d/1_JcvnJOoGrkaA1rP-jQhsR2sMmhgNscB/view?usp=sharing)

# ENTREVISTA
## Link
- [Entrevista1](https://drive.google.com/drive/folders/1TTn2h-Z3sSz5ciMGMDi5mqIKiaWJ94f7?usp=sharing)
[![Video](https://img.youtube.com/vi/9kZT8WSCRc4/0.jpg)](https://www.youtube.com/watch?v=9kZT8WSCRc4)

# VIDEOS INDIVIDUALES



