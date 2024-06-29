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

    def fetch_products(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id_producto, nombre_producto, precio_unit FROM PRODUCTO LIMIT 10")
        products = cursor.fetchall()
        cursor.close()
        return products

    def fetch_new_id_venta(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT MAX(id_venta) FROM ventaxprod")
        max_id_venta = cursor.fetchone()[0]
        nuevo_id_venta = 900100 if max_id_venta is None else max_id_venta + 1
        cursor.close()
        return nuevo_id_venta

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

    def fetch_all_sales_history(self):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT vp.id_venta, p.usuario, pr.nombre_producto, vp.cant_prod, pr.precio_unit, "
            "vp.cant_prod * pr.precio_unit as monto, t.nombre_tipo as tipo_pago "
            "FROM VentaXProd vp "
            "JOIN venta v ON vp.id_venta=v.id_venta "
            "JOIN producto pr ON pr.id_producto=vp.id_producto "
            "JOIN persona p ON p.id_persona=v.id_persona "
            "JOIN detalle_pago d ON v.id_detalle_pago = d.id_detalle_pago "
            "JOIN tipos_pago t ON t.id_tipo_pago = d.id_tipo_pago "
            "ORDER BY vp.id_venta"
        )
        sales_history = cursor.fetchall()
        cursor.close()
        return sales_history

    def fetch_product_details(self, producto_id):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT p.nombre_producto, p.descripcion_prod, p.precio_unit, p.cant_max, t.nombre as tipo_producto, c.nombre as categoria_prod "
            "FROM PRODUCTO p "
            "JOIN CATEGORIA_PROD c ON c.ID_CATEGORIA_PROD = p.ID_CATEGORIA_PROD "
            "JOIN TIPO_PROD t ON c.ID_tipo_prod = t.id_tipo_prod "
            "WHERE p.id_producto = %s", (producto_id,)
        )
        product_details = cursor.fetchone()
        cursor.close()
        return product_details
    

    def fetch_tipo_pago_id(self, tipo_pago):
        try:
            self.cursor.execute("SELECT id_tipo_pago FROM tipos_pago WHERE nombre_tipo = %s", (tipo_pago,))
            id_tipo_pago = self.cursor.fetchone()[0]
            return id_tipo_pago
        except psycopg2.Error as e:
            messagebox.showerror("Error", f"No se pudo obtener el ID del tipo de pago: {e}")
            return None

    def insert_detalle_pago(self, id_tipo_pago, nro_tarjeta):
        # Insertar detalle de pago
        try:
            self.cur.execute("INSERT INTO detalle_pago (ID_TIPO_PAGO, nro_tarjeta) VALUES (%s, %s) RETURNING ID_DETALLE_PAGO", (id_tipo_pago, nro_tarjeta))
            id_detalle_pago = self.cur.fetchone()[0]
            self.conn.commit()
            return id_detalle_pago
        except psycopg2.Error as e:
            messagebox.showerror("Error", f"No se pudo insertar el detalle de pago: {e}")
            return None

    def insert_venta(self, monto_final, id_detalle_pago, id_persona, nro_tarjeta):
        # Insertar venta
        try:
            self.cur.execute("INSERT INTO venta (monto_final, id_detalle_pago, id_persona, nro_tarjeta) VALUES (%s, %s, %s, %s) RETURNING ID_VENTA", (monto_final, id_detalle_pago, id_persona, nro_tarjeta))
            id_venta = self.cur.fetchone()[0]
            self.conn.commit()
            return id_venta
        except psycopg2.Error as e:
            messagebox.showerror("Error", f"No se pudo insertar la venta: {e}")
            return None

    def get_monto_final_carrito(self, id_persona):

        try:
            self.cur.execute("""
                SELECT SUM(p.precio_unit * v.cant_prod) AS monto_final
                FROM producto p
                JOIN ventaxprod v ON p.id_producto = v.id_producto
                JOIN venta ve ON ve.id_venta = v.id_venta
                JOIN persona pe ON pe.id_persona = ve.id_persona
                WHERE ve.id_persona = %s
                GROUP BY ve.id_venta
            """, (id_persona,))
            monto_final = self.cur.fetchone()[0]
            return monto_final
        except psycopg2.Error as e:
            messagebox.showerror("Error", f"No se pudo obtener el monto final del carrito: {e}")
            return None

    def close(self):
        self.conn.close()

def abrir_ventana_catalogo(dao, usuario_actual):
    ventana_catalogo = tk.Tk()
    ventana_catalogo.title("Catálogo de Productos")
    ventana_catalogo.geometry("800x600")
    ventana_catalogo.configure(bg="#FADBD8")

    frame_catalogo = tk.Frame(ventana_catalogo, bg="#FADBD8")
    frame_catalogo.pack(fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(frame_catalogo, bg="#FADBD8")
    scrollbar = tk.Scrollbar(frame_catalogo, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#FADBD8")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

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
        ventana_carro.geometry("800x600")
        ventana_carro.configure(bg="#FADBD8")

        tk.Label(ventana_carro, text="Carro de Compras", font=("Arial", 24), bg="#FADBD8").pack(pady=10)

        total_price = 0

        for producto_id, detalles in carrito.items():
            producto_frame = tk.Frame(ventana_carro, padx=20, pady=10, bg="#FADBD8")
            producto_frame.pack(fill='x', padx=10, pady=5)

            tk.Label(producto_frame, text=f"{detalles['nombre']}", font=("Arial", 14), bg="#FADBD8").pack(side=tk.LEFT)
            tk.Label(producto_frame, text=f"Cantidad: {detalles['cantidad']}", font=("Arial", 14), bg="#FADBD8").pack(side=tk.LEFT, padx=20)
            subtotal = detalles['precio'] * detalles['cantidad']
            tk.Label(producto_frame, text=f"Subtotal: ${subtotal}", font=("Arial", 14), bg="#FADBD8").pack(side=tk.LEFT, padx=20)

            total_price += subtotal

        tk.Label(ventana_carro, text=f"Monto Total de la Compra: ${total_price}", font=("Arial", 16), bg="#FADBD8").pack(pady=10)

        def mostrar_entry_numero_tarjeta(*args):
            
            payment_methods = dao.fetch_payment_methods()
            metodo_pago_var = tk.StringVar(ventana_carro)
            metodo_pago_var.set(payment_methods[0][1])

            opciones_pago = ttk.Combobox(ventana_carro, textvariable=metodo_pago_var, values=[metodo[1] for metodo in payment_methods], state="readonly", font=("Arial", 14))
            opciones_pago.pack(pady=10)

            label_numero_tarjeta = tk.Label(ventana_carro, text="Número de Tarjeta:", font=("Arial", 14), bg="#FADBD8")
            entry_numero_tarjeta = tk.Entry(ventana_carro, font=("Arial", 14))

            if metodo_pago_var.get() in ["Tarjeta de crédito", "Tarjeta de débito", "A contra entrega"]:
                label_numero_tarjeta.pack(pady=5)
                entry_numero_tarjeta.pack(pady=5)
            else:
                label_numero_tarjeta.pack_forget()
                entry_numero_tarjeta.pack_forget()

        metodo_pago_var.trace("w", mostrar_entry_numero_tarjeta)

        tk.Button(ventana_carro, text="Confirmar Método de Pago", font=("Arial", 14), command=lambda: messagebox.showinfo("Método de Pago", f"Método seleccionado: {metodo_pago_var.get()}"), bg="#F5B7B1").pack(pady=20)

        tk.Button(ventana_carro, text="Confirmar Compra", font=("Arial", 14), command=lambda: messagebox.showinfo("Compra Confirmada", "¡Compra realizada con éxito!"), bg="#F5B7B1").pack(pady=20)

        tk.Button(ventana_carro, text="Regresar al Catálogo", font=("Arial", 14), command=lambda: abrir_ventana_catalogo(dao, usuario_actual), bg="#F5B7B1").pack(pady=20)

        ventana_carro.mainloop()

    def mostrar_info_producto(producto_id):
        ventana_info = tk.Toplevel()
        ventana_info.title("Información del Producto")
        ventana_info.geometry("400x300")
        ventana_info.configure(bg="#FADBD8")

        detalles = dao.fetch_product_details(producto_id)

        if detalles:
            nombre_producto, descripcion, precio_unit, cantidad_en_stock, tipo_producto, categoria_prod = detalles
            tk.Label(ventana_info, text=f"Nombre: {nombre_producto}", font=("Arial", 14), bg="#FADBD8").pack(pady=5)
            tk.Label(ventana_info, text=f"Descripción: {descripcion}", font=("Arial", 14), bg="#FADBD8").pack(pady=5)
            tk.Label(ventana_info, text=f"Precio: ${precio_unit}", font=("Arial", 14), bg="#FADBD8").pack(pady=5)
            tk.Label(ventana_info, text=f"Cantidad en stock: {cantidad_en_stock}", font=("Arial", 14), bg="#FADBD8").pack(pady=5)
            tk.Label(ventana_info, text=f"Tipo de producto: {tipo_producto}", font=("Arial", 14), bg="#FADBD8").pack(pady=5)
            tk.Label(ventana_info, text=f"Categoría: {categoria_prod}", font=("Arial", 14), bg="#FADBD8").pack(pady=5)
        else:
            tk.Label(ventana_info, text="No se encontró información del producto.", font=("Arial", 14), bg="#FADBD8").pack(pady=5)

    for producto in productos:
        producto_id, nombre_producto, precio_unit = producto
        producto_frame = tk.Frame(scrollable_frame, padx=20, pady=10, bg="#FADBD8")
        producto_frame.pack(fill='x', padx=10, pady=5)

        tk.Label(producto_frame, text=f"{nombre_producto}", font=("Arial", 14), bg="#FADBD8").pack(side=tk.LEFT)
        tk.Label(producto_frame, text=f"Precio: ${precio_unit}", font=("Arial", 14), bg="#FADBD8").pack(side=tk.LEFT, padx=20)

        boton_agregar = tk.Button(producto_frame, text="Agregar al Carrito", font=("Arial", 12), command=lambda p_id=producto_id, p_nombre=nombre_producto, p_precio=precio_unit: agregar_al_carro(p_id, p_nombre, p_precio), bg="#F5B7B1")
        boton_agregar.pack(side=tk.RIGHT, padx=10)
        boton_mas_info = tk.Button(producto_frame, text="Más info", font=("Arial", 12), command=lambda p_id=producto_id: mostrar_info_producto(p_id), bg="white")
        boton_mas_info.pack(side=tk.RIGHT, padx=40)
    frame_botones = tk.Frame(ventana_catalogo, bg="#FADBD8")
    frame_botones.pack(pady=20)

    tk.Button(frame_botones, text="Ir al Carrito", font=("Arial", 14), command=lambda: abrir_ventana_carro(ventana_catalogo), bg="#F5B7B1").pack(side=tk.LEFT, padx=10)
    tk.Button(frame_botones, text="Ver mi historial", font=("Arial", 14), command=lambda: messagebox.showinfo("Historial", "Función aún no implementada"), bg="#F5B7B1").pack(side=tk.LEFT, padx=10)
    tk.Button(frame_botones, text="Historial de Ventas", font=("Arial", 14), command=lambda: messagebox.showinfo("Historial de Ventas", "Función aún no implementada"), bg="#F5B7B1").pack(side=tk.LEFT, padx=10)

    ventana_catalogo.mainloop()

    def confirmar_metodo_pago(dao, metodo_pago_var, usuario_actual, nro_tarjeta_entry):
        metodo_pago_seleccionado = metodo_pago_var.get()
        if metodo_pago_seleccionado:
            # Obtener el ID_TIPO_PAGO correspondiente al tipo seleccionado
            id_tipo_pago = dao.fetch_tipo_pago_id(metodo_pago_seleccionado)

            if id_tipo_pago:
                # Obtener el monto final del carrito del usuario actual
                monto_final = dao.get_monto_final_carrito(usuario_actual)

                if monto_final is not None:
                    # Insertar en la tabla detalle_pago
                    id_detalle_pago = dao.insert_detalle_pago(id_tipo_pago, nro_tarjeta_entry.get())

                    if id_detalle_pago:
                        # Mostrar mensaje de éxito
                        messagebox.showinfo("Método de Pago Registrado", f"Se ha registrado el método de pago '{metodo_pago_seleccionado}' correctamente.")
                        
                        # Aquí se insertaría en la tabla ventas
                        id_venta = dao.insert_venta(monto_final, id_detalle_pago, usuario_actual, nro_tarjeta_entry.get())

                        if id_venta:
                            messagebox.showinfo("Venta Registrada", f"Se ha registrado la venta correctamente con ID {id_venta}.")
                        else:
                            messagebox.showerror("Error", "No se pudo registrar la venta.")
                    else:
                        messagebox.showerror("Error", "No se pudo registrar el detalle de pago.")
                else:
                    messagebox.showerror("Error", "No se pudo obtener el monto final del carrito.")
            else:
                messagebox.showerror("Error", "No se encontró el ID del tipo de pago seleccionado.")
        else:
            messagebox.showwarning("Selección de Método de Pago", "Por favor, seleccione un método de pago.")
        
    ventana_carro = tk.Toplevel()
    ventana_carro.title("Carrito de Compras")
    ventana_carro.geometry("600x400")
    ventana_carro.configure(bg="#FADBD8")

    # Interfaz gráfica para confirmar el método de pago
    tk.Label(ventana_carro, text="Seleccione Método de Pago:", font=("Arial", 14), bg="#FADBD8").pack(pady=10)

    metodo_pago_var = tk.StringVar()
    metodo_pago_var.set("")  # Valor inicial

    tipos_pago = ["Tarjeta de crédito", "Tarjeta de débito", "Efectivo", "A contra entrega", "Yape/Plin"]
    for tipo in tipos_pago:
        tk.Radiobutton(ventana_carro, text=tipo, variable=metodo_pago_var, value=tipo, font=("Arial", 12), bg="#FADBD8").pack()

    nro_tarjeta_label = tk.Label(ventana_carro, text="Número de Tarjeta:", font=("Arial", 14), bg="#FADBD8")
    nro_tarjeta_label.pack(pady=5)
    nro_tarjeta_entry = tk.Entry(ventana_carro, font=("Arial", 12))
    nro_tarjeta_entry.pack()

    boton_confirmar_compra = tk.Button(ventana_carro, text="Confirmar Compra", font=("Arial", 14), command=lambda: messagebox.showinfo("Compra Confirmada", "¡Compra realizada con éxito!"), bg="#F5B7B1")
    boton_confirmar_compra.pack(pady=20)

    boton_regresar_catalogo = tk.Button(ventana_carro, text="Regresar al Catálogo", font=("Arial", 14), command=lambda: abrir_ventana_catalogo(dao, usuario_actual), bg="#F5B7B1")
    boton_regresar_catalogo.pack(pady=20)

    ventana_carro.mainloop()

def main():
    usuario_actual = "usuario_prueba"
    dao = DatabaseDAO()
    abrir_ventana_catalogo(dao, usuario_actual)
    dao.close()
    
if __name__ == "__main__":
    main()

