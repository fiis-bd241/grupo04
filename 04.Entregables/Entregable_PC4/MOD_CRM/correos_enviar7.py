import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import psycopg2
import smtplib
from email.mime.text import MIMEText

class EmailApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Emails")
        self.root.configure(bg='#FFC0CB')  # Fondo rosa
        self.selected_recipients = []
        self.setup_ui()
        self.fetch_emails()
        self.load_sent_emails()

    def connect_db(self):
        return psycopg2.connect(
            host='localhost',
            port='5432',
            dbname='MIGNI',
            user='postgres',
            password='chocopancho65'
        )

    def fetch_emails(self):
        """Conecta a la base de datos y recupera los emails y nombres."""
        try:
            connection = self.connect_db()
            cursor = connection.cursor()
            cursor.execute("SELECT Id_persona, Nombre, Correo FROM Persona;")
            self.emails = cursor.fetchall()
            for id_persona, name, email in self.emails:
                self.email_list.insert("", 'end', values=(id_persona, name, email))
        except Exception as e:
            messagebox.showerror("Error de Base de Datos", f"No se pudo obtener los datos: {e}")
        finally:
            if connection:
                cursor.close()
                connection.close()

    def load_sent_emails(self):
        """Carga todos los emails enviados desde la base de datos y los muestra en la lista."""
        try:
            connection = self.connect_db()
            cursor = connection.cursor()
            cursor.execute("SELECT email_name FROM EmailSend;")
            sent_emails = cursor.fetchall()
            for email_name in sent_emails:
                self.sent_emails_list.insert(tk.END, email_name[0])
        except Exception as e:
            messagebox.showerror("Error de Base de Datos", f"No se pudieron cargar los emails enviados: {e}")
        finally:
            if connection:
                cursor.close()
                connection.close()

    def add_recipients(self):
        """Agrega los contactos seleccionados a la lista de destinatarios."""
        selected_items = self.email_list.selection()
        for item in selected_items:
            id_persona, name, email = self.email_list.item(item, 'values')
            recipient = f"{name} <{email}>"
            if recipient not in self.selected_recipients:
                self.selected_recipients.append(recipient)
                self.recipients_list.insert(tk.END, recipient)

    def send_and_save_email(self):
        """Envía un email a los contactos seleccionados y guarda el registro en la base de datos."""
        msg_text = self.email_body.get("1.0", tk.END)
        email_name = self.email_name_entry.get()
        email_subject = self.subject_entry.get()

        if not email_name.strip():
            messagebox.showerror("Error", "El nombre del email está vacío.")
            return
        if not msg_text.strip():
            messagebox.showerror("Error", "El cuerpo del mensaje está vacío.")
            return
        if not email_subject.strip():
            messagebox.showerror("Error", "El asunto del email está vacío.")
            return
        if not self.selected_recipients:
            messagebox.showerror("Error", "No se ha seleccionado ningún contacto.")
            return
        
        recipients = [recipient.split('<')[1][:-1] for recipient in self.selected_recipients]

        msg = MIMEText(msg_text)
        msg['Subject'] = email_subject
        msg['From'] = 'marcoloza65@gmail.com'
        msg['Bcc'] = ', '.join(recipients)

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('marcoloza65@gmail.com', 'jtpl fmno zmpb oatv')
            server.send_message(msg)
            self.save_sent_email(email_name, recipients, msg_text)
            messagebox.showinfo("Éxito", "Emails enviados correctamente.")
        except Exception as e:
            messagebox.showerror("Error de Envío", f"No se pudo enviar los emails: {e}")
        finally:
            server.quit()

    def save_sent_email(self, email_name, recipients, content):
        """Guarda la información del email enviado en la base de datos."""
        try:
            connection = self.connect_db()
            cursor = connection.cursor()
            query = """INSERT INTO EmailSend (email_name, enviados, email_content) VALUES (%s, %s::text[], %s)"""
            cursor.execute(query, (email_name, recipients, content))
            connection.commit()
            self.sent_emails_list.insert(tk.END, email_name)
        except Exception as e:
            messagebox.showerror("Error de Base de Datos", f"No se pudo guardar el email enviado: {e}")
        finally:
            if connection:
                cursor.close()
                connection.close()

    def load_sent_email_details(self, event):
        """Carga los detalles del email enviado seleccionado."""
        selected_email = self.sent_emails_list.get(self.sent_emails_list.curselection())
        try:
            connection = self.connect_db()
            cursor = connection.cursor()
            query = """SELECT email_name, email_content, enviados FROM EmailSend WHERE email_name = %s"""
            cursor.execute(query, (selected_email,))
            email_details = cursor.fetchone()
            if email_details:
                self.email_name_entry.delete(0, tk.END)
                self.email_name_entry.insert(0, email_details[0])
                self.email_body.delete("1.0", tk.END)
                self.email_body.insert(tk.END, email_details[1])
                self.recipients_list.delete(0, tk.END)
                for recipient in email_details[2]:
                    self.recipients_list.insert(tk.END, recipient)
        except Exception as e:
            messagebox.showerror("Error de Base de Datos", f"No se pudo cargar los detalles del email: {e}")
        finally:
            if connection:
                cursor.close()
                connection.close()

    def delete_sent_email(self):
        """Elimina el email enviado seleccionado de la base de datos y la lista."""
        selected_email = self.sent_emails_list.get(self.sent_emails_list.curselection())
        try:
            connection = self.connect_db()
            cursor = connection.cursor()
            query = """DELETE FROM EmailSend WHERE email_name = %s"""
            cursor.execute(query, (selected_email,))
            connection.commit()
            self.sent_emails_list.delete(self.sent_emails_list.curselection())
            messagebox.showinfo("Éxito", "Email eliminado correctamente.")
        except Exception as e:
            messagebox.showerror("Error de Base de Datos", f"No se pudo eliminar el email: {e}")
        finally:
            if connection:
                cursor.close()
                connection.close()

    def setup_ui(self):
        # Panel para selección de contactos y escritura de email
        frame = tk.Frame(self.root)
        frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Lista de Emails con selección múltiple
        self.email_list = ttk.Treeview(frame, columns=("ID", "Nombre", "Email"), show="headings", selectmode='extended')
        self.email_list.heading("ID", text="ID")
        self.email_list.heading("Nombre", text="Nombre")
        self.email_list.heading("Email", text="Email")
        self.email_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar para la lista de emails
        self.scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.email_list.yview)
        self.email_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=tk.LEFT, fill='y')

        # Botón para agregar destinatarios
        add_recipients_button = tk.Button(frame, text="Agregar Destinatarios", command=self.add_recipients)
        add_recipients_button.pack(pady=10)

        # Panel de escritura de Email
        form_frame = tk.Frame(self.root)
        form_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Etiqueta y cuadro de entrada para el asunto del email
        tk.Label(form_frame, text="Asunto:").pack(anchor='w')
        self.subject_entry = tk.Entry(form_frame, width=50)
        self.subject_entry.pack(pady=5)

        # Etiqueta y cuadro de entrada para el nombre del email
        tk.Label(form_frame, text="Nombre del Email:").pack(anchor='w')
        self.email_name_entry = tk.Entry(form_frame, width=50)
        self.email_name_entry.pack(pady=5)

        # Etiqueta y cuadro de texto para el cuerpo del email
        tk.Label(form_frame, text="Cuerpo del Email:").pack(anchor='w')
        self.email_body = scrolledtext.ScrolledText(form_frame, width=50, height=10)
        self.email_body.pack(pady=5)

        # Botón para enviar y guardar email
        send_save_button = tk.Button(form_frame, text="Guardar y Enviar Email", command=self.send_and_save_email)
        send_save_button.pack(pady=5)

        # Lista de Emails Enviados
        tk.Label(form_frame, text="Emails Enviados:").pack(anchor='w')
        self.sent_emails_list = tk.Listbox(form_frame, height=10, width=50)
        self.sent_emails_list.pack(fill=tk.X, pady=5)
        self.sent_emails_list.bind('<<ListboxSelect>>', self.load_sent_email_details)

        # Botón para eliminar email enviado
        delete_button = tk.Button(form_frame, text="Eliminar Email Enviado", command=self.delete_sent_email)
        delete_button.pack(pady=5)

        # Lista de destinatarios
        tk.Label(form_frame, text="Destinatarios:").pack(anchor='w')
        self.recipients_list = tk.Listbox(form_frame, height=5, width=50)
        self.recipients_list.pack(fill=tk.X, pady=5)

# Configuración inicial de Tkinter
root = tk.Tk()
app = EmailApp(root)
root.mainloop()
