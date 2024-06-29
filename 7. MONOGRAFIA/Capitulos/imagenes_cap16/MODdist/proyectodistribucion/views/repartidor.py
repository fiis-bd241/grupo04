import tkinter as tk
from tkinter import ttk
from config.database import get_db_connection

class RepartidorView(tk.Toplevel):
    def __init__(self, root, repartidor_id):
        super().__init__(root)
        self.title("Panel de Repartidor")
        self.geometry("400x300")
        self.repartidor_id = repartidor_id

        self.historial_button = tk.Button(self, text="Ver Historial de Pedidos", command=self.ver_historial)
        self.historial_button.pack()

        self.pendientes_button = tk.Button(self, text="Ver Pedidos Pendientes", command=self.ver_pendientes)
        self.pendientes_button.pack()

        self.volver_button = tk.Button(self, text="Cerrar Sesión", command=self.close_window)
        self.volver_button.pack()

    def ver_historial(self):
        historial_window = tk.Toplevel(self)
        historial_window.title("Historial de Pedidos")
        tree = ttk.Treeview(historial_window, columns=("id_pedido", "id_venta", "cliente", "estado", "fecha"))
        tree.heading("#0", text="ID Pedido")
        tree.heading("#1", text="ID Venta")
        tree.heading("#2", text="Cliente")
        tree.heading("#3", text="Estado")
        tree.heading("#4", text="Fecha")
        tree.pack(fill=tk.BOTH, expand=True)

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT p.id_pedido, p.id_venta, CONCAT(per.nombre, ' ', per.apellido1) AS cliente, p.id_est_pedido, p.fecha_entrega
            FROM pedido p
            JOIN venta v ON p.id_venta = v.id_venta
            JOIN persona per ON v.id_persona = per.id_persona
            WHERE p.id_repartidor = %s
        """, (self.repartidor_id,))
        rows = cur.fetchall()

        for row in rows:
            tree.insert("", "end", text=row[0], values=(row[1], row[2], row[3], row[4]))

        cur.close()
        conn.close()

    def ver_pendientes(self):
        pendientes_window = tk.Toplevel(self)
        pendientes_window.title("Pedidos Pendientes")
        tree = ttk.Treeview(pendientes_window, columns=("id_pedido", "id_venta", "cliente", "estado", "fecha"))
        tree.heading("#0", text="ID Pedido")
        tree.heading("#1", text="ID Venta")
        tree.heading("#2", text="Cliente")
        tree.heading("#3", text="Estado")
        tree.heading("#4", text="Fecha")
        tree.pack(fill=tk.BOTH, expand=True)

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT p.id_pedido, p.id_venta, CONCAT(per.nombre, ' ', per.apellido1) AS cliente, p.id_est_pedido, p.fecha_entrega
            FROM pedido p
            JOIN venta v ON p.id_venta = v.id_venta
            JOIN persona per ON v.id_persona = per.id_persona
            WHERE p.id_repartidor = %s AND p.id_est_pedido = 'P'
        """, (self.repartidor_id,))
        rows = cur.fetchall()

        for row in rows:
            tree.insert("", "end", text=row[0], values=(row[1], row[2], row[3], row[4]))

        cur.close()
        conn.close()

    def close_window(self):
        self.destroy()


