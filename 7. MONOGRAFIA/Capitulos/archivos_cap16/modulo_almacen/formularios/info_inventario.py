from tkinter import Frame,Label,TOP,RIGHT,LEFT,BOTH,END,Entry,Button,X,W,E
from tkinter import ttk
from config import color_cuerpo_principal,color_marco_izquierdo,color_marco_derecho,borde_marco
import util.util_mensaje as util_mensaje
import util.util_imagen as util_img
import BD.conexion_bd as bd
import os

class InfoInventario():

    def __init__(self,panel_principal):
        self.marco_superior = Frame(panel_principal,bg=color_cuerpo_principal,height=80)
        self.marco_superior.pack(side=TOP,padx=5,pady=5,fill=X,expand=False)

        self.marco_izquierdo = Frame(panel_principal,bg=color_marco_izquierdo)
        self.marco_izquierdo.pack(side=LEFT,padx=3,pady=3,fill=BOTH,expand=True)

        self.marco_derecha = Frame(panel_principal,width=250,bg=color_marco_derecho)
        self.marco_derecha.pack(side=RIGHT,fill=BOTH,expand=False)

        self.InProd = Label(self.marco_superior,text="Filtrar por:")
        self.InProd.config(fg="#222d33",font=("Roboto",15),bg=color_cuerpo_principal)
        self.InProd.grid(row=0,column=1)

        self.InProd = Label(self.marco_superior,text="Ingresar Código Producto")
        self.InProd.config(fg="#222d33",font=("Roboto",10),bg=color_cuerpo_principal)
        self.InProd.grid(row=1,column=2)

        self.entry_InProd = Entry(self.marco_superior)
        self.entry_InProd.grid(row=1,column=3)

        self.InMarca = Label(self.marco_superior,text="Ingresar Marca Producto")
        self.InMarca.config(fg="#222d33",font=("Roboto",10),bg=color_cuerpo_principal)
        self.InMarca.grid(row=1,column=4)

        conn,cursor = bd.conectar()

        query = '''
            SELECT id_marca FROM Marca
        '''
        cursor.execute(query)
        rows = cursor.fetchall()
        id_marcas = [marca[0] for marca in rows]

        self.entry_InMarca = ttk.Combobox(self.marco_superior,values=id_marcas,width=15)
        self.entry_InMarca.grid(row=1,column=5)

        self.InStock = Label(self.marco_superior,text="Ingresar Stock Mínimo")
        self.InStock.config(fg="#222d33",font=("Roboto",10),bg=color_cuerpo_principal)
        self.InStock.grid(row=1,column=7)

        self.entry_InStock = Entry(self.marco_superior,width=4)
        self.entry_InStock.grid(row=1,column=8)

        self.InCateg = Label(self.marco_superior,text="Ingresar Categoría")
        self.InCateg.config(fg="#222d33",font=("Roboto",10),bg=color_cuerpo_principal)
        self.InCateg.grid(row=2,column=1)

        query4 = '''
            SELECT nombre_categoria FROM Categoria_Producto
        '''
        cursor.execute(query4)
        rows = cursor.fetchall()
        id_categorias = [categoria[0] for categoria in rows]

        self.entry_InCategoria = ttk.Combobox(self.marco_superior,values=id_categorias,width=15)
        self.entry_InCategoria.grid(row=2,column=2)

        self.buscar_button = Button(self.marco_superior,text="Buscar",command=self.ver_filtro)
        self.buscar_button.grid(row=1,column=1,sticky=W+E)

        self.todo_button = Button(self.marco_superior,text="TODO",command=self.ver_filtro3)
        self.todo_button.grid(row=0,column=2,sticky=W+E)

        self.almacen1_button = Button(self.marco_superior,text="Maquillaje",command=self.ver_filtro1)
        self.almacen1_button.grid(row=0,column=3,sticky=W+E)

        self.almacen2_button = Button(self.marco_superior,text="Papelería",command=self.ver_filtro2)
        self.almacen2_button.grid(row=0,column=4,sticky=W+E)

        self.sinstock_button = Button(self.marco_superior,text="Sin Stock",command=self.ver_filtro4)
        self.sinstock_button.grid(row=0,column=5,sticky=W+E)

        query2 = '''
          SELECT
            i.id_producto,
            p.nombre_producto,
            pr.tipo_presentacion,
            c.nombre_color,
            (i.entradas - i.salidas) AS stock,
            CONCAT(i.seccion, '-', i.id_stand, '-', i.id_repisas) AS ubicacion
            FROM Inventario i
            JOIN Producto p ON i.id_producto = p.id_producto
            JOIN Presentacion pr ON p.id_presentacion = pr.id_presentacion
            JOIN Colores c ON p.id_color = c.id_color
        '''
        cursor.execute(query2)
        self.tabla_frame(cursor.fetchall())

        query3 = '''
            SELECT 
                p.id_producto,
                i.path_imagen,
                (p.precio_unitario*(inv.entradas - inv.salidas)) AS importe,
                CONCAT(p.ancho_present*p.largo_present*p.alto_present,' cm³') AS volumen
            FROM 
                Producto p
            JOIN 
                Imagenes i ON p.id_producto = i.id_producto
            JOIN 
                Inventario inv ON p.id_producto = inv.id_producto
        '''
        cursor.execute(query3)
        img = cursor.fetchall()
        self.id_img_prod = {str(imagen[0]):
            {'path_imagen': imagen[1],'Importe': imagen[2],'Volumen': imagen[3]} for imagen in img}

        cursor.close()
        conn.commit()
        conn.close()
    
    def tabla_frame(self,filas):
        style = ttk.Style()
        style.configure("Custom.Treeview",background="#c9c9c9",
        fieldbackground="#c9c9c9",foreground="black")
        style.configure("Custom.Treeview.Heading",background="lightblue",font=("Helvetica",10,"bold"))

        self.marco = Frame(self.marco_izquierdo,bg=borde_marco)
        self.marco.config(borderwidth=2,width=100,height=50)
        self.marco.pack(fill=BOTH,expand=True)

        self.tabla = ttk.Treeview(self.marco,columns=("col1","col2","col3","col4","col5","col6"),
        show='headings',style="Custom.Treeview")

        self.tabla.heading("col1",text="ID Producto")
        self.tabla.heading("col2",text="Nombre")
        self.tabla.heading("col3",text="Presentación")
        self.tabla.heading("col4",text="Color")
        self.tabla.heading("col5",text="Stock")
        self.tabla.heading("col6",text="Ubicación")

        self.tabla.column("col1",width=5)
        self.tabla.column("col2",width=30)
        self.tabla.column("col3",width=15)
        self.tabla.column("col4",width=15)
        self.tabla.column("col5",width=5)
        self.tabla.column("col6",width=7)

        self.tabla.pack(expand=True,fill=BOTH)

        for x in filas:
            self.tabla.insert("",END,values=x)
        
        self.tabla.bind("<ButtonRelease-1>",self.mostrar_imagen)
       
    def limpiar_panel(self,panel):
        for widget in panel.winfo_children():
            widget.destroy()

    def ver_filtro(self):
        valor_producto = self.entry_InProd.get().strip()
        valor_marca = self.entry_InMarca.get().strip()
        valor_stock = self.entry_InStock.get().strip()
        valor_categoria = self.entry_InCategoria.get().strip()

        conn,cursor = bd.conectar()
        cursor.execute('SELECT id_producto FROM Inventario')
        check_prod = [str(id_prod[0]) for id_prod in cursor.fetchall()]
        
        if not valor_producto and not valor_marca and not valor_stock and not valor_categoria:
            util_mensaje.ProdNotInfo()
            return
        else:
            if valor_producto:
                query = '''
                    SELECT
                        p.id_producto,
                        p.nombre_producto,
                        pr.tipo_presentacion,
                        c.nombre_color,
                        (i.entradas - i.salidas) AS stock,
                        CONCAT(i.seccion, '-', i.id_stand, '-', i.id_repisas) AS ubicacion
                    FROM
                        Inventario i
                        JOIN Producto p ON i.id_producto = p.id_producto
                        JOIN Presentacion pr ON p.id_presentacion = pr.id_presentacion
                        JOIN Colores c ON p.id_color = c.id_color
                    WHERE
                        p.id_producto LIKE %s
                    ORDER BY
                        p.id_producto           
                '''
                cursor.execute(query,('%'+valor_producto+'%',))
                rows = cursor.fetchall()
                self.limpiar_panel(self.marco_izquierdo)
                self.tabla_frame(rows)

                cursor.close()
                conn.commit()
                conn.close()
            elif valor_marca:
                query = '''
                    SELECT
                        p.id_producto,
                        p.nombre_producto,
                        pr.tipo_presentacion,
                        c.nombre_color,
                        (i.entradas - i.salidas) AS stock,
                        CONCAT(i.seccion, '-', i.id_stand, '-', i.id_repisas) AS ubicacion
                    FROM
                        Inventario i
                        JOIN Producto p ON i.id_producto = p.id_producto
                        JOIN Presentacion pr ON p.id_presentacion = pr.id_presentacion
                        JOIN Colores c ON p.id_color = c.id_color
                        JOIN Marca m ON p.id_marca = m.id_marca
                    WHERE
                        m.id_marca = %s
                    ORDER BY
                        p.id_producto
                '''
                cursor.execute(query,(valor_marca,))
                rows = cursor.fetchall()
                self.limpiar_panel(self.marco_izquierdo)
                self.tabla_frame(rows)

                cursor.close()
                conn.commit()
                conn.close()
            elif valor_stock:
                query = '''
                    SELECT
                        p.id_producto,
                        p.nombre_producto,
                        pr.tipo_presentacion,
                        c.nombre_color,
                        (i.entradas - i.salidas) AS stock,
                        CONCAT(i.seccion, '-', i.id_stand, '-', i.id_repisas) AS ubicacion
                    FROM
                        Inventario i
                        JOIN Producto p ON i.id_producto = p.id_producto
                        JOIN Presentacion pr ON p.id_presentacion = pr.id_presentacion
                        JOIN Colores c ON p.id_color = c.id_color
                    WHERE
                        (i.entradas - i.salidas) >= %s
                    ORDER BY
                        p.id_producto
                '''
                cursor.execute(query,(valor_stock,))
                rows = cursor.fetchall()
                self.limpiar_panel(self.marco_izquierdo)
                self.tabla_frame(rows)

                cursor.close()
                conn.commit()
                conn.close()
            elif valor_categoria:
                query = '''
                    SELECT
                        p.id_producto,
                        p.nombre_producto,
                        pr.tipo_presentacion,
                        c.nombre_color,
                        (i.entradas - i.salidas) AS stock,
                        CONCAT(i.seccion, '-', i.id_stand, '-', i.id_repisas) AS ubicacion
                    FROM
                        Inventario i
                        JOIN Producto p ON i.id_producto = p.id_producto
                        JOIN Presentacion pr ON p.id_presentacion = pr.id_presentacion
                        JOIN Colores c ON p.id_color = c.id_color
                        JOIN Categoria_Producto cp ON p.nombre_categoria = cp.nombre_categoria
                    WHERE
                        cp.nombre_categoria = %s
                    ORDER BY
                        p.id_producto
                '''
                cursor.execute(query,(valor_categoria,))
                rows = cursor.fetchall()
                self.limpiar_panel(self.marco_izquierdo)
                self.tabla_frame(rows)

                cursor.close()
                conn.commit()
                conn.close()
            else:
                if valor_producto not in check_prod:
                    util_mensaje.ProdNotCheck()
                    return
        cursor.close()
        conn.commit()
        conn.close()
        
    def ver_filtro1(self):
        self.limpiar_panel(self.marco_izquierdo)
        conn,cursor = bd.conectar()
        query = '''
            SELECT
                i.id_producto,
                p.nombre_producto,
                pr.tipo_presentacion,
                c.nombre_color,
                (i.entradas - i.salidas) AS stock,
                CONCAT(i.seccion, '-', i.id_stand, '-', i.id_repisas) AS ubicacion
            FROM Inventario i
            JOIN Producto p ON i.id_producto = p.id_producto
            JOIN Presentacion pr ON p.id_presentacion = pr.id_presentacion
            JOIN Colores c ON p.id_color = c.id_color
            JOIN Categoria_Producto cp ON p.nombre_categoria = cp.nombre_categoria
            JOIN Tipo_Producto tp ON cp.id_tipo_producto = tp.id_tipo_producto
            WHERE tp.nombre_tipo_producto = 'Maquillaje';
        '''
        cursor.execute(query)
        self.tabla_frame(cursor.fetchall())

        cursor.close()
        conn.commit()
        conn.close()

    def ver_filtro2(self):
        self.limpiar_panel(self.marco_izquierdo)
        conn,cursor = bd.conectar()
        query = '''
            SELECT
                i.id_producto,
                p.nombre_producto,
                pr.tipo_presentacion,
                c.nombre_color,
                (i.entradas - i.salidas) AS stock,
                CONCAT(i.seccion, '-', i.id_stand, '-', i.id_repisas) AS ubicacion
            FROM Inventario i
            JOIN Producto p ON i.id_producto = p.id_producto
            JOIN Presentacion pr ON p.id_presentacion = pr.id_presentacion
            JOIN Colores c ON p.id_color = c.id_color
            JOIN Categoria_Producto cp ON p.nombre_categoria = cp.nombre_categoria
            JOIN Tipo_Producto tp ON cp.id_tipo_producto = tp.id_tipo_producto
            WHERE tp.nombre_tipo_producto = 'Papelería';
        '''
        cursor.execute(query)
        self.tabla_frame(cursor.fetchall())

        cursor.close()
        conn.commit()
        conn.close()

    def ver_filtro3(self):
        self.limpiar_panel(self.marco_izquierdo)
        conn,cursor = bd.conectar()
        query = '''
            SELECT
                i.id_producto,
                p.nombre_producto,
                pr.tipo_presentacion,
                c.nombre_color,
                (i.entradas - i.salidas) AS stock,
                CONCAT(i.seccion, '-', i.id_stand, '-', i.id_repisas) AS ubicacion
            FROM Inventario i
            JOIN Producto p ON i.id_producto = p.id_producto
            JOIN Presentacion pr ON p.id_presentacion = pr.id_presentacion
            JOIN Colores c ON p.id_color = c.id_color
        '''
        cursor.execute(query)
        self.tabla_frame(cursor.fetchall())

        cursor.close()
        conn.commit()
        conn.close()
    
    def ver_filtro4(self):
        self.limpiar_panel(self.marco_izquierdo)
        conn,cursor = bd.conectar()
        query = '''
          SELECT
                i.id_producto,
                p.nombre_producto,
                pr.tipo_presentacion,
                c.nombre_color,
                (i.entradas - i.salidas) AS stock,
                CONCAT(i.seccion, '-', i.id_stand, '-', i.id_repisas) AS ubicacion
            FROM
                Inventario i
            JOIN
                Producto p ON i.id_producto = p.id_producto
            JOIN
                Presentacion pr ON p.id_presentacion = pr.id_presentacion
            JOIN
                Colores c ON p.id_color = c.id_color
            WHERE
                (i.entradas - i.salidas) = 0
        '''
        cursor.execute(query)
        self.tabla_frame(cursor.fetchall())

        cursor.close()
        conn.commit()
        conn.close()

    def mostrar_imagen(self,event):
        item = self.tabla.selection()[0]
        id_producto = str(self.tabla.item(item,"values")[0])

        if id_producto in self.id_img_prod:
            path_imagen = self.id_img_prod[id_producto]['path_imagen']
            importe_inventario = self.id_img_prod[id_producto]['Importe']
            volumen_producto = self.id_img_prod[id_producto]['Volumen']
            if not os.path.isfile(path_imagen):
                 path_imagen = "./imagenes/Falta_Imagen.png"
        else:
            path_imagen = "./imagenes/Falta_Imagen.png"
        
        self.img_prod_derecha = util_img.leer_imagen(path_imagen,(280,280))

        self.label_imagen = Label(self.marco_derecha,image=self.img_prod_derecha)
        self.label_imagen.place(x=0,y=0,relwidth=1,relheight=1)
        self.label_imagen.config(bg=color_marco_derecho)

        self.Importe = Label(self.marco_derecha,text=f"Importe Inventario S/{importe_inventario}")
        self.Importe.place(x=0,y=380)
        self.Importe.config(fg="#333333",font=("Roboto",12,"bold"),bg=color_marco_derecho)

        self.Volumen = Label(self.marco_derecha,text=f"Volumen Producto {volumen_producto}")
        self.Volumen.place(x=0,y=400)
        self.Volumen.config(fg="#333333",font=("Roboto",8,"bold"),bg=color_marco_derecho)

        