import tkinter as tk
from client.gui_app import Frame, barra_menu

def ventana_facturas(root):
    ventana = tk.Toplevel(root)
    ventana.title('Facturas')
    ventana.resizable(0,0)
    barra_menu(ventana)

    app = Frame (root = ventana)

if __name__=='__main__':
    root = tk.Tk()
    root.title('Home')
    root.geometry('600x300')
    barra_menu (root)

    fac = tk.Label(root, text='Registrar Factura:')
    fac.config(font = ('Arial', 12, 'bold'))
    fac.grid(row = 0, column = 0, padx = 10, pady = 10)

    # Crear botones para abrir las ventanas de Facturas
    boton1=tk.Button(root, text="Registrar facturas", command=lambda: ventana_facturas(root))
    boton1.config(width = 20, font = ('Arial', 12, 'bold'), 
                    fg = '#DAD5D6', bg = '#158645',
                    cursor = 'hand2', activebackground = '#35BD6F')

    boton1.grid(row = 0, column = 1)
  

    root.mainloop()