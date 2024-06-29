from tkinter import Frame,Label,TOP,RIGHT,LEFT,BOTH,END,Entry,Button,X,Y,W,E
from tkinter import ttk
from config import color_cuerpo_principal,color_marco_izquierdo,color_marco_derecho,borde_marco
import util.util_mensaje as util_mensaje
import BD.conexion_bd as bd

class InfoKardex():
    def __init__(self,panel_principal):
        self.marco_superior = Frame(panel_principal,bg=color_cuerpo_principal,height=80)
        self.marco_superior.pack(side=TOP,padx=5,pady=5,fill=X,expand=False)

        self.marco_izquierdo = Frame(panel_principal,bg=color_marco_izquierdo)
        self.marco_izquierdo.pack(side=LEFT,padx=3,pady=3,fill=BOTH,expand=True)

        self.marco_derecha = Frame(panel_principal,bg=color_marco_derecho)
        self.marco_derecha.pack(side=RIGHT,fill=BOTH,expand=True)
    
        conn,cursor = bd.conectar()
        query = '''
            SELECT
                k.id_kardex,
                TO_CHAR(k.fecha_kx,'YYYY-MM-DD HH24:MI:SS') AS fecha_kx,
                tm.nombre_movimiento,
                k.id_pedido,
                te.nombre_tipo_entrega
            FROM
                Kardex k
            INNER JOIN
                Tipo_Movimiento tm ON k.id_tipo_mov = tm.id_tipo_mov
            INNER JOIN
                Pedido p ON k.id_pedido = p.id_pedido
            INNER JOIN
                Tipo_Entrega te ON p.id_tipo_entrega = te.id_tipo_entrega        
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

        self.tabla = ttk.Treeview(self.marco,columns=("col1","col2","col3","col4","col5"),
        show='headings',style="Custom.Treeview")

        self.tabla.heading("col1",text="ID Kardex")
        self.tabla.heading("col2",text="Fecha")
        self.tabla.heading("col3",text="Movimiento")
        self.tabla.heading("col4",text="Pedido")
        self.tabla.heading("col5",text="Tipo Entrega")

        self.tabla.column("col1",width=3)
        self.tabla.column("col2",width=5)
        self.tabla.column("col3",width=10)
        self.tabla.column("col4",width=5)
        self.tabla.column("col5",width=15)

        self.tabla.pack(expand=True,fill=BOTH)

        for x in filas:
            self.tabla.insert("",END,values=x)
        
        self.tabla.bind("<ButtonRelease-1>",self.mostrar_detalles)
    
    def tabla_info(self,filas):
        style = ttk.Style()
        style.configure("Custom.Treeview",background="#c9c9c9",
        fieldbackground="#c9c9c9",foreground="black")
        style.configure("Custom.Treeview.Heading",background="lightblue",font=("Helvetica",10,"bold"))

        self.marco = Frame(self.marco_derecha,bg=borde_marco)
        self.marco.config(borderwidth=2,width=500,height=100)
        self.marco.pack(fill=X,pady=6)

        self.tabla2 = ttk.Treeview(self.marco,columns=("col1","col2"),
        show='headings',style="Custom.Treeview")

        self.tabla2.heading("col1",text="Producto")
        self.tabla2.heading("col2",text="Cantidad")

        self.tabla2.column("col1",width=70)
        self.tabla2.column("col2",width=10)

        self.tabla2.pack(expand=True,fill=BOTH)

        for x in filas:
            self.tabla2.insert("",END,values=x)
    
    def mostrar_detalles(self,event):
        item = self.tabla.selection()[0]
        id_detalle = str(self.tabla.item(item,"values")[0])

        conn,cursor = bd.conectar()
        query = '''
            SELECT p.nombre_producto,kp.cantidad_kx
            FROM KardexxProducto kp
            JOIN Producto p ON kp.id_producto = p.id_producto
            WHERE kp.id_kardex = %s
        '''
        cursor.execute(query,(id_detalle,))
        self.limpiar_panel(self.marco_derecha)
        self.tabla_info(cursor.fetchall())

        cursor.close()
        conn.commit()
        conn.close()
    
    def limpiar_panel(self,panel):
        for widget in panel.winfo_children():
            widget.destroy()