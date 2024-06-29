import tkinter as tk
from tkinter import ttk

from model.proveedor_dao import Proveedor
from model.proveedor_dao import guardar, listar, editar
#from prueba_proveedor2 import ventana_cotizacion


def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width = 300, height = 300)

    menu_inicio = tk.Menu(barra_menu, tearoff = 0)
    barra_menu.add_cascade(label = 'Inicio', menu = menu_inicio)
     

    #menu_inicio.add_command(label = 'Crear Registro en BD')
    #menu_inicio.add_command(label = 'Eliminar Registro en BD')
    #menu_inicio.add_command(label = 'Salir', command = root.destroy)



class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root,width = 480, height = 320)
        self.root = root
        self.configure(background='pink')
        self.pack()

        # Boton volver
        self.volver_button = tk.Button(self, text="Volver", command= root.destroy)
        self.volver_button.config(width = 20, font = ('Arial', 12, 'bold'), 
                                fg = '#DAD5D6', bg = '#BD152E',
                                cursor = 'hand2', activebackground = '#E15370')
        self.volver_button.grid(row = 9, column = 1, padx = 10, pady = 10)

        self.ruc_proveedor = None
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
        self.entry_razonsocial = tk.Entry(self, textvariable = self.mi_razonsocial)
        self.entry_razonsocial.config(width = 50, font = ('Arial', 12))
        self.entry_razonsocial.grid(row = 1, column = 1, padx = 10, pady = 10, columnspan = 2)

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
        self.entry_razonsocial.config(state = 'normal')
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
        self.entry_razonsocial.config(state = 'disabled')
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
        if self.ruc_proveedor == None:
            guardar(proveedor)
        else:
            editar(proveedor, self.ruc_proveedor)

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

        #Iterar lista proveedores
        for p in self.lista_proveedor:
            self.tabla.insert('', 0, text = p[0], 
            values = (p[1], p[2], p[3],p[4], p[5], p[6]))
        
        # Boton editar
        self.boton_editar = tk.Button(self, text = "Editar", command= self.editar_datos)
        self.boton_editar.config(width = 20, font = ('Arial', 12, 'bold'), 
                                fg = '#DAD5D6', bg = '#158645',
                                cursor = 'hand2', activebackground = '#35BD6F')
        self.boton_editar.grid(row = 9, column = 0, padx = 10, pady = 10)



    def editar_datos(self):
        
        self.ruc_proveedor = self.tabla.item(self.tabla.selection())['text']
        self.razon_social = self.tabla.item(self.tabla.selection())['values'][0]
        self.web_proveedor = self.tabla.item(self.tabla.selection())['values'][1]
        self.rubro = self.tabla.item(self.tabla.selection())['values'][2]
        self.direccion = self.tabla.item(self.tabla.selection())['values'][3]
        self.telefono = self.tabla.item(self.tabla.selection())['values'][4]
        self.estproveedor = self.tabla.item(self.tabla.selection())['values'][5]
            
        self.habilitar_campos()

        self.entry_ruc.insert(0,self.ruc_proveedor)
        self.entry_razonsocial.insert(0,self.razon_social)
        self.entry_webpro.insert(0,self.web_proveedor)
        self.entry_rubro.insert(0,self.rubro)
        self.entry_direccion.insert(0,self.direccion)
        self.entry_telefono.insert(0,self.telefono)
        self.entry_estproveedor.insert(0,self.estproveedor)

        
    




            

