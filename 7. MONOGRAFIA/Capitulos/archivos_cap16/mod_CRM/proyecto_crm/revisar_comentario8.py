import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import psycopg2

# Configuración de la base de datos
db_params = {
    'host': 'localhost',
    'port': 5432,
    'dbname': 'MIGNI',
    'user': 'postgres',
    'password': 'chocopancho65'
}

class CommentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Comentarios")
        self.root.configure(bg='#FFC0CB')  # Fondo rosa
        self.setup_ui()
        self.fetch_comments()
        self.fetch_reviews()

    def setup_ui(self):
        self.main_frame = tk.Frame(self.root, bg='#FFC0CB')
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        tk.Label(self.main_frame, text="Comentarios", bg='#FFC0CB').grid(row=0, column=0, sticky=tk.W)

        # Frame para la lista de comentarios con scroll horizontal y vertical
        comment_frame = tk.Frame(self.main_frame, bg='#FFC0CB')
        comment_frame.grid(row=1, column=0, columnspan=4, pady=10, sticky='nsew')

        self.comment_list = ttk.Treeview(comment_frame, columns=("Persona", "Producto", "Comentario", "Hora", "Fecha", "ID"), show="headings")
        self.comment_list.heading("Persona", text="Persona")
        self.comment_list.heading("Producto", text="Producto")
        self.comment_list.heading("Comentario", text="Comentario")
        self.comment_list.heading("Hora", text="Hora")
        self.comment_list.heading("Fecha", text="Fecha")
        self.comment_list.heading("ID", text="ID")
        self.comment_list.column("ID", width=0, stretch=tk.NO)  # Ocultar la columna ID

        scrollbar_x = tk.Scrollbar(comment_frame, orient=tk.HORIZONTAL, command=self.comment_list.xview)
        scrollbar_y = tk.Scrollbar(comment_frame, orient=tk.VERTICAL, command=self.comment_list.yview)
        self.comment_list.configure(xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.comment_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        tk.Button(self.main_frame, text="Eliminar Comentario", command=self.delete_comment).grid(row=2, column=0, pady=10)
        tk.Button(self.main_frame, text="Guardar en Revisión", command=self.save_review).grid(row=2, column=1, pady=10)

        tk.Label(self.main_frame, text="Revisión de Comentarios", bg='#FFC0CB').grid(row=3, column=0, sticky=tk.W)

        # Frame para la lista de revisiones con scroll horizontal y vertical
        review_frame = tk.Frame(self.main_frame, bg='#FFC0CB')
        review_frame.grid(row=4, column=0, columnspan=4, pady=10, sticky='nsew')

        self.review_list = ttk.Treeview(review_frame, columns=("Persona", "Producto", "Puntos", "ID", "Comentario", "Descripción"), show="headings")
        self.review_list.heading("Persona", text="Persona")
        self.review_list.heading("Producto", text="Producto")
        self.review_list.heading("Puntos", text="Puntos")
        self.review_list.heading("ID", text="ID")
        self.review_list.heading("Comentario", text="Comentario")
        self.review_list.heading("Descripción", text="Descripción")
        self.review_list.column("ID", width=0, stretch=tk.NO)  # Ocultar la columna ID

        scrollbar_x_review = tk.Scrollbar(review_frame, orient=tk.HORIZONTAL, command=self.review_list.xview)
        scrollbar_y_review = tk.Scrollbar(review_frame, orient=tk.VERTICAL, command=self.review_list.yview)
        self.review_list.configure(xscrollcommand=scrollbar_x_review.set, yscrollcommand=scrollbar_y_review.set)
        scrollbar_x_review.pack(side=tk.BOTTOM, fill=tk.X)
        scrollbar_y_review.pack(side=tk.RIGHT, fill=tk.Y)
        self.review_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        tk.Button(self.main_frame, text="Eliminar Revisión", command=self.delete_review).grid(row=5, column=0, pady=10)

        self.comment_list.bind('<Double-1>', self.show_comment_details)
        self.review_list.bind('<Double-1>', self.show_review_details)

    def connect_db(self):
        return psycopg2.connect(**db_params)

    def fetch_comments(self):
        """Recupera los comentarios de la base de datos y los muestra en la lista."""
        try:
            connection = self.connect_db()
            cursor = connection.cursor()
            cursor.execute("""
                SELECT p.Nombre || ' ' || p.Primer_apell || ' ' || p.Segundo_apell, prod.nombre_producto, c.descrip_comentario, c.hora_comentario, c.fecha_comentario, c.Id_comentario
                FROM Comentario c
                JOIN Persona p ON c.Id_persona = p.Id_persona
                JOIN Producto prod ON c.id_producto = prod.id_producto;
            """)
            comments = cursor.fetchall()
            for comment in comments:
                self.comment_list.insert("", 'end', values=comment)
        except Exception as e:
            messagebox.showerror("Error de Base de Datos", f"No se pudo obtener los comentarios: {e}")
        finally:
            if connection:
                cursor.close()
                connection.close()

    def fetch_reviews(self):
        """Recupera las revisiones de comentarios de la base de datos y las muestra en la lista."""
        try:
            connection = self.connect_db()
            cursor = connection.cursor()
            cursor.execute("""
                SELECT p.Nombre || ' ' || p.Primer_apell || ' ' || p.Segundo_apell, prod.nombre_producto, r.puntos, c.Id_comentario, c.descrip_comentario, prod.descripcion_prod
                FROM Revision r 
                JOIN Comentario c ON r.id_comentario = c.Id_comentario
                JOIN Persona p ON c.Id_persona = p.Id_persona
                JOIN Producto prod ON c.id_producto = prod.id_producto;
            """)
            reviews = cursor.fetchall()
            for review in reviews:
                self.review_list.insert("", 'end', values=review)
        except Exception as e:
            messagebox.showerror("Error de Base de Datos", f"No se pudo obtener las revisiones: {e}")
        finally:
            if connection:
                cursor.close()
                connection.close()

    def delete_comment(self):
        """Elimina el comentario seleccionado de la base de datos y de la lista."""
        selected_item = self.comment_list.selection()
        if selected_item:
            comment_id = self.comment_list.item(selected_item, 'values')[5]  # Obtener el ID del comentario
            try:
                connection = self.connect_db()
                cursor = connection.cursor()
                cursor.execute("DELETE FROM Comentario WHERE Id_comentario = %s", (comment_id,))
                connection.commit()
                self.comment_list.delete(selected_item)
                messagebox.showinfo("Éxito", "Comentario eliminado correctamente")
            except Exception as e:
                messagebox.showerror("Error de Base de Datos", f"No se pudo eliminar el comentario: {e}")
            finally:
                if connection:
                    cursor.close()
                    connection.close()
        else:
            messagebox.showwarning("Advertencia", "Seleccione un comentario para eliminar")

    def save_review(self):
        """Guarda el comentario seleccionado en la tabla de revisiones con puntos."""
        selected_item = self.comment_list.selection()
        if selected_item:
            comment_id = self.comment_list.item(selected_item, 'values')[5]  # Obtener el ID del comentario
            puntos = simpledialog.askinteger("Puntos", "Ingrese la puntuación para este comentario:", minvalue=1, maxvalue=100)
            if puntos is not None:
                try:
                    connection = self.connect_db()
                    cursor = connection.cursor()
                    cursor.execute("INSERT INTO Revision (id_comentario, puntos) VALUES (%s, %s)", (comment_id, puntos))
                    connection.commit()
                    comment_values = self.comment_list.item(selected_item, 'values')
                    self.review_list.insert("", 'end', values=(comment_values[0], comment_values[1], puntos, comment_id, comment_values[2], ""))
                    messagebox.showinfo("Éxito", "Comentario guardado en revisión correctamente")
                except Exception as e:
                    messagebox.showerror("Error de Base de Datos", f"No se pudo guardar el comentario en revisión: {e}")
                finally:
                    if connection:
                        cursor.close()
                        connection.close()
        else:
            messagebox.showwarning("Advertencia", "Seleccione un comentario para guardar en revisión")

    def delete_review(self):
        """Elimina la revisión seleccionada de la base de datos y de la lista."""
        selected_item = self.review_list.selection()
        if selected_item:
            review_id = self.review_list.item(selected_item, 'values')[3]  # Obtener el ID del comentario
            try:
                connection = self.connect_db()
                cursor = connection.cursor()
                cursor.execute("DELETE FROM Revision WHERE id_comentario = %s", (review_id,))
                connection.commit()
                self.review_list.delete(selected_item)
                messagebox.showinfo("Éxito", "Revisión eliminada correctamente")
            except Exception as e:
                messagebox.showerror("Error de Base de Datos", f"No se pudo eliminar la revisión: {e}")
            finally:
                if connection:
                    cursor.close()
                    connection.close()
        else:
            messagebox.showwarning("Advertencia", "Seleccione una revisión para eliminar")

    def show_comment_details(self, event):
        """Muestra los detalles del comentario no revisado en una ventana emergente."""
        selected_item = self.comment_list.selection()
        if selected_item:
            selected_comment = self.comment_list.item(selected_item, 'values')
            persona = selected_comment[0]
            producto = selected_comment[1]
            comentario = selected_comment[2]
            hora = selected_comment[3]
            fecha = selected_comment[4]
            
            details = f"Persona: {persona}\nProducto: {producto}\nComentario: {comentario}\nHora: {hora}\nFecha: {fecha}"
            messagebox.showinfo("Detalles del Comentario", details)

    def show_review_details(self, event):
        """Muestra los detalles del comentario y producto en una ventana emergente."""
        selected_item = self.review_list.selection()
        if selected_item:
            selected_review = self.review_list.item(selected_item, 'values')
            persona = selected_review[0]
            producto = selected_review[1]
            puntos = selected_review[2]
            comentario = selected_review[4]
            desc_producto = selected_review[5]
            
            details = f"Persona: {persona}\nProducto: {producto}\nDescripción del Producto: {desc_producto}\nPuntos: {puntos}\nComentario: {comentario}"
            messagebox.showinfo("Detalles de la Revisión", details)

# Configuración inicial de Tkinter
root = tk.Tk()
app = CommentApp(root)
root.mainloop()
