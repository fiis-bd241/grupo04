from tkinter import Frame,Label,TOP,RIGHT,LEFT,BOTH,END,BOTTOM,Button,X,W,E
from tkinter import ttk
from config import color_cuerpo_principal,color_marco_izquierdo,color_marco_derecho,borde_marco
import util.util_mensaje as util_mensaje
import BD.conexion_bd as bd

class InfoPedidos():
    def __init__(self,panel_principal):
        self.marco_superior = Frame(panel_principal,bg=color_cuerpo_principal,height=80)
        self.marco_superior.pack(side=TOP,padx=5,pady=5,fill=X,expand=False)

        self.marco_izquierdo = Frame(panel_principal,bg=color_marco_izquierdo)
        self.marco_izquierdo.pack(side=LEFT,padx=3,pady=3,fill=BOTH,expand=True)

        self.marco_derecha = Frame(panel_principal,bg=color_marco_derecho)
        self.marco_derecha.pack(side=RIGHT,fill=BOTH,expand=True)

        self.buscar_button = Button(self.marco_superior,text="Buscar",command=self.ver_pedido)
        self.buscar_button.grid(row=0,column=1,sticky=W+E)

        self.actualizar_button = Button(self.marco_superior,text="Actualizar",command=self.actualizar_tabla)
        self.actualizar_button.grid(row=2,column=1,sticky=W+E)
      
        conn,cursor = bd.conectar()

        self.InEntrega = Label(self.marco_superior,text="Tipo Entrega")
        self.InEntrega.config(fg="#222d33",font=("Roboto",10),bg=color_cuerpo_principal)
        self.InEntrega.grid(row=0,column=2)

        query2 = '''
            SELECT nombre_tipo_entrega FROM Tipo_Entrega
        '''
        cursor.execute(query2)
        rows = cursor.fetchall()
        id_entrega = [entregas[0] for entregas in rows]

        self.entry_InEntrega = ttk.Combobox(self.marco_superior,values=id_entrega,width=10)
        self.entry_InEntrega.grid(row=0,column=3)

        self.InEstado = Label(self.marco_superior,text="Estado Pedido")
        self.InEstado.config(fg="#222d33",font=("Roboto",10),bg=color_cuerpo_principal)
        self.InEstado.grid(row=0,column=4)

        query3 = '''
            SELECT nombre_estado_pedido FROM Estado_Pedido
        '''
        cursor.execute(query3)
        rows = cursor.fetchall()
        id_estado = [estados[0] for estados in rows]

        self.entry_InEstado = ttk.Combobox(self.marco_superior,values=id_estado,width=10)
        self.entry_InEstado.grid(row=0,column=5)

        query = '''
            SELECT
                p.id_pedido,
                te.nombre_tipo_entrega,
                p.fecha_entrega,
                (p.fecha_entrega - CURRENT_DATE) AS dias_faltantes,
                p.cod_venta,
                CONCAT(pe.nombre, ' ', pe.primer_apellido) AS nombre_repartidor
            FROM
                Pedido p
            INNER JOIN
                Tipo_Entrega te ON p.id_tipo_entrega = te.id_tipo_entrega
            LEFT JOIN
                Persona pe ON p.id_repartidor = pe.id_persona
            WHERE
                p.id_estado_pedido = 'L'
        '''
        cursor.execute(query)
        self.tabla_frame(cursor.fetchall())

        cursor.close()
        conn.commit()
        conn.close()

    def tabla_frame(self,filas):
        style = ttk.Style()
        style.configure("Custom.Treeview",background="#c9c9c9",
        fieldbackground="#c9c9c9",foreground="black")
        style.configure("Custom.Treeview.Heading",background="lightblue",font=("Helvetica",10,"bold"))

        self.marco = Frame(self.marco_izquierdo,bg=borde_marco)
        self.marco.config(borderwidth=2,width=500,height=100)
        self.marco.pack(fill=X,pady=6,padx=6)

        self.tabla = ttk.Treeview(self.marco,columns=("col1","col2","col3","col4","col5","col6"),
        show='headings',style="Custom.Treeview")

        self.tabla.heading("col1",text="ID Pedido")
        self.tabla.heading("col2",text="Tipo Entrega")
        self.tabla.heading("col3",text="Fecha Entrega")
        self.tabla.heading("col4",text="Días Faltantes")
        self.tabla.heading("col5",text="Cod Venta")
        self.tabla.heading("col6",text="Repartidor") 

        self.tabla.column("col1",width=3)
        self.tabla.column("col2",width=10)
        self.tabla.column("col3",width=10)
        self.tabla.column("col4",width=5)
        self.tabla.column("col5",width=3)
        self.tabla.column("col6",width=15)

        self.tabla.pack(expand=True,fill=BOTH)

        for x in filas:
            self.tabla.insert("",END,values=x)
        
        self.tabla.bind("<ButtonRelease-1>",self.mostrar_productos)
    
    def tabla_info(self,filas):
        style = ttk.Style()
        style.configure("Custom.Treeview",background="#c9c9c9",
        fieldbackground="#c9c9c9",foreground="black")
        style.configure("Custom.Treeview.Heading",background="lightblue",font=("Helvetica",10,"bold"))

        self.marco = Frame(self.marco_derecha,bg=borde_marco)
        self.marco.config(borderwidth=2,width=500,height=100)
        self.marco.pack(fill=X,pady=6)

        self.tabla2 = ttk.Treeview(self.marco,columns=("col1","col2","col3","col4"),
        show='headings',style="Custom.Treeview")

        self.tabla2.heading("col1",text="ID Producto")
        self.tabla2.heading("col2",text="Nombre")
        self.tabla2.heading("col3",text="Cantidad")
        self.tabla2.heading("col4",text="Ubicación")

        self.tabla2.column("col1",width=70)
        self.tabla2.column("col2",width=70)
        self.tabla2.column("col3",width=70)
        self.tabla2.column("col4",width=70)

        self.tabla2.pack(expand=True,fill=BOTH)

        for x in filas:
            self.tabla2.insert("",END,values=x)

    def mostrar_productos(self,event):
        item = self.tabla.selection()[0]
        id_pedido = str(self.tabla.item(item,"values")[0])
        global pedidokx
        pedidokx = id_pedido
        
        conn,cursor = bd.conectar()
        query = '''
            SELECT 
                cxp.id_producto,
                p.nombre_producto,
                cxp.cantidad,
                CONCAT(inv.seccion, '-', inv.id_stand, '-', inv.id_repisas) AS ubicacion
            FROM 
                Pedido pd
            JOIN 
                Venta v ON pd.cod_venta = v.cod_venta AND pd.id_persona = v.id_persona
            JOIN 
                Cliente cl ON v.id_persona = cl.id_persona
            JOIN 
                ClientexProducto cxp ON cl.id_persona = cxp.id_persona
            JOIN 
                Producto p ON cxp.id_producto = p.id_producto
            LEFT JOIN
                Inventario inv ON p.id_producto = inv.id_producto
            WHERE 
                pd.id_pedido = %s
                AND pd.id_estado_pedido = 'L'
                AND v.id_estado_venta = 'C'   
        '''
        cursor.execute(query,(id_pedido,))
        self.limpiar_panel(self.marco_derecha)
        self.registrar_button = Button(self.marco_derecha,text="Registrar",command=self.registrar_prod)
        self.registrar_button.place(x=50,y=380,width=150,height=50)
        self.tabla_info(cursor.fetchall())

        cursor.close()
        conn.commit()
        conn.close()

    def limpiar_panel(self,panel):
        for widget in panel.winfo_children():
            widget.destroy()
    
    def actualizar_tabla(self):
        conn,cursor = bd.conectar()
        query = '''
            SELECT
                p.id_pedido,
                te.nombre_tipo_entrega,
                p.fecha_entrega,
                (p.fecha_entrega - CURRENT_DATE) AS dias_faltantes,
                p.cod_venta,
                CONCAT(pe.nombre, ' ', pe.primer_apellido) AS nombre_repartidor
            FROM
                Pedido p
            INNER JOIN
                Tipo_Entrega te ON p.id_tipo_entrega = te.id_tipo_entrega
            LEFT JOIN
                Persona pe ON p.id_repartidor = pe.id_persona
            WHERE
                p.id_estado_pedido = 'L'
        '''
        cursor.execute(query)
        self.limpiar_panel(self.marco_izquierdo)
        self.tabla_frame(cursor.fetchall())

        cursor.close()
        conn.commit()
        conn.close()
    
    def ver_pedido(self):
        valor_entrega = self.entry_InEntrega.get().strip()
        valor_estado = self.entry_InEstado.get().strip()

        conn,cursor = bd.conectar()
        
        if not valor_entrega and not valor_estado:
            util_mensaje.PedidoNotInfo()
            return
        else:
            if valor_entrega:
                query = '''
                    SELECT
                        p.id_pedido,
                        te.nombre_tipo_entrega,
                        p.fecha_entrega,
                        (p.fecha_entrega - CURRENT_DATE) AS dias_faltantes,
                        p.cod_venta,
                        CONCAT(pe.nombre, ' ', pe.primer_apellido) AS nombre_repartidor
                    FROM
                        Pedido p
                    INNER JOIN
                        Tipo_Entrega te ON p.id_tipo_entrega = te.id_tipo_entrega
                    LEFT JOIN
                        Persona pe ON p.id_repartidor = pe.id_persona
                    WHERE
                        te.nombre_tipo_entrega = %s           
                '''
                cursor.execute(query,(valor_entrega,))
                rows = cursor.fetchall()
                self.limpiar_panel(self.marco_izquierdo)
                self.tabla_frame(rows)

                cursor.close()
                conn.commit()
                conn.close()
            elif valor_estado:
                query = '''
                    SELECT
                        p.id_pedido,
                        te.nombre_tipo_entrega,
                        p.fecha_entrega,
                        (p.fecha_entrega - CURRENT_DATE) AS dias_faltantes,
                        p.cod_venta,
                        CONCAT(pe.nombre, ' ', pe.primer_apellido) AS nombre_repartidor
                    FROM
                        Pedido p
                    INNER JOIN
                        Tipo_Entrega te ON p.id_tipo_entrega = te.id_tipo_entrega
                    LEFT JOIN
                        Persona pe ON p.id_repartidor = pe.id_persona
                    INNER JOIN
                        Estado_Pedido ep ON p.id_estado_pedido = ep.id_estado_pedido
                    WHERE
                        ep.nombre_estado_pedido = %s
                '''
                cursor.execute(query,(valor_estado,))
                rows = cursor.fetchall()
                self.limpiar_panel(self.marco_izquierdo)
                self.tabla_frame(rows)

                cursor.close()
                conn.commit()
                conn.close()
    
        cursor.close()
        conn.commit()
        conn.close()
    
    def registrar_prod(self):
        conn,cursor = bd.conectar()
        query2 = '''
            SELECT id_tipo_entrega
            FROM Pedido
            WHERE id_pedido = %s        
        '''
        cursor.execute(query2,(pedidokx,))
        one = cursor.fetchone()

        if one:
            id_tipo_entrega = one[0]
        else:
            id_tipo_entrega = None

        if id_tipo_entrega == 'A':
            mov = 1
        elif id_tipo_entrega == 'B':
            mov = 2
        elif id_tipo_entrega == 'C':
            mov = 3
        else:
            mov = None          

        query = '''
            WITH NumerosKardex AS (
                SELECT COUNT(*) + 1 AS siguiente_numero
                FROM Kardex
            )

            INSERT INTO Kardex (id_kardex,fecha_kx,id_tipo_mov,id_pedido,id_tipo_entrega)
            VALUES (
                (SELECT 'KX0' || siguiente_numero FROM NumerosKardex),
                CURRENT_TIMESTAMP,%s,%s,%s
            )  
        '''
        cursor.execute(query,(mov,pedidokx,id_tipo_entrega))

        query6 = '''
            WITH NumerosKardex AS (
                SELECT COUNT(*) AS siguiente_numero
                FROM Kardex
            )
            SELECT 'KX0' || siguiente_numero AS id_kardex
            FROM NumerosKardex
        '''
        cursor.execute(query6)
        id_kx = cursor.fetchone()
        id_kx2 = id_kx[0]

        query7 = '''
            SELECT id_persona
            FROM Pedido
            WHERE id_pedido = %s
        '''
        cursor.execute(query7,(pedidokx,))
        person = cursor.fetchone()
        person2 = person[0]
        
        query5 = '''
            INSERT INTO KardexxProducto (id_kardex,id_producto,cantidad_kx)
            SELECT %s,id_producto,cantidad
            FROM ClientexProducto
            WHERE id_persona = %s AND id_estado_compra = 'C';       
        '''
        cursor.execute(query5,(id_kx2,person2,))

        query3 = '''
            UPDATE Pedido
            SET id_estado_pedido = 'P'
            WHERE id_pedido = %s
        '''
        cursor.execute(query3,(pedidokx,))

        query4 = '''
            UPDATE Venta
            SET id_estado_venta = 'D'
            WHERE cod_venta = (
                SELECT cod_venta
                FROM Pedido
                WHERE id_pedido = %s
            )
        '''
        cursor.execute(query4,(pedidokx,))
        util_mensaje.ConfirmarRegistro()
        cursor.close()
        conn.commit()
        conn.close()

