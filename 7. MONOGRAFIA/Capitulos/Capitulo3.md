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
