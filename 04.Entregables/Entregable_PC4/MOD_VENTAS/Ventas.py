import psycopg2
import tkinter as tk
from tkinter import messagebox, ttk

class DatabaseDAO:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="DBD - GRUPO 4",
            user="postgres",
            password="soyuningeniero",
            host="localhost",
            port="5432"
        )

    def fetch_user(self, nombre_usuario, contrasena):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM persona WHERE usuario = %s AND contraseña = %s", (nombre_usuario, contrasena))
        user = cursor.fetchone()
        cursor.close()
        return user

    def fetch_new_id_venta(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT MAX(id_venta) FROM ventaxprod")
        max_id_venta = cursor.fetchone()[0]
        nuevo_id_venta = 900100 if max_id_venta is None else max_id_venta + 1
        cursor.close()
        return nuevo_id_venta

    def fetch_products(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id_producto, nombre_producto, precio_unit FROM PRODUCTO LIMIT 10")
        products = cursor.fetchall()
        cursor.close()
        return products

    def insert_product_to_cart(self, id_venta, producto_id, cantidad, monto_total):
        try:
            cursor = self.conn.cursor()
            id_prod_venta = int(f"{id_venta}{producto_id}")
            cursor.execute(
                "INSERT INTO ventaxprod (id_prod_venta, id_venta, id_producto, cant_prod, monto_total) VALUES (%s, %s, %s, %s, %s)",
                (id_prod_venta, id_venta, producto_id, cantidad, monto_total)
            )
            self.conn.commit()
            cursor.close()
        except Exception as e:
            self.conn.rollback()
            print(f"Error al insertar en ventaxprod: {e}")
            raise e

    def fetch_cart_details(self, id_venta):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT p.nombre_producto, vp.cant_prod, p.precio_unit "
            "FROM ventaxprod vp "
            "JOIN producto p ON vp.id_producto = p.id_producto "
            "WHERE vp.id_venta = %s", (id_venta,)
        )
        cart_details = cursor.fetchall()
        cursor.close()
        return cart_details

    def fetch_payment_methods(self):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT id_tipo_pago, nombre_tipo FROM Tipos_pago"
        )
        payment_methods = cursor.fetchall()
        cursor.close()
        return payment_methods

    def fetch_client_purchase_history(self, nombre_usuario):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT vp.id_venta, pr.id_producto, pr.nombre_producto, vp.cant_prod as cantidad, "
            "pr.precio_unit as precio_unitario, vp.cant_prod*pr.precio_unit as sub_total, "
            "c.esta_activo, vp.cant_prod*pr.precio_unit as monto, t.nombre_tipo as tipo_pago "
            "FROM VentaXProd vp "
            "JOIN venta v ON vp.id_venta=v.id_venta "
            "JOIN producto pr ON pr.id_producto=vp.id_producto "
            "JOIN persona p ON p.id_persona=v.id_persona "
            "JOIN cupón c ON c.id_cupón=vp.id_cupón "
            "JOIN detalle_pago d ON v.id_detalle_pago = d.id_detalle_pago "
            "JOIN tipos_pago t ON t.id_tipo_pago = d.id_tipo_pago "
            "WHERE p.usuario = %s "
            "ORDER BY vp.id_venta", (nombre_usuario,)
        )
        purchase_history = cursor.fetchall()
        cursor.close()
        return purchase_history

    def close(self):
        self.conn.close()

def verificar_usuario(dao, nombre_usuario, contrasena):
    user = dao.fetch_user(nombre_usuario, contrasena)
    return user is not None

def abrir_ventana_catalogo(dao, usuario_actual):
    ventana_catalogo = tk.Tk()
    ventana_catalogo.title("Catálogo de Productos")
    ventana_catalogo.geometry("1000x800")
    ventana_catalogo.configure(bg="#FADBD8")  

    productos = dao.fetch_products()
    carrito = {}


    def agregar_al_carro(producto_id, nombre_producto, precio_unit):
        if producto_id in carrito:
            carrito[producto_id]['cantidad'] += 1
        else:
            carrito[producto_id] = {'nombre': nombre_producto, 'precio': precio_unit, 'cantidad': 1}
        messagebox.showinfo("Carro de Compras", f"Agregado al carro: '{nombre_producto}'")


    def abrir_ventana_carro(ventana_actual):
        ventana_actual.destroy()
        ventana_carro = tk.Tk()
        ventana_carro.title("Carro de Compras")
        ventana_carro.geometry("1000x800")

    
        tk.Label(ventana_carro, text="Carro de Compras", font=("Arial", 24)).pack(pady=10)
        
        total_price = 0

        for producto_id, detalles in carrito.items():
            producto_frame = tk.Frame(ventana_carro, padx=20, pady=10)
            producto_frame.pack(fill='x', padx=10, pady=5)

            tk.Label(producto_frame, text=f"{detalles['nombre']}", font=("Arial", 14)).pack(side=tk.LEFT)
            tk.Label(producto_frame, text=f"Cantidad: {detalles['cantidad']}", font=("Arial", 14)).pack(side=tk.LEFT, padx=20)
            subtotal = detalles['precio'] * detalles['cantidad']
            tk.Label(producto_frame, text=f"Subtotal: ${subtotal}", font=("Arial", 14)).pack(side=tk.LEFT, padx=20)

            total_price += subtotal

    
        tk.Label(ventana_carro, text=f"Monto Total de la Compra: ${total_price}", font=("Arial", 16)).pack(pady=10)

        historial_frame = tk.Frame(ventana_carro, padx=20, pady=10)
        historial_frame.pack(fill='x', padx=10, pady=20)

        tk.Label(historial_frame, text="Historial de Compras:", font=("Arial", 18, "bold")).pack(side=tk.TOP)

        purchase_history = dao.fetch_client_purchase_history(usuario_actual)
        for compra in purchase_history:
            compra_str = f"ID Venta: {compra[0]}, Producto: {compra[2]}, Cantidad: {compra[3]}, Subtotal: ${compra[5]}, Método de Pago: {compra[8]}"
            tk.Label(historial_frame, text=compra_str, font=("Arial", 14)).pack(side=tk.TOP, anchor=tk.W)

        tk.Label(ventana_carro, text="Seleccione Método de Pago:", font=("Arial", 16)).pack(pady=10)

        payment_methods = dao.fetch_payment_methods()
        metodo_pago_var = tk.StringVar(ventana_carro)
        metodo_pago_var.set(payment_methods[0][1])  

        opciones_pago = ttk.Combobox(ventana_carro, textvariable=metodo_pago_var, values=[metodo[1] for metodo in payment_methods], state="readonly", font=("Arial", 14))
        opciones_pago.pack(pady=10)

        def confirmar_metodo_pago():
            messagebox.showinfo("Método de Pago", f"Seleccionado: {metodo_pago_var.get()}")

        tk.Button(ventana_carro, text="Confirmar Método de Pago", font=("Arial", 14), command=confirmar_metodo_pago).pack(pady=20)

        def confirmar_compra():
            try:
                nuevo_id_venta = dao.fetch_new_id_venta()
                for producto_id, detalles in carrito.items():
                    dao.insert_product_to_cart(nuevo_id_venta, producto_id, detalles['cantidad'], detalles['precio'] * detalles['cantidad'])
                messagebox.showinfo("Compra Confirmada", "¡Compra realizada con éxito!")
                ventana_carro.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo confirmar la compra: {e}")

        tk.Button(ventana_carro, text="Confirmar Compra", font=("Arial", 14), command=confirmar_compra).pack(pady=20)

        ventana_carro.mainloop()

    for i, producto in enumerate(productos):
        columna = i // 5  # Dos
        fila = i % 5

        producto_frame = tk.Frame(ventana_catalogo, padx=20, pady=10, bg="#FADBD8")
        producto_frame.grid(row=fila, column=columna, padx=10, pady=10, sticky="nsew")

        tk.Label(producto_frame, text=f"{producto[1]} - ${producto[2]}", font=("Arial", 14), bg="#FADBD8").pack(side=tk.TOP)

        btn_agregar_carro = tk.Button(producto_frame, text="Agregar al Carro", font=("Arial", 12), bg="#58D68D",
                                      padx=10, pady=5,
                                      command=lambda prod_id=producto[0], nombre=producto[1], precio=producto[2]: agregar_al_carro(prod_id, nombre, precio))
        btn_agregar_carro.pack(side=tk.BOTTOM, pady=5)

    tk.Button(ventana_catalogo, text="Ir al Carro de Compras", font=("Arial", 14),
              command=lambda: abrir_ventana_carro(ventana_catalogo)).grid(row=5, column=0, columnspan=2, pady=20)

    ventana_catalogo.mainloop()

def iniciar_sesion(dao):
    nombre_usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()

    if verificar_usuario(dao, nombre_usuario, contrasena):
        messagebox.showinfo("Inicio de Sesión", "¡Inicio de sesión exitoso!")
        ventana_inicio.destroy()
        abrir_ventana_catalogo(dao, nombre_usuario)
    else:
        messagebox.showerror("Inicio de Sesión", "Usuario o contraseña incorrectos")


ventana_inicio = tk.Tk()
ventana_inicio.title("Inicio de Sesión")
ventana_inicio.geometry("600x400")

dao = DatabaseDAO()

tk.Label(ventana_inicio, text="Usuario:", font=("Arial", 14)).pack(pady=10)
entry_usuario = tk.Entry(ventana_inicio, font=("Arial", 14))
entry_usuario.pack()

tk.Label(ventana_inicio, text="Contraseña:", font=("Arial", 14)).pack(pady=10)
entry_contrasena = tk.Entry(ventana_inicio, font=("Arial", 14), show="*")
entry_contrasena.pack()

btn_iniciar_sesion = tk.Button(ventana_inicio, text="Iniciar Sesión", font=("Arial", 14), command=lambda: iniciar_sesion(dao))
btn_iniciar_sesion.pack(pady=20)

ventana_inicio.mainloop()


