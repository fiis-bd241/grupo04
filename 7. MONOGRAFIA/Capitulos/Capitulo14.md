# Capítulo 14: PL/pgSQL - Proceso Batch

- Proceso Batch para actualizar el stock de mi inventario que calcula y actualiza el campo stock en la tabla Inventario para cada producto, basado en las entradas y salidas registradas. Se ejecuta mensualmente como parte de un proceso batch para mantener actualizado el stock en tu base de datos

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
