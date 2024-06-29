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

```py
query2 = '''
          SELECT
            i.id_producto,
            p.nombre_producto,
            pr.tipo_presentacion,
            c.nombre_color,
            (i.entradas - i.salidas) AS stock,
            CONCAT(i.seccion, '-', i.id_stand, '-', i.id_repisas) AS ubicacion
            FROM Inventario i
            JOIN Producto p ON i.id_producto = p.id_producto
            JOIN Presentacion pr ON p.id_presentacion = pr.id_presentacion
            JOIN Colores c ON p.id_color = c.id_color
        '''
        cursor.execute(query2)
        self.tabla_frame(cursor.fetchall())
```

```py
conn,cursor = bd.conectar()
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
 cursor.close()
conn.commit()
conn.close()
  '''
```

![Imagen](../../imagenes_cap16/mod_Almacen/Filtro_Código.png)
* Filtrar por las iniciales PAL
  
```py
query = '''
                    SELECT
                        p.id_producto,
                        p.nombre_producto,
                        pr.tipo_presentacion,
                        c.nombre_color,
                        (i.entradas - i.salidas) AS stock,
                        CONCAT(i.seccion, '-', i.id_stand, '-', i.id_repisas) AS ubicacion
                    FROM
                        Inventario i
                        JOIN Producto p ON i.id_producto = p.id_producto
                        JOIN Presentacion pr ON p.id_presentacion = pr.id_presentacion
                        JOIN Colores c ON p.id_color = c.id_color
                    WHERE
                        p.id_producto LIKE %s
                    ORDER BY
                        p.id_producto           
                '''
                cursor.execute(query,('%'+valor_producto+'%',))
                rows = cursor.fetchall()
```

![Imagen](../../imagenes_cap16/mod_Almacen/Filtro_Marca.png)
*Filtrar por Marca

```py
    query = '''
            SELECT id_marca FROM Marca
        '''
        cursor.execute(query)
        rows = cursor.fetchall()
        id_marcas = [marca[0] for marca in rows]
```

```py
query = '''
                    SELECT
                        p.id_producto,
                        p.nombre_producto,
                        pr.tipo_presentacion,
                        c.nombre_color,
                        (i.entradas - i.salidas) AS stock,
                        CONCAT(i.seccion, '-', i.id_stand, '-', i.id_repisas) AS ubicacion
                    FROM
                        Inventario i
                        JOIN Producto p ON i.id_producto = p.id_producto
                        JOIN Presentacion pr ON p.id_presentacion = pr.id_presentacion
                        JOIN Colores c ON p.id_color = c.id_color
                        JOIN Marca m ON p.id_marca = m.id_marca
                    WHERE
                        m.id_marca = %s
                    ORDER BY
                        p.id_producto
                '''
                cursor.execute(query,(valor_marca,))
                rows = cursor.fetchall()
```

![Imagen](../../imagenes_cap16/mod_Almacen/Filtro_Papeleria.png)
*Todo lo que es papelería

```py
query = '''
            SELECT
                i.id_producto,
                p.nombre_producto,
                pr.tipo_presentacion,
                c.nombre_color,
                (i.entradas - i.salidas) AS stock,
                CONCAT(i.seccion, '-', i.id_stand, '-', i.id_repisas) AS ubicacion
            FROM Inventario i
            JOIN Producto p ON i.id_producto = p.id_producto
            JOIN Presentacion pr ON p.id_presentacion = pr.id_presentacion
            JOIN Colores c ON p.id_color = c.id_color
            JOIN Categoria_Producto cp ON p.nombre_categoria = cp.nombre_categoria
            JOIN Tipo_Producto tp ON cp.id_tipo_producto = tp.id_tipo_producto
            WHERE tp.nombre_tipo_producto = 'Papelería';
        '''
        cursor.execute(query)
        self.tabla_frame(cursor.fetchall())
```

![Imagen](../../imagenes_cap16/mod_Almacen/Filtro_Sin_Stock.png)
*Productos que no se tiene Stock
```py
query = '''
          SELECT
                i.id_producto,
                p.nombre_producto,
                pr.tipo_presentacion,
                c.nombre_color,
                (i.entradas - i.salidas) AS stock,
                CONCAT(i.seccion, '-', i.id_stand, '-', i.id_repisas) AS ubicacion
            FROM
                Inventario i
            JOIN
                Producto p ON i.id_producto = p.id_producto
            JOIN
                Presentacion pr ON p.id_presentacion = pr.id_presentacion
            JOIN
                Colores c ON p.id_color = c.id_color
            WHERE
                (i.entradas - i.salidas) = 0
        '''
        cursor.execute(query)
        self.tabla_frame(cursor.fetchall())
```

![Imagen](../../imagenes_cap16/mod_Almacen/Filtro_Stock_Minimo.png)
*Productos que tienes stock mayor al ingresado

```py
query = '''
                    SELECT
                        p.id_producto,
                        p.nombre_producto,
                        pr.tipo_presentacion,
                        c.nombre_color,
                        (i.entradas - i.salidas) AS stock,
                        CONCAT(i.seccion, '-', i.id_stand, '-', i.id_repisas) AS ubicacion
                    FROM
                        Inventario i
                        JOIN Producto p ON i.id_producto = p.id_producto
                        JOIN Presentacion pr ON p.id_presentacion = pr.id_presentacion
                        JOIN Colores c ON p.id_color = c.id_color
                    WHERE
                        (i.entradas - i.salidas) >= %s
                    ORDER BY
                        p.id_producto
                '''
                cursor.execute(query,(valor_stock,))
                rows = cursor.fetchall()
```

![Imagen](../../imagenes_cap16/mod_Almacen/Filtro_Categoria.png)
*Filtrar por categoría del producto

```py
 query4 = '''
            SELECT nombre_categoria FROM Categoria_Producto
        '''
        cursor.execute(query4)
        rows = cursor.fetchall()
        id_categorias = [categoria[0] for categoria in rows]
```

```py
query = '''
                    SELECT
                        p.id_producto,
                        p.nombre_producto,
                        pr.tipo_presentacion,
                        c.nombre_color,
                        (i.entradas - i.salidas) AS stock,
                        CONCAT(i.seccion, '-', i.id_stand, '-', i.id_repisas) AS ubicacion
                    FROM
                        Inventario i
                        JOIN Producto p ON i.id_producto = p.id_producto
                        JOIN Presentacion pr ON p.id_presentacion = pr.id_presentacion
                        JOIN Colores c ON p.id_color = c.id_color
                        JOIN Categoria_Producto cp ON p.nombre_categoria = cp.nombre_categoria
                    WHERE
                        cp.nombre_categoria = %s
                    ORDER BY
                        p.id_producto
                '''
                cursor.execute(query,(valor_categoria,))
                rows = cursor.fetchall()
```

![Imagen](../../imagenes_cap16/mod_Almacen/Accion_Ocultar.png)
*Para maximizar la pantalla, clic en el ícono al costado del nombre Migni Store

![Imagen](../../imagenes_cap16/mod_Almacen/Aviso_Sin_Busqueda.png)
*Mensaje si se da clic en buscar pero no se da ningún parámetro de entrada

![Imagen](../../imagenes_cap16/mod_Almacen/Vista_Pedidos.png)
*Vista de la sección Pedidos que están en estado L (Leídos para procedor a preparar)

```py
  query = '''
            SELECT
                p.id_pedido,
                te.nombre_tipo_entrega,
                p.fecha_entrega,
                (p.fecha_entrega - CURRENT_DATE) AS dias_faltantes,
                p.cod_venta,
                CONCAT(pe.nombre, ' ', pe.primer_apellido) AS nombre_repartidor
            FROM
                Pedido p
            INNER JOIN
                Tipo_Entrega te ON p.id_tipo_entrega = te.id_tipo_entrega
            LEFT JOIN
                Persona pe ON p.id_repartidor = pe.id_persona
            WHERE
                p.id_estado_pedido = 'L'
        '''
        cursor.execute(query)
        self.tabla_frame(cursor.fetchall())
```
![Imagen](../../imagenes_cap16/mod_Almacen/Pedido_Detalles.png)
* Al dar clic en la fila de la tabla pedido, se mostrará al lado derecho los detalles de la venta que se ha efectuado

```py
query = '''
            SELECT 
                cxp.id_producto,
                p.nombre_producto,
                cxp.cantidad,
                CONCAT(inv.seccion, '-', inv.id_stand, '-', inv.id_repisas) AS ubicacion
            FROM 
                Pedido pd
            JOIN 
                Venta v ON pd.cod_venta = v.cod_venta AND pd.id_persona = v.id_persona
            JOIN 
                Cliente cl ON v.id_persona = cl.id_persona
            JOIN 
                ClientexProducto cxp ON cl.id_persona = cxp.id_persona
            JOIN 
                Producto p ON cxp.id_producto = p.id_producto
            LEFT JOIN
                Inventario inv ON p.id_producto = inv.id_producto
            WHERE 
                pd.id_pedido = %s
                AND pd.id_estado_pedido = 'L'
                AND v.id_estado_venta = 'C'   
        '''
        cursor.execute(query,(id_pedido,))
```
![Imagen](../../imagenes_cap16/mod_Almacen/Filtro_Entrega.png)
*Se puede filtrar para ver pedidos actuales o pasados por tipo de entrega o estado de pedido

```py
query = '''
                    SELECT
                        p.id_pedido,
                        te.nombre_tipo_entrega,
                        p.fecha_entrega,
                        (p.fecha_entrega - CURRENT_DATE) AS dias_faltantes,
                        p.cod_venta,
                        CONCAT(pe.nombre, ' ', pe.primer_apellido) AS nombre_repartidor
                    FROM
                        Pedido p
                    INNER JOIN
                        Tipo_Entrega te ON p.id_tipo_entrega = te.id_tipo_entrega
                    LEFT JOIN
                        Persona pe ON p.id_repartidor = pe.id_persona
                    WHERE
                        te.nombre_tipo_entrega = %s           
                '''
                cursor.execute(query,(valor_entrega,))
                rows = cursor.fetchall()
```
