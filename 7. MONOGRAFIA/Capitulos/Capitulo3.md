# Capítulo 03: Módulos
###  Módulo Marketing

- Descripción: Este módulo de gestión de publicidad permite al gestor de marketing tener control sobre las campañas realizadas por el equipo de maeketing con el fin de atraer más clientes. El gestor de marketing puede visualizar y editar las campañas vigentes, además puede revisar y tomar decisiones sobre las campañas propuestas comunicandose con el equipo de marketing encargado.

- Responsabilidades: Gestionar las campañas vigentes, revisar aceptando o rechazando campañas propuestas, comunicar observaciones al equipo de marketing generador de la campaña en caso de rachazar. 

- Interacción: Con el módulo de compras y almacén.

- Detalles de estado:
  - VIGENTE: La campaña esta vigente, se pueden editar algunos aspectos como la fecha final y la modalidad de la publicidad, además de agregar o quitar algunos productos y /o servicios y cambiar la direcion 
    del archivo de publicidad.
  - PROPUESTA: La campaña esta a disposición del gerente de marketing, dependiendo de su desición, esta puede pasar a ser aceptada o rechazada.
  - ACEPTADA: La campaña ha sido aceptada, por lo tanto estará en espera a entrar en vigencia dependiendo de su fecha de inicio y fecha final.
  - RECHAZADA: La campaña ha sido rechazada, el director de marketing le comunica las observaciones al equipo de marketing para su corrección.

- Funcionalidad:

  **- Home Gestor de marketing**
    - Responsabilidades: Permite al gestor de marketing tener acceso a las funciones de campañas vigentes y campañas propuestas.

  **- Campañas vigentes**
    - Responsabilidades: Permite al gestor visualizar las campañas vigentes.

  **- Editar campaña**
    - Responsabilidades: Permite al gestor editar las campañas vigentes, puede cambiar información correspondiente a cada campaña.
    - 
  **- Campañas propuestas**
    - Responsabilidades: Permite al gestor de marketing visualizar las campañas propuestas por el equipo de marketing.
      
  **- Registrar observaciones**
    - Responsabilidades: Permite al gestor de marketing comunicar observaciones al equipo de marketing después de rechazar su propuesta de campaña correspondiente.

  **- Proponer campaña**
    - Responsabilidades: Permite al equipo de marketing generar campañas para la posterior revision del gestor de marketing.

 ### Módulo Compra-Proveedores
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

### Módulo Distribución

- Descripcion: Este modulo de distribucion permite al cliente ver el estado de sus pedidos,al gestor de ventas acceder a la base de datos de los pedidos para ver los detalles de las entregas y asignarles un repartidor,y este ultimo podra visualizar la lista de pedidos pendientes que se les asigno accediendo a la base datos y actualizar los estados de los pedidos.

- Responsabilidades: Gestionar las entregas de los pedidos,asignarles una fecha,elegir el repartidor,ver detalles de la entrega,actualizar los estados de entrega,y notificarle al cliente la llegada de su pedido.

- Interacción: Con el módulo de ventas y almacen.

- Detalles de estado:

  - CANCELADO: El pedido ha sido reprogramado,el cliente cambió la fecha,por lo que se cancela la entrega del pedido en la fecha pre-establecida.
  - PENDIENTE: El pedido aun no ha sido entregado.
  - ENTREGADO: El pedido fue entregado al cliente con exito.

- Funcionalidad:

  **- Home Gestor de distribucion**
    - Responsabilidades: Permite al gestor de ventas tener su propia vista de las partes que constituyen su módulo, como son el acceso al historial de ventas, pedidos y gestion de los pedidos .

  **- Gestionar pedidos**
    - Responsabilidades: Permite al gestor de distribucion vizualizar los pedidos,su estado y si hay asignado o no un repartidor para cada entrega.

  **- Asignar repartidor**
    - Responsabilidades: Permite al gestor de distribucion asignar un repartidor a cada pedido para su respectiva entrega.

  **- Historial de pedidos-gestor de distribucion**
    - Responsabilidades: Permite al gestor de distribucion visualizar todos los pedidos,entregados o cancelados, que se realizaron en el mes.

  **- Home Repartidor**
    - Responsabilidades: Permite al repartidor tener su propia vista de las partes que constituyen su módulo, como son el acceso al la lista de sus pedidos pendientes y el historial de sus entregas .

  **- Pedidos pendientes**
    - Responsabilidades: Permite al repartidor visualizar los pedidos que se le asignaron,sus detalles y estado.

  **- Aceptar-repartidor**
    - Responsabilidades: Permite al repartidor,que esta listo con el pedido para la entrega,aceptar el pedido para dirigirse a la direccion dada,lo cual actualiza y notifica al cliente con "SU PEDIDO ESTA EN CAMINO".

  **- Entregado-repartidor**
    - Responsabilidades: Permite al repartidor,que ya hizo la entrega, actualizar el estado del pedido de "PENDIENTE" a "ENTREGADO",tanto para la lista del gestor de distribucion y para el historial del repartidor.

  **- Ver mis pedidos**
    - Responsabilidades: Permite al cliente visualizar el estado de sus pedidos y sus detalles.

  **- Ver detalles de su compra**
    - Responsabilidades: Permite al cliente ver los detalles de la compra que realizó,como la fecha,hora,los productos que compró,su precio y el monto total .

  **- Establecer la fecha de entrega**
    - Responsabilidades: Permite al cliente establecer la fecha en la que se va a realizar la entrega.

  **- Ver detalles de la entrega**
    - Responsabilidades: Permite al cliente ver los detalles de la entrega,como la fecha,el perfil del repartidor que fue asignado.


