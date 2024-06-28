import tkinter as tk
from equipo_mark.gui_app import LoginFrame, Frame, barra_menu

def main():
    root = tk.Tk()
    root.title("Módulo de equipo de marketing")
    root.resizable(0, 0)

    login_frame = LoginFrame(root, on_login_success)
    login_frame.pack()

    root.mainloop()

def on_login_success(root, equipo_id):
    for widget in root.winfo_children():
        widget.destroy()
    
    barra_menu(root)
    app = Frame(root=root, equipo_id=equipo_id)
    app.pack()

if __name__ == '__main__':
    main()


