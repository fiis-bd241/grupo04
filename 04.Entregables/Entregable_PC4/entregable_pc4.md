# 1. Índices y otros objetos de BD

## 1.1 Índices

### Índice RUC
```sql
DROP INDEX IX_RUC;
CREATE INDEX IX_RUC ON cotizacion(ruc_proveedor);

EXPLAIN ANALYZE
SELECT * FROM cotizacion
WHERE ruc_proveedor = '20780385968';
```
Proceso Sin Índice:
![image](SININDICE_RUC.png)

Proceso Con Índice:
![image](INDICE_RUC.png)

### Índice fecha_fin
```sql
DROP INDEX IX_fecha_fin;
CREATE INDEX IX_fecha_fin ON campaña(fecha_fin);

EXPLAIN ANALYZE
SELECT * FROM campaña
WHERE CURRENT_DATE BETWEEN fecha_ini AND fecha_fin;
```
Proceso Sin Índice:
![image](marketing_sin_index.png)

Proceso Con Índice:
![image](marketing_con_index.png)


# 2. PL/pgSQL – Proceso Batch

# 3. Actualizaciones a la Arquitectura de la Aplicación

## 3.1 Stack Tecnológico
| Stack                         | Detalle                                               |
|-------------------------------|-------------------------------------------------------|
| Lenguaje de programación      | Python <br>![Python](https://img.shields.io/badge/Python-3.9-yellow.svg?style=for-the-badge&logo=python&logoColor=white)|
| Librería GUI                  | Tkinter <br> ![Tkinter](https://img.shields.io/badge/Tkinter-blue.svg?style=for-the-badge&logo=python&logoColor=white)|
| Editor de código              | Visual Studio Code <br> ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-1.89.0-skyblue.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)|
| Base de datos                 | PostgreSQL <br> ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14.0-skyblue.svg?style=for-the-badge&logo=postgresql&logoColor=white)|
| Controlador de base de datos  | pgAdmin <br> ![pgadmin](https://img.shields.io/badge/pgAdmin-4-blue.svg?style=for-the-badge&logo=pgadmin)|

## 3.2 Diagrama de componentes

![image](https://github.com/fiis-bd241/grupo04/blob/main/04.Entregables/Entregable_PC3/DIAGCOMP.png)

# 4. Versión Final de la Aplicación
## Módulo de Compras

[CÓDIGO](MOD_COMPRAS/Proveedores)
[marketing](MOD_MARKETING)
# 5. Próximos Pasos

## Módulo de Compras
#### Cotizaciones por proveedor 
- Como parte de los requerimientos iniciales que se planteo para el proyecto se consideraba que uno podía acceder a cada proveedor individualmente y desde ahí poder ver un historial personalizado de las cotizaciones realizadas por un proveedor. Sin embargo, por el momento lo que se tiene en el aplicativo es un historial general de todas las cotizaciones que se han realizado.
#### Productos por Proveedor
* También se había considerado tener un historial de los precios de cada producto que nos da el proveedor, y tener a partir de ahí poder compararlo con otros proveedores para poder elegir de forma mas eficiente con que proveedor trabajar.

Ambos casos planteados previamente en el módulo de compra podrían ser realizados si se rediseña el aplicativo, optando talvez por el uso de otra tecnología aparte de un aplicativo de escritorio, por ejemplo, librerías personalizadas que nos permiten facilitar ciertas selecciones tanto en las cotizaciones como en los productos ofrecidos por los proveedores.



# 6. Videos individuales

[Quispe Mitma Cesar](../../06.Videos_Individuales/VideosPC4/Quispe_Mitma_Cesar_Fernando-VideoIndividual.md)
