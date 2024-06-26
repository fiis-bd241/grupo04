from tkinter import Tk,Canvas,Frame,Label,Entry,Button,W,E,Listbox,END,Toplevel
from tkinter import ttk
import tkinter as tk
import psycopg2


root = Tk()
root.title("Migni Almacen")

#Conectar BD
def conectar():
    conn = psycopg2.connect(
        dbname="Migni Store",
        user="postgres",
        password="123456_stark",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    return conn,cursor

#Ver Pedido
def ver_pedido(id_pedido):
    conn,cursor = conectar()
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
        AND v.id_estado_venta = 'B'   
    '''
    cursor.execute(query,(id_pedido,))
    rows = cursor.fetchall()

    marco = ttk.Frame(root)
    marco.pack()
    marco.place(relx=0.1,rely=0.35,relwidth=0.8,relheight=0.35)
    tabla = ttk.Treeview(marco,columns=("col1","col2","col3","col4"),show='headings')

    tabla.heading("col1",text="ID Producto")
    tabla.heading("col2",text="Nombre Producto")
    tabla.heading("col3",text="Cantidad")
    tabla.heading("col4",text="Ubicacion")

    tabla.column("col1",width=10)
    tabla.column("col2",width=150)
    tabla.column("col3",width=10)
    tabla.column("col4",width=15)

    tabla.pack(expand=True, fill=tk.BOTH)

    for x in rows:
        tabla.insert("",tk.END,values=x)

    show_entrega(id_pedido)

    cursor.close()
    conn.commit()
    conn.close()

def ingresar_prod(id_kardex,id_producto,cantidad):
    conn,cursor = conectar()
    query = '''
     INSERT INTO KardexxProducto(id_kardex,id_producto,cantidad_kx) 
     VALUES (%s,%s,%s)
    '''
    cursor.execute(query,(id_kardex, id_producto, cantidad))

    query2 = '''
    SELECT id_producto,cantidad_kx
    FROM KardexxProducto
    '''
    cursor.execute(query2,(id_kardex, id_producto, cantidad))
    rows= cursor.fetchall()

    ventana_kardex = Toplevel(root)
    ventana_kardex.title("Ingreso al Kardex")

    marco2 = ttk.Frame(ventana_kardex)
    marco2.pack()
    marco2.place(relx=0.1,rely=0.35,relwidth=0.8,relheight=0.35)
    tabla = ttk.Treeview(marco2,columns=("col1","col2"),show='headings')

    tabla.heading("col1",text="ID Producto")
    tabla.heading("col2",text="Cantidad")

    tabla.column("col1",width=150)
    tabla.column("col2",width=10)

    tabla.pack(expand=True, fill=tk.BOTH)

    for x in rows:
        tabla.insert("",tk.END,values=x)

    cursor.close()
    conn.commit()
    conn.close()

#Alistar el pedido para el Kardex
def alistar_pedido(id_pedido):

    conn,cursor = conectar()
    query = '''
    UPDATE Pedido
    SET id_estado_pedido = 'P'
    WHERE id_pedido = %s   
    '''
    cursor.execute(query,(id_pedido,))

    query2 = '''
    UPDATE Venta
    SET id_estado_venta = 'D'
    WHERE cod_venta = (
    SELECT cod_venta
    FROM Pedido
    WHERE id_pedido = %s
    )    
    '''
    cursor.execute(query2,(id_pedido,))  

    cursor.close()
    conn.commit()
    conn.close()

    ventana_kx(id_pedido)

#Nueva Ventana para Kardex
def ventana_kx(id_pedido):
    ventana_kardex = Toplevel(root)
    ventana_kardex.title("Kardex")

    estructura_kardex = Canvas(ventana_kardex, height=380, width=600, bg='lightblue')
    estructura_kardex.pack()

    conn,cursor = conectar()
    query3 = '''
    WITH NumerosKardex AS (
    SELECT COUNT(*) + 1 AS siguiente_numero
    FROM Kardex
    )

    INSERT INTO Kardex (id_kardex, fecha_kx, id_tipo_mov, id_pedido, id_tipo_entrega)
    VALUES (
    (SELECT 'KX0' || siguiente_numero FROM NumerosKardex),
    CURRENT_TIMESTAMP,
    1,
    (SELECT cod_venta FROM Pedido WHERE id_pedido = %s),
    (SELECT id_tipo_entrega FROM Pedido WHERE id_pedido = %s)
    )    
    '''
    cursor.execute(query3,(id_pedido,))

    query4 = '''
    SELECT id_kardex FROM Kardex WHERE id_pedido = %s    
    '''
    cursor.execute(query4,(id_pedido,))
    row = cursor.fetchall()
    
    marco = Frame(ventana_kardex)
    marco.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

    headerkx = Label(marco,text="Kardex:")
    headerkx.grid(row=0,column=1)
    header_kx = Label(marco,text=row)
    header_kx.grid(row=0,column=2)

    #Kardex Input
    inprod = Label(marco,text="Código Producto")
    inprod.grid(row=1,column=0)
    entry_prod = Entry(marco)
    entry_prod.grid(row=1,column=1)

    incantprod = Label(marco,text="Cantidad")
    incantprod.grid(row=1,column=0)
    entry_cantprod = Entry(marco)
    entry_cantprod.grid(row=1,column=1)

    #Boton Ingresar
    ingresar = Button(marco,text="Ingresar",command=lambda:ingresar_prod(row,
    entry_prod.get(),entry_cantprod.get()))
    ingresar.grid(row=2,column=1,sticky=W+E)

    cursor.close()
    conn.commit()
    conn.close()


#Mostrar el tipo y fecha de entrega + Botton Alistar
def show_entrega(id_pedido):
    conn,cursor = conectar()

    query = '''
    SELECT te.nombre_tipo_entrega
    FROM Pedido p
    JOIN Tipo_Entrega te ON p.id_tipo_entrega = te.id_tipo_entrega
    WHERE p.id_pedido = %s
    '''
    cursor.execute(query,(id_pedido,))
    row = cursor.fetchone()

    query2 = '''
    SELECT p.fecha_entrega
    FROM Pedido p
    WHERE p.id_pedido = %s    
    '''
    cursor.execute(query2,(id_pedido,))
    row2 = cursor.fetchone()    

    tipo_entrega = Label(marco,text="Tipo Entrega: ")
    tipo_entrega.grid(row=1,column=5)
    show_entrega = Label(marco,text=row)
    show_entrega.grid(row=1,column=6)  

    fecha_entrega = Label(marco,text="Fecha Entrega: ")
    fecha_entrega.grid(row=2,column=5)
    show_fecha = Label(marco,text=row2)
    show_fecha.grid(row=2,column=6)

    #Botton Alistar
    boton_alistar = Button(marco,text="Alistar",command=lambda:alistar_pedido(id_pedido))
    boton_alistar.place(relx=0.1,rely=0.80,relwidth=0.3,relheight=0.1)

    cursor.close()
    conn.commit()
    conn.close()

#Canva
estructura = Canvas(root,height=380,width=600)
estructura.pack()

marco = Frame()
marco.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

headerpedi = Label(marco,text="Ingresar Pedido")
headerpedi.grid(row=0,column=1)

#Pedido Input
inpedi = Label(marco,text="Código Pedido")
inpedi.grid(row=1,column=0)
entry_pedi = Entry(marco)
entry_pedi.grid(row=1,column=1)

#Botton Buscar
buscar = Button(marco,text="Buscar",command=lambda:ver_pedido(entry_pedi.get()))
buscar.grid(row=2,column=1,sticky=W+E)

root.mainloop()
