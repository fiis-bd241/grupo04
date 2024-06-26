import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Modulo CRM")
        self.root.geometry("300x350")
        self.root.configure(bg='#FFC0CB')  # Fondo rosa

        tk.Label(root, text="Ingrese sus credenciales", bg='#FFC0CB').pack(pady=10)
        
        tk.Label(root, text="Usuario:", bg='#FFC0CB').pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack(pady=5)

        tk.Label(root, text="Contraseña:", bg='#FFC0CB').pack()
        password_frame = tk.Frame(root, bg='#FFC0CB')
        password_frame.pack(pady=5)

        self.password_entry = tk.Entry(password_frame, show="*")
        self.password_entry.pack(side=tk.LEFT)

        self.show_password = False
        self.show_password_button = tk.Button(password_frame, text='👁️', command=self.toggle_password)
        self.show_password_button.pack(side=tk.LEFT, padx=5)

        tk.Button(root, text="Ingresar", command=self.check_credentials).pack(pady=10)

        # Cargar y mostrar la imagen
        self.load_image()

    def check_credentials(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "sandrac" and password == "sandrac":
            messagebox.showinfo("Login", "Credenciales correctas")
            self.root.destroy()  # Cierra la ventana de login
            self.run_main_panel()  # Ejecuta el archivo panel_principal.py
        else:
            messagebox.showerror("Login", "Credenciales incorrectas, vuelva a ingresarlas")

    def run_main_panel(self):
        os.system('python panel_principal.py')

    def toggle_password(self):
        if self.show_password:
            self.password_entry.config(show="*")
            self.show_password = False
        else:
            self.password_entry.config(show="")
            self.show_password = True

    def load_image(self):
        image_path = "C:/Users/Administrador/Desktop/imagenesDBD/MIGNI.png"  # Usa barras diagonales
        image = Image.open(image_path)
        image = image.resize((150, 150), Image.LANCZOS)  # Redimensionar la imagen si es necesario
        self.photo = ImageTk.PhotoImage(image)
        tk.Label(self.root, image=self.photo, bg='#FFC0CB').pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
