import tkinter as tk
from tkinter import ttk, messagebox
from model.querys import actualizar_campaña, actualizar_canales_por_campaña, actualizar_estado_observacion, actualizar_productos_por_campaña, insertar_campaña, insertar_campañaxcanal, insertar_campañaxprod, obtener_campaña_por_id, obtener_canales_por_campaña, obtener_max_id_campaña, obtener_observaciones_pendientes, obtener_productos_por_campaña, verificar_credenciales

# Variable global para almacenar el equipo_id después del login
equipo_id_global = None

class LoginFrame(tk.Frame):
    def __init__(self, root, on_login_success):
        super().__init__(root)
        self.root = root
        self.on_login_success = on_login_success
        self.create_widgets()

    def create_widgets(self):
        self.user_label = tk.Label(self, text="Usuario")
        self.user_label.grid(row=0, column=0)
        self.user_entry = tk.Entry(self)
        self.user_entry.grid(row=0, column=1)
        self.pass_label = tk.Label(self, text="Contraseña")
        self.pass_label.grid(row=1, column=0)
        self.pass_entry = tk.Entry(self, show='*')
        self.pass_entry.grid(row=1, column=1)
        self.login_button = tk.Button(self, text="Ingresar", command=self.check_login)
        self.login_button.grid(row=2, columnspan=2)

    def check_login(self):
        usuario = self.user_entry.get()
        contraseña = self.pass_entry.get()
        id_equipo_mark = verificar_credenciales(usuario, contraseña)
        if id_equipo_mark:
            global equipo_id_global
            equipo_id_global = id_equipo_mark  # Almacenar equipo_id_global globalmente
            self.on_login_success(self.root, id_equipo_mark)
        else:
            messagebox.showerror("Error", "Credenciales incorrectas o no perteneces a un equipo")

class Frame(tk.Frame):
    def __init__(self, root=None, equipo_id=None):
        super().__init__(root)
        self.root = root
        self.equipo_id = equipo_id
        self.create_widgets()

    def create_widgets(self):
        self.propuesta_frame = tk.Frame(self)
        self.propuesta_frame.pack()

        id_equipo_mark_label = tk.Label(self.propuesta_frame, text=f"ID Equipo: {equipo_id_global}")
        id_equipo_mark_label.grid(row=0, column=0)

        self.id_campaña = obtener_max_id_campaña() + 1
        self.id_campaña_label = tk.Label(self.propuesta_frame, text=f"ID Campaña: {self.id_campaña}")
        self.id_campaña_label.grid(row=1, column=0)

        self.nombre_campaña_label = tk.Label(self.propuesta_frame, text="Nombre de la Campaña:")
        self.nombre_campaña_label.grid(row=2, column=0)
        self.nombre_campaña = tk.Entry(self.propuesta_frame)
        self.nombre_campaña.grid(row=2, column=1)

        self.fecha_ini_label = tk.Label(self.propuesta_frame, text="Fecha de Inicio:")
        self.fecha_ini_label.grid(row=3, column=0)
        self.fecha_ini = tk.Entry(self.propuesta_frame)
        self.fecha_ini.grid(row=3, column=1)

        self.fecha_fin_label = tk.Label(self.propuesta_frame, text="Fecha de Fin:")
        self.fecha_fin_label.grid(row=4, column=0)
        self.fecha_fin = tk.Entry(self.propuesta_frame)
        self.fecha_fin.grid(row=4, column=1)

        self.dir_url_label = tk.Label(self.propuesta_frame, text="Dirección de la Página:")
        self.dir_url_label.grid(row=5, column=0)
        self.dir_url = tk.Entry(self.propuesta_frame)
        self.dir_url.grid(row=5, column=1)

        self.modalidad_label = tk.Label(self.propuesta_frame, text="Modalidad:")
        self.modalidad_label.grid(row=6, column=0)
        self.modalidad = tk.Entry(self.propuesta_frame)
        self.modalidad.grid(row=6, column=1)

        self.archivo_label = tk.Label(self.propuesta_frame, text="Link del Archivo:")
        self.archivo_label.grid(row=7, column=0)
        self.archivo = tk.Entry(self.propuesta_frame)
        self.archivo.grid(row=7, column=1)

        self.desc_campaña_label = tk.Label(self.propuesta_frame, text="Descuento:")
        self.desc_campaña_label.grid(row=8, column=0)
        self.desc_campaña = tk.Entry(self.propuesta_frame)
        self.desc_campaña.grid(row=8, column=1)

        self.producto_label = tk.Label(self.propuesta_frame, text="Producto:")
        self.producto_label.grid(row=9, column=0)
        self.producto_entries = []
        self.add_producto()

        self.canal_label = tk.Label(self.propuesta_frame, text="Canal:")
        self.canal_label.grid(row=9, column=3)
        self.canal_entries = []
        self.add_canal()

        self.enviar_btn = tk.Button(self.propuesta_frame, text="Enviar", command=self.enviar_propuesta)
        self.enviar_btn.grid(row=5, column=5)

    def add_producto(self):
        producto_frame = tk.Frame(self.propuesta_frame)
        producto_frame.grid(row=len(self.producto_entries) + 9, column=1, columnspan=2)

        producto_entry = tk.Entry(producto_frame)
        producto_entry.pack(side="left")

        add_btn = tk.Button(producto_frame, text="+", command=self.add_producto)
        add_btn.pack(side="left")
        remove_btn = tk.Button(producto_frame, text="-", command=lambda: self.remove_producto(producto_frame))
        remove_btn.pack(side="left")

        self.producto_entries.append(producto_entry)

    def remove_producto(self, producto_frame):
        producto_frame.destroy()
        self.producto_entries.remove(producto_frame.winfo_children()[0].winfo_children()[0])

    def add_canal(self):
        canal_frame = tk.Frame(self.propuesta_frame)
        canal_frame.grid(row=len(self.canal_entries) + len(self.producto_entries) + 8, column=4, columnspan=2)

        canal_entry = tk.Entry(canal_frame)
        canal_entry.pack(side="left")

        add_btn = tk.Button(canal_frame, text="+", command=self.add_canal)
        add_btn.pack(side="left")
        remove_btn = tk.Button(canal_frame, text="-", command=lambda: self.remove_canal(canal_frame))
        remove_btn.pack(side="left")

        self.canal_entries.append(canal_entry)

    def remove_canal(self, canal_frame):
        canal_frame.destroy()
        self.canal_entries.remove(canal_frame.winfo_children()[0].winfo_children()[0])

    def enviar_propuesta(self):
        id_campaña = obtener_max_id_campaña() + 1
        nom_campaña = self.nombre_campaña.get()
        fecha_ini = self.fecha_ini.get()
        fecha_fin = self.fecha_fin.get()
        dir_url = self.dir_url.get()
        modalidad = self.modalidad.get()
        archivo = self.archivo.get()
        desc_campaña = self.desc_campaña.get()
        id_equipo_mark = equipo_id_global  # Usar el equipo_id_global almacenado
        id_gest_mark = 1005

        insertar_campaña(id_campaña, nom_campaña, fecha_ini, fecha_fin, dir_url, modalidad, archivo, desc_campaña, id_equipo_mark, id_gest_mark)

        for producto_entry in self.producto_entries:
            id_producto = producto_entry.get()
            insertar_campañaxprod(id_campaña, id_producto)

        for canal_entry in self.canal_entries:
            id_canal = canal_entry.get()
            insertar_campañaxcanal(id_campaña, id_canal)

        messagebox.showinfo("Éxito", "Propuesta creada exitosamente")

        # Limpiar los campos después de enviar la propuesta
        self.nombre_campaña.delete(0, tk.END)
        self.fecha_ini.delete(0, tk.END)
        self.fecha_fin.delete(0, tk.END)
        self.dir_url.delete(0, tk.END)
        self.modalidad.delete(0, tk.END)
        self.archivo.delete(0, tk.END)
        self.desc_campaña.delete(0, tk.END)

        for producto_entry in self.producto_entries:
            producto_entry.delete(0, tk.END)

        for canal_entry in self.canal_entries:
            canal_entry.delete(0, tk.END)

        # Reiniciar los campos de productos y canales
        self.producto_entries = []
        self.canal_entries = []

        self.add_producto()
        self.add_canal()

class ObservacionesFrame(tk.Frame):
    def __init__(self, root=None, equipo_id=None):
        super().__init__(root)
        self.root = root
        self.equipo_id = equipo_id
        self.pack()

        self.campos_inicial()
        self.tabla_observaciones()

    def campos_inicial(self):
        pass

    def tabla_observaciones(self):
        # Canvas para contener el Treeview y las barras de desplazamiento
        self.canvas = tk.Canvas(self, bg="pink")
        self.canvas.grid(row=1, column=0, columnspan=2, sticky="nsew")

        # Scrollbar vertical
        self.scrollbar_vertical = tk.Scrollbar(self.canvas, orient="vertical")
        self.scrollbar_vertical.pack(side="right", fill="y")

        # Scrollbar horizontal
        self.scrollbar_horizontal = tk.Scrollbar(self.canvas, orient="horizontal")
        self.scrollbar_horizontal.pack(side="bottom", fill="x")

        # Treeview
        self.tree = ttk.Treeview(self.canvas, yscrollcommand=self.scrollbar_vertical.set, xscrollcommand=self.scrollbar_horizontal.set, columns=("ID Observacion", "Descripcion", "ID Campaña", "Estado Atendido"), show="headings")
        self.tree.pack(expand=True, fill='both')

        self.scrollbar_vertical.config(command=self.tree.yview)
        self.scrollbar_horizontal.config(command=self.tree.xview)

        self.tree.heading('ID Observacion', text='ID Observacion')
        self.tree.heading('Descripcion', text='Descripcion')
        self.tree.heading('ID Campaña', text='ID Campaña')
        self.tree.heading('Estado Atendido', text='Estado Atendido')

        self.tree.column('ID Observacion', minwidth=0, width=150, stretch=False)
        self.tree.column('Descripcion', minwidth=0, width=150, stretch=False)
        self.tree.column('ID Campaña', minwidth=0, width=150, stretch=False)
        self.tree.column('Estado Atendido', minwidth=0, width=150, stretch=False)

        self.tree.bind('<ButtonRelease-1>', self.seleccionar_fila)

        observaciones = obtener_observaciones_pendientes(self.equipo_id)
        for obs in observaciones:
            self.tree.insert("", tk.END, values=(obs[0], obs[1], obs[2], obs[3]))

        self.boton_ateneder = tk.Button(self, text="Atender", state=tk.DISABLED, command=self.abrir_observacion)
        self.boton_ateneder.grid(row=2, column=0, columnspan=2)

    def seleccionar_fila(self, event):
        item = self.tree.selection()
        if item:
            self.boton_ateneder.config(state=tk.NORMAL)
        else:
            self.boton_ateneder.config(state=tk.DISABLED)

    def abrir_observacion(self):
        selected_item = self.tree.selection()[0]
        item = self.tree.item(selected_item)
        id_observacion = item['values'][0]
        campaña_id = item['values'][2]
        frame_emergente = FrameEmergente(self.root, id_observacion, campaña_id)
        frame_emergente.grab_set()

class FrameEmergente(tk.Toplevel):
    def __init__(self, root, id_observacion, campaña_id):
        super().__init__(root)
        self.root = root
        self.id_observacion = id_observacion
        self.campaña_id = campaña_id
        self.title("Editar Campaña y Observación")
        self.geometry("600x400")
        self.resizable(0, 0)
        self.create_widgets()

    def create_widgets(self):
        observacion_label = tk.Label(self, text=f"ID Observación: {self.id_observacion}")
        observacion_label.pack()

        campaña_label = tk.Label(self, text=f"ID Campaña: {self.campaña_id}")
        campaña_label.pack()

        # Obtener datos de la campaña por su id
        campaña_data = obtener_campaña_por_id(self.campaña_id)

        if campaña_data:
            nombre_label = tk.Label(self, text="Nombre de la Campaña:")
            nombre_label.pack()
            self.nombre_entry = tk.Entry(self)
            self.nombre_entry.insert(tk.END, campaña_data[1])  # Nombre de la campaña
            self.nombre_entry.pack()

            fecha_ini_label = tk.Label(self, text="Fecha de Inicio:")
            fecha_ini_label.pack()
            self.fecha_ini_entry = tk.Entry(self)
            self.fecha_ini_entry.insert(tk.END, campaña_data[2])  # Fecha de inicio
            self.fecha_ini_entry.pack()

            fecha_fin_label = tk.Label(self, text="Fecha de Fin:")
            fecha_fin_label.pack()
            self.fecha_fin_entry = tk.Entry(self)
            self.fecha_fin_entry.insert(tk.END, campaña_data[3])  # Fecha de fin
            self.fecha_fin_entry.pack()

            dir_url_label = tk.Label(self, text="Dirección de la Página:")
            dir_url_label.pack()
            self.dir_url_entry = tk.Entry(self)
            self.dir_url_entry.insert(tk.END, campaña_data[4])  # Dirección de la página
            self.dir_url_entry.pack()

            modalidad_label = tk.Label(self, text="Modalidad:")
            modalidad_label.pack()
            self.modalidad_entry = tk.Entry(self)
            self.modalidad_entry.insert(tk.END, campaña_data[5])  # Modalidad
            self.modalidad_entry.pack()

            archivo_label = tk.Label(self, text="Link del Archivo:")
            archivo_label.pack()
            self.archivo_entry = tk.Entry(self)
            self.archivo_entry.insert(tk.END, campaña_data[6])  # Link del archivo
            self.archivo_entry.pack()

            desc_campaña_label = tk.Label(self, text="Descuento:")
            desc_campaña_label.pack()
            self.desc_campaña_entry = tk.Entry(self)
            self.desc_campaña_entry.insert(tk.END, campaña_data[7])  # Descuento
            self.desc_campaña_entry.pack()

            actualizar_btn = tk.Button(self, text="Actualizar", command=self.actualizar_campaña)
            actualizar_btn.pack()

        productos_btn = tk.Button(self, text="Productos", command=self.abrir_productos)
        productos_btn.pack()

        canales_btn = tk.Button(self, text="Canales", command=self.abrir_canales)
        canales_btn.pack()

    def abrir_canales(self):
        # Lógica para abrir la ventana de canales asociados a la campaña
        canales_frame = EditarCanales(self.root, self.campaña_id)
        canales_frame.grab_set()
    
    def abrir_productos(self):
        # Lógica para abrir la ventana de productos asociados a la campaña
        productos_frame = EditarProductos(self.root, self.campaña_id)
        productos_frame.grab_set()

    def actualizar_campaña(self):
        nombre = self.nombre_entry.get()
        fecha_ini = self.fecha_ini_entry.get()
        fecha_fin = self.fecha_fin_entry.get()
        dir_url = self.dir_url_entry.get()
        modalidad = self.modalidad_entry.get()
        archivo = self.archivo_entry.get()
        desc_campaña = self.desc_campaña_entry.get()

        actualizar_campaña(self.campaña_id, nombre, fecha_ini, fecha_fin, dir_url, modalidad, archivo, desc_campaña)
        actualizar_estado_observacion(self.id_observacion)

        messagebox.showinfo("Éxito", "Campaña actualizada y observación atendida exitosamente")
        self.destroy()

class EditarCanales(tk.Toplevel):
    def __init__(self, parent, campaña_id):
        super().__init__(parent)
        self.campaña_id = campaña_id
        self.title("Editar Canales")
        self.geometry("400x300")

        canales = obtener_canales_por_campaña(self.campaña_id)
        self.entries = []

        for idx, canal_id in enumerate(canales):
            label = tk.Label(self, text=f"Canal {idx+1}")
            label.grid(row=idx, column=0, padx=10, pady=5)
            entry = tk.Entry(self)
            entry.grid(row=idx, column=1, padx=10, pady=5)
            entry.insert(0, canal_id)
            self.entries.append(entry)

        self.boton_guardar = tk.Button(self, text="Guardar Canales", command=self.guardar_canales)
        self.boton_guardar.grid(row=len(canales)+1, column=1, padx=10, pady=10)

    def guardar_canales(self):
        canales_actualizados = [entry.get() for entry in self.entries]
        actualizar_canales_por_campaña(self.campaña_id, canales_actualizados)
        self.destroy()

class EditarProductos(tk.Toplevel):
    def __init__(self, parent, campaña_id):
        super().__init__(parent)
        self.campaña_id = campaña_id
        self.title("Editar Productos")
        self.geometry("400x300")

        productos = obtener_productos_por_campaña(self.campaña_id)
        self.entries = []

        for idx, producto_id in enumerate(productos):
            label = tk.Label(self, text=f"Producto {idx+1}")
            label.grid(row=idx, column=0, padx=10, pady=5)
            entry = tk.Entry(self)
            entry.grid(row=idx, column=1, padx=10, pady=5)
            entry.insert(0, producto_id)
            self.entries.append(entry)

        self.boton_guardar = tk.Button(self, text="Guardar Productos", command=self.guardar_productos)
        self.boton_guardar.grid(row=len(productos)+1, column=1, padx=10, pady=10)

    def guardar_productos(self):
        productos_actualizados = [entry.get() for entry in self.entries]
        actualizar_productos_por_campaña(self.campaña_id, productos_actualizados)
        self.destroy()


def barra_menu(root):
    menubar = tk.Menu(root)

    campañas_menu = tk.Menu(menubar, tearoff=0)
    campañas_menu.add_command(label="Crear Propuestas", command=lambda: mostrar_campaña_propuestas(root, equipo_id_global))
    campañas_menu.add_command(label="Atender Observaciones", command=lambda: atender_observaciones(root, equipo_id_global))

    menubar.add_cascade(label="Campañas", menu=campañas_menu)

    root.config(menu=menubar)

def mostrar_campaña_propuestas(root, equipo_id):
    for widget in root.winfo_children():
        widget.pack_forget()
    frame = Frame(root, equipo_id)
    frame.pack()

def atender_observaciones(root, equipo_id):
    for widget in root.winfo_children():
        widget.pack_forget()
    observaciones_frame = ObservacionesFrame(root, equipo_id)
    observaciones_frame.pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Equipo de Marketing")

    barra_menu(root)

    login_frame = LoginFrame(root, on_login_success=mostrar_campaña_propuestas)
    login_frame.pack()

    root.mainloop()