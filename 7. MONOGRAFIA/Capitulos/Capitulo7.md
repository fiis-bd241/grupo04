# Capítulo 07: Validación del esquema (Look Up Tables)

### Cotizacion
- Tipo estado Cotizacion
Columnas: id_est_cotizacion, est_cotizacion

|id_est_cotizacion|est_cotizacion|
|----------------------|------------|
|A|Aceptado|
|N|No Aceptado|
|P|Pendiente|

### Proveedor

- Tipo estado Proveedor
Columnas: id_est_proveedor, est_proveedor

|id_est_proveedor|est_proveedor|
|----------------------|------------|
|A|Activo|
|N|No Activo|

![image](imagenes_cap7/P1.png)

### Pedido
- Tipo estado pedido
Columnas: id_est_pedido, estado_pedido

|id_est_pedido|estado_pedido|
|----------------------|------------|
|E|ENTREGADO|
|P|PENDIENTE|
|C|CANCELADO|

### Estado_Cliente
Columnas: id_estado_cliente, id_estado_cliente

|id_estado_cliente|id_estado_cliente|
|----------------------|------------|
|A|Activo|
|C|No concurrente|
|F|Falta pago|
|I|Incomunicado|

### Tipo_Almacén
Columnas: id_almacen, tipo_almacen

|id_almacen|tipo_almacen|
|----------------------|------------|
|A1|Maquillaje|
|A2|Papelería|

### Tipo_Movimiento
Columnas: id_movimiento,nombre_movimiento

|id_movimiento|nombre_movimiento|
|----------------------|------------|
|1|Salida Entrega|
|2|Salida Despacho|
|3|Salida Envío|
|4|Entrada Recepción|
|5|Entrada Devolución|

### Tipo_Entrega
Columnas: id_tipo_entrega,nombre_tipo_entrega

|id_tipo_entrega|nombre_tipo_entrega|
|----------------------|------------|
|A|Domicilio|
|B|Recojo|
|C|Envío|

### Estado_Pedido
Columnas: id_estado_pedido,nombre_tipo_entrega

|id_estado_pedido|nombre_estado_pedido|
|----------------------|------------|
|L|Leído|
|P|En Preparación|
|D|Despachado|
|R|Retornado|





