from model.conexion_db import ConexionDB


class Factura:
    def __init__(self,nro_factura,fecha_emision,monto,id_persona,ruc_proveedor,id_tip_fac,id_estado):
        self.nro_factura = nro_factura
        self.fecha_emision = fecha_emision
        self.monto = monto
        self.id_persona = id_persona
        self.ruc_proveedor = ruc_proveedor
        self.id_tip_fac = id_tip_fac
        self.id_estado = id_estado
    def __str__(self):
        return f'factura[{self.nro_factura},{self.fecha_emision},{self.monto},{self.id_persona},{self.ruc_proveedor},{self.id_tip_fac},{self.id_estado}]'

def guardar(factura):
    conexion = ConexionDB()
    query =f"INSERT INTO Factura(nro_factura, fecha_emision, monto, id_persona, ruc_proveedor, id_tip_fac, id_estado) VALUES ('{Factura.nro_factura}', '{Factura.fecha_emision}', '{Factura.monto}', '{Factura.id_persona}','{Factura.ruc_proveedor}', '{Factura.id_tip_fac}', '{Factura.id_estado}')"
    conexion.cursor.execute(query)
    print("Datos guardados")
    conexion.cerrar()

def listar():
    conexion = ConexionDB()
    lista_facturas = []
    query = 'select * from factura'
    conexion.cursor.execute(query)
    lista_facturas = conexion.cursor.fetchall()
    conexion.cerrar()

    return lista_facturas

def editar(factura, nro_factura):
    conexion = ConexionDB()
    sql = f"""UPDATE factura
    SET fecha_emision = '{factura.fecha_emision}',monto = '{factura.monto}',id_persona= '{factura.id_persona}',ruc_proveedor = {factura.ruc_proveedor}, id_tip_factura = '{factura.id_tip_factura}',id_estado = '{factura.id_estado}'
    WHERE nro_factura = '{factura.nro_factura}'"""
    conexion.cursor.execute(sql)
    conexion.cerrar()