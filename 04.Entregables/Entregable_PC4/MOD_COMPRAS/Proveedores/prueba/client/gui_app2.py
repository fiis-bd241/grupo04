import tkinter as tk
from tkinter import ttk
from model.cotizacion_dao import Cotizacion
from model.cotizacion_dao import guardar, listar, editar

def barra_menu(root):
    barra_menu2 = tk.Menu(root)
    root.config(menu = barra_menu2, width = 300, height = 300)

    menu_inicio = tk.Menu(barra_menu2, tearoff = 0)
    barra_menu2.add_cascade(label = 'Cotizacion', menu = menu_inicio)



class Frame2(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root,width = 480, height = 320)
        self.root = root
        self.pack()

        self.id_cotizacion = None
        self.campos_cotizacion()
        self.deshabilitar_campos()
        self.tabla_cotizacion()

    def campos_cotizacion(self):
        # Label de cada campo
        self.label_id = tk.Label(self, text = 'ID: ')
        self.label_id.config(font = ('Arial', 12, 'bold'))
        self.label_id.grid(row = 0, column = 0, padx = 10, pady = 10)

        self.label_montototal = tk.Label(self, text = 'Monto: ')
        self.label_montototal.config(font = ('Arial', 12, 'bold'))
        self.label_montototal.grid(row = 1, column = 0, padx = 10, pady = 10)

        self.label_ruc = tk.Label(self, text = 'RUC: ')
        self.label_ruc.config(font = ('Arial', 12, 'bold'))
        self.label_ruc.grid(row = 2, column = 0, padx = 10, pady = 10)

        self.label_fecha = tk.Label(self, text = 'Fecha: ')
        self.label_fecha.config(font = ('Arial', 12, 'bold'))
        self.label_fecha.grid(row = 3, column = 0, padx = 10, pady = 10)

        self.label_estado = tk.Label(self, text = 'Estado: ')
        self.label_estado.config(font = ('Arial', 12, 'bold'))
        self.label_estado.grid(row = 4, column = 0, padx = 10, pady = 10)

        #Entry de cada campo
        self.mi_id = tk.IntVar()
        self.entry_id = tk.Entry(self, textvariable = self.mi_id)
        self.entry_id.config(width = 50, font = ('Arial', 12))
        self.entry_id.grid(row = 0, column = 1, padx = 10, pady = 10, columnspan = 2)

        self.mi_monto = tk.DoubleVar()
        self.entry_monto = tk.Entry(self, textvariable = self.mi_monto)
        self.entry_monto.config(width = 50, font = ('Arial', 12))
        self.entry_monto.grid(row = 1, column = 1, padx = 10, pady = 10, columnspan = 2)

        self.mi_ruc = tk.StringVar()
        self.entry_ruc = tk.Entry(self, textvariable = self.mi_ruc)
        self.entry_ruc.config(width = 50, font = ('Arial', 12))
        self.entry_ruc.grid(row = 2, column = 1, padx = 10, pady = 10, columnspan = 2)

        self.mi_fecha = tk.StringVar()
        self.entry_fecha = tk.Entry(self, textvariable = self.mi_fecha)
        self.entry_fecha.config(width = 50, font = ('Arial', 12))
        self.entry_fecha.grid(row = 3, column = 1, padx = 10, pady = 10, columnspan = 2)

        self.mi_estado = tk.StringVar()
        self.entry_estado = tk.Entry(self, textvariable = self.mi_estado)
        self.entry_estado.config(width = 50, font = ('Arial', 12))
        self.entry_estado.grid(row = 4, column = 1, padx = 10, pady = 10, columnspan = 2)

        # Botones
        # Boton nuevo
        self.boton_nuevo = tk.Button(self, text = "Nuevo", command = self.habilitar_campos)
        self.boton_nuevo.config(width = 20, font = ('Arial', 12, 'bold'), 
                                fg = '#DAD5D6', bg = '#158645',
                                cursor = 'hand2', activebackground = '#35BD6F')
        self.boton_nuevo.grid(row = 5, column = 0, padx = 10, pady = 10)

        # Boton guardar
        self.boton_guardar = tk.Button(self, text = "Guardar", command = self.guardar_datos)
        self.boton_guardar.config(width = 20, font = ('Arial', 12, 'bold'), 
                                fg = '#DAD5D6', bg = '#1658A2',
                                cursor = 'hand2', activebackground = '#3586DF')
        self.boton_guardar.grid(row = 5, column = 1, padx = 10, pady = 10)

        # Boton cancelar
        self.boton_cancelar = tk.Button(self, text = "Cancelar",command = self.deshabilitar_campos)
        self.boton_cancelar.config(width = 20, font = ('Arial', 12, 'bold'), 
                                fg = '#DAD5D6', bg = '#BD152E',
                                cursor = 'hand2', activebackground = '#E15370')
        self.boton_cancelar.grid(row = 5, column = 2, padx = 10, pady = 10)
    def habilitar_campos(self):
        self.mi_id.set('')
        self.mi_monto.set('')
        self.mi_ruc.set('')
        self.mi_fecha.set('')
        self.mi_estado.set('')

        self.entry_id.config(state = 'normal')
        self.entry_monto.config(state = 'normal')
        self.entry_ruc.config(state = 'normal')
        self.entry_fecha.config(state = 'normal')
        self.entry_estado.config(state = 'normal')

        self.boton_guardar.config(state = 'normal')
        self.boton_cancelar.config(state = 'normal')

    def deshabilitar_campos(self):
        self.mi_id.set('')
        self.mi_monto.set('')
        self.mi_ruc.set('')
        self.mi_fecha.set('')
        self.mi_estado.set('')

        self.entry_id.config(state = 'disabled')
        self.entry_monto.config(state = 'disabled')
        self.entry_ruc.config(state = 'disabled')
        self.entry_fecha.config(state = 'disabled')
        self.entry_estado.config(state = 'disabled')

        self.boton_guardar.config(state = 'disabled')
        self.boton_cancelar.config(state = 'disabled')
    def guardar_datos(self):
        
        cotizacion = Cotizacion(
            self.mi_id.get(),
            self.mi_monto.get(),
            self.mi_ruc.get(),
            self.mi_fecha.get(),
            self.mi_estado.get(),

        )
        if self.id_cotizacion == None:
            guardar(cotizacion)
        else:
            editar(cotizacion, self.id_cotizacion)
        self.tabla_cotizacion()

        self.deshabilitar_campos()
        
    def tabla_cotizacion(self):
        #Recuperar lista
        self.lista_cotizacion = listar()
        self.lista_cotizacion.reverse()

        self.tabla = ttk.Treeview(self,
                                  column = ('ID', 'MONTO', 'RUC', 'FECHA', 'ESTADO'))
        self.tabla.grid(row = 6, column = 0, columnspan = 4, sticky='nse')

        #Scrollbar
        self.scroll = ttk.Scrollbar(self, orient='vertical', command = self.tabla.yview)
        self.scroll.grid(row = 6, column = 4, sticky='nse')
        self.tabla.configure(yscrollcommand = self.scroll.set)

        self.tabla.heading('#0', text = 'ID')
        self.tabla.heading('#1', text = 'MONTO')
        self.tabla.heading('#2', text = 'RUC')
        self.tabla.heading('#3', text = 'FECHA')
        self.tabla.heading('#4', text = 'ESTADO')


        #Iterar lista peliculas
        for p in self.lista_cotizacion:
            self.tabla.insert('', 0, text = p[0], 
            values = (p[1], p[2], p[3],p[4]))
        
        # Boton editar
        self.boton_editar = tk.Button(self, text = "Editar",command= self.editar_datos)
        self.boton_editar.config(width = 20, font = ('Arial', 12, 'bold'), 
                                fg = '#DAD5D6', bg = '#158645',
                                cursor = 'hand2', activebackground = '#35BD6F')
        self.boton_editar.grid(row = 7, column = 0, padx = 10, pady = 10)

        # Boton eliminar
        #self.boton_eliminar = tk.Button(self, text = "Eliminar")
        #self.boton_eliminar.config(width = 20, font = ('Arial', 12, 'bold'), 
        #                        fg = '#DAD5D6', bg = '#BD152E',
        #                        cursor = 'hand2', activebackground = '#E15370')
        #self.boton_eliminar.grid(row = 7, column = 1, padx = 10, pady = 10)

    def editar_datos(self):
        
        self.id_cotizacion = self.tabla.item(self.tabla.selection())['text']
        self.monto_total = self.tabla.item(self.tabla.selection())['values'][0]
        self.ruc_proveedor = self.tabla.item(self.tabla.selection())['values'][1]
        self.fecha = self.tabla.item(self.tabla.selection())['values'][2]
        self.id_est_cotizacion = self.tabla.item(self.tabla.selection())['values'][3]

            
        self.habilitar_campos()

        self.entry_id.insert(0,self.id_cotizacion)
        self.entry_monto.insert(0,self.monto_total)
        self.entry_ruc.insert(0,self.ruc_proveedor)
        self.entry_fecha.insert(0,self.fecha)
        self.entry_estado.insert(0,self.id_est_cotizacion)

        