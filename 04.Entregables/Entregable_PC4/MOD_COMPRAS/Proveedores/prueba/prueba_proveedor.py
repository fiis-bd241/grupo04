import tkinter as tk
from client.gui_app import Frame, barra_menu



def ventana_proveedor():
    root = tk.Tk()
    root.title('Proveedores')
   #root.iconbitmap('img/123.ico')
    root.resizable(0,0)
    barra_menu(root)
    app = Frame(root = root)

    app.mainloop()


if __name__=='__main__':
       ventana_proveedor()
