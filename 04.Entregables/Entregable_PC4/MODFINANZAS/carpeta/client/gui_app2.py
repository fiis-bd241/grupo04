import tkinter as tk
from tkinter import ttk
from tkinter import*
from tkinter import messagebox
from model.verfactura_dao import Factura
from model.verfactura_dao import buscar, guardar, listar, editar
def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width = 300, height = 300 )

    menu_inicio = tk.Menu (barra_menu, tearoff= 0)
    barra_menu.add_cascade(label = 'Inicio', menu = menu_inicio )
class Frame2(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width = 480, height = 320)
        self.root = root
        self.pack()

        self.nro_factura = None
        self.config( bg ='#F1DEE8')
        self.facturas()
        self.deshabilitar_campos()
        self.tabla_facturas()

    def ventana_login(self):
        self.frame_login = Frame(self)
        self.frame_login.pack()

        self.lblframe_login=LabelFrame(self.frame_login, text='Acceso')
        self.lblframe_login.pack(padx=20, pady=20)

        lbltitulo =Label(self.lblframe_login,text='Inicio sesión')
        lbltitulo.pack()

        txt_usuario=Entry(self.lblframe_login)
        txt_usuario.pack(padx=20,pady=20)
        txt_clave=Entry(self.lblframe_login)
        txt_clave.pack(padx=20,pady=20)
        btn_acceso=Button(self.lblframe_login)
        btn_acceso.pack(padx=20,pady=20)

    def facturas(self):
    
        #Botones
        self.boton_nuevo = tk.Button(self, text = "Nuevo", command=self.habilitar_campos)
        self.boton_nuevo.config(width=20, font=('Arial', 12, 'bold'),
                                 fg = 'white', bg ='#92074E', cursor = 'hand2', activebackground='#5B1539')
        self.boton_nuevo.grid(row = 4, column= 0, padx = 10, pady = 10)

        self.boton_guardar = tk.Button(self, text = "Guardar", command=self.guardar_datos)
        self.boton_guardar.config(width=20, font=('Arial', 12, 'bold'),
                                 fg = 'white', bg ='#92074E', cursor = 'hand2', activebackground='#5B1539')
        self.boton_guardar.grid(row = 4, column= 1, padx = 10, pady = 10)

        self.boton_cancelar = tk.Button(self, text = "Cancelar", command=self.deshabilitar_campos)
        self.boton_cancelar.config(width=20, font=('Arial', 12, 'bold'),
                                 fg = 'white', bg ='#92074E', cursor = 'hand2', activebackground='#5B1539')
        self.boton_cancelar.grid(row = 4, column= 2, padx = 10, pady = 10)

    def habilitar_campos(self):
        self.mi_nrofac.set('')
        self.mi_fechae.set('')
        self.mi_monto.set('')
        self.mi_nombres.set('')
        self.mi_RUC.set('')
        self.mi_tipof.set('')
        self.mi_estado.set('')

        self.entry_nrofac.config(state='normal')
        self.entry_fechae.config(state='normal')
        self.entry_monto.config(state='normal')
        self.entry_nombres.config(state='normal')
        self.entry_RUC.config(state='normal')
        self.entry_tipof.config(state='normal')
        self.entry_estado.config(state='normal')

        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')

    def deshabilitar_campos(self):
        self.mi_nrofac.set('')
        self.mi_fechae.set('')
        self.mi_monto.set('')
        self.mi_nombres.set('')
        self.mi_RUC.set('')
        self.mi_tipof.set('')
        self.mi_estado.set('')

        self.entry_nrofac.config(state='disabled')
        self.entry_fechae.config(state='disabled')
        self.entry_monto.config(state='disabled')
        self.entry_nombres.config(state='disabled')
        self.entry_RUC.config(state='disabled')
        self.entry_tipof.config(state='disabled')
        self.entry_estado.config(state='disabled')

        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')
    
    def guardar_datos(self):

        factura = Factura(
            self.mi_nrofac.get(),
            self.mi_fechae.get(),
            self.mi_monto.get(),
            self.mi_nombres.get(),
            self.mi_RUC.get(),
            self.mi_tipof.get(),
            self.mi_estado.get()
        )
        if self.nro_factura == None:
            guardar(factura)
        else: 
            editar(factura, self.nro_factura)
            
        #Deshabilitar campos
        self.tabla_facturas()
        self.deshabilitar_campos()
    
    def tabla_facturas(self):

        self.lista_factura = listar()
        self.lista_factura.reverse()

        self.tabla = ttk.Treeview(self, 
        column = ('Nro.Factura', 'Fecha emision', 'Monto','Id Persona','RUC Proveedor','Id tipfac','Estado de Factura') )
        self.tabla.grid(row = 5, column=0, columnspan=4, sticky='nse')

        #Scrollbar
        self.scroll = ttk.Scrollbar(self, orient='vertical', command = self.tabla.yview)
        self.scroll.grid(row = 8, column = 4, sticky='nse')
        self.tabla.configure(yscrollcommand = self.scroll.set)

        #self.tabla.heading('#0', text='ID')
        self.tabla.heading('#0', text='Nro.Factura')
        self.tabla.heading('#1', text='Fecha emision')
        self.tabla.heading('#2', text='Monto')
        self.tabla.heading('#3', text='ID Persona')
        self.tabla.heading('#4', text='RUC Proveedor')
        self.tabla.heading('#5', text='Id tipfac')
        self.tabla.heading('#6', text='Estado de Factura')

        for p in self.lista_factura:
            self.tabla.insert('', 0, text = p[0], 
            values = (p[1], p[2], p[3],p[4], p[5], p[6]))
       
    
        #Boton editar 
        self.boton_editar = tk.Button(self, text = "Editar")
        self.boton_editar.config(width=20, font=('Arial', 12, 'bold'),
                                 fg = 'white', bg ='#92074E', cursor = 'hand2', activebackground='#5B1539')
        self.boton_editar.grid(row = 6, column= 0, padx = 10, pady = 10)

        #Boton Eliminar
        #self.boton_eliminar = tk.Button(self, text = "Eliminar")
        #self.boton_eliminar.config(width=20, font=('Arial', 12, 'bold'),
                                 #fg = 'white', bg ='#92074E', cursor = 'hand2', activebackground='#5B1539')
        #self.boton_eliminar.grid(row = 6, column= 1, padx = 10, pady = 10)

    def editar_datos(self):
        
        self.nro_factura = self.tabla.item(self.tabla.selection())['text']
        self.fecha_emision = self.tabla.item(self.tabla.selection())['values'][0]
        self.monto= self.tabla.item(self.tabla.selection())['values'][1]
        self.id_persona= self.tabla.item(self.tabla.selection())['values'][2]
        self.ruc_proveedor = self.tabla.item(self.tabla.selection())['values'][3]
        self.id_tip_Fac = self.tabla.item(self.tabla.selection())['values'][4]
        self.id_estado = self.tabla.item(self.tabla.selection())['values'][5]
        
            
        self.habilitar_campos()

        self.entry_nrofac.insert(0,self.nro_factura)
        self.entry_fechae.insert(0,self.fecha_emision)
        self.entry_monto.insert(0,self.monto)
        self.entry_nombres.insert(0,self.id_persona)
        self.entry_RUC.insert(0,self.ruc_proveedor)
        self.entry_tipof.insert(0,self.id_tip_Fac)
        self.entry_estado.insert(0,self.id_estado)