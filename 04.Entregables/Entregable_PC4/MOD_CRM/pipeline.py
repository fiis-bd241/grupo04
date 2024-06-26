import psycopg2
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd

# Configuración de la conexión a la base de datos
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    dbname="MIGNI",
    user="postgres",
    password="chocopancho65"
)

def fetch_data(query):
    try:
        df = pd.read_sql(query, conn)
        return df
    except Exception as e:
        messagebox.showerror("Database Error", str(e))
        return None

def display_data(df):
    for i in tree.get_children():
        tree.delete(i)
    tree["column"] = list(df.columns)
    tree["show"] = "headings"
    for col in tree["column"]:
        tree.heading(col, text=col)
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        tree.insert("", "end", values=row)

def fetch_and_display(query):
    df = fetch_data(query)
    if df is not None:
        display_data(df)

def on_select_stage(event):
    selected_stage = stage_combobox.get()
    fetch_and_display(f"SELECT * FROM Persona WHERE etapa = '{selected_stage}'")

def update_stage(person_id, new_stage):
    try:
        cur = conn.cursor()
        cur.execute("UPDATE Persona SET etapa = %s WHERE Id_persona = %s", (new_stage, person_id))
        conn.commit()
        cur.close()
        messagebox.showinfo("Success", "Stage updated successfully")
    except Exception as e:
        messagebox.showerror("Database Error", str(e))

def on_mark_won():
    selected_item = tree.selection()[0]
    person_id = tree.item(selected_item)["values"][0]
    update_stage(person_id, "ganado")

def on_set_reminder():
    selected_item = tree.selection()[0]
    person_id = tree.item(selected_item)["values"][0]
    reminder_date = reminder_entry.get()
    try:
        cur = conn.cursor()
        cur.execute("UPDATE Persona SET reminder_date = %s WHERE Id_persona = %s", (reminder_date, person_id))
        conn.commit()
        cur.close()
        messagebox.showinfo("Success", "Reminder set successfully")
    except Exception as e:
        messagebox.showerror("Database Error", str(e))

# Configuración de la ventana principal
root = tk.Tk()
root.title("CRM Pipeline")
root.geometry("1000x600")
root.configure(bg="#FFD1DC")  # Fondo rosa pastel

frame = tk.Frame(root, bg="#FFD1DC")
frame.pack(pady=20)

# Combobox para seleccionar la etapa del pipeline
stages = ["nuevo", "calificado", "propuesta", "negociacion", "ganado"]
stage_combobox = ttk.Combobox(frame, values=stages)
stage_combobox.pack(pady=10)
stage_combobox.bind("<<ComboboxSelected>>", on_select_stage)

# Treeview para mostrar los datos
tree = ttk.Treeview(root)
tree.pack()

# Botón para marcar como ganado
mark_won_button = tk.Button(root, text="Marcar como Ganado", command=on_mark_won, bg="#FFD1DC")
mark_won_button.pack(pady=10)

# Entrada y botón para establecer un recordatorio
reminder_frame = tk.Frame(root, bg="#FFD1DC")
reminder_frame.pack(pady=10)

reminder_label = tk.Label(reminder_frame, text="Fecha de recordatorio (YYYY-MM-DD):", bg="#FFD1DC")
reminder_label.pack(side="left")
reminder_entry = tk.Entry(reminder_frame)
reminder_entry.pack(side="left")

set_reminder_button = tk.Button(reminder_frame, text="Establecer Recordatorio", command=on_set_reminder, bg="#FFD1DC")
set_reminder_button.pack(side="left")

# Botón para salir de la aplicación
exit_button = tk.Button(root, text="Salir", command=root.quit, bg="#FFD1DC")
exit_button.pack(pady=10)

# Iniciar la aplicación
root.mainloop()

# Cerrar la conexión a la base de datos
conn.close()

