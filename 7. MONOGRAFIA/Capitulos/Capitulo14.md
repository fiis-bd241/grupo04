# Capítulo 14: PL/pgSQL - Proceso Batch

- Proceso Batch del módulo de almacén para actualizar el stock de mi inventario que calcula y actualiza el campo stock en la tabla Inventario para cada producto, basado en las entradas y salidas registradas. Se ejecuta mensualmente como parte de un proceso batch para mantener actualizado el stock en tu base de datos

```sql

CREATE OR REPLACE FUNCTION actualizar_stock_inventario()
RETURNS VOID AS $$
DECLARE
    producto_id VARCHAR(8);
    cantidad_actual INT;
    nuevo_stock INT;
BEGIN

    FOR producto_id IN SELECT id_producto FROM Inventario LOOP
        -- Calcular el stock actual
        SELECT (entradas - salidas) INTO cantidad_actual
        FROM Inventario
        WHERE id_producto = producto_id;

        UPDATE Inventario
        SET stock = cantidad_actual
        WHERE id_producto = producto_id;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

SELECT actualizar_stock_inventario();
```

- Proceso Batch del módulo de almacén ingresar nuevos productos a mi tabla Producto, que puede ser en un periodo semestral al traer nueva mercancía para comercializar

```sql
DO $$
DECLARE
    valor_dado TEXT := 'nombre_categoria';
    primeras_tres_letras TEXT;
    numero_x INTEGER;
    id_producto_final TEXT;
    id_color INTEGER;
BEGIN
    -- Paso 1 y 2: Convertir las tres primeras letras a mayúsculas y concatenar con '0'
    primeras_tres_letras := UPPER(SUBSTRING(valor_dado FROM 1 FOR 3)) || '0';

    -- Paso 3: Contar las veces que aparece 'nombre_categoria' en mi tabla Producto actual
    SELECT COUNT(*) INTO numero_x
    FROM Producto
    WHERE nombre_categoria = 'nombre_categoria';

    -- Paso 4: Concatenar el resultado anterior con el número x
    id_producto_final := primeras_tres_letras || numero_x;

    -- Paso 5: Obtener los valores de los demás campos:

    SELECT id_color INTO id_color
    FROM Colores
    WHERE nombre_color = 'nombre_color;

    SELECT id_presentacion
    FROM Presentacion
    WHERE tipo_presentacion = 'nombre_presentacion'

    SELECT 
     CP.nombre_categoria
            FROM 
                Categoria_Producto CP
            JOIN 
                Tipo_Producto TP ON CP.id_tipo_producto = TP.id_tipo_producto
            WHERE 
                TP.nombre_tipo_producto = %s
   (SELECT M.id_marca
                FROM Marca M
                WHERE 
                M.rubro NOT LIKE '%Artículos%'
    O
    SELECT M.id_marca
                FROM Marca M
                WHERE 
                M.rubro LIKE '%Artículos%'
    )
    (SELECT tipo_presentacion
                FROM Presentacion
                WHERE 
                (id_presentacion >=1 AND id_presentacion <=16)
    O
     SELECT tipo_presentacion
                FROM Presentacion
                WHERE 
                (id_presentacion >=16 AND id_presentacion <=25)
    )
    -- Paso 6: Insertar estos valores en la tabla Producto
   INSERT INTO Producto (id_producto,id_presentacion,id_color,
    nombre_producto,id_marca,especificaciones,observaciones,
    precio_unitario,peso_unitario,ancho_present,largo_present,alto_present,
    fecha_creacion,fecha_actualizacion,cantidad_minima,nombre_categoria)
            VALUES(d_producto,id_presentacion,id_color,nombre_producto,id_marca,especificaciones,observaciones,precio_unitario,peso_unitario,ancho_present,largo_present,alto_present,CURRENT_DATE,CURRENT_DATE,6,nombre_categoria)

END $$;
```
- Proceso Batch para el Módulo de marketing, se actualizará los estados de observacion de la tabla obsservacion, el criterio para elegir será las observaciones que tengan asociada una campaña que ya finalizó, esto con el propósito de ya no mostrar campañas que ya finalizaron al equipo de marketing en su funcionalidad de "atender observación".

```sql
CREATE OR REPLACE FUNCTION actualizar_observaciones_campañas_finalizadas()
RETURNS VOID AS $$
DECLARE
    observacion_id INT;
    campaña_id INT;
    fecha_final DATE;
BEGIN
    FOR observacion_id, campaña_id IN
        SELECT id_observacion, id_campaña
        FROM Observacion
        WHERE estado_atendido = false
    LOOP
        SELECT c.fecha_fin INTO fecha_final
        FROM Campaña c
        WHERE c.id_campaña = campaña_id;
        
        IF fecha_final < CURRENT_DATE THEN  
            UPDATE Observacion
            SET estado_atendido = true
            WHERE id_observacion = observacion_id;
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

SELECT actualizar_observaciones_campañas_finalizadas();

```
