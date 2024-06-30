import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import psycopg2
import smtplib
from email.mime.text import MIMEText
import requests
import json
import datetime

class PipelineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Pipeline")
        self.root.configure(bg='#FFC0CB')
        self.setup_ui()
        self.fetch_users()

    def connect_db(self):
        return psycopg2.connect(
            host='localhost',
            port='5432',
            dbname='MIGNI',
            user='postgres',
            password='chocopancho65'
        )

    def fetch_users(self):
        try:
            connection = self.connect_db()
            cursor = connection.cursor()
            cursor.execute("SELECT Id_persona, Nombre, Correo, Telefono FROM Persona;")
            self.users = cursor.fetchall()
            for id_persona, name, email, phone in self.users:
                self.user_list.insert("", 'end', values=(id_persona, name, email, phone, "no clasificado"))
        except Exception as e:
            messagebox.showerror("Error de Base de Datos", f"No se pudo obtener los datos: {e}")
        finally:
            if connection:
                cursor.close()
                connection.close()

    def update_pipeline(self):
        selected_items = self.user_list.selection()
        estado = self.pipeline_status.get()
        if not selected_items:
            messagebox.showerror("Error", "No se ha seleccionado ningún usuario.")
            return
        if not estado:
            messagebox.showerror("Error", "No se ha seleccionado ningún estado.")
            return
        
        try:
            connection = self.connect_db()
            cursor = connection.cursor()
            for item in selected_items:
                id_persona = self.user_list.item(item, 'values')[0]
                cursor.execute("""
                    INSERT INTO Pipeline (Id_persona, estado) 
                    VALUES (%s, %s) 
                    ON CONFLICT (Id_persona) 
                    DO UPDATE SET estado = EXCLUDED.estado;
                """, (id_persona, estado))
                self.user_list.item(item, values=(id_persona, self.user_list.item(item, 'values')[1], self.user_list.item(item, 'values')[2], self.user_list.item(item, 'values')[3], estado))
            connection.commit()
            messagebox.showinfo("Éxito", "Usuarios actualizados en el pipeline.")
        except Exception as e:
            messagebox.showerror("Error de Base de Datos", f"No se pudo actualizar el pipeline: {e}")
        finally:
            if connection:
                cursor.close()
                connection.close()

    def setup_ui(self):
        frame = tk.Frame(self.root)
        frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.user_list = ttk.Treeview(frame, columns=("ID", "Nombre", "Email", "Teléfono", "Estado"), show="headings", selectmode='extended')
        self.user_list.heading("ID", text="ID")
        self.user_list.heading("Nombre", text="Nombre")
        self.user_list.heading("Email", text="Email")
        self.user_list.heading("Teléfono", text="Teléfono")
        self.user_list.heading("Estado", text="Estado")
        self.user_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.user_list.yview)
        self.user_list.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.LEFT, fill='y')

        self.user_list.bind('<Double-1>', self.on_user_click)

        form_frame = tk.Frame(self.root)
        form_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        tk.Label(form_frame, text="Estado del Pipeline:").pack(anchor='w')
        self.pipeline_status = ttk.Combobox(form_frame, values=["no clasificado", "nuevo", "calificado", "propuesta", "negociación", "ganado"])
        self.pipeline_status.pack(pady=5)

        update_button = tk.Button(form_frame, text="Actualizar Pipeline", command=self.update_pipeline)
        update_button.pack(pady=5)

    def on_user_click(self, event):
        selected_item = self.user_list.selection()[0]
        user_info = self.user_list.item(selected_item, 'values')
        user_id, user_name, user_email, user_phone, user_estado = user_info

        action_window = tk.Toplevel(self.root)
        action_window.title(f"Acciones para {user_name}")
        action_window.configure(bg='#FFC0CB')

        email_button = tk.Button(action_window, text="Enviar Email", command=lambda: self.open_email_window(user_id, user_email))
        email_button.pack(pady=5)

        whatsapp_button = tk.Button(action_window, text="Enviar WhatsApp", command=lambda: self.open_whatsapp_window(user_id, user_phone))
        whatsapp_button.pack(pady=5)

    def open_email_window(self, user_id, email):
        email_window = tk.Toplevel(self.root)
        email_window.title("Enviar Email")
        email_window.configure(bg='#FFC0CB')

        tk.Label(email_window, text="Asunto:").pack(anchor='w')
        subject_entry = tk.Entry(email_window, width=50)
        subject_entry.pack(pady=5)

        tk.Label(email_window, text="Cuerpo del Email:").pack(anchor='w')
        email_body = scrolledtext.ScrolledText(email_window, width=50, height=10)
        email_body.pack(pady=5)

        def send_email():
            subject = subject_entry.get()
            body = email_body.get("1.0", tk.END).strip()
            if not subject or not body:
                messagebox.showerror("Error", "Asunto y cuerpo del email no pueden estar vacíos.")
                return

            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = 'marcoloza65@gmail.com'
            msg['To'] = email

            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login('marcoloza65@gmail.com', 'jtpl fmno zmpb oatv')
                server.send_message(msg)
                server.quit()
                self.save_sent_email(subject, email, body, user_id)
                messagebox.showinfo("Éxito", "Email enviado correctamente.")
            except Exception as e:
                messagebox.showerror("Error de Envío", f"No se pudo enviar el email: {e}")

        send_button = tk.Button(email_window, text="Enviar Email", command=send_email)
        send_button.pack(pady=5)

    def save_sent_email(self, email_name, recipient, content, user_id):
        try:
            connection = self.connect_db()
            cursor = connection.cursor()
            query = """INSERT INTO EmailSend (email_name, enviados, email_content, fechahora, Id_persona) VALUES (%s, %s::text[], %s, %s, %s)"""
            fecha_hora_actual = datetime.datetime.now()
            cursor.execute(query, (email_name, [recipient], content, fecha_hora_actual, user_id))
            connection.commit()
        except Exception as e:
            messagebox.showerror("Error de Base de Datos", f"No se pudo guardar el email enviado: {e}")
        finally:
            if connection:
                cursor.close()
                connection.close()

    def open_whatsapp_window(self, user_id, phone):
        whatsapp_window = tk.Toplevel(self.root)
        whatsapp_window.title("Enviar WhatsApp")
        whatsapp_window.configure(bg='#FFC0CB')

        tk.Label(whatsapp_window, text="Mensaje de WhatsApp:").pack(anchor='w')
        whatsapp_body = scrolledtext.ScrolledText(whatsapp_window, width=50, height=10)
        whatsapp_body.pack(pady=5)

        def send_whatsapp():
            body = whatsapp_body.get("1.0", tk.END).strip()
            if not body:
                messagebox.showerror("Error", "El cuerpo del mensaje no puede estar vacío.")
                return

            data = {
                "messaging_product": "whatsapp",
                "to": f"+51{phone}",
                "type": "text",
                "text": {
                    "body": body
                }
            }
            headers = {
                "Authorization": f"Bearer {'EAAVsf3uqKBoBO94ZC8PdhGE5aYfcRy8ZAvlUxG7aZAlfQl93WNpxwvZASE5O56BZCMEwa7L3ZA55VKJFmNS4NhqxIeFTmOwHADFCgu3PbCZCfGCWcuuTqPy3ZCddZCm7QeRFtBxUMkCWzsDLs3R2FIt5d0rnTYN7EhpaJn6JtbpBpW8Cu6ZCy2vO9QdkfTlpEz1rAFh00w8LiADXIRfkAm0LIZD'}",
                "Content-Type": "application/json"
            }

            try:
                response = requests.post('https://graph.facebook.com/v19.0/327764460428670/messages', headers=headers, json=data)
                if response.status_code == 200:
                    self.save_sent_message("WhatsApp", [f"+51{phone}"], body, user_id)
                    messagebox.showinfo("Éxito", "Mensaje de WhatsApp enviado correctamente.")
                else:
                    error_data = response.json()
                    error_message = error_data.get("error", {}).get("message", "Error desconocido")
                    raise Exception(f"Error al enviar mensaje: {error_message}")
            except Exception as e:
                messagebox.showerror("Error de Envío", f"No se pudo enviar el mensaje: {e}")

        send_button = tk.Button(whatsapp_window, text="Enviar WhatsApp", command=send_whatsapp)
        send_button.pack(pady=5)

    def save_sent_message(self, mensaje_name, recipients, content, user_id):
        try:
            connection = self.connect_db()
            cursor = connection.cursor()
            query = """INSERT INTO MensajeSend (mensaje_name, enviados, mensaje_content, fechahora, Id_persona) VALUES (%s, %s::text[], %s, %s, %s)"""
            fecha_hora_actual = datetime.datetime.now()
            cursor.execute(query, (mensaje_name, recipients, content, fecha_hora_actual, user_id))
            connection.commit()
        except Exception as e:
            messagebox.showerror("Error de Base de Datos", f"No se pudo guardar el mensaje enviado: {e}")
        finally:
            if connection:
                cursor.close()
                connection.close()

root = tk.Tk()
app = PipelineApp(root)
root.mainloop()
