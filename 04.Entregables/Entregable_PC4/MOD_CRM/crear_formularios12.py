import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import psycopg2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class FormularioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestionar Formularios")
        self.root.geometry("1200x800")

        self.create_widgets()
        self.connect_db()
        self.load_formularios()
        self.fetch_emails()

    def connect_db(self):
        try:
            self.conn = psycopg2.connect(
                host='localhost',
                port=5432,
                dbname='MIGNI',
                user='postgres',
                password='chocopancho65'
            )
            self.cursor = self.conn.cursor()
            messagebox.showinfo("Conexión", "Conectado a la base de datos")
        except Exception as e:
            messagebox.showerror("Error de Conexión", str(e))

    def create_widgets(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.create_form_frame = tk.Frame(self.notebook, bg='#FFD1DC')
        self.manage_form_frame = tk.Frame(self.notebook, bg='#FFD1DC')
        self.email_form_frame = tk.Frame(self.notebook, bg='#FFD1DC')

        self.notebook.add(self.create_form_frame, text="Crear Formulario")
        self.notebook.add(self.manage_form_frame, text="Gestionar Formularios")
        self.notebook.add(self.email_form_frame, text="Enviar Formulario")

        self.create_form_ui()
        self.manage_form_ui()
        self.email_form_ui()

    def create_form_ui(self):
        frame = self.create_form_frame

        ttk.Label(frame, text="Descripción del Formulario:", background='#FFD1DC').grid(column=0, row=0, padx=10, pady=10)
        self.desc_entry = ttk.Entry(frame, width=50)
        self.desc_entry.grid(column=1, row=0, padx=10, pady=10)

        ttk.Label(frame, text="Tipo de Pregunta:", background='#FFD1DC').grid(column=0, row=1, padx=10, pady=10)
        self.tipo_preg_var = tk.StringVar()
        self.tipo_preg_combo = ttk.Combobox(frame, textvariable=self.tipo_preg_var)
        self.tipo_preg_combo['values'] = ("Texto", "Múltiple Opción")
        self.tipo_preg_combo.grid(column=1, row=1, padx=10, pady=10)

        ttk.Label(frame, text="Pregunta:", background='#FFD1DC').grid(column=0, row=2, padx=10, pady=10)
        self.preg_entry = ttk.Entry(frame, width=50)
        self.preg_entry.grid(column=1, row=2, padx=10, pady=10)

        ttk.Label(frame, text="Alternativas (separadas por comas):", background='#FFD1DC').grid(column=0, row=3, padx=10, pady=10)
        self.alt_entry = ttk.Entry(frame, width=50)
        self.alt_entry.grid(column=1, row=3, padx=10, pady=10)

        ttk.Button(frame, text="Añadir Pregunta", command=self.add_question).grid(column=2, row=3, padx=10, pady=10)

        self.question_list = tk.Listbox(frame, width=50, height=10)
        self.question_list.grid(column=1, row=4, padx=10, pady=10)

        ttk.Button(frame, text="Crear Formulario", command=self.create_form).grid(column=1, row=5, padx=10, pady=10)

    def manage_form_ui(self):
        frame = self.manage_form_frame

        ttk.Label(frame, text="Formularios Creados:", background='#FFD1DC').grid(column=0, row=0, padx=10, pady=10)
        self.form_listbox = tk.Listbox(frame, width=50, height=20)
        self.form_listbox.grid(column=1, row=0, padx=10, pady=10)
        self.form_listbox.bind('<<ListboxSelect>>', self.show_form_details)

        ttk.Button(frame, text="Eliminar Formulario", command=self.delete_form).grid(column=2, row=0, padx=10, pady=10)

        ttk.Label(frame, text="Preguntas del Formulario:", background='#FFD1DC').grid(column=0, row=1, padx=10, pady=10)
        self.question_listbox = tk.Listbox(frame, width=50, height=10)
        self.question_listbox.grid(column=1, row=1, padx=10, pady=10)

        ttk.Label(frame, text="Personas que Respondieron:", background='#FFD1DC').grid(column=0, row=2, padx=10, pady=10)
        self.respondent_listbox = tk.Listbox(frame, width=50, height=10)
        self.respondent_listbox.grid(column=1, row=2, padx=10, pady=10)
        self.respondent_listbox.bind('<<ListboxSelect>>', self.show_respondent_details)

        ttk.Label(frame, text="Respuestas de la Persona:", background='#FFD1DC').grid(column=0, row=3, padx=10, pady=10)
        self.response_listbox = tk.Listbox(frame, width=50, height=10)
        self.response_listbox.grid(column=1, row=3, padx=10, pady=10)

    def email_form_ui(self):
        frame = self.email_form_frame

        ttk.Label(frame, text="Formularios Creados:", background='#FFD1DC').grid(column=0, row=0, padx=10, pady=10)
        self.email_form_listbox = tk.Listbox(frame, width=50, height=20)
        self.email_form_listbox.grid(column=1, row=0, padx=10, pady=10)

        ttk.Label(frame, text="Enviar Formulario a:", background='#FFD1DC').grid(column=0, row=1, padx=10, pady=10)
        self.email_list = ttk.Treeview(frame, columns=("ID", "Nombre", "Email"), show="headings", selectmode='extended')
        self.email_list.heading("ID", text="ID")
        self.email_list.heading("Nombre", text="Nombre")
        self.email_list.heading("Email", text="Email")
        self.email_list.grid(column=1, row=1, padx=10, pady=10)

        ttk.Button(frame, text="Agregar Destinatarios", command=self.add_recipients).grid(column=2, row=1, padx=10, pady=10)

        self.recipients_list = tk.Listbox(frame, width=50, height=5)
        self.recipients_list.grid(column=1, row=2, padx=10, pady=10)

        ttk.Button(frame, text="Enviar Formulario", command=self.send_form).grid(column=1, row=3, padx=10, pady=10)

    def load_formularios(self):
        try:
            self.form_listbox.delete(0, tk.END)
            self.email_form_listbox.delete(0, tk.END)
            self.cursor.execute("SELECT Id_formulario, descrip_formulario FROM Formulario ORDER BY descrip_formulario")
            formularios = self.cursor.fetchall()
            for form in formularios:
                form_text = f"{form[0]} - {form[1]}"
                self.form_listbox.insert(tk.END, form_text)
                self.email_form_listbox.insert(tk.END, form_text)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def fetch_emails(self):
        try:
            self.email_list.delete(*self.email_list.get_children())
            self.cursor.execute("SELECT Id_persona, Nombre, Correo FROM Persona;")
            emails = self.cursor.fetchall()
            for id_persona, name, email in emails:
                self.email_list.insert("", 'end', values=(id_persona, name, email))
        except Exception as e:
            messagebox.showerror("Error de Base de Datos", f"No se pudo obtener los datos: {e}")

    def add_question(self):
        question = self.preg_entry.get()
        tipo_preg = self.tipo_preg_var.get()
        alternativas = self.alt_entry.get()

        if question and tipo_preg:
            if tipo_preg == "Múltiple Opción" and not alternativas:
                messagebox.showwarning("Advertencia", "Debe proporcionar alternativas para una pregunta de Múltiple Opción")
                return

            question_text = f"{question} ({tipo_preg})"
            if alternativas:
                question_text += f" [Alternativas: {alternativas}]"
            self.question_list.insert(tk.END, question_text)
            self.preg_entry.delete(0, tk.END)
            self.alt_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "La pregunta y el tipo de pregunta no pueden estar vacíos")

    def create_form(self):
        desc = self.desc_entry.get()
        questions = self.question_list.get(0, tk.END)

        if not desc or not questions:
            messagebox.showwarning("Advertencia", "La descripción y las preguntas no pueden estar vacías")
            return

        try:
            self.cursor.execute("INSERT INTO Formulario (descrip_formulario, fecha_creacion, Id_est_formulario) VALUES (%s, CURRENT_DATE, %s) RETURNING Id_formulario", (desc, 1))
            form_id = self.cursor.fetchone()[0]

            for question in questions:
                parts = question.split(" (")
                pregunta = parts[0]
                tipo_preg = parts[1].split(")")[0]
                alternativas = None
                if "[" in parts[1]:
                    alternativas = parts[1].split("[Alternativas: ")[1].replace("]", "")
                
                if alternativas:
                    self.cursor.execute("INSERT INTO Alternativa (alternativa) VALUES (%s) RETURNING id_alternativa", (alternativas.split(","),))
                    alternativa_id = self.cursor.fetchone()[0]
                    self.cursor.execute("INSERT INTO Pregunta (pregunta, tipo_preg, id_alternativa) VALUES (%s, %s, %s) RETURNING Id_pregunta", (pregunta, tipo_preg, alternativa_id))
                else:
                    self.cursor.execute("INSERT INTO Pregunta (pregunta, tipo_preg) VALUES (%s, %s) RETURNING Id_pregunta", (pregunta, tipo_preg))

                question_id = self.cursor.fetchone()[0]
                self.cursor.execute("INSERT INTO FormularioxPregunta (Id_formulario, Id_pregunta) VALUES (%s, %s)", (form_id, question_id))

            self.conn.commit()
            messagebox.showinfo("Éxito", "Formulario creado exitosamente")
            self.load_formularios()
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror("Error", str(e))

    def add_recipients(self):
        selected_items = self.email_list.selection()
        for item in selected_items:
            id_persona, name, email = self.email_list.item(item, 'values')
            recipient = f"{name} <{email}>"
            if recipient not in self.recipients_list.get(0, tk.END):
                self.recipients_list.insert(tk.END, recipient)

    def send_form(self):
        selection = self.email_form_listbox.curselection()
        if not selection:
            messagebox.showwarning("Advertencia", "Seleccione un formulario para enviar")
            return

        form_id = self.email_form_listbox.get(selection[0]).split(' - ')[0]
        recipients = [recipient.split('<')[1][:-1] for recipient in self.recipients_list.get(0, tk.END)]

        try:
            self.cursor.execute("SELECT descrip_formulario FROM Formulario WHERE Id_formulario = %s", (form_id,))
            form_desc = self.cursor.fetchone()[0]

            self.cursor.execute("SELECT pregunta FROM Pregunta INNER JOIN FormularioxPregunta ON Pregunta.Id_pregunta = FormularioxPregunta.Id_pregunta WHERE FormularioxPregunta.Id_formulario = %s", (form_id,))
            questions = self.cursor.fetchall()

            msg = MIMEMultipart()
            msg['From'] = 'tu_email@gmail.com'
            msg['Subject'] = "Nueva Encuesta"
            msg['Bcc'] = ', '.join(recipients)

            body = f"Descripción: {form_desc}\n\nPreguntas:\n" + "\n".join([q[0] for q in questions])
            msg.attach(MIMEText(body, 'plain', 'utf-8'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('tu_email@gmail.com', 'tu_contraseña')
            server.send_message(msg)
            server.quit()

            messagebox.showinfo("Éxito", "Encuesta enviada correctamente.")
        except Exception as e:
            messagebox.showerror("Error de Envío", f"No se pudo enviar la encuesta: {e}")

    def show_form_details(self, event):
        selection = self.form_listbox.curselection()
        if selection:
            form_id = self.form_listbox.get(selection[0]).split(' - ')[0]
            try:
                self.question_listbox.delete(0, tk.END)
                self.cursor.execute("SELECT pregunta FROM Pregunta INNER JOIN FormularioxPregunta ON Pregunta.Id_pregunta = FormularioxPregunta.Id_pregunta WHERE FormularioxPregunta.Id_formulario = %s", (form_id,))
                questions = self.cursor.fetchall()
                for question in questions:
                    self.question_listbox.insert(tk.END, question[0])

                self.respondent_listbox.delete(0, tk.END)
                self.cursor.execute("SELECT Persona.Id_persona, Persona.Nombre FROM Persona INNER JOIN Respuesta ON Persona.Id_persona = Respuesta.Id_persona INNER JOIN Pregunta ON Respuesta.Id_pregunta = Pregunta.Id_pregunta INNER JOIN FormularioxPregunta ON Pregunta.Id_pregunta = FormularioxPregunta.Id_pregunta WHERE FormularioxPregunta.Id_formulario = %s", (form_id,))
                respondents = self.cursor.fetchall()
                for respondent in respondents:
                    self.respondent_listbox.insert(tk.END, f"{respondent[0]} - {respondent[1]}")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def show_respondent_details(self, event):
        selection = self.respondent_listbox.curselection()
        if selection:
            person_id = self.respondent_listbox.get(selection[0]).split(' - ')[0]
            form_id = self.form_listbox.get(self.form_listbox.curselection()).split(' - ')[0]
            try:
                self.response_listbox.delete(0, tk.END)
                self.cursor.execute("SELECT Pregunta.pregunta, Respuesta.respuesta FROM Respuesta INNER JOIN Pregunta ON Respuesta.Id_pregunta = Pregunta.Id_pregunta INNER JOIN FormularioxPregunta ON Pregunta.Id_pregunta = FormularioxPregunta.Id_pregunta WHERE FormularioxPregunta.Id_formulario = %s AND Respuesta.Id_persona = %s", (form_id, person_id))
                responses = self.cursor.fetchall()
                for response in responses:
                    self.response_listbox.insert(tk.END, f"{response[0]}: {response[1]}")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def delete_form(self):
        selection = self.form_listbox.curselection()
        if selection:
            form_id = self.form_listbox.get(selection[0]).split(' - ')[0]
            try:
                self.cursor.execute("DELETE FROM Respuesta WHERE Id_pregunta IN (SELECT Id_pregunta FROM FormularioxPregunta WHERE Id_formulario = %s)", (form_id,))
                self.cursor.execute("DELETE FROM FormularioxPregunta WHERE Id_formulario = %s", (form_id,))
                self.cursor.execute("DELETE FROM Formulario WHERE Id_formulario = %s", (form_id,))
                self.conn.commit()
                messagebox.showinfo("Éxito", "Formulario eliminado exitosamente")
                self.load_formularios()
            except Exception as e:
                self.conn.rollback()
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Advertencia", "Seleccione un formulario para eliminar")

if __name__ == "__main__":
    root = tk.Tk()
    app = FormularioApp(root)
    root.mainloop()
