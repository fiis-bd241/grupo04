import tkinter as tk
from tkinter import ttk, messagebox
from config.database import get_db_connection

class GestorDistribucionView(tk.Toplevel):
    def __init__(self, root, on_volver):
        super().__init__(root)
        self.title("Panel de Gestor de Distribución")
        self.geometry("600x400")  # Ajusta el tamaño de la ventana
        self.configure(bg="pink")  # Color de fondo rosado
        self.on_volver = on_volver

        self.historial_button = tk.Button(self, text="Ver Historial de Pedidos", command=self.ver_historial, bg="green", fg="black")
        self.historial_button.pack(pady=10)

        self.pendientes_button = tk.Button(self, text="Ver Pedidos Pendientes", command=self.ver_pendientes, bg="green", fg="black")
        self.pendientes_button.pack(pady=10)

        self.volver_button = tk.Button(self, text="Volver", command=self.volver, bg="red", fg="black")
        self.volver_button.pack(pady=10)

    def ver_historial(self):
        historial_window = tk.Toplevel(self)
        historial_window.title("Historial de Pedidos")
        historial_window.geometry("800x600")  # Ajusta el tamaño de la ventana
        historial_window.configure(bg="pink")  # Color de fondo rosado

        tree = ttk.Treeview(historial_window, columns=("id_pedido", "id_venta", "cliente", "fecha", "estado"))
        tree.heading("#0", text="ID Pedido")
        tree.heading("#1", text="ID Venta")
        tree.heading("#2", text="Cliente")
        tree.heading("#3", text="Fecha")
        tree.heading("#4", text="Estado")
        tree.pack(fill=tk.BOTH, expand=True)

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT p.id_pedido, p.id_venta, CONCAT(per.nombre, ' ', per.primer_apell) AS cliente, 
                   p.fecha_entrega, p.id_est_pedido
            FROM pedido p
            INNER JOIN venta v ON p.id_venta = v.id_venta
            INNER JOIN persona per ON v.id_persona = per.id_persona
        """)
        rows = cur.fetchall()

        for row in rows:
            tree.insert("", "end", text=row[0], values=(row[1], row[2], row[3], row[4]))

        cur.close()
        conn.close()

    def ver_pendientes(self):
        pendientes_window = tk.Toplevel(self)
        pendientes_window.title("Pedidos Pendientes")
        pendientes_window.geometry("800x600")  # Ajusta el tamaño de la ventana
        pendientes_window.configure(bg="pink")  # Color de fondo rosado

        tree = ttk.Treeview(pendientes_window, columns=("id_pedido", "id_venta", "cliente", "fecha", "repartidor", "estado"))
        tree.heading("#0", text="ID Pedido")
        tree.heading("#1", text="ID Venta")
        tree.heading("#2", text="Cliente")
        tree.heading("#3", text="Fecha")
        tree.heading("#4", text="Repartidor")
        tree.heading("#5", text="Estado")
        tree.pack(fill=tk.BOTH, expand=True)

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT p.id_pedido, p.id_venta, CONCAT(per.nombre, ' ', per.primer_apell) AS cliente, 
                   p.fecha_entrega, p.id_repartidor, p.id_est_pedido
            FROM pedido p
            INNER JOIN venta v ON p.id_venta = v.id_venta
            INNER JOIN persona per ON v.id_persona = per.id_persona
            WHERE p.id_est_pedido = 'P'
        """)
        rows = cur.fetchall()

        for row in rows:
            tree.insert("", "end", text=row[0], values=(row[1], row[2], row[3], row[4], row[5]))

        cur.close()
        conn.close()

        def on_select(event):
            selected_item = tree.focus()
            if selected_item:
                editar_button.config(state=tk.NORMAL)

        tree.bind("<ButtonRelease-1>", on_select)

        editar_button = tk.Button(pendientes_window, text="Editar", state=tk.DISABLED, command=lambda: self.editar_pedido(tree), bg="green", fg="black")
        editar_button.pack(pady=10)

    def editar_pedido(self, tree):
        selected_item = tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "Por favor, seleccione un pedido para editar.")
            return

        item_values = tree.item(selected_item, "values")
        id_pedido = tree.item(selected_item, "text")

        edit_window = tk.Toplevel(self)
        edit_window.title(f"Editar Pedido - ID: {id_pedido}")
        edit_window.geometry("800x600")  # Ajusta el tamaño de la ventana
        edit_window.configure(bg="pink")  # Color de fondo rosado

        tk.Label(edit_window, text="ID Repartidor:", bg="pink").pack()
        id_repartidor_entry = tk.Entry(edit_window)
        id_repartidor_entry.pack()

        tk.Label(edit_window, text="ID Ruta:", bg="pink").pack()
        id_ruta_entry = tk.Entry(edit_window)
        id_ruta_entry.pack()

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT per.id_distrito
            FROM pedido p
            INNER JOIN venta v ON p.id_venta = v.id_venta
            INNER JOIN persona per ON v.id_persona = per.id_persona
            WHERE p.id_pedido = %s
        """, (id_pedido,))
        distrito_cliente = cur.fetchone()[0]

        cur.execute("""
            SELECT r.id_repartidor, r.nombre
            FROM repartidor r
            INNER JOIN distrito d ON r.id_zona = d.id_zona
            WHERE d.id_distrito = %s
        """, (distrito_cliente,))
        repartidores = cur.fetchall()

        tk.Label(edit_window, text="Repartidores Disponibles:", bg="pink").pack()
        tree_repartidores = ttk.Treeview(edit_window, columns=("ID Repartidor", "Nombre"), show="headings")
        tree_repartidores.heading("ID Repartidor", text="ID Repartidor")
        tree_repartidores.heading("Nombre", text="Nombre")
        tree_repartidores.pack(fill=tk.BOTH, expand=True)

        for repartidor in repartidores:
            tree_repartidores.insert("", "end", values=(repartidor[0], repartidor[1]))

        cur.close()
        conn.close()

        def actualizar_pedido():
            repartidor_id = id_repartidor_entry.get()
            ruta_id = id_ruta_entry.get()

            if not repartidor_id or not ruta_id:
                messagebox.showerror("Error", "Por favor, ingrese el ID de repartidor y el ID de ruta.")
                return

            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("""
                UPDATE pedido
                SET id_repartidor = %s, id_ruta = %s
                WHERE id_pedido = %s
            """, (repartidor_id, ruta_id, id_pedido))
            conn.commit()
            cur.close()
            conn.close()

            messagebox.showinfo("Éxito", f"Pedido ID {id_pedido} actualizado correctamente.")
            edit_window.destroy()

        confirmar_button = tk.Button(edit_window, text="Confirmar", command=actualizar_pedido, bg="green", fg="black")
        confirmar_button.pack(pady=10)

    def volver(self):
        self.destroy()
        self.on_volver()










"""from tkinter import Frame, Label

class GestorDistribucionView(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = Label(self, text="Ventana del Gestor de Distribución")
        self.label.pack()
"""