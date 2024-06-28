# Capítulo 02: Requerimientos
## Requerimientos Funcionales
### Casos de uso para Marketing
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

### Casos de uso para Compras
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


### Requerimientos de atributos de Calidad

   **Simplicidad y Facilidad de Uso:**
   - La página web debe ser intuitiva y fácil de usar, especialmente para usuarios nuevos. Se deben evitar interfaces complicadas que puedan confundir a los 
     usuarios.
   **Rendimiento:**
   - La página web debe cargar rápidamente y proporcionar una experiencia de usuario fluida en todos los dispositivos y conexiones a internet. Se debe minimizar 
     el tiempo de carga de las páginas y optimizar el rendimiento del sitio.

### Restricciones:

   **Compatibilidad con Navegadores:**
   - La página web debe ser compatible con una variedad de navegadores web modernos, incluidos Chrome, Firefox, Safari y Edge, para garantizar una experiencia de 
     usuario consistente.

   **Cumplimiento Legal Básico:**
   - Se deben cumplir con las leyes y regulaciones básicas relacionadas con la protección de datos y la privacidad en línea, pero considerando la capacidad 
     limitada de recursos para cumplir con estándares más complejos desde el principio.
