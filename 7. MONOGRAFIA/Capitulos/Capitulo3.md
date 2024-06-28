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
