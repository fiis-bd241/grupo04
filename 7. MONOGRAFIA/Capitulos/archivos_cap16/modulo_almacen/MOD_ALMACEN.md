# MODULO DE ALMACEN

## EXPLICACION DE LAS PANTALLAS
### GESTOR DE ALMACEN
- Menu Principal, donde se visualizarán las opciones de Inventario, Pedidos y Kardex

![Imagen](../../imagenes_cap16/mod_Almacen/Presentación.png)

Al dar clic en Iventario se visualizará todo el inventario disponible de los 2 almacenes, con los campos de tabla:
  - ID Producto
  - Nombre
  - Presentación
  - Color
  - Stock
  - Ubicación

Y que se puede filtrar bajos los parámetro:
  - Ver todo
  - Ver solo maquillaje
  - Ver solo papelería
  - Ver los productos que no se tiene Stock
  - Buscar por Codigo Producto que puede ser las 3 iniciales
  - Buscar por la marca del producto
  - Buscar por stock mínimo (si ingreso 15 me mostrará los producto que tengo más de 15und)
  - Buscar por categoría

Al dar clic en cada fila de la tabla que se muestra, en el lado derecho se mostrará la imagen del producto junto con su importe de inventario total que existe, y el volumen del producto para su respectivo despacho.

![Imagen](../../imagenes_cap16/mod_Almacen/Seleccionar_Fila.png)
*Acción de seleccionar una fila

query3 = '''
    SELECT 
        p.id_producto,
        i.path_imagen,
        (p.precio_unitario*(inv.entradas - inv.salidas)) AS importe,
        CONCAT(p.ancho_present*p.largo_present*p.alto_present,' cm³') AS volumen
            FROM 
                Producto p
            JOIN 
                Imagenes i ON p.id_producto = i.id_producto
            JOIN 
                Inventario inv ON p.id_producto = inv.id_producto
        '''
        cursor.execute(query3)
        img = cursor.fetchall()
        self.id_img_prod = {str(imagen[0]):
            {'path_imagen': imagen[1],'Importe': imagen[2],'Volumen': imagen[3]} for imagen in img}
  '''

![Imagen](../../imagenes_cap16/mod_Almacen/Filtro_Código.png)
* Filtrar por las iniciales PAL

![Imagen](../../imagenes_cap16/mod_Almacen/Filtro_Marca.png)
*Filtrar por Marca

![Imagen](../../imagenes_cap16/mod_Almacen/Filtro_Papeleria.png)
*Todo lo que es papelería

![Imagen](../../imagenes_cap16/mod_Almacen/Filtro_Sin_Stock.png)
*Productos que no se tiene Stock

![Imagen](../../imagenes_cap16/mod_Almacen/Filtro_Stock_Minimo.png)
*Productos que tienes stock mayor al ingresado

![Imagen](../../imagenes_cap16/mod_Almacen/Filtro_Categoria.png)
*Filtrar por categoría del producto

![Imagen](../../imagenes_cap16/mod_Almacen/Accion_Ocultar.png)
*Para maximizar la pantalla, clic en el ícono al costado del nombre Migni Store

![Imagen](../../imagenes_cap16/mod_Almacen/Aviso_Sin_Busqueda.png)
*Mensaje si se da clic en buscar pero no se da ningún parámetro de entrada




## CODIGO DEL APLICATIVO
[APLICATIVO COMPRAS](archivos_cap16/modulo_almacen)
