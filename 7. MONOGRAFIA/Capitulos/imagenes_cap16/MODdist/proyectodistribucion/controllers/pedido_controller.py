from config.database import get_db_connection

def obtener_historial_pedidos():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT id_pedido, id_venta, id_est_pedido
        FROM pedido
    """)
    pedidos = cur.fetchall()
    cur.close()
    conn.close()
    return [{"id_pedido": p[0], "id_venta": p[1], "id_est_pedido": p[2]} for p in pedidos]

def obtener_pedidos_pendientes():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT id_pedido, id_venta, id_est_pedido
        FROM pedido
        WHERE id_est_pedido = 'P'
    """)
    pedidos = cur.fetchall()
    cur.close()
    conn.close()
    return [{"id_pedido": p[0], "id_venta": p[1], "id_est_pedido": p[2]} for p in pedidos]

