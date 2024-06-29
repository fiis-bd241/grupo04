# Capítulo 18: Aplicación de una base de datos NoSQL
## Desarrollo conceptual
### ¿Que es una base de datos NoSQL?
- Una base de datos NoSQL es un tipo de sistema de gestión de bases de datos que no utiliza el modelo relacional tradicional basado en tablas. En lugar de eso, almacena datos de manera más flexible, como en documentos JSON, pares clave-valor, gráficos o columnas, lo que permite un escalado horizontal más fácil y una mejor gestión de grandes volúmenes de datos no estructurados o semi-estructurados.

### ¿Qué es InfluxDB?
- InfluxDB es una base de datos de series temporales (TSDB) diseñada para manejar grandes volúmenes de datos con marcas de tiempo, como registros de eventos, métricas y datos de monitoreo en tiempo real. Es especialmente útil para aplicaciones que requieren almacenamiento y análisis de datos en tiempo real, como la monitorización de infraestructura, el análisis de datos de sensores IoT y el seguimiento de datos de rendimiento de aplicaciones. InfluxDB es parte de la plataforma TICK stack de InfluxData, que incluye herramientas para la recolección, almacenamiento, visualización y procesamiento de datos de series temporales.

## Descripción del escenario de uso
### Escenario de uso
- Se creará la tabla de cotizacion, gracias a que InfluxDB nos permite tener una marca de tiempo en el momento en que se realiza una insercion de datos, sera mucho mas facil trabajar con los tiempo pues automaticamente se asignara una marca de tiempo.

## Configuración
### Instalación de InfluxDB
1. En el buscador de google, buscamos influxdb y en la pagina principal, seleccionamos InfluxData Downloads
![image](ImagenCap18/1-1.png)
2. Ya dentro de la página: https://www.influxdata.com/downloads/ | copiamos el comando marcado abajo
![image](ImagenCap18/6.png)
3. Ahora ejecutamos Windows PowerSheell como administrador
![image](ImagenCap18/7.png)
4. Ejecutamos el comando que antes copiamos
![image](ImagenCap18/8.png)
5. Ejecutamos WindowsPowerShell en la carpeta donde se instalo y usamos el comando ".\influxdb.exe"
![image](ImagenCap18/9.png)
6. Nos sale este texto, que indica el puerto que tenemos habilitado para ejecutar influxdb
![image](ImagenCap18/10.png)
7. En nuestro navegador ponemos "http://127.0.0.1:8086/signin" y le damos a Get Started
![image](ImagenCap18/11.png)
8. Nos registramos y le damos a Continue
![image](ImagenCap18/12.png)
9. En este pantalla podemos configurar más a detalle, por el momento le daremos a Configure Later
![image](ImagenCap18/13.png)
10. Y listo tendriamos influxdb operativo para trabajar
![image](ImagenCap18/14.png)

## Implementación
### Trabajar con InfluxDB

![image](ImagenCap18/bucket.png)
![image](ImagenCap18/add_data.png)
![image](ImagenCap18/line_protocol.png)
![image](ImagenCap18/INS1.png)
![image](ImagenCap18/INS2.png)
![image](ImagenCap18/INS3.png)
![image](ImagenCap18/SELECT.png)
![image](ImagenCap18/SELECT2.png)
