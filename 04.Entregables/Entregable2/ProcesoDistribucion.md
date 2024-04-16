# Proceso de distribucion


|Secuencia|Proceso|Descripcion|Responsable|
|---------|-------|-----------|-----------|
|1        |Preparacion del pedido solicitado|Se separan los productos que se van a entregar.|Gestor de ventas|
|2|Coordinacion del lugar|El cliente y el gestor de ventas coordinan el lugar de entrega del producto|Gestor de ventas y cliente|
|3|Cotizacion de delivery|Si el lugar de entrega no se encuentra dentro de los puntos de encuentro disponibles, se cotiza el transporte realizado de acuerdo al lugar|Gestor de ventas|
|4|Coordinar la fecha y hora|Escogido el lugar de encuentro, se establece la hora y fecha de entrega|Gestor de ventas y cliente|
|5|Actualizacion del pedido|Se actualiza el estado del pedido en PENDIENTE|Gestor de ventas|
|6|Cancelacion de entrega|El cliente ha cancelado la entrega y el proceso termina|Cliente|
|7|Preparacion del pedido|Se empaqueta los productos para su respectiva entrega|Gestor de ventas |
|8|Eleccion del personal disponible para la entrega|Se elige al personal que se encuentra disponible y listo para la entrega|Repartidor|
|9|Personal en el punto de entrega|El personal llega al punto de entrega|Repartidor|
|10|Emision de nueva fecha de entrega|Si el cliente tiene demora en el punto de encuentro|Gestor de ventas |
|11|Verificacion de código de compra|Se verifica si el código de compra que presenta el cliente es correcto|Repartidor|
|12|Recepcion del producto por el cliente|Si el código es correcto,el cliente recibe el producto |Repartidor|
|13|Actualizar el estado de productos de almacen|Si la entrega se realiza con éxito,se actualiza el estado del pedido a ENTREGADO|Repartidor|

