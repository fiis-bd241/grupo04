import tkinter as tk
from client.gui_app import Frame, barra_menu
from client.gui_app2 import Frame2

def ventana_proveedor(root):
    ventana = tk.Toplevel(root)
    ventana.title('Proveedores')
    ventana.resizable(1, 1)
    barra_menu(ventana)
    app = Frame(root=ventana)

def ventana_cotizacion(root):
    ventana = tk.Toplevel(root)
    ventana.title('Cotización')
    ventana.resizable(1, 1)
    barra_menu(ventana)
    app = Frame2(root=ventana)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Aplicación Principal')
    root.geometry('600x300')
    barra_menu(root)
    
    prov = tk.Label(root, text = 'ABRIR PROVEEDORES: ')
    prov.config(font = ('Arial', 12, 'bold'))
    prov.grid(row = 0, column = 0, padx = 10, pady = 10)

    cot = tk.Label(root, text = 'ABRIR COTIZACIONES: ')
    cot.config(font = ('Arial', 12, 'bold'))
    cot.grid(row = 1, column = 0, padx = 10, pady = 10)
    # Crear botones para abrir las ventanas de proveedores y cotización
    boton1=tk.Button(root, text="Proveedores", command=lambda: ventana_proveedor(root))
    boton2=tk.Button(root, text="Cotización", command=lambda: ventana_cotizacion(root))
    boton1.config(width = 20, font = ('Arial', 12, 'bold'), 
                    fg = '#DAD5D6', bg = '#158645',
                    cursor = 'hand2', activebackground = '#35BD6F')
    boton2.config(width = 20, font = ('Arial', 12, 'bold'), 
                    fg = '#DAD5D6', bg = '#1658A2',
                    cursor = 'hand2', activebackground = '#3586DF')
    boton1.grid(row = 0, column = 1)
    boton2.grid(row = 1, column = 1)

    #img = tk.PhotoImage(file="migni.png")
    #lbl_img = tk.Label(root, image = img)
    #lbl_img.pack()

    root.mainloop()