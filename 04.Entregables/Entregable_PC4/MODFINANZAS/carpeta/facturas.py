import tkinter as tk
from client.gui_app import Frame, barra_menu
from client.gui_app2 import Frame2, barra_menu

def ventana_facturas(root):
    ventana = tk.Toplevel(root)
    ventana.title('Facturas')
    ventana.resizable(0,0)
    barra_menu(ventana)

    app = Frame (root = ventana)

def ventana_verfacturas(root):
    ventana = tk.Toplevel(root)
    ventana.title('Historial de Facturas')
    ventana.resizable(0,0)
    barra_menu(ventana)

    app = Frame2 (root = ventana)

if __name__=='__main__':
    root = tk.Tk()
    root.title('Home')
    root.geometry('600x300')
    root.configure(background='pink')
    barra_menu (root)

    prov = tk.Label(root,fg = "brown",bg="pink", text = 'Bienvenido, Contador General')
    prov.config(font = ('Arial', 16, 'bold'))
    prov.grid(row = 0, column = 1, padx = 10, pady = 10)

    fac = tk.Label(root,fg = "brown",bg="pink", text='Registrar Factura:')
    fac.config(font = ('Arial', 12, 'bold'))
    fac.grid(row = 2, column = 0, padx = 10, pady = 10)

    fac = tk.Label(root,fg = "brown",bg="pink", text='Ver Facturas:')
    fac.config(font = ('Arial', 12, 'bold'))
    fac.grid(row = 3, column = 0, padx = 10, pady = 10)

    fac = tk.Label(root,fg = "brown",bg="pink", text='Ver Asientos Contables:')
    fac.config(font = ('Arial', 12, 'bold'))
    fac.grid(row = 4, column = 0, padx = 10, pady = 10)

    fac = tk.Label(root,fg = "brown",bg="pink", text='Ver Estado de Resultados:')
    fac.config(font = ('Arial', 12, 'bold'))
    fac.grid(row = 5, column = 0, padx = 10, pady = 10)

    # Crear botones para abrir las ventanas de Facturas
    boton1=tk.Button(root, text="Registrar facturas", command=lambda: ventana_facturas(root))
    boton1.config(width = 20, font = ('Arial', 12, 'bold'), 
                    fg = '#DAD5D6', bg ='#E4418B',
                    cursor = 'hand2', activebackground = '#35BD6F')

    boton1.grid(row = 2, column = 1)

    boton2=tk.Button(root, text="Ver facturas", command=lambda: ventana_verfacturas(root))
    boton2.config(width = 20, font = ('Arial', 12, 'bold'), 
                    fg = '#DAD5D6', bg ='#E4418B',
                    cursor = 'hand2', activebackground = '#35BD6F')

    boton2.grid(row = 3, column = 1)

    boton3=tk.Button(root, text=" Asientos Contables ", command=lambda: ventana_facturas(root))
    boton3.config(width = 20, font = ('Arial', 12, 'bold'), 
                    fg = '#DAD5D6', bg ='#E4418B',
                    cursor = 'hand2', activebackground = '#35BD6F')

    boton3.grid(row = 4, column = 1)

    boton4=tk.Button(root, text="Estado de Resultados", command=lambda: ventana_facturas(root))
    boton4.config(width = 20, font = ('Arial', 12, 'bold'), 
                    fg = '#DAD5D6', bg ='#E4418B',
                    cursor = 'hand2', activebackground = '#35BD6F')

    boton4.grid(row = 5, column = 1)
  
   


    root.mainloop()