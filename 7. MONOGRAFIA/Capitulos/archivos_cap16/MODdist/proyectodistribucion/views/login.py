import tkinter as tk
from tkinter import messagebox
from controllers.login_controller import login
from views.repartidor import RepartidorView
from views.cliente import ClienteView
from views.gestor_distribucion import GestorDistribucionView

class LoginView(tk.Frame):
    def __init__(self, root, on_login_success):
        super().__init__(root)
        self.root = root
        self.on_login_success = on_login_success

        self.configure(bg="pink")  # Fondo rosado

        # Ajusta el tamaño de la ventana
        root.geometry("400x300")

        self.usuario_label = tk.Label(self, text="Usuario", bg="pink")  # Fondo rosado
        self.usuario_label.pack()

        self.usuario_entry = tk.Entry(self)
        self.usuario_entry.pack()

        self.contraseña_label = tk.Label(self, text="Contraseña", bg="pink")  # Fondo rosado
        self.contraseña_label.pack()

        self.contraseña_entry = tk.Entry(self, show="*")
        self.contraseña_entry.pack()

        self.cliente_button = tk.Button(self, text="Login como Cliente", command=lambda: self.perform_login("CLI"), bg="green", fg="black")  # Botón verde con texto negro
        self.cliente_button.pack(pady=10)

        self.gestor_button = tk.Button(self, text="Login como Gestor", command=lambda: self.perform_login("GDT"), bg="blue", fg="white")  # Botón azul con texto blanco
        self.gestor_button.pack(pady=10)

        self.repartidor_button = tk.Button(self, text="Login como Repartidor", command=lambda: self.perform_login("repartidor"), bg="orange", fg="black")  # Botón naranja con texto negro
        self.repartidor_button.pack(pady=10)

    def perform_login(self, role):
        usuario = self.usuario_entry.get()
        contraseña = self.contraseña_entry.get()
        login_result = login(usuario, contraseña, role)  # Agregar role como argumento para el login

        if isinstance(login_result, str):  # Si es un string, es el rol (GDT o CLI)
            if login_result == "GDT":
                messagebox.showinfo("Login", "Bienvenido, Gestor de Distribución")
                self.on_login_success(login_result)  # Llamamos a on_login_success con el rol
            elif login_result == "CLI":
                messagebox.showinfo("Login", "Bienvenido, Cliente")
                self.on_login_success(login_result, usuario)  # Llamamos a on_login_success con el rol y el usuario como id_persona
            elif login_result == "repartidor":
                messagebox.showinfo("Login", "Bienvenido, Repartidor")
                self.on_login_success('repartidor', login_result)  # Llamamos a on_login_success con 'repartidor' y el ID
        else:
            messagebox.showerror("Login", "Usuario o contraseña incorrectos")

    def on_login_success(self, role, id_persona=None):
        if role == "GDT":
            gestor_view = GestorDistribucionView(self.root)
            self.destroy()  # Cerrar la ventana de login
        elif role == "CLI":
            # Aquí se debería obtener el id_persona del cliente desde la base de datos
            # Supongamos que login_result contiene el id_persona del cliente
            cliente_view = ClienteView(self.root, id_persona=id_persona)  # Pasar id_persona como argumento
            self.destroy()  # Cerrar la ventana de login
        elif role == "repartidor":
            repartidor_view = RepartidorView(self.root, id_persona=id_persona)
            self.destroy()  # Cerrar la ventana de login









"""class LoginView(tk.Frame):
    def __init__(self, root, on_login_success):
        super().__init__(root)
        self.root = root
        self.on_login_success = on_login_success

        self.usuario_label = tk.Label(self, text="Usuario")
        self.usuario_label.pack()
        self.usuario_entry = tk.Entry(self)
        self.usuario_entry.pack()

        self.contraseña_label = tk.Label(self, text="Contraseña")
        self.contraseña_label.pack()
        self.contraseña_entry = tk.Entry(self, show="*")
        self.contraseña_entry.pack()

        self.login_button = tk.Button(self, text="Login", command=self.perform_login)
        self.login_button.pack()

    def perform_login(self):
        usuario = self.usuario_entry.get()
        contraseña = self.contraseña_entry.get()
        login_result = login(usuario, contraseña)  # Obtenemos el resultado del login

        if isinstance(login_result, str):  # Si es un string, es el rol (GDT o CLI)
            if login_result == "GDT":
                messagebox.showinfo("Login", "Bienvenido, Gestor de Distribución")
            elif login_result == "CLI":
                messagebox.showinfo("Login", "Bienvenido, Cliente")
            self.on_login_success(login_result)  # Llamamos a on_login_success con el rol
        elif isinstance(login_result, int):  # Si es un entero, es el ID del repartidor
            messagebox.showinfo("Login", "Bienvenido, Repartidor")
            self.on_login_success('repartidor', login_result)  # Llamamos a on_login_success con 'repartidor' y el ID

        else:
            messagebox.showerror("Login", "Usuario o contraseña incorrectos")

    def on_login_success(self, role, repartidor_id=None):
        if role == "GDT":
            self.on_login_success('GDT')
        elif role == "CLI":
            self.on_login_success('CLI')
        elif role == "repartidor":
            repartidor_view = RepartidorView(self.root, repartidor_id)  # Pasamos repartidor_id al constructor de RepartidorView
            repartidor_view.mainloop()  # Iniciamos el bucle principal de la ventana de repartidor
            self.destroy()  # Cerramos la ventana de login
"""









