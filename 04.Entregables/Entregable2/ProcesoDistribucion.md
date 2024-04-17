# Proceso de distribucion AS IS


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

# Proceso de distribucion TO BE

|Secuencia|Proceso|Descripcion|Responsable|
|---------|-------|-----------|-----------|
|1        |Actualizacion de pedido en la lista de "mis pedidos"|El pedido aparece en la lista de "mis pedidos" del cliente|Cliente|
|2|Coordinar la fecha y hora|En la vista de "mis pedidos" el cliente establece la hora y fecha de entrega|Cliente|
|3|Actualizacion del pedido en la lista de pedidos|Se actualiza el estado del pedido en PENDIENTE y aparece en la vista del gestor de ventas|Gestor de ventas|
|4|Asignacion del repartidor disponible para la entrega|Se elige al repartidor que se encuentra disponible para la entrega|Gestor de ventas|
|5|Actualizacion del pedido en la lista del repartidor|El pedido aparece en la lista del repartidor al que se ha asignado|Repartidor|
|6|Cancelacion de entrega|El cliente cancela la entrega y se reprograma una nueva fecha|Cliente|
|7|Actualizacion de pedido a "CANCELADO"|El pedido se actualiza en "CANCELADO" en la lista de pedidos del gestor de ventas y de pedidos pendientes del repartidor si es que ya se le habia asignado|Gestor de ventas y repartidor|
|8|Preparacion del pedido|Se empaqueta los productos para su respectiva entrega|Gestor de ventas |
|9|Repartidor acepta el pedido|El repartidor entra en la lista de sus pedidos pendientes y acepta el pedido que va a entregar|Repartidor|
|10|Actualizacion de estado de pedido "SU PEDIDO ESTA EN CAMINO"|El pedido se actualiza en la lista de "mis pedidos" del cliente a "SU PEDIDO ESTA EN CAMINO"|Cliente|
|11|El repartidor llega al punto de encuentro|El repartidor se dirige al lugar de entrega hasta llegar al punto|Repartidor|
|12|Verificacion de código de compra|El repartidor se encuentra con el cliente y verifica si el código de compra que presenta el cliente es correcto|Repartidor y cliente|
|13|Recepcion del producto por el cliente|Verificado que el código es correcto,el cliente recibe el producto |Cliente|
|14|Actualizar el estado del pedido a "ENTREGADO"|El repartidor entra a la lista de sus pedidos y confirma que se ha entregado el pedido ,lo que actualiza el estado del pedido a ENTREGADO automaticamente en la lista del gestor de ventas|Repartidor|
|15|Reprogramar pedido|El pedido por alguna razon,como que el cliente no llegó al punto de encuentro,el codigo de compra era incorrecto, no se pudo entregar,el repartidor oprime la opcion de reprogramar pedido y el cliente debe establecer nueva fecha|Repartidor|
