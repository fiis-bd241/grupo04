import tkinter as tk
from tkinter import ttk
from controllers.pedido_controller import obtener_pedidos_pendientes

class PedidosPendientesView(tk.Frame):
    def __init__(self, master, on_volver):
        super().__init__(master)
        self.master = master
        self.on_volver = on_volver
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Pedidos Pendientes")
        self.label.pack(pady=10)

        self.tree = ttk.Treeview(self, columns=("ID Pedido", "ID Venta", "Estado"), show="headings")
        self.tree.heading("ID Pedido", text="ID Pedido")
        self.tree.heading("ID Venta", text="ID Venta")
        self.tree.heading("Estado", text="Estado")
        self.tree.pack(pady=10)

        pedidos = obtener_pedidos_pendientes()
        for pedido in pedidos:
            self.tree.insert("", "end", values=(pedido['id_pedido'], pedido['id_venta'], pedido['id_est_pedido']))

        self.volver_button = tk.Button(self, text="Volver", command=self.on_volver)
        self.volver_button.pack(pady=10)
