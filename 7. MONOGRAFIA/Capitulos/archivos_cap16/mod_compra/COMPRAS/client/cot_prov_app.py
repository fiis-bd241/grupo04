import tkinter as tk
from tkinter import ttk
from model.cot_prov_dao import listar1, buscar2, Proveedor
from model.cot_prov_dao import listar2, guardar2, editar2, Cotizacion

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width = 300, height = 300)

    menu_inicio = tk.Menu(barra_menu, tearoff = 0)
    barra_menu.add_cascade(label = 'LANZAR', menu = menu_inicio)

class Frame3(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root,width = 500, height = 500)
        self.root = root
        self.configure(background='pink')
        
        self.pack()  

        self.historial_button = tk.Button(self, text="Ver Historial de Proveedores", command= self.ver_proveedores)
        self.historial_button.config(width = 20, font = ('Arial', 12, 'bold'), 
                                fg = '#DAD5D6', bg = '#158645',
                                cursor = 'hand2', activebackground = '#35BD6F')
        self.historial_button.grid(row = 0, column = 0, padx = 10, pady = 10)

        self.pendientes_button = tk.Button(self, text="Ver Cotizaciones Pendientes", command= self.ver_cotizacion)
        self.pendientes_button.config(width = 20, font = ('Arial', 12, 'bold'), 
                                fg = '#DAD5D6', bg = '#1658A2',
                                cursor = 'hand2', activebackground = '#3586DF')
        self.pendientes_button.grid(row = 1, column = 0, padx = 10, pady = 10)

        self.volver_button = tk.Button(self, text="Volver", command= root.destroy)
        self.volver_button.config(width = 20, font = ('Arial', 12, 'bold'), 
                                fg = '#DAD5D6', bg = '#BD152E',
                                cursor = 'hand2', activebackground = '#E15370')
        self.volver_button.grid(row = 2, column = 0, padx = 10, pady = 10)
    def ver_cotizacion(self):
        ver_cotizacion = Frame4(self)
        ver_cotizacion.grab_set()

    def ver_proveedores(self):
        #Recuperar lista
        ver_proveedor = Frame5(self)
        ver_proveedor.grab_set()
class Frame5(tk.Toplevel):    
    def __init__(self, root=None):
        super().__init__(root)
        self.title("Proveedores Activos")
        self.resizable(1, 1)
        self.configure(background='pink')
        self.geometry('1300x700')
        
        self.volver_button = tk.Button(self, text="Volver", command= self.destroy)
        self.volver_button.config(width = 20, font = ('Arial', 12, 'bold'), 
                                fg = '#DAD5D6', bg = '#BD152E',
                                cursor = 'hand2', activebackground = '#E15370')
        self.volver_button.grid(row = 3, column = 0, padx = 10, pady = 10)

        self.ruc_proveedor = None
        self.campos_proveedores()
        self.deshabilitar_campos_prov()
        self.tabla_proveedores()
    
    def campos_proveedores(self):
        # Label de cada campo
        self.label_ruc = tk.Label(self, text = 'RUC: ')
        self.label_ruc.config(font = ('Arial', 12, 'bold'))
        self.label_ruc.grid(row = 0, column = 0, padx = 10, pady = 10)

        #Entry de cada campo
        self.mi_ruc = tk.IntVar()
        self.entry_ruc = tk.Entry(self, textvariable = self.mi_ruc)
        self.entry_ruc.config(width = 50, font = ('Arial', 12))
        self.entry_ruc.grid(row = 0, column = 1, padx = 10, pady = 10, columnspan = 2)

        self.boton_buscar = tk.Button(self, text = "Buscar", command= self.tabla_cotizacion_prov)
        self.boton_buscar.config(width = 20, font = ('Arial', 12, 'bold'), 
                                fg = '#DAD5D6', bg = '#1658A2',
                                cursor = 'hand2', activebackground = '#3586DF')
        self.boton_buscar.grid(row = 1, column = 2, padx = 10, pady = 10)
        
        self.boton_cancelar = tk.Button(self, text = "Cancelar",command = self.deshabilitar_campos_prov)
        self.boton_cancelar.config(width = 20, font = ('Arial', 12, 'bold'), 
                                fg = '#DAD5D6', bg = '#BD152E',
                                cursor = 'hand2', activebackground = '#E15370')
        self.boton_cancelar.grid(row = 1, column = 3, padx = 10, pady = 10)
        
    def tabla_proveedores(self):
        #Recuperar lista
        self.lista_proveedor = listar1()
        self.lista_proveedor.reverse()

        self.tabla = ttk.Treeview(self,
                                  column = ('RUC', 'Razon_social', 'webProveedor', 'rubro','direccion','telefono','id_est_proveedor',))
        self.tabla.grid(row = 2, column = 0, columnspan = 4, sticky='nse')

        #Scrollbar
        self.scroll = ttk.Scrollbar(self, orient='vertical', command = self.tabla.yview)
        self.scroll.grid(row = 2, column = 4, sticky='nse')
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
        
        self.boton_seleccionar = tk.Button(self, text = "Seleccionar", command= self.seleccionar_datos_prov)
        self.boton_seleccionar.config(width = 20, font = ('Arial', 12, 'bold'), 
                                fg = '#DAD5D6', bg = '#158645',
                                cursor = 'hand2', activebackground = '#35BD6F')
        self.boton_seleccionar.grid(row = 1, column = 0, padx = 10, pady = 10)

    def habilitar_campos_prov(self):
        self.mi_ruc.set('')

        self.entry_ruc.config(state = 'normal')
        self.boton_buscar.config(state = 'normal')
        self.boton_cancelar.config(state = 'normal')

    def deshabilitar_campos_prov(self):
        self.mi_ruc.set('')

        self.entry_ruc.config(state = 'disabled')

        self.boton_cancelar.config(state = 'disabled')
        self.boton_buscar.config(state = 'disabled')

    def guardar_datos_prov(self):
        
        proveedor = Proveedor(
            self.mi_ruc.get(),
        )
        if self.ruc_proveedor == None:
            pass
        else:
            buscar2(proveedor, self.ruc_proveedor)

        self.tabla_proveedores()

        self.deshabilitar_campos_prov()

    def seleccionar_datos_prov(self):
        
        self.ruc_proveedor = self.tabla.item(self.tabla.selection())['text']
            
        self.habilitar_campos_prov()

        self.entry_ruc.insert(0,self.ruc_proveedor)
    

    def tabla_cotizacion_prov(self):
        proveedor = Proveedor(
            self.mi_ruc.get(),
        )
        #Recuperar lista
        self.lista_cotizacion_prov = buscar2(proveedor)
        self.lista_cotizacion_prov.reverse()

        self.tabla = ttk.Treeview(self,
                                  column = ('ID', 'MONTO', 'RUC', 'HORA', 'ESTADO'))
        self.tabla.grid(row = 5, column = 0, columnspan = 4, sticky='nse')

        #Scrollbar
        self.scroll = ttk.Scrollbar(self, orient='vertical', command = self.tabla.yview)
        self.scroll.grid(row = 5, column = 4, sticky='nse')
        self.tabla.configure(yscrollcommand = self.scroll.set)

        self.tabla.heading('#0', text = 'ID')
        self.tabla.heading('#1', text = 'MONTO')
        self.tabla.heading('#2', text = 'RUC')
        self.tabla.heading('#3', text = 'HORA')
        self.tabla.heading('#4', text = 'ESTADO')


        #Iterar lista cotizaciones
        for p in self.lista_cotizacion_prov:
            self.tabla.insert('', 0, text = p[0], 
            values = (p[1], p[2], p[3],p[4]))
    

class Frame4(tk.Toplevel):    
    def __init__(self, root=None):
        super().__init__(root)
        self.title('Cotizaciones Pendientes')
        self.resizable(1, 1)
        self.configure(background='pink')
        self.geometry('1300x700')
        
        self.volver_button = tk.Button(self, text="Volver", command=self.destroy)
        self.volver_button.config(width=20, font=('Arial', 12, 'bold'), 
                                  fg='#DAD5D6', bg='#BD152E',
                                  cursor='hand2', activebackground='#E15370')
        self.volver_button.grid(row=4, column=1, padx=10, pady=10)
        self.id_cotizacion = None
        
        self.campos_cotizacion()
        self.deshabilitar_campos_cot()
        self.tabla_cotizacion()


    def campos_cotizacion(ver_cotizacion):
        # Label de cada campo
        ver_cotizacion.label_id = tk.Label(ver_cotizacion, text = 'ID: ')
        ver_cotizacion.label_id.config(font = ('Arial', 12, 'bold'))
        ver_cotizacion.label_id.grid(row = 0, column = 0, padx = 10, pady = 10)

        ver_cotizacion.label_estado = tk.Label(ver_cotizacion, text = 'Estado: ')
        ver_cotizacion.label_estado.config(font = ('Arial', 12, 'bold'))
        ver_cotizacion.label_estado.grid(row = 1, column = 0, padx = 10, pady = 10)

        #Entry de cada campo
        ver_cotizacion.mi_id = tk.IntVar()
        ver_cotizacion.entry_id = tk.Entry(ver_cotizacion, textvariable = ver_cotizacion.mi_id)
        ver_cotizacion.entry_id.config(width = 50, font = ('Arial', 12))
        ver_cotizacion.entry_id.grid(row = 0, column = 1, padx = 10, pady = 10, columnspan = 2)

        ver_cotizacion.mi_estado = tk.StringVar()
        ver_cotizacion.entry_estado = tk.Entry(ver_cotizacion, textvariable = ver_cotizacion.mi_estado)
        ver_cotizacion.entry_estado.config(width = 50, font = ('Arial', 12))
        ver_cotizacion.entry_estado.grid(row = 1, column = 1, padx = 10, pady = 10, columnspan = 2)

        # Botones

        # Boton guardar
        ver_cotizacion.boton_guardar = tk.Button(ver_cotizacion, text = "Guardar", command = ver_cotizacion.guardar_datos_cot)
        ver_cotizacion.boton_guardar.config(width = 20, font = ('Arial', 12, 'bold'), 
                                fg = '#DAD5D6', bg = '#1658A2',
                                cursor = 'hand2', activebackground = '#3586DF')
        ver_cotizacion.boton_guardar.grid(row = 2, column = 1, padx = 10, pady = 10)

        # Boton cancelar
        ver_cotizacion.boton_cancelar = tk.Button(ver_cotizacion, text = "Cancelar",command = ver_cotizacion.deshabilitar_campos_cot)
        ver_cotizacion.boton_cancelar.config(width = 20, font = ('Arial', 12, 'bold'), 
                                fg = '#DAD5D6', bg = '#BD152E',
                                cursor = 'hand2', activebackground = '#E15370')
        ver_cotizacion.boton_cancelar.grid(row = 2, column = 2, padx = 10, pady = 10)

    def tabla_cotizacion(ver_cotizacion):
        #Recuperar lista
        ver_cotizacion.lista_cotizacion = listar2()
        ver_cotizacion.lista_cotizacion.reverse()

        ver_cotizacion.tabla = ttk.Treeview(ver_cotizacion,
                                  column = ('ID', 'MONTO', 'RUC', 'HORA', 'ESTADO'))
        ver_cotizacion.tabla.grid(row = 3, column = 0, columnspan = 4, sticky='nse')

        #Scrollbar
        ver_cotizacion.scroll = ttk.Scrollbar(ver_cotizacion, orient='vertical', command = ver_cotizacion.tabla.yview)
        ver_cotizacion.scroll.grid(row = 3, column = 4, sticky='nse')
        ver_cotizacion.tabla.configure(yscrollcommand = ver_cotizacion.scroll.set)

        ver_cotizacion.tabla.heading('#0', text = 'ID')
        ver_cotizacion.tabla.heading('#1', text = 'MONTO')
        ver_cotizacion.tabla.heading('#2', text = 'RUC')
        ver_cotizacion.tabla.heading('#3', text = 'HORA')
        ver_cotizacion.tabla.heading('#4', text = 'ESTADO')


        #Iterar lista cotizaciones
        for p in ver_cotizacion.lista_cotizacion:
            ver_cotizacion.tabla.insert('', 0, text = p[0], 
            values = (p[1], p[2], p[3],p[4]))
        
        # Boton editar
        ver_cotizacion.boton_editar = tk.Button(ver_cotizacion, text = "Editar",command= ver_cotizacion.editar_datos_cot)
        ver_cotizacion.boton_editar.config(width = 20, font = ('Arial', 12, 'bold'), 
                                fg = '#DAD5D6', bg = '#158645',
                                cursor = 'hand2', activebackground = '#35BD6F')
        ver_cotizacion.boton_editar.grid(row = 2, column = 0, padx = 10, pady = 10)
    def habilitar_campos_cot(ver_cotizacion):
        ver_cotizacion.mi_id.set('')
        ver_cotizacion.mi_estado.set('')

        ver_cotizacion.entry_id.config(state = 'normal')
        ver_cotizacion.entry_estado.config(state = 'normal')

        ver_cotizacion.boton_guardar.config(state = 'normal')
        ver_cotizacion.boton_cancelar.config(state = 'normal')

    def deshabilitar_campos_cot(lista_cotizacion):
        lista_cotizacion.mi_id.set('')
        lista_cotizacion.mi_estado.set('')

        lista_cotizacion.entry_id.config(state = 'disabled')
        lista_cotizacion.entry_estado.config(state = 'disabled')

        lista_cotizacion.boton_guardar.config(state = 'disabled')
        lista_cotizacion.boton_cancelar.config(state = 'disabled')
    def guardar_datos_cot(ver_cotizacion):
        
        cotizacion = Cotizacion(
            ver_cotizacion.mi_id.get(),
            ver_cotizacion.mi_estado.get(),

        )
        if ver_cotizacion.id_cotizacion == None:
            guardar2(cotizacion)
        else:
            editar2(cotizacion, ver_cotizacion.id_cotizacion)
        ver_cotizacion.tabla_cotizacion()

        ver_cotizacion.deshabilitar_campos_cot()

    def editar_datos_cot(ver_cotizacion):
        
        ver_cotizacion.id_cotizacion = ver_cotizacion.tabla.item(ver_cotizacion.tabla.selection())['text']
        ver_cotizacion.id_est_cotizacion = ver_cotizacion.tabla.item(ver_cotizacion.tabla.selection())['values'][3]

            
        ver_cotizacion.habilitar_campos_cot()

        ver_cotizacion.entry_id.insert(0,ver_cotizacion.id_cotizacion)
        ver_cotizacion.entry_estado.insert(0,ver_cotizacion.id_est_cotizacion)

        
        

    

        

        

