# Capítulo 03: Módulos
## Módulo Marketing

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

 ## Módulo Compra-Proveedores
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

## Módulo Distribución

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

## Módulo de Finanzas
- Descripción: Este módulo permite obtener las facturas y verificar su estado, facilitando la realización de asientos contables relacionados con ingresos y gastos derivados de compras, ventas, gastos y pagos. Esto es esencial para elaborar el estado de resultados y generar un reporte que muestre las ganancias de la empresa.

- Responsabilidades: Registrar, editar y ver facturas; ver y editar asientos contables; ver estado de resultados que permita editar, verificar y enviar comentarios, ver resumen contable así como el reporte contables que permita enviar comentarios así como acotaciones; gestionar y asignar presupuestos.

- Interacción: Con el módulo de compras , almacén, ventas y marketing.
- Detalles de Estado:
  - Facturas:
     - VIGENTE: Las facturas están activas y pueden ser editadas en cuanto a fecha y modalidad de pago, además de agregar o quitar productos y/o servicios.
     - PROPUESTA: Las facturas están a disposición del contador general así como el gerente general para su revisión y decisión de aceptación o rechazo.
     - ACEPTADA: Las facturas han sido aceptadas y están en espera para ser registradas en los sistemas contables.
     - RECHAZADA: Las facturas han sido rechazadas y el contador contable comunica las observaciones necesarias para su corrección.
  - Presupuesto:
     - VIGENTE: El presupuesto está activo y puede ser editado para ajustar cifras y conceptos según necesidades actuales.
     - PROPUESTA: El presupuesto está a disposición del contador general y del gerente general para su revisión y decisión de aceptación o rechazo.
     - ACEPTADA: El presupuesto ha sido aceptado y está listo para su implementación en las operaciones de la empresa.
     - RECHAZADA: El presupuesto ha sido rechazado y el contador general comunica las observaciones necesarias para su corrección.
  - Asientos contables:
     - VIGENTE: Los asientos contables están activos y pueden ser creados, revisados y aprobados según sea necesario.
     - PROPUESTA: Los asientos contables están a disposición del contador general para su revisión y decisión de aceptación o rechazo.
     - ACEPTADA: Los asientos contables han sido aceptados y registrados en el sistema contable.
     - RECHAZADA: Los asientos contables han sido rechazados y el contador general comunica las observaciones necesarias para su corrección
  - Estado de resultados:
     - VIGENTE: El estado de resultados está activo y puede ser consultado y editado para reflejar las operaciones actuales.
     - PROPUESTA: El estado de resultados está a disposición del contador general para su revisión y aprobación.
     - ACEPTADA: El estado de resultados ha sido aprobado y está listo para su presentación.
     - RECHAZADA: El estado de resultados ha sido rechazado y se comunican las observaciones necesarias para su corrección.
- Funcionalidad:

  **- Home Contador General**
    - Responsabilidades: Permite al contador general tener acceso a funciones como el registro de facturas, visualización de resúmenes contables y generación de reportes contables.

  **- Historial de Ventas y Compras**
    - Responsabilidades: Mostrar un registro detallado de todas las transacciones de ventas y compras realizadas por la empresa.
    - Funciones: Filtrar y buscar transacciones por fecha, cliente, proveedor, producto, etc.

  **- Registro Automatizado de Facturas**
    - Responsabilidades: Permitir el registro automático de facturas de ventas y compras.
    - Funciones:Reconocimiento automático de datos relevantes en las facturas para facilitar el proceso de registro.
      
  **- Campañas propuestas**
    - Responsabilidades: Permite al gestor de marketing visualizar las campañas propuestas por el equipo de marketing designado, además de poder desplegar la vista de revisar campaña.

  **- Asientos Contables Automatizados**
    - Responsabilidades: Generar automáticamente asientos contables basados en las transacciones registradas.
    - Funciones:Integrar con el módulo de ventas y compras para capturar datos necesarios para la contabilidad.
      
  **- Estado de Resultados Automatizado**
    - Responsabilidades: Calcular automáticamente el estado de resultados utilizando la información de ventas, compras, gastos y pagos.
    - Funciones: Mostrar ingresos, costos de ventas, gastos operativos y beneficios netos.

  **- Reportes Financieros**
    - Responsabilidades: Generar reportes financieros personalizados en el que pueda deesglosar y filtrar por producto, periodo, año, etc.
    - Funciones: Permitir el análisis de diferentes parámetros asignados para los ingresos, egresos, etc.
  
  **- Presupuestos**
    - Responsabilidades: Gestionar la creación y revisión de presupuestos financieros.
    - Funciones: Proyectar ingresos y gastos futuros. Ajustar presupuestos según necesidades cambiantes de la empresa.
      
  **- Alertas y Notificaciones**
    - Responsabilidades: Enviar alertas sobre transacciones pendientes, vencimientos de pagos y otras actividades financieras importantes.
      
  **- Integración con Otros Módulos**
    - Responsabilidades: Integrar con módulos de almacén, marketing, compras y ventas.
    - Funciones: Obtener una visión completa de la situación financiera de la empresa.
       
  **- Análisis Financiero**
    - Responsabilidades: Ofrecer herramientas de análisis financiero.
    - Funciones: Evaluar la rentabilidad, liquidez y solvencia de la empresa. Realizar proyecciones financieras y escenarios hipotéticos para la toma de decisiones 
      estratégicas.


## Módulo CRM

- Descripción: Este módulo está diseñado para gestionar la interacción con los clientes a través de diversos canales, clasificar y analizar comentarios, y facilitar la comunicación masiva vía WhatsApp y correo electrónico. Además, incluye herramientas de análisis de datos para identificar tendencias de compra y productos menos comprados, así como la visualización de tablas en PostgreSQL y la clasificación de usuarios mediante un pipeline.

- Responsabilidades: Gestionar y clasificar comentarios de usuarios,puntuar comentarios basados en la posibilidad de compra,hacer formularios,enviar y atender mensajes de WhatsApp y correos electrónicos,realizar análisis de datos para detectar tendencias de compra y productos menos comprados,visualizar y gestionar tablas en PostgreSQL yclasificar usuarios mediante un pipeline.

- Interacción: Con el módulo de ventas y soporte técnico.

- Detalles de estado:
  
  - Comentarios de Usuarios
  - NUEVO: Comentarios recién recibidos que aún no han sido clasificados.
  - CLASIFICADO: Comentarios que han sido analizados y categorizados.
  - PUNTUADO: Comentarios que han sido puntuados según la posibilidad de compra.


  - Mensajes de WhatsApp y Correo Electrónico
  - ENVIADO: Mensajes que han sido enviados a múltiples destinatarios.
  - ATENDIDO: Mensajes que han recibido una respuesta y han sido gestionados.
  
  
  - Análisis de Datos
  - PROCESADO: Datos que han sido analizados para detectar tendencias de compra y productos menos comprados.

  - Tablas de PostgreSQL
  VISUALIZADO: Tablas que han sido consultadas por el gestor de CRM.

  - Clasificación de Usuarios
  - NUEVO: Usuarios que han sido recién ingresados al pipeline.
  - CALIFICADO: Usuarios que han sido evaluados y clasificados según criterios definidos.



- Funcionalidad:

  **- Home Gestor de CRM**
    - Responsabilidades: Permite al gestor de CRM acceder a las funciones principales del módulo, como la gestión de comentarios, el envío de mensajes, el análisis de datos, la visualización de tablas y la clasificación de usuarios.

  **- Gestión de Comentarios**
    - Responsabilidades: Permite al gestor clasificar y puntuar los comentarios de los usuarios en base a productos específicos y la posibilidad de compra.

  **- Enviar y Atender Mensajes de WhatsApp**
    - Responsabilidades: Facilita el envío masivo de mensajes de WhatsApp y la atención de respuestas recibidas.
    - 
  **- Enviar y Atender Mensajes de Email**
    - Responsabilidades: Facilita el envío masivo de correos electrónicos y la gestión de las respuestas recibidas.
      
  **- Análisis de Datos**
    - Responsabilidades: Permite al gestor analizar datos para identificar productos menos comprados y tendencias de compra de los clientes.


  **- Visualización de Tablas de PostgreSQL**
    - Responsabilidades: Permite al gestor de CRM visualizar y gestionar las tablas de la base de datos PostgreSQL para obtener una visión completa de la información.

  **- Clasificación de Usuarios mediante Pipeline**
    - Responsabilidades: Permite al gestor clasificar usuarios en diferentes etapas del pipeline según su interacción y calificación.

 