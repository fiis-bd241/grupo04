import tkinter as tk
from tkinter import messagebox, scrolledtext
from tkinter import ttk
import psycopg2
import requests
import json

# Configuración de la base de datos
db_params = {
    'host': 'localhost',
    'port': 5432,
    'dbname': 'MIGNI',
    'user': 'postgres',
    'password': 'chocopancho65'
}

# Configuración de la API de WhatsApp
whatsapp_api_url = 'https://developers.facebook.com/apps/1041337737622920/whatsapp-business/wa-dev-console/?business_id=2655225811296630'
access_token = 'EAAOzF1XxNYgBO0uY15yZAe5XackKmi3QY8AHtybZCg1CwrYgkZCZAolHZBxNzHHU5yg8e00BPBTp6Y9wfj85ovlqSi7kkfm4LzKxbxHfeuZCj3GsrZAeroXV3veRSPPQeDKWUur7T7mMNdLWEn4uJTb3jRraDBlflVZCNhzZCpR0338pREdYVTa7p7FcSMyTHqFqUrZC1PlZAm6oqkn2u4wmbb5'

class WhatsAppApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de WhatsApp")
        self.root.configure(bg='#FFC0CB')  # Fondo rosa
        self.selected_recipients = []
        self.setup_ui()
        self.fetch_contacts()
        self.load_sent_messages()

    def connect_db(self):
        return psycopg2.connect(**db_params)

    def fetch_contacts(self):
        """Conecta a la base de datos y recupera los contactos."""
        try:
            connection = self.connect_db()
            cursor = connection.cursor()
            cursor.execute("SELECT Id_persona, Nombre, Telefono FROM Persona;")
            self.contacts = cursor.fetchall()
            for id_persona, name, phone in self.contacts:
                self.contact_list.insert("", 'end', values=(id_persona, name, phone))
        except Exception as e:
            messagebox.showerror("Error de Base de Datos", f"No se pudo obtener los datos: {e}")
        finally:
            if connection:
                cursor.close()
                connection.close()

    def load_sent_messages(self):
        """Carga todos los mensajes enviados desde la base de datos y los muestra en la lista."""
        try:
            connection = self.connect_db()
            cursor = connection.cursor()
            cursor.execute("SELECT mensaje_name FROM MensajeSend;")
            sent_messages = cursor.fetchall()
            for mensaje_name in sent_messages:
                self.sent_messages_list.insert(tk.END, mensaje_name[0])
        except Exception as e:
            messagebox.showerror("Error de Base de Datos", f"No se pudieron cargar los mensajes enviados: {e}")
        finally:
            if connection:
                cursor.close()
                connection.close()

    def add_recipients(self):
        """Agrega los contactos seleccionados a la lista de destinatarios."""
        selected_items = self.contact_list.selection()
        for item in selected_items:
            id_persona, name, phone = self.contact_list.item(item, 'values')
            recipient = f"{name} <{phone}>"
            if recipient not in self.selected_recipients:
                self.selected_recipients.append(recipient)
                self.recipients_list.insert(tk.END, recipient)

    def send_and_save_message(self):
        """Envía un mensaje a los contactos seleccionados y guarda el registro en la base de datos."""
        msg_text = self.message_body.get("1.0", tk.END).strip()
        mensaje_name = self.message_name_entry.get().strip()

        if not mensaje_name:
            messagebox.showerror("Error", "El nombre del mensaje está vacío.")
            return
        if not msg_text:
            messagebox.showerror("Error", "El cuerpo del mensaje está vacío.")
            return
        if not self.selected_recipients:
            messagebox.showerror("Error", "No se ha seleccionado ningún contacto.")
            return
        
        recipients = [recipient.split('<')[1][:-1] for recipient in self.selected_recipients]
        recipients = [f"+51{recipient}" if not recipient.startswith('+') else recipient for recipient in recipients]

        try:
            for recipient in recipients:
                data = {
                    "messaging_product": "whatsapp",
                    "to": recipient,
                    "type": "text",
                    "text": {
                        "body": msg_text
                    }
                }
                headers = {
                    "Authorization": f"Bearer {access_token}",
                    "Content-Type": "application/json"
                }
                response = requests.post(whatsapp_api_url, headers=headers, json=data)
                if response.status_code != 200:
                    error_data = response.json()
                    error_message = error_data.get("error", {}).get("message", "Error desconocido")
                    raise Exception(f"Error al enviar mensaje: {error_message}")

            self.save_sent_message(mensaje_name, recipients, msg_text)
            messagebox.showinfo("Éxito", "Mensajes enviados correctamente.")
        except Exception as e:
            messagebox.showerror("Error de Envío", f"No se pudo enviar los mensajes: {e}")

    def save_sent_message(self, mensaje_name, recipients, content):
        """Guarda la información del mensaje enviado en la base de datos."""
        try:
            connection = self.connect_db()
            cursor = connection.cursor()
            query = """INSERT INTO MensajeSend (mensaje_name, enviados, mensaje_content, Id_persona) VALUES (%s, %s::text[], %s, %s)"""
            cursor.execute(query, (mensaje_name, recipients, content, None))
            connection.commit()
            self.sent_messages_list.insert(tk.END, mensaje_name)
        except Exception as e:
            messagebox.showerror("Error de Base de Datos", f"No se pudo guardar el mensaje enviado: {e}")
        finally:
            if connection:
                cursor.close()
                connection.close()

    def load_sent_message_details(self, event):
        """Carga los detalles del mensaje enviado seleccionado."""
        selected_message = self.sent_messages_list.get(self.sent_messages_list.curselection())
        try:
            connection = self.connect_db()
            cursor = connection.cursor()
            query = """SELECT mensaje_name, mensaje_content, enviados FROM MensajeSend WHERE mensaje_name = %s"""
            cursor.execute(query, (selected_message,))
            message_details = cursor.fetchone()
            if message_details:
                self.message_name_entry.delete(0, tk.END)
                self.message_name_entry.insert(0, message_details[0])
                self.message_body.delete("1.0", tk.END)
                self.message_body.insert(tk.END, message_details[1])
                self.recipients_list.delete(0, tk.END)
                for recipient in message_details[2]:
                    self.recipients_list.insert(tk.END, recipient)
        except Exception as e:
            messagebox.showerror("Error de Base de Datos", f"No se pudo cargar los detalles del mensaje: {e}")
        finally:
            if connection:
                cursor.close()
                connection.close()

    def delete_sent_message(self):
        """Elimina el mensaje enviado seleccionado de la base de datos y la lista."""
        selected_message = self.sent_messages_list.get(self.sent_messages_list.curselection())
        try:
            connection = self.connect_db()
            cursor = connection.cursor()
            query = """DELETE FROM MensajeSend WHERE mensaje_name = %s"""
            cursor.execute(query, (selected_message,))
            connection.commit()
            self.sent_messages_list.delete(self.sent_messages_list.curselection())
            messagebox.showinfo("Éxito", "Mensaje eliminado correctamente.")
        except Exception as e:
            messagebox.showerror("Error de Base de Datos", f"No se pudo eliminar el mensaje: {e}")
        finally:
            if connection:
                cursor.close()
                connection.close()

    def setup_ui(self):
        # Panel para selección de contactos y escritura de mensaje
        frame = tk.Frame(self.root)
        frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Lista de Contactos con selección múltiple
        self.contact_list = ttk.Treeview(frame, columns=("ID", "Nombre", "Teléfono"), show="headings", selectmode='extended')
        self.contact_list.heading("ID", text="ID")
        self.contact_list.heading("Nombre", text="Nombre")
        self.contact_list.heading("Teléfono", text="Teléfono")
        self.contact_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar para la lista de contactos
        self.scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.contact_list.yview)
        self.contact_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=tk.LEFT, fill='y')

        # Botón para agregar destinatarios
        add_recipients_button = tk.Button(frame, text="Agregar Destinatarios", command=self.add_recipients)
        add_recipients_button.pack(pady=10)

        # Panel de escritura de Mensaje
        form_frame = tk.Frame(self.root)
        form_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Etiqueta y cuadro de entrada para el nombre del mensaje
        tk.Label(form_frame, text="Nombre del Mensaje:").pack(anchor='w')
        self.message_name_entry = tk.Entry(form_frame, width=50)
        self.message_name_entry.pack(pady=5)

        # Etiqueta y cuadro de texto para el cuerpo del mensaje
        tk.Label(form_frame, text="Cuerpo del Mensaje:").pack(anchor='w')
        self.message_body = scrolledtext.ScrolledText(form_frame, width=50, height=10)
        self.message_body.pack(pady=5)

        # Botón para enviar y guardar mensaje
        send_save_button = tk.Button(form_frame, text="Guardar y Enviar Mensaje", command=self.send_and_save_message)
        send_save_button.pack(pady=5)

        # Lista de Mensajes Enviados
        tk.Label(form_frame, text="Mensajes Enviados:").pack(anchor='w')
        self.sent_messages_list = tk.Listbox(form_frame, height=10, width=50)
        self.sent_messages_list.pack(fill=tk.X, pady=5)
        self.sent_messages_list.bind('<<ListboxSelect>>', self.load_sent_message_details)

        # Botón para eliminar mensaje enviado
        delete_button = tk.Button(form_frame, text="Eliminar Mensaje Enviado", command=self.delete_sent_message)
        delete_button.pack(pady=5)

        # Lista de destinatarios
        tk.Label(form_frame, text="Destinatarios:").pack(anchor='w')
        self.recipients_list = tk.Listbox(form_frame, height=5, width=50)
        self.recipients_list.pack(fill=tk.X, pady=5)

# Configuración inicial de Tkinter
root = tk.Tk()
app = WhatsAppApp(root)
root.mainloop()
