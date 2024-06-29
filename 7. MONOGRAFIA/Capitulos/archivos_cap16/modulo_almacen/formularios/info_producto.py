from tkinter import Frame,Label,Entry,Text,TOP,RIGHT,LEFT,BOTH,END,BOTTOM,Button,X,W,E
from tkinter import ttk
from config import color_cuerpo_principal,color_marco_izquierdo,color_marco_derecho,borde_marco
import util.util_mensaje as util_mensaje
import BD.conexion_bd as bd

class InfoProducto():
    def __init__(self,panel_principal):
        self.marco_superior = Frame(panel_principal,bg=color_cuerpo_principal,height=50)
        self.marco_superior.pack(side=TOP,padx=5,pady=5,fill=X,expand=False)

        self.marco_inferior = Frame(panel_principal,bg=color_marco_izquierdo)
        self.marco_inferior.pack(side=BOTTOM,padx=3,pady=3,fill=BOTH,expand=True)

        self.InAlmacen = Label(self.marco_superior,text="Almacén",height=5)
        self.InAlmacen.config(fg="#222d33",font=("Roboto",10),bg=color_cuerpo_principal)
        self.InAlmacen.grid(row=0,column=1)

        conn,cursor = bd.conectar()

        query = '''
            SELECT nombre_tipo_producto
            FROM Tipo_Producto
        '''
        cursor.execute(query)
        rows = cursor.fetchall()
        id_almacen = [almacen[0] for almacen in rows]

        self.entry_InAlmacen = ttk.Combobox(self.marco_superior,values=id_almacen,height=5,width=10)
        self.entry_InAlmacen.grid(row=0,column=2)
        self.entry_InAlmacen.bind("<<ComboboxSelected>>",self.actualizar_categorias)

        self.InCategoria = Label(self.marco_superior,text="Categoría",height=5)
        self.InCategoria.config(fg="#222d33",font=("Roboto",10),bg=color_cuerpo_principal)
        self.InCategoria.grid(row=0,column=3)

        self.entry_InCategoria = ttk.Combobox(self.marco_superior,height=5,width=10)
        self.entry_InCategoria.grid(row=0,column=4)

        self.InMarca = Label(self.marco_superior,text="Marca",height=5)
        self.InMarca.config(fg="#222d33",font=("Roboto",10),bg=color_cuerpo_principal)
        self.InMarca.grid(row=0,column=5)

        self.entry_InMarca = ttk.Combobox(self.marco_superior,height=5,width=15)
        self.entry_InMarca.grid(row=0,column=6)

        self.InPresenta = Label(self.marco_superior,text="Presentación",height=5)
        self.InPresenta.config(fg="#222d33",font=("Roboto",10),bg=color_cuerpo_principal)
        self.InPresenta.grid(row=0,column=7)
        
        self.entry_InPresentacion = ttk.Combobox(self.marco_superior,height=5,width=20)
        self.entry_InPresentacion.grid(row=0,column=8)
        
        self.InColor = Label(self.marco_superior,text="Color",height=5)
        self.InColor.config(fg="#222d33",font=("Roboto",10),bg=color_cuerpo_principal)
        self.InColor.grid(row=0,column=9)

        query2 = '''
            SELECT nombre_color FROM Colores
        '''
        cursor.execute(query2)
        rows = cursor.fetchall()
        id_colores = [color[0] for color in rows]

        self.entry_InColor = ttk.Combobox(self.marco_superior,values=id_colores,height=5,width=10)
        self.entry_InColor.grid(row=0,column=10)

        cursor.close()
        conn.commit()
        conn.close()

        self.InNombre = Label(self.marco_inferior,text="Nombre Producto",height=5)
        self.InNombre.config(fg="#222d33",font=("Roboto",12),bg=color_marco_izquierdo)
        self.InNombre.grid(row=1,column=1)

        self.entry_InNombre = Text(self.marco_inferior,width=20,height=1)
        self.entry_InNombre.grid(row=1,column=2)
        
        self.InEspecif = Label(self.marco_inferior,text="Especificaciones",height=5)
        self.InEspecif.config(fg="#222d33",font=("Roboto",12),bg=color_marco_izquierdo)
        self.InEspecif.grid(row=2,column=1)

        self.entry_InEspecif = Text(self.marco_inferior,height=6,width=25)
        self.entry_InEspecif.grid(row=2,column=2)

        self.InObserv = Label(self.marco_inferior,text="Observaciones",height=5)
        self.InObserv.config(fg="#222d33",font=("Roboto",12),bg=color_marco_izquierdo)
        self.InObserv.grid(row=4,column=1)

        self.entry_InObserv = Text(self.marco_inferior,height=6,width=25)
        self.entry_InObserv.grid(row=4,column=2)

        self.InPrecio = Label(self.marco_inferior,text="Precio Unitario S/",height=5)
        self.InPrecio.config(fg="#222d33",font=("Roboto",10),bg=color_marco_izquierdo)
        self.InPrecio.grid(row=1,column=3)

        self.entry_InPrecio = Text(self.marco_inferior,width=6,height=1)
        self.entry_InPrecio.grid(row=1,column=4)

        self.InPeso= Label(self.marco_inferior,text="Peso Unitario (g)",height=5)
        self.InPeso.config(fg="#222d33",font=("Roboto",10),bg=color_marco_izquierdo)
        self.InPeso.grid(row=1,column=5)

        self.entry_InPeso = Text(self.marco_inferior,height=1,width=6)
        self.entry_InPeso.grid(row=1,column=6)

        self.InAncho= Label(self.marco_inferior,text="Ancho (cm)",height=5)
        self.InAncho.config(fg="#222d33",font=("Roboto",10),bg=color_marco_izquierdo)
        self.InAncho.grid(row=3,column=3)

        self.entry_InAncho = Text(self.marco_inferior,height=1,width=4)
        self.entry_InAncho.grid(row=3,column=4)

        self.InLargo= Label(self.marco_inferior,text="Largo (cm)",height=5)
        self.InLargo.config(fg="#222d33",font=("Roboto",10),bg=color_marco_izquierdo)
        self.InLargo.grid(row=3,column=5)

        self.entry_InLargo = Text(self.marco_inferior,height=1,width=4)
        self.entry_InLargo.grid(row=3,column=6)

        self.InAlto= Label(self.marco_inferior,text="Alto (cm)",height=5)
        self.InAlto.config(fg="#222d33",font=("Roboto",10),bg=color_marco_izquierdo)
        self.InAlto.grid(row=3,column=7)

        self.entry_InAlto = Text(self.marco_inferior,height=1,width=4)
        self.entry_InAlto.grid(row=3,column=8)

        self.ingresar_button = Button(self.marco_inferior,text="Registrar",command=self.registro)
        self.ingresar_button.grid(row=4,column=5,sticky=W+E)

    def registro(self):
        primeras_tres_letras = self.entry_InCategoria.get()[:3].upper() + '0'
        conn,cursor = bd.conectar()

        query_count = '''
                SELECT COUNT(*)
                FROM Producto
                WHERE nombre_categoria = %s
        '''
        cursor.execute(query_count,(self.entry_InCategoria.get(),))
        numero_x = cursor.fetchone()[0]
        numero_x2 = numero_x+1

        global id_producto_final
        id_producto_final = primeras_tres_letras + str(numero_x2)

        query_present = '''
                SELECT id_presentacion
                FROM Presentacion
                WHERE tipo_presentacion = %s
            '''
        cursor.execute(query_present,(self.entry_InPresentacion.get(),))
        id_presentacion = cursor.fetchone()[0]

        query_color = '''
                SELECT id_color
                FROM Colores
                WHERE nombre_color = %s
            '''
        cursor.execute(query_color,(self.entry_InColor.get(),))
        id_color = cursor.fetchone()[0]

        query_insert = '''
                INSERT INTO Producto
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,CURRENT_DATE,CURRENT_DATE,6,4,%s)
            '''
        cursor.execute(query_insert, (id_producto_final, id_presentacion, id_color,
        self.entry_InNombre.get("1.0", END).strip(),
        self.entry_InMarca.get(), self.entry_InEspecif.get("1.0", END).strip(),
        self.entry_InObserv.get("1.0", END).strip(),
        self.entry_InPrecio.get("1.0", END).strip(),
        self.entry_InPeso.get("1.0", END).strip(),
        self.entry_InAncho.get("1.0", END).strip(),
        self.entry_InLargo.get("1.0", END).strip(),
        self.entry_InAlto.get("1.0", END).strip(),
        self.entry_InCategoria.get()))

        util_mensaje.ProdIn()

        cursor.close()
        conn.commit()
        conn.close()

        self.InCant= Label(self.marco_inferior,text="Cantidad",height=5)
        self.InCant.config(fg="#222d33",font=("Roboto",10),bg=color_marco_izquierdo)
        self.InCant.grid(row=4,column=6)

        self.entry_InCant = Text(self.marco_inferior,height=1,width=4)
        self.entry_InCant.grid(row=4,column=7)

        self.ubicacion_button = Button(self.marco_inferior,text="Ver Ubicación",command=self.ubicar)
        self.ubicacion_button.grid(row=4,column=8,sticky=W+E)



    def ubicar(self):
        volumen = self.entry_InCant.get("1.0", END).strip()*self.entry_InAncho.get("1.0", END).strip()*self.entry_InLargo.get("1.0", END).strip()*self.entry_InAlto.get("1.0", END).strip()
        conn,cursor = bd.conectar()
        query_ubi = '''
            SELECT U.seccion,U.id_stand,U.id_repisas
                (I.entradas - I.salidas) AS stock,
                P.largo_present,
                P.ancho_present,
                P.alto_present,
                ((I.entradas - I.salidas) * P.largo_present * P.ancho_present * P.alto_present) AS volumen_disponible
            FROM Inventario I
            JOIN Ubicacion U ON I.seccion = U.seccion AND I.id_stand = U.id_stand AND I.id_repisas = U.id_repisas
            JOIN Producto P ON I.id_producto = P.id_producto
            WHERE ((I.entradas - I.salidas) * P.largo_present * P.ancho_present * P.alto_present) >= @volumen_dado
            ORDER BY volumen_disponible DESC
            LIMIT 1
        '''
        cursor.execute(query_ubi,(volumen,))
        row = cursor.fetchone()

        query_count = '''
                SELECT COUNT(*)
                FROM Inventario
                WHERE entradas > 0
        '''
        cursor.execute(query_count)
        id_count = cursor.fetchone()

        query_insert = '''
                INSERT INTO Inventario
                VALUES (%s,%s,%s,0,%s,%s,%s,CURRENT_DATE)
        '''
        cursor.execute(query_insert,(id_count,id_producto_final,self.entry_InCant.get(),
        row[0],row[1],row[2]))

        cursor.close()
        conn.commit()
        conn.close()

    def actualizar_categorias(self,event):
        tipo_producto_seleccionado = self.entry_InAlmacen.get()
        conn,cursor = bd.conectar()

        query = '''
            SELECT 
                CP.nombre_categoria
            FROM 
                Categoria_Producto CP
            JOIN 
                Tipo_Producto TP ON CP.id_tipo_producto = TP.id_tipo_producto
            WHERE 
                TP.nombre_tipo_producto = %s
        '''
        cursor.execute(query,(tipo_producto_seleccionado,))
        rows = cursor.fetchall()
        categorias = [categoria[0] for categoria in rows]

        self.entry_InCategoria['values'] = categorias

        if tipo_producto_seleccionado == 'Maquillaje':
            query2 = '''
                SELECT M.id_marca
                FROM Marca M
                WHERE 
                M.rubro NOT LIKE '%Artículos%'    
            '''
            cursor.execute(query2)
            rows = cursor.fetchall()
            marcas = [marca[0] for marca in rows]

            query3 = '''
                SELECT tipo_presentacion
                FROM Presentacion
                WHERE 
                (id_presentacion >=1 AND id_presentacion <=16)
            '''
            cursor.execute(query3)
            rows = cursor.fetchall()
            presentas = [presenta[0] for presenta in rows]

        elif tipo_producto_seleccionado == 'Papelería':
            query2 = '''
                SELECT M.id_marca
                FROM Marca M
                WHERE 
                M.rubro LIKE '%Artículos%'       
            '''
            cursor.execute(query2)
            rows = cursor.fetchall()
            marcas = [marca[0] for marca in rows] 

            query3 = '''
                SELECT tipo_presentacion
                FROM Presentacion
                WHERE 
                (id_presentacion >=16 AND id_presentacion <=25)
            '''
            cursor.execute(query3)
            rows = cursor.fetchall()
            presentas = [presenta[0] for presenta in rows]     

        self.entry_InMarca['values'] = marcas
        self.entry_InPresentacion['values'] = presentas

        cursor.close()
        conn.commit()
        conn.close()

        
