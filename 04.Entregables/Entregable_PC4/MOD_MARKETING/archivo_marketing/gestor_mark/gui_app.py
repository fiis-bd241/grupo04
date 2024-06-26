import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date
from model.querys_dao import obtener_campañas_vigentes, obtener_campañas_propuestas, actualizar_campaña, obtener_campaña_por_id, borrar_campaña, obtener_ultimo_id_observacion, agregar_observacion

class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        self.config(bg="pink")

        self.label_nombre = tk.Label(self, text="Campañas Vigentes")
        self.label_nombre.config(font=("Arial", 12, "bold"))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)

        self.campos_inicial()
        self.tabla_campañas()

    def campos_inicial(self):
        pass

    def tabla_campañas(self):
        # Canvas para contener el Treeview y las barras de desplazamiento
        self.canvas = tk.Canvas(self, bg="pink")
        self.canvas.grid(row=1, column=0, columnspan=2, sticky="nsew")

        # Scrollbar vertical
        self.scrollbar_y = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar_y.grid(row=1, column=2, sticky='ns')

        # Scrollbar horizontal
        self.scrollbar_x = tk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.scrollbar_x.grid(row=2, column=0, columnspan=2, sticky='ew')

        self.canvas.configure(yscrollcommand=self.scrollbar_y.set)
        self.canvas.configure(xscrollcommand=self.scrollbar_x.set)

        # Frame contenedor dentro del Canvas
        self.frame_tabla = tk.Frame(self.canvas, bg="pink")
        self.canvas.create_window((0, 0), window=self.frame_tabla, anchor="nw")

        self.tabla = ttk.Treeview(
            self.frame_tabla,
            columns=("Id_campaña", "nom_campaña", "fecha_ini", "fecha_fin", "dir_url", "modalidad", "archivo", "desc_campaña", "Id_equipo_mark", "Id_gest_mark"),
            show="headings"
        )
        self.tabla.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        for col in self.tabla["columns"]:
            self.tabla.heading(col, text=col)

        # Configurar eventos para el desplazamiento
        self.frame_tabla.bind("<Configure>", self.on_frame_configure)

        # Botones
        self.boton_editar = tk.Button(
            self, text="Editar", state=tk.DISABLED, command=self.editar_fila
        )
        self.boton_editar.config(width=20, font=("Arial", 12, "bold"),
                                 fg="black", bg="green", cursor="hand2", 
                                 activebackground="white")
        self.boton_editar.grid(row=3, column=0, padx=10, pady=10)
        self.tabla.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.boton_borrar = tk.Button(
            self, text="Borrar", state=tk.DISABLED, command=self.borrar_fila
        )
        self.boton_borrar.config(width=20, font=("Arial", 12, "bold"),
                                 fg="black", bg="red", cursor="hand2", 
                                 activebackground="white")
        self.boton_borrar.grid(row=3, column=1, padx=10, pady=10)
        self.tabla.bind("<<TreeviewSelect>>", self.on_tree_select)

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_tree_select(self, event):
        selected_items = self.tabla.selection()
        if selected_items:
            self.boton_editar.config(state=tk.NORMAL)
            self.boton_borrar.config(state=tk.NORMAL)
            self.boton_observacion.config(state=tk.NORMAL)  
        else:
            self.boton_editar.config(state=tk.DISABLED)
            self.boton_borrar.config(state=tk.DISABLED)
            self.boton_observacion.config(state=tk.DISABLED) 

    def editar_fila(self):
        selected_item = self.tabla.selection()[0]
        item = self.tabla.item(selected_item)
        campaña_id = item['values'][0]
        EditarCampaña(self.root, campaña_id, self.actualizar_tabla)

    def borrar_fila(self):
        selected_item = self.tabla.selection()[0]
        item = self.tabla.item(selected_item)
        campaña_id = item['values'][0]
        borrar_campaña(campaña_id)
        self.tabla.delete(selected_item)

    def actualizar_tabla(self):
        # Eliminar todos los elementos de la tabla
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        # Volver a cargar los datos de la base de datos para campañas vigentes por defecto
        self.actualizar_tabla_campañas_vigentes()

    def actualizar_tabla_campañas_vigentes(self):
        # Limpiar la tabla antes de actualizar
        self.tabla.delete(*self.tabla.get_children())

        # Obtener y mostrar campañas vigentes
        campañas_vigentes = obtener_campañas_vigentes(date.today())
        self.label_nombre.config(text="Campañas Vigentes")
        for campaña in campañas_vigentes:
            self.tabla.insert("", tk.END, values=campaña)

    def actualizar_tabla_campañas_propuestas(self):
        # Limpiar la tabla antes de actualizar
        self.tabla.delete(*self.tabla.get_children())

        # Obtener y mostrar campañas propuestas
        campañas_propuestas = obtener_campañas_propuestas(date.today())
        self.label_nombre.config(text="Campañas Propuestas")
        for campaña in campañas_propuestas:
            self.tabla.insert("", tk.END, values=campaña)
        
        # Ocultar botones de editar y borrar en el frame de campañas propuestas
        self.boton_editar.grid_forget()
        self.boton_borrar.grid_forget()

        self.boton_observacion = tk.Button(
            self, text="Observacion", state=tk.DISABLED, command=self.mostrar_ventana_observacion
        )
        self.boton_observacion.config(width=20, font=("Arial", 12, "bold"),
                               fg="black", bg="blue", cursor="hand2", 
                               activebackground="white")
        self.boton_observacion.grid(row=3, column=0, padx=10, pady=10)
        self.tabla.bind("<<TreeviewSelect>>", self.on_tree_select)

    def mostrar_ventana_observacion(self):
        selected_item = self.tabla.selection()[0]
        item = self.tabla.item(selected_item)
        campaña_id = item['values'][0]
        EditarObservacion(self.root, campaña_id)


class EditarCampaña(tk.Toplevel):
    def __init__(self, parent, campaña_id, actualizar_callback):
        super().__init__(parent)
        self.campaña_id = campaña_id
        self.actualizar_callback = actualizar_callback
        self.title("Editar Campaña")
        self.geometry("480x320")
        
        # Obtener datos de la campaña
        campaña = obtener_campaña_por_id(self.campaña_id)
        
        self.campos = ["nom_campaña", "fecha_ini", "fecha_fin", "dir_url", "modalidad", "archivo", "desc_campaña", "Id_equipo_mark", "Id_gest_mark"]
        self.entries = {}
        
        for idx, campo in enumerate(self.campos):
            label = tk.Label(self, text=campo.replace("_", " ").capitalize())
            label.grid(row=idx, column=0, padx=10, pady=5)
            entry = tk.Entry(self)
            entry.grid(row=idx, column=1, padx=10, pady=5)
            entry.insert(0, campaña[idx+1])
            self.entries[campo] = entry
        
        self.boton_guardar = tk.Button(self, text="Guardar", command=self.guardar_cambios)
        self.boton_guardar.grid(row=len(self.campos)+1, column=1, padx=10, pady=10)

    def guardar_cambios(self):
        datos_actualizados = {campo: self.entries[campo].get() for campo in self.campos}
        
        # Actualizar la campaña en la base de datos
        actualizar_campaña(self.campaña_id, datos_actualizados)
        
        # Llamar al callback para actualizar la tabla
        self.actualizar_callback()
        
        self.destroy()

class EditarObservacion(tk.Toplevel):
    def __init__(self, parent, campaña_id):
        super().__init__(parent)
        self.campaña_id = campaña_id
        self.title("Observar Campaña")
        self.geometry("400x200")

        # Obtener el último id_observacion y sumar 1
        ultimo_id = obtener_ultimo_id_observacion()
        if ultimo_id:
            siguiente_id = ultimo_id + 1
        else:
            siguiente_id = 1

        # Crear campos de observación
        self.label_id = tk.Label(self, text=f"ID Observación: {siguiente_id}")
        self.label_id.grid(row=0, column=0, padx=10, pady=5)

        self.label_campaña = tk.Label(self, text=f"ID Campaña: {self.campaña_id}")
        self.label_campaña.grid(row=1, column=0, padx=10, pady=5)

        self.label_descripcion = tk.Label(self, text="Descripción:")
        self.label_descripcion.grid(row=2, column=0, padx=10, pady=5)

        self.entry_descripcion = tk.Entry(self, width=50)
        self.entry_descripcion.grid(row=2, column=1, padx=10, pady=5)

        self.boton_observar = tk.Button(self, text="Observar", command=self.registrar_observacion)
        self.boton_observar.grid(row=3, column=1, padx=10, pady=10)

    def registrar_observacion(self):
        descripcion = self.entry_descripcion.get()

        if descripcion.strip() == "":
            messagebox.showwarning("Campo Vacío", "Por favor ingrese una descripción para la observación.")
            return
        
        # Agregar la observación a la base de datos
        exito = agregar_observacion(self.campaña_id, descripcion)

        if exito:
            messagebox.showinfo("Observación Registrada", "Se ha registrado la observación correctamente.")
            self.destroy()
        else:
            messagebox.showerror("Error", "Ha ocurrido un error al registrar la observación. Por favor inténtelo nuevamente.")

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)

    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Gestionar", menu=menu_inicio)
    menu_inicio.add_command(label="Mostrar Campañas Vigentes", command=lambda: mostrar_campañas_vigentes(root))
    menu_inicio.add_command(label="Mostrar Campañas Propuestas", command=lambda: mostrar_campañas_propuestas(root))

def mostrar_campañas_vigentes(root):
    # Limpiar frame actual y mostrar campañas vigentes
    for widget in root.winfo_children():
        widget.destroy()
    
    barra_menu(root)
    app = Frame(root=root)
    app.actualizar_tabla_campañas_vigentes()

def mostrar_campañas_propuestas(root):
    # Limpiar frame actual y mostrar campañas propuestas
    for widget in root.winfo_children():
        widget.destroy()
    
    barra_menu(root)
    app = Frame(root=root)
    app.actualizar_tabla_campañas_propuestas()


