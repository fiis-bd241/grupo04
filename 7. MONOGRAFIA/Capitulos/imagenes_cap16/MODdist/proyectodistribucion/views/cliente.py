import tkinter as tk
from tkinter import ttk
from config.database import get_db_connection

class ClienteView(tk.Toplevel):
    def __init__(self, root, id_persona):
        super().__init__(root)
        self.title("Historial de Compras")
        self.geometry("600x400")

        self.id_persona = id_persona

        self.compras_treeview = ttk.Treeview(self, columns=("id_venta", "fecha", "total"))
        self.compras_treeview.heading("#0", text="ID Venta")
        self.compras_treeview.heading("#1", text="Fecha")
        self.compras_treeview.heading("#2", text="Total")
        self.compras_treeview.pack(fill=tk.BOTH, expand=True)

        self.load_compras()

    def load_compras(self):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT id_venta, fecha, total
            FROM venta
            WHERE id_persona = %s
        """, (self.id_persona,))
        rows = cur.fetchall()

        for row in rows:
            self.compras_treeview.insert("", "end", text=row[0], values=(row[1], row[2]))

        cur.close()
        conn.close()

