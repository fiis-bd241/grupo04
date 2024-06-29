from tkinter import Tk
from views.cliente import ClienteView
from views.gestor_distribucion import GestorDistribucionView
from views.repartidor import RepartidorView
from views.login import LoginView

def main():
    root = Tk()
    root.title("Sistema de Distribución")

    def on_login_success(role):
        print(f"Login successful for role: {role}")  # Mensaje de depuración
        if role == "GDT":
            login_view.pack_forget()
            GestorDistribucionView(root, on_volver)
        elif role == "CLI":
            login_view.pack_forget()
            ClienteView(root)
        elif role == "repartidor":
            login_view.pack_forget()
            RepartidorView(root)

    def on_volver():
        print("Returning to login view")  # Mensaje de depuración
        login_view.pack()

    login_view = LoginView(root, on_login_success)
    login_view.pack()

    root.mainloop()

if __name__ == "__main__":
    main()





"""
from tkinter import Tk
from views.cliente import ClienteView
from views.gestor_distribucion import GestorDistribucionView
from views.repartidor import RepartidorView
from views.login import LoginView

def main():
    root = Tk()
    root.title("Sistema de Distribución")

    def on_login_success(role):
        if role == "GDT":
            gestor_view = GestorDistribucionView(root, on_volver)
            gestor_view.pack()
        elif role == "CLI":
            cliente_view = ClienteView(root)
            cliente_view.pack()
        elif role == "repartidor":
            repartidor_view = RepartidorView(root)
            repartidor_view.pack()

    def on_volver():
        login_view.pack()

    login_view = LoginView(root)
    login_view.on_login_success = on_login_success
    #   login_view.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
"""


"""from tkinter import Tk
from views.cliente import ClienteView
from views.gestor_distribucion import GestorDistribucionView
from views.repartidor import RepartidorView
from views.login import LoginView

def main():
    root = Tk()
    root.title("Sistema de Distribución")
    
    # Crea una instancia de LoginView y pasa root como argumento
    login_view = LoginView(root)
    
    # Función para cambiar a la vista correspondiente después del login
    def on_login_success(role):
        if role == 'CLI':
            ClienteView(root)
        elif role == 'GDT':
            GestorDistribucionView(root)
        else:
            RepartidorView(root)

    # Pasa la función de callback al LoginView
    login_view.on_login_success = on_login_success
    
    # Mantén la ventana abierta hasta que se cierre manualmente
    root.mainloop()

if __name__ == "__main__":
    main()"""

