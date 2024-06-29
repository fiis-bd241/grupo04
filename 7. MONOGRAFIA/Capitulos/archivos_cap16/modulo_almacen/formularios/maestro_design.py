import tkinter as tk
from tkinter import font
from tkinter import Frame,Label,Button,BOTH,TOP,LEFT,RIGHT
from tkinter import ttk
from config import color_barra_superior,color_menu_lateral,color_cuerpo_principal,color_menu_cursor_encima
import util.util_ventana as util_ventana
import util.util_imagen as util_img
import BD.conexion_bd as bd
from formularios.info_inventario import InfoInventario
from formularios.info_pedidos import InfoPedidos
from formularios.info_kardex import InfoKardex
from formularios.info_producto import InfoProducto

class MaestroDesign(tk.Tk):
    def __init__(self):
        super().__init__()
        self.perfil = util_img.leer_imagen("./imagenes/Almacen.png",(150,150))
        self.fondo= util_img.leer_imagen("./imagenes/Fondo.png",(435,474))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral()
        self.controles_cuerpo()

    def config_window(self):
        self.title('Area Almacen')
        self.iconbitmap("./imagenes/Icono.ico")
        w,h = 1200,600
        util_ventana.centrar_ventana(self,w,h)

    def paneles(self):        
        self.barra_superior = Frame(self,bg=color_barra_superior,height=50)
        self.barra_superior.pack(side=TOP,fill=BOTH)      

        self.menu_lateral = Frame(self,bg=color_menu_lateral,width=150)
        self.menu_lateral.pack(side=LEFT,fill=BOTH,expand=False) 
        
        self.cuerpo_principal = Frame(self,bg=color_cuerpo_principal)
        self.cuerpo_principal.pack(side=RIGHT,fill=BOTH,expand=True)
    
    def controles_barra_superior(self):
        font_awesome = font.Font(family='FontAwesome',size=12)

        self.labelTitulo = Label(self.barra_superior,text="Migni Store")
        self.labelTitulo.config(fg="#fff",font=("Roboto",15),
        bg=color_barra_superior,pady=10,width=16)
        self.labelTitulo.pack(side=LEFT)

        self.buttonMenuLateral = Button(self.barra_superior,text="\uf0c9",font=font_awesome,
        command=self.toggle_panel,bd=0,bg=color_barra_superior,fg="white",relief=tk.FLAT)
        self.buttonMenuLateral.pack(side=LEFT)

        conn,cursor = bd.conectar()
        query = '''
        SELECT p.correo_persona
        FROM Persona p
        JOIN Gestor g ON p.id_persona = g.id_persona
        WHERE g.nombre_usuario = 'manuelramirez';
        '''
        cursor.execute(query)
        row = cursor.fetchone()

        self.labelTitulo = Label(self.barra_superior,text=row)
        self.labelTitulo.config(fg="#fff",font=("Roboto", 10),
        bg=color_barra_superior,padx=10,width=20)
        self.labelTitulo.pack(side=RIGHT)

        cursor.close()
        conn.commit()
        conn.close()
    
    def controles_menu_lateral(self):
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome',size=15)
         
        self.labelPerfil = tk.Label(self.menu_lateral,image=self.perfil,bg=color_menu_lateral)
        self.labelPerfil.pack(side=tk.TOP,pady=10)
        
        self.buttonInventario = tk.Button(self.menu_lateral)        
        self.buttonPedidos = tk.Button(self.menu_lateral)        
        self.buttonKardex = tk.Button(self.menu_lateral)
        self.buttonProducto = tk.Button(self.menu_lateral)

        buttons_info = [
            ("Inventario","\uf109",self.buttonInventario,self.abrir_inventario),
            ("Pedidos","\uf109",self.buttonPedidos,self.abrir_pedidos),
            ("Kardex","\uf03e",self.buttonKardex,self.abrir_kardex),
            ("Nuevo Producto","\uf03e",self.buttonProducto,self.abrir_producto)
        ]

        for text,icon,button,comando in buttons_info:
            self.configurar_boton_menu(button,text,icon,font_awesome,ancho_menu,alto_menu,comando)
    
    def configurar_boton_menu(self,button,text,icon,font_awesome,ancho_menu,alto_menu,comando):
        button.config(text=f"  {icon}    {text}",anchor="w",font=font_awesome,bd=0,
        bg=color_menu_lateral,fg="black",width=ancho_menu,height=alto_menu,command=comando)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)
    
    def bind_hover_events(self,button):
        button.bind("<Enter>",lambda event: self.on_enter(event,button))
        button.bind("<Leave>",lambda event: self.on_leave(event,button))
    
    def on_enter(self,event,button):
        button.config(bg=color_menu_cursor_encima,fg='black')

    def on_leave(self, event, button):
        button.config(bg=color_menu_lateral,fg='black')

    def toggle_panel(self):
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=LEFT,fill='y')
    
    def controles_cuerpo(self): 
        label = Label(self.cuerpo_principal,image=self.fondo,bg=color_cuerpo_principal)
        label.place(x=0,y=0,relwidth=1,relheight=1)   
    
    def abrir_inventario(self):   
        self.limpiar_panel(self.cuerpo_principal)     
        InfoInventario(self.cuerpo_principal)
    
    def abrir_pedidos(self):   
        self.limpiar_panel(self.cuerpo_principal)     
        InfoPedidos(self.cuerpo_principal)
    
    def abrir_kardex(self):   
        self.limpiar_panel(self.cuerpo_principal)     
        InfoKardex(self.cuerpo_principal)

    def abrir_producto(self):   
        self.limpiar_panel(self.cuerpo_principal)     
        InfoProducto(self.cuerpo_principal)

    def limpiar_panel(self,panel):
        for widget in panel.winfo_children():
            widget.destroy()
