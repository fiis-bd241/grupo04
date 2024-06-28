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
