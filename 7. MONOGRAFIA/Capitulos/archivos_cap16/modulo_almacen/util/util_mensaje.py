from tkinter import Toplevel,Label
import util.util_ventana as util_ventana

class ProdNotInfo(Toplevel):
    def __init__(self) -> None:
        super().__init__()
        self.config_window()
        self.contruirWidget()

    def config_window(self):
        self.title('Error')
        self.iconbitmap("./imagenes/Icono.ico")
        w,h = 400,100        
        util_ventana.centrar_ventana(self,w,h)     
                
    def contruirWidget(self):         
        self.labelVersion = Label(self,text="Ingresar al menos el Id Producto")
        self.labelVersion.config(fg="#000000",font=("Roboto",15),pady=1,width=50)
        self.labelVersion.pack()

class ProdNotCheck(Toplevel):
    def __init__(self) -> None:
        super().__init__()
        self.config_window()
        self.contruirWidget()

    def config_window(self):
        self.title('Error')
        self.iconbitmap("./imagenes/Icono.ico")
        w,h = 400,100        
        util_ventana.centrar_ventana(self,w,h)     
                
    def contruirWidget(self):         
        self.labelVersion = Label(self,text="Producto No Encontrado")
        self.labelVersion.config(fg="#000000",font=("Roboto",20),pady=2,width=20)
        self.labelVersion.pack()

class PedidoNotInfo(Toplevel):
    def __init__(self) -> None:
        super().__init__()
        self.config_window()
        self.contruirWidget()

    def config_window(self):
        self.title('Error')
        self.iconbitmap("./imagenes/Icono.ico")
        w,h = 400,100        
        util_ventana.centrar_ventana(self,w,h)     
                
    def contruirWidget(self):         
        self.labelVersion = Label(self,text="Ingresar al menos una búsqueda")
        self.labelVersion.config(fg="#000000",font=("Roboto",15),pady=1,width=50)
        self.labelVersion.pack()

class ConfirmarRegistro(Toplevel):
    def __init__(self) -> None:
        super().__init__()
        self.config_window()
        self.contruirWidget()

    def config_window(self):
        self.title('Error')
        self.iconbitmap("./imagenes/Icono.ico")
        w,h = 400,100        
        util_ventana.centrar_ventana(self,w,h)     
                
    def contruirWidget(self):         
        self.labelVersion = Label(self,text="Productos Agregados a Kardex")
        self.labelVersion.config(fg="#000000",font=("Roboto",15),pady=1,width=50)
        self.labelVersion.pack()
