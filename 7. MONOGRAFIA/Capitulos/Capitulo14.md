# Capítulo 14: PL/pgSQL - Proceso Batch

- Proceso Batch para actualizar_stock_inventario que calcula y actualiza el campo stock en la tabla Inventario para cada producto, basado en las entradas y salidas registradas. Se ejecuta mensualmente como parte de un proceso batch para mantener actualizado el stock en tu base de datos


-- Creación de la función PL/pgSQL para actualizar el stock en el inventario
CREATE OR REPLACE FUNCTION actualizar_stock_inventario()
RETURNS VOID AS $$
DECLARE
    producto_id VARCHAR(8);
    cantidad_actual INT;
    nuevo_stock INT;
BEGIN
    -- Iterar sobre los productos en el inventario
    FOR producto_id IN SELECT id_producto FROM Inventario LOOP
        -- Calcular el stock actual
        SELECT (entradas - salidas) INTO cantidad_actual
        FROM Inventario
        WHERE id_producto = producto_id;
        
        -- Actualizar el stock en la tabla de Inventario
        UPDATE Inventario
        SET stock = cantidad_actual
        WHERE id_producto = producto_id;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

-- Ejecutar la función para actualizar el stock al crearla
SELECT actualizar_stock_inventario();
