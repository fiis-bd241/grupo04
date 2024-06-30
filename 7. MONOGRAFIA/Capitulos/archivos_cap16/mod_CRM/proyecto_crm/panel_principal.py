import tkinter as tk
from tkinter import ttk
import webbrowser
import os
from PIL import Image, ImageTk
from datetime import datetime
import threading

class MainPanelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Panel Principal")
        self.root.geometry("1200x800")
        self.root.configure(bg='#F8E2E7')  # Fondo rosa claro

        self.create_sidebar()
        self.create_header()
        self.create_main_content()
        self.load_image()  # Añadir la imagen al final
        self.create_clock()  # Añadir el reloj

    def create_sidebar(self):
        sidebar = tk.Frame(self.root, bg='#D480A3', width=200, height=800)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)

        menu_button = tk.Button(sidebar, text="≡", font=('Arial', 20), bg='#D480A3', fg='white', borderwidth=0)
        menu_button.pack(pady=20)

        account_button = tk.Button(sidebar, text="Cuenta", font=('Arial', 14), bg='#D480A3', fg='white', borderwidth=0)
        account_button.pack(pady=10)

        config_button = tk.Button(sidebar, text="Configuración", font=('Arial', 14), bg='#D480A3', fg='white', borderwidth=0)
        config_button.pack(side=tk.BOTTOM, pady=10)

        exit_button = tk.Button(sidebar, text="Salir", font=('Arial', 14), bg='#D480A3', fg='white', borderwidth=0, command=self.exit_and_open_login)
        exit_button.pack(side=tk.BOTTOM, pady=10)

    def exit_and_open_login(self):
        self.root.destroy()
        os.system('python c:/Users/Administrador/Desktop/pythonproyects/apli_escri/login3.py')

    def create_header(self):
        header = tk.Frame(self.root, bg='#800020', height=100)
        header.pack(side=tk.TOP, fill=tk.X)

        welcome_label = tk.Label(header, text="WELCOME", font=('Arial', 16), bg='#800020', fg='white')
        welcome_label.pack(side=tk.LEFT, padx=20)

        nav_frame = tk.Frame(header, bg='#800020')
        nav_frame.pack(side=tk.RIGHT, padx=20)

        dashboard_button = tk.Button(nav_frame, text="DASHBOARD Y REPORTES", font=('Arial', 12), bg='#800020', fg='white', borderwidth=0)
        dashboard_button.grid(row=0, column=0, padx=5)

        def open_email():
            webbrowser.open('https://mail.google.com/mail/u/0/#inbox')

        email_button = tk.Button(nav_frame, text="AVISOS EMAIL", font=('Arial', 12), bg='#800020', fg='white', borderwidth=0, command=open_email)
        email_button.grid(row=0, column=1, padx=5)

        def open_social_media():
            webbrowser.open('https://www.tiktok.com/@migni.store')

        social_button = tk.Button(nav_frame, text="IR A REDES SOCIALES", font=('Arial', 12), bg='#800020', fg='white', borderwidth=0, command=open_social_media)
        social_button.grid(row=0, column=2, padx=5)

    def create_main_content(self):
        content_frame = tk.Frame(self.root, bg='#F8E2E7')
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Main content arranged horizontally
        main_content_frame = tk.Frame(content_frame, bg='#F8E2E7')
        main_content_frame.pack(fill=tk.X)

        # Ser Más Listo section
        ser_mas_listo_frame = tk.Frame(main_content_frame, bg='#F8E2E7')
        ser_mas_listo_frame.pack(side=tk.LEFT, fill=tk.Y, expand=True, padx=10, pady=10)

        ser_mas_listo_label = tk.Label(ser_mas_listo_frame, text="Ser Mas Listo", font=('Arial', 14), bg='#F8E2E7', fg='black')
        ser_mas_listo_label.pack(anchor='n', pady=5)

        btn_whatsapp = tk.Button(ser_mas_listo_frame, text="Wattsapp", font=('Arial', 14), bg='#F5C6CB', fg='black', command=self.run_enviar_wats)
        btn_whatsapp.pack(pady=5)

        btn_comentarios = tk.Button(ser_mas_listo_frame, text="Comentarios", font=('Arial', 14), bg='#F5C6CB', fg='black', command=self.run_revisar_comentarios)
        btn_comentarios.pack(pady=5)

        # Ser Más Productivo section
        ser_mas_productivo_frame = tk.Frame(main_content_frame, bg='#F8E2E7')
        ser_mas_productivo_frame.pack(side=tk.LEFT, fill=tk.Y, expand=True, padx=10, pady=10)

        ser_mas_productivo_label = tk.Label(ser_mas_productivo_frame, text="Ser Más Productivo", font=('Arial', 14), bg='#F8E2E7', fg='black')
        ser_mas_productivo_label.pack(anchor='n', pady=5)

        btn_formulario = tk.Button(ser_mas_productivo_frame, text="Crear Formulario", font=('Arial', 14), bg='#F5C6CB', fg='black', command=self.run_crear_formularios)
        btn_formulario.pack(pady=5)

        btn_email = tk.Button(ser_mas_productivo_frame, text="Crear Email", font=('Arial', 14), bg='#F5C6CB', fg='black', command=self.run_correos_enviar)
        btn_email.pack(pady=5)

        # Obtenga El Mejor Valor section
        mejor_valor_frame = tk.Frame(main_content_frame, bg='#F8E2E7')
        mejor_valor_frame.pack(side=tk.LEFT, fill=tk.Y, expand=True, padx=10, pady=10)

        mejor_valor_label = tk.Label(mejor_valor_frame, text="Obtenga El Mejor Valor", font=('Arial', 14), bg='#F8E2E7', fg='black')
        mejor_valor_label.pack(anchor='n', pady=5)

        btn_potenciales = tk.Button(mejor_valor_frame, text="Mis Clientes Potenciales", font=('Arial', 14), bg='#F5C6CB', fg='black', command=self.run_analisis)
        btn_potenciales.pack(pady=5)

        btn_ver_datos = tk.Button(mejor_valor_frame, text="Ver Datos", font=('Arial', 14), bg='#F5C6CB', fg='black', command=self.run_verinfo)
        btn_ver_datos.pack(pady=5)

        # Data analysis section
        analysis_frame = tk.Frame(content_frame, bg='#F8E2E7')
        analysis_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        analysis_label = tk.Label(analysis_frame, text="Análisis de Pipeline de Datos", font=('Arial', 16), bg='#F8E2E7', fg='black')
        analysis_label.pack()

        btn_pipeline = tk.Button(analysis_frame, text="Abrir Pipeline", font=('Arial', 14), bg='#F5C6CB', fg='black', command=self.run_pipeline)
        btn_pipeline.pack(pady=5)

        # Placeholder for the data analysis content
        analysis_content = tk.Label(analysis_frame, text="[Contenido de análisis de datos]", font=('Arial', 14), bg='#F8E2E7', fg='black')
        analysis_content.pack()

    def run_enviar_wats(self):
        os.system('python c:/Users/Administrador/Desktop/pythonproyects/apli_escri/enviar_wats5.py')

    def run_revisar_comentarios(self):
        os.system('python c:/Users/Administrador/Desktop/pythonproyects/apli_escri/revisar_comentario8.py')

    def run_crear_formularios(self):
        os.system('python c:/Users/Administrador/Desktop/pythonproyects/apli_escri/crear_formularios14.py')

    def run_correos_enviar(self):
        os.system('python c:/Users/Administrador/Desktop/pythonproyects/apli_escri/correos_enviar8.py')

    def run_analisis(self):
        os.system('python c:/Users/Administrador/Desktop/pythonproyects/apli_escri/analisis4.py')

    def run_verinfo(self):
        os.system('python c:/Users/Administrador/Desktop/pythonproyects/apli_escri/verinfo.py')

    def run_pipeline(self):
        os.system('python c:/Users/Administrador/Desktop/pythonproyects/apli_escri/Pipelinefino3.py')

    def load_image(self):
        image_path = "C:/Users/Administrador/Desktop/imagenesDBD/MIGNI.png"  # Usa barras diagonales
        image = Image.open(image_path)
        image = image.resize((150, 150), Image.LANCZOS)  # Redimensionar la imagen si es necesario
        self.photo = ImageTk.PhotoImage(image)
        tk.Label(self.root, image=self.photo, bg='#F8E2E7').pack(side=tk.BOTTOM, pady=10)

    def create_clock(self):
        clock_label = tk.Label(self.root, font=('Arial', 14), bg='#F8E2E7', fg='black')
        clock_label.pack(side=tk.BOTTOM, pady=10)
        self.update_clock(clock_label)

    def update_clock(self, label):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        label.config(text=now)
        self.root.after(1000, self.update_clock, label)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainPanelApp(root)
    root.mainloop()
