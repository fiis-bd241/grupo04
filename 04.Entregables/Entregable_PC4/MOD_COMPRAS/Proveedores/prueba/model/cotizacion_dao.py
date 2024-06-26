from model.conexion_db import ConexionDB

class Cotizacion:
    def __init__(self, id_cotizacion, monto_total, ruc_proveedor, fecha, id_est_cotizacion):
        self.id_cotizacion = id_cotizacion
        self.monto_total = monto_total
        self.ruc_proveedor = ruc_proveedor
        self.fecha = fecha
        self.id_est_cotizacion = id_est_cotizacion

    def __str__(self):
        return f'cotizacion[{self.id_cotizacion},{self.monto_total},{self.ruc_proveedor},{self.fecha},{self.id_est_cotizacion}]'

def guardar(cotizacion):
    conexion = ConexionDB()
    query = f"INSERT INTO cotizacion(id_cotizacion, monto_total, ruc_proveedor, fecha, id_est_cotizacion) VALUES ('{cotizacion.id_cotizacion}', '{cotizacion.monto_total}', '{cotizacion.ruc_proveedor}', '{cotizacion.fecha}', '{cotizacion.id_est_cotizacion}')"
    conexion.cursor.execute(query)
    print("Datos Guardados")
    conexion.cerrar()

def listar():
    conexion = ConexionDB()
    lista_cotizacion = []
    query = 'SELECT * FROM cotizacion'
    conexion.cursor.execute(query)
    lista_cotizacion = conexion.cursor.fetchall()
    conexion.cerrar()

    return lista_cotizacion

def editar(proveedor, id_cotizacion):
    conexion = ConexionDB()

    sql = f"""UPDATE cotizacion
    SET monto_total = '{proveedor.monto_total}', ruc_proveedor = '{proveedor.ruc_proveedor}',fecha = '{proveedor.fecha}',id_est_cotizacion = '{proveedor.id_est_cotizacion}'
    WHERE id_cotizacion = {id_cotizacion}"""

    conexion.cursor.execute(sql)
    conexion.cerrar()