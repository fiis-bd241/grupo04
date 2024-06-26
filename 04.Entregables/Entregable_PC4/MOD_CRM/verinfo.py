import psycopg2
import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter import messagebox

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

def on_select_table(event):
    selected_table = table_combobox.get()
    fetch_and_display(f"SELECT * FROM {selected_table}")

# Configuración de la ventana principal
root = tk.Tk()
root.title("CRM Pipeline")
root.geometry("800x600")

frame = tk.Frame(root)
frame.pack(pady=20)

# Combobox para seleccionar la tabla
tables = ["tipo_prod", "Categoria_prod", "Area", "zona", "distrito", "Equipo_Marketing", "Rol", "Ruta", "Tipo_mov", "Tipo_Genero", "Tipo_est_cotizacion", "Tipo_est_proveedor", "Tipos_pago", "Persona", "Proveedor", "Cotizacion", "Repartidor", "Campaña", "Detalle_pago", "Producto", "CampañaXProd", "Canal", "CampañaXCanal", "Observacion", "CotizaciónxProducto", "ProveedorxProducto", "Venta", "Cupón", "VentaXProd", "Tipo_est_pedido", "Pedido", "Alternativa", "Pregunta", "Tipo_est_formulario", "Formulario", "Respuesta", "FormularioxPregunta", "PreguntaxRespuesta", "Comentario", "Almacen", "Secciones", "Estands", "Repisas", "Ubicacion", "Transportista", "Orden_Almacen", "Movimiento", "Inventario", "Tipo_Factura", "Estado", "Tip_valor", "Tip_operación", "Tipo_presupuesto", "tipo_asiento_contable", "Estado_de_Resultados", "Factura", "Presupuesto", "Asiento_Contable", "Item_estado_resultados", "EstadoxItem", "EmailSend", "MensajeSend", "Revision"]

table_combobox = ttk.Combobox(frame, values=tables)
table_combobox.pack(pady=10)
table_combobox.bind("<<ComboboxSelected>>", on_select_table)

# Treeview para mostrar los datos
tree = ttk.Treeview(root)
tree.pack()

# Botón para salir de la aplicación
exit_button = tk.Button(root, text="Salir", command=root.quit)
exit_button.pack(pady=10)

# Iniciar la aplicación
root.mainloop()

# Cerrar la conexión a la base de datos
conn.close()
