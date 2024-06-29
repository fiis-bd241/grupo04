import tkinter as tk
from client.prov_app import Frame, barra_menu
from client.cot_app2 import Frame2
from client.cot_prov_app import Frame3

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

def ventana_cot_prov(root):
    ventana = tk.Toplevel(root)
    ventana.title('Cotización / Proveedor')
    ventana.resizable(1, 1)
    barra_menu(ventana)
    app = Frame3(root=ventana)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Menu Principal Gestor de Compras')
    root.geometry('900x700')
    root.configure(background='pink')
    barra_menu(root)
    
    prov = tk.Label(root,fg = "brown",bg="pink", text = 'BIENVENIDO GESTOR DE COMPRAS')
    prov.config(font = ('Arial', 16, 'bold'))
    prov.grid(row = 0, column = 1, padx = 10, pady = 10)

    prov = tk.Label(root,fg = "brown",bg="pink", text = 'ABRIR PROVEEDORES: ')
    prov.config(font = ('Arial', 12, 'bold'))
    prov.grid(row = 1, column = 0, padx = 10, pady = 10)

    cot = tk.Label(root,fg = "brown",bg="pink", text = 'ABRIR COTIZACIONES: ')
    cot.config(font = ('Arial', 12, 'bold'))
    cot.grid(row = 2, column = 0, padx = 10, pady = 10)
    
    cot_prov = tk.Label(root,fg = "brown",bg="pink", text = 'VER DETALLES: ')
    cot_prov.config(font = ('Arial', 12, 'bold'))
    cot_prov.grid(row = 3, column = 0, padx = 10, pady = 10)
    # Crear botones para abrir las ventanas de proveedores y cotización
    boton1=tk.Button(root, text="Añadir Proveedores", command=lambda: ventana_proveedor(root))
    boton1.config(width = 20, font = ('Arial', 12, 'bold'), 
                    fg = '#DAD5D6', bg = '#E4418B',
                    cursor = 'hand2', activebackground = '#35BD6F')
    boton1.grid(row = 1, column = 1)

    boton2=tk.Button(root, text="Añadir Cotización", command=lambda: ventana_cotizacion(root))
    boton2.config(width = 20, font = ('Arial', 12, 'bold'), 
                    fg = '#DAD5D6', bg = '#FE76B4',
                    cursor = 'hand2', activebackground = '#3586DF')
    boton2.grid(row = 2, column = 1)
    boton3=tk.Button(root, text="Ver Cotización / Proveedor", command=lambda: ventana_cot_prov(root))
    
    boton3.config(width = 20, font = ('Arial', 12, 'bold'), 
                    fg = '#DAD5D6', bg = '#F194BE',
                    cursor = 'hand2', activebackground = '#E15370')
    boton3.grid(row = 3, column = 1)

    img = tk.PhotoImage(file="migni.png")
    img = img.subsample(4, 4)

    # Creo el label para el logo o imagen
    lblLogo = tk.Label(root, image=img)
    lblLogo.grid(row=4, column=1, padx = 10, pady = 10)
    
    root.mainloop()