import psycopg2
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import threading

# Conectar a la base de datos PostgreSQL
def connect_db():
    try:
        conn = psycopg2.connect(
            host='localhost',
            port=5432,
            dbname='MIGNI',
            user='postgres',
            password='chocopancho65'
        )
        return conn
    except Exception as e:
        messagebox.showerror("Error", f"No se puede conectar a la base de datos: {e}")
        return None

# Obtener datos de la tabla Producto
def get_product_data(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Producto")
        data = cursor.fetchall()
        cursor.close()
        return data
    except Exception as e:
        messagebox.showerror("Error", f"No se pueden obtener los datos: {e}")
        return []

column_map = {
    'id_producto': 0,
    'nombre_producto': 1,
    'descripcion_prod': 2,
    'Cant_min': 3,
    'Cant_max': 4,
    'Precio_unit': 5,
    'Id_categoria_prod': 6
}

class Application:
    def __init__(self, master):
        self.master = master
        self.conn = connect_db()
        if not self.conn:
            return
        
        self.data = get_product_data(self.conn)
        self.figures = []
        
        self.frame = tk.Frame(master, bg='pink')
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.chart_type_label = tk.Label(self.frame, text="Tipo de Gráfico:", bg='pink')
        self.chart_type_label.grid(row=0, column=0, sticky=tk.W)
        
        self.chart_type = ttk.Combobox(self.frame, values=["Barras", "Circular", "Dispersión", "Lineal"])
        self.chart_type.grid(row=0, column=1, sticky=tk.W)
        self.chart_type.current(0)
        
        self.x_col_label = tk.Label(self.frame, text="Columna X:", bg='pink')
        self.x_col_label.grid(row=1, column=0, sticky=tk.W)
        
        self.x_col = ttk.Combobox(self.frame, values=list(column_map.keys()))
        self.x_col.grid(row=1, column=1, sticky=tk.W)
        self.x_col.current(1)
        
        self.y_col_label = tk.Label(self.frame, text="Columna Y:", bg='pink')
        self.y_col_label.grid(row=2, column=0, sticky=tk.W)
        
        self.y_col = ttk.Combobox(self.frame, values=list(column_map.keys()))
        self.y_col.grid(row=2, column=1, sticky=tk.W)
        self.y_col.current(5)
        
        self.plot_button = ttk.Button(self.frame, text="Graficar", command=self.start_plot_thread)
        self.plot_button.grid(row=3, column=0, columnspan=2, sticky=tk.W)
        
        self.save_button = ttk.Button(self.frame, text="Guardar Gráfico", command=self.save_chart)
        self.save_button.grid(row=5, column=0, columnspan=2, sticky=tk.W)
        
        self.load_button = ttk.Button(self.frame, text="Cargar Datos", command=self.load_data_from_file)
        self.load_button.grid(row=6, column=0, columnspan=2, sticky=tk.W)
        
        self.canvas_frame = tk.Frame(master, bg='pink')
        self.canvas_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    def start_plot_thread(self):
        threading.Thread(target=self.on_plot_button_click).start()

    def on_plot_button_click(self):
        fig = self.plot_data(self.data, self.chart_type.get(), self.x_col.get(), self.y_col.get())
        self.figures.append(fig)
        
        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def plot_data(self, data, chart_type, x_col, y_col):
        fig, ax = plt.subplots(figsize=(10, 6))
        
        x_index = column_map[x_col]
        y_index = column_map[y_col]
        
        x_data = [row[x_index] for row in data]
        y_data = [row[y_index] for row in data]
        
        if chart_type == 'Barras':
            ax.bar(x_data, y_data)
        elif chart_type == 'Circular':
            ax.pie(y_data, labels=x_data, autopct='%1.1f%%', startangle=90)
        elif chart_type == 'Dispersión':
            ax.scatter(x_data, y_data)
        elif chart_type == 'Lineal':
            ax.plot(x_data, y_data)
        
        ax.set_xlabel(x_col, fontsize=12)
        ax.set_ylabel(y_col, fontsize=12)
        ax.set_title(f'{chart_type} de {x_col} vs {y_col}', fontsize=14)
        ax.grid(True)
        return fig

    def save_chart(self):
        if self.figures:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
            if file_path:
                for fig in self.figures:
                    fig.savefig(file_path)
                messagebox.showinfo("Guardar Gráfico", "Gráfico guardado exitosamente.")
        else:
            messagebox.showerror("Error", "No hay gráficos para guardar.")

    def load_data_from_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx"), ("All files", "*.*")])
        if file_path:
            if file_path.endswith('.csv'):
                data = pd.read_csv(file_path)
            elif file_path.endswith('.xlsx'):
                data = pd.read_excel(file_path)
            self.data = data.to_numpy().tolist()

def create_main_window():
    root = tk.Tk()
    root.title("Sistema de Información")
    app = Application(root)
    root.mainloop()

if __name__ == "__main__":
    create_main_window()
