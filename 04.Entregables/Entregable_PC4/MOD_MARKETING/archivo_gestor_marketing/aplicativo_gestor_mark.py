import tkinter as tk
from gestor_mark.gui_app import Frame, barra_menu

def main():
    root = tk.Tk()
    root.title("Módulo de gestor de marketing")
    root.resizable(0,0)
    barra_menu(root)

    app=Frame(root=root)

    app.mainloop()


if __name__ == '__main__':
    main()
    
