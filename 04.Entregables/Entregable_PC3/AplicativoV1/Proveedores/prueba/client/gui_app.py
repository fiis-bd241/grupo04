import tkinter as tk
from tkinter import ttk
import psycopg2


def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width = 300, height = 300)

    menu_inicio = tk.Menu(barra_menu, tearoff = 0)
    barra_menu.add_cascade(label = 'Inicio', menu = menu_inicio)


    menu_inicio.add_command(label = 'Crear Registro en BD')
    menu_inicio.add_command(label = 'Eliminar Registro en BD')
    menu_inicio.add_command(label = 'Salir', command = root.destroy)

    barra_menu.add_cascade(label = 'Consultas')
    barra_menu.add_cascade(label = 'Configuraciones')
    barra_menu.add_cascade(label = 'Ayuda')


class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root,width = 480, height = 320)
        self.root = root
        self.pack()
        #self.config(bg = 'grey')

        self.campos_proveedores()
        self.deshabilitar_campos()
        self.tabla_proveedores()

    def campos_proveedores(self):
        # Label de cada campo
        self.label_ruc = tk.Label(self, text = 'RUC: ')
        self.label_ruc.config(font = ('Arial', 12, 'bold'))
        self.label_ruc.grid(row = 0, column = 0, padx = 10, pady = 10)

        self.label_razonsocial = tk.Label(self, text = 'Razon_social: ')
        self.label_razonsocial.config(font = ('Arial', 12, 'bold'))
        self.label_razonsocial.grid(row = 1, column = 0, padx = 10, pady = 10)

        self.label_webpro = tk.Label(self, text = 'Webproveedor: ')
        self.label_webpro.config(font = ('Arial', 12, 'bold'))
        self.label_webpro.grid(row = 2, column = 0, padx = 10, pady = 10)

        self.label_rubro = tk.Label(self, text = 'Rubro: ')
        self.label_rubro.config(font = ('Arial', 12, 'bold'))
        self.label_rubro.grid(row = 3, column = 0, padx = 10, pady = 10)

        self.label_direccion = tk.Label(self, text = 'Direccion: ')
        self.label_direccion.config(font = ('Arial', 12, 'bold'))
        self.label_direccion.grid(row = 4, column = 0, padx = 10, pady = 10)

        self.label_telefono = tk.Label(self, text = 'Telefono: ')
        self.label_telefono.config(font = ('Arial', 12, 'bold'))
        self.label_telefono.grid(row = 5, column = 0, padx = 10, pady = 10)
        
        self.label_estproveedor = tk.Label(self, text = 'id_est_proveedor: ')
        self.label_estproveedor.config(font = ('Arial', 12, 'bold'))
        self.label_estproveedor.grid(row = 6, column = 0, padx = 10, pady = 10)

        #Entry de cada campo
        self.mi_ruc = tk.IntVar()
        self.entry_ruc = tk.Entry(self, textvariable = self.mi_ruc)
        self.entry_ruc.config(width = 50, font = ('Arial', 12))
        self.entry_ruc.grid(row = 0, column = 1, padx = 10, pady = 10, columnspan = 2)

        self.mi_razonsocial = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable = self.mi_razonsocial)
        self.entry_nombre.config(width = 50, font = ('Arial', 12))
        self.entry_nombre.grid(row = 1, column = 1, padx = 10, pady = 10, columnspan = 2)

        self.mi_webpro = tk.StringVar()
        self.entry_webpro = tk.Entry(self, textvariable = self.mi_webpro)
        self.entry_webpro.config(width = 50, font = ('Arial', 12))
        self.entry_webpro.grid(row = 2, column = 1, padx = 10, pady = 10, columnspan = 2)

        self.mi_rubro = tk.StringVar()
        self.entry_rubro = tk.Entry(self, textvariable = self.mi_rubro)
        self.entry_rubro.config(width = 50, font = ('Arial', 12))
        self.entry_rubro.grid(row = 3, column = 1, padx = 10, pady = 10, columnspan = 2)

        self.mi_direccion = tk.StringVar()
        self.entry_direccion = tk.Entry(self, textvariable = self.mi_direccion)
        self.entry_direccion.config(width = 50, font = ('Arial', 12))
        self.entry_direccion.grid(row = 4, column = 1, padx = 10, pady = 10, columnspan = 2)

        self.mi_telefono = tk.StringVar()
        self.entry_telefono = tk.Entry(self, textvariable = self.mi_telefono)
        self.entry_telefono.config(width = 50, font = ('Arial', 12))
        self.entry_telefono.grid(row = 5, column = 1, padx = 10, pady = 10, columnspan = 2)

        self.mi_estproveedor = tk.StringVar()
        self.entry_estproveedor = tk.Entry(self, textvariable = self.mi_estproveedor)
        self.entry_estproveedor.config(width = 50, font = ('Arial', 12))
        self.entry_estproveedor.grid(row = 6, column = 1, padx = 10, pady = 10, columnspan = 2)

        # Botones
        # Boton nuevo
        self.boton_nuevo = tk.Button(self, text = "Nuevo", command = self.habilitar_campos)
        self.boton_nuevo.config(width = 20, font = ('Arial', 12, 'bold'), 
                                fg = '#DAD5D6', bg = '#158645',
                                cursor = 'hand2', activebackground = '#35BD6F')
        self.boton_nuevo.grid(row = 7, column = 0, padx = 10, pady = 10)

        # Boton guardar
        self.boton_guardar = tk.Button(self, text = "Guardar", command = self.guardar_datos)
        self.boton_guardar.config(width = 20, font = ('Arial', 12, 'bold'), 
                                fg = '#DAD5D6', bg = '#1658A2',
                                cursor = 'hand2', activebackground = '#3586DF')
        self.boton_guardar.grid(row = 7, column = 1, padx = 10, pady = 10)

        # Boton cancelar
        self.boton_cancelar = tk.Button(self, text = "Cancelar",command = self.deshabilitar_campos)
        self.boton_cancelar.config(width = 20, font = ('Arial', 12, 'bold'), 
                                fg = '#DAD5D6', bg = '#BD152E',
                                cursor = 'hand2', activebackground = '#E15370')
        self.boton_cancelar.grid(row = 7, column = 2, padx = 10, pady = 10)
    def habilitar_campos(self):
        self.mi_ruc.set('')
        self.mi_razonsocial.set('')
        self.mi_webpro.set('')
        self.mi_rubro.set('')
        self.mi_direccion.set('')
        self.mi_telefono.set('')
        self.mi_estproveedor.set('')

        self.entry_ruc.config(state = 'normal')
        self.entry_nombre.config(state = 'normal')
        self.entry_webpro.config(state = 'normal')
        self.entry_rubro.config(state = 'normal')
        self.entry_direccion.config(state = 'normal')
        self.entry_telefono.config(state = 'normal')
        self.entry_estproveedor.config(state = 'normal')

        self.boton_guardar.config(state = 'normal')
        self.boton_cancelar.config(state = 'normal')

    def deshabilitar_campos(self):
        self.mi_ruc.set('')
        self.mi_razonsocial.set('')
        self.mi_webpro.set('')
        self.mi_rubro.set('')
        self.mi_direccion.set('')
        self.mi_telefono.set('')
        self.mi_estproveedor.set('')

        self.entry_ruc.config(state = 'disabled')
        self.entry_nombre.config(state = 'disabled')
        self.entry_webpro.config(state = 'disabled')
        self.entry_rubro.config(state = 'disabled')
        self.entry_direccion.config(state = 'disabled')
        self.entry_telefono.config(state = 'disabled')
        self.entry_estproveedor.config(state = 'disabled')

        self.boton_guardar.config(state = 'disabled')
        self.boton_cancelar.config(state = 'disabled')
    def guardar_datos(self):
        
        proveedor = Proveedor(
            self.mi_ruc.get(),
            self.mi_razonsocial.get(),
            self.mi_webpro.get(),
            self.mi_rubro.get(),
            self.mi_direccion.get(),
            self.mi_telefono.get(),
            self.mi_estproveedor.get()
        )
        guardar(proveedor)
        self.tabla_proveedores()

        self.deshabilitar_campos()
        
    def tabla_proveedores(self):
        #Recuperar lista
        self.lista_proveedor = listar()
        self.lista_proveedor.reverse()

        self.tabla = ttk.Treeview(self,
                                  column = ('RUC', 'Razon_social', 'webProveedor', 'rubro','direccion','telefono','id_est_proveedor',))
        self.tabla.grid(row = 8, column = 0, columnspan = 4, sticky='nse')

        #Scrollbar
        self.scroll = ttk.Scrollbar(self, orient='vertical', command = self.tabla.yview)
        self.scroll.grid(row = 8, column = 4, sticky='nse')
        self.tabla.configure(yscrollcommand = self.scroll.set)

        self.tabla.heading('#0', text = 'RUC')
        self.tabla.heading('#1', text = 'RAZON SOCIAL')
        self.tabla.heading('#2', text = 'WEBPROV')
        self.tabla.heading('#3', text = 'RUBRO')
        self.tabla.heading('#4', text = 'DIRECCION')
        self.tabla.heading('#5', text = 'TELEFONO')
        self.tabla.heading('#6', text = 'EST_PROVEEDOR')

        #Iterar lista peliculas
        for p in self.lista_proveedor:
            self.tabla.insert('', 0, text = p[0], 
            values = (p[1], p[2], p[3],p[4], p[5], p[6]))
        
        # Boton editar
        self.boton_editar = tk.Button(self, text = "Editar")
        self.boton_editar.config(width = 20, font = ('Arial', 12, 'bold'), 
                                fg = '#DAD5D6', bg = '#158645',
                                cursor = 'hand2', activebackground = '#35BD6F')
        self.boton_editar.grid(row = 9, column = 0, padx = 10, pady = 10)

        # Boton eliminar
        self.boton_eliminar = tk.Button(self, text = "Eliminar")
        self.boton_eliminar.config(width = 20, font = ('Arial', 12, 'bold'), 
                                fg = '#DAD5D6', bg = '#BD152E',
                                cursor = 'hand2', activebackground = '#E15370')
        self.boton_eliminar.grid(row = 9, column = 1, padx = 10, pady = 10)


class Proveedor:
    def __init__(self, ruc_proveedor, razon_social, web_proveedor, rubro, direccion, telefono, id_est_proveedor):
        self.ruc_proveedor = ruc_proveedor
        self.razon_social = razon_social
        self.web_proveedor = web_proveedor
        self.rubro = rubro
        self.direccion = direccion
        self.telefono = telefono
        self.id_est_proveedor = id_est_proveedor
    def __str__(self):
        return f'proveedor[{self.ruc_proveedor},{self.razon_social},{self.web_proveedor},{self.rubro},{self.direccion},{self.telefono},{self.est_prov}]'
def guardar(proveedor):
    conex = psycopg2.connect(
            dbname = "MIGNI STORE V11",
            user = "postgres",
            password = "1234",
            host = "localhost",
            port = "8000"
    )
    cursor = conex.cursor()
    query = f"INSERT INTO proveedor(ruc_proveedor, razon_social, web_proveedor, rubro, direccion, telefono, id_est_proveedor) VALUES ('{proveedor.ruc_proveedor}', '{proveedor.razon_social}', '{proveedor.web_proveedor}', '{proveedor.rubro}', '{proveedor.direccion}', '{proveedor.telefono}', '{proveedor.id_est_proveedor}')"
    cursor.execute(query)
    print("Datos Guardados")
    conex.commit()
    conex.close()

def listar():
    conex = psycopg2.connect(
            dbname = "MIGNI STORE V11",
            user = "postgres",
            password = "1234",
            host = "localhost",
            port = "8000"
    )
    cursor = conex.cursor()
    lista_proveedores = []
    query = 'SELECT * FROM proveedor'
    cursor.execute(query)
    conex.commit()
    lista_proveedores = cursor.fetchall()
    conex.close()

    return lista_proveedores