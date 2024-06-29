from model.conexion_db import ConexionDB

# Conectar a la base de datos y obtener los datos
class Proveedor:
    def __init__(self, ruc_proveedor):
        self.ruc_proveedor = ruc_proveedor
    def __str__(self):
        return f'proveedor[{self.ruc_proveedor}]'

class Cotizacion:
    def __init__(self,id_cotizacion,id_est_cotizacion):
        self.id_cotizacion = id_cotizacion
        self.id_est_cotizacion = id_est_cotizacion

    def __str__(self):
        return f'cotizacion[{self.id_cotizacion},{self.id_est_cotizacion}]'

def listar1():
    conexion = ConexionDB()
    lista_proveedores = []
    query = '''SELECT * FROM proveedor WHERE id_est_proveedor = 'A' '''
    conexion.cursor.execute(query)
    lista_proveedores = conexion.cursor.fetchall()
    conexion.cerrar()

    return lista_proveedores
def guardar1(proveedor):
    conexion = ConexionDB()
    query = f"INSERT INTO proveedor(ruc_proveedor, razon_social, web_proveedor, rubro, direccion, telefono, id_est_proveedor) VALUES ('{proveedor.ruc_proveedor}', '{proveedor.razon_social}', '{proveedor.web_proveedor}', '{proveedor.rubro}', '{proveedor.direccion}', '{proveedor.telefono}', '{proveedor.id_est_proveedor}')"
    conexion.cursor.execute(query)
    print("Datos Guardados")
    conexion.cerrar()


def buscar2(proveedor):
    conexion = ConexionDB()
    lista_cotizacion_prov = []
    query = f'''SELECT * FROM cotizacion WHERE ruc_proveedor ='{proveedor.ruc_proveedor}' '''
    conexion.cursor.execute(query)
    lista_cotizacion_prov = conexion.cursor.fetchall()
    conexion.cerrar()

    return lista_cotizacion_prov


def listar2():
    conexion = ConexionDB()
    lista_cotizacion = []
    query = '''SELECT * FROM cotizacion WHERE id_est_cotizacion = 'P' '''
    conexion.cursor.execute(query)
    lista_cotizacion = conexion.cursor.fetchall()
    conexion.cerrar()

    return lista_cotizacion


def guardar2(cotizacion):
    conexion = ConexionDB()
    query = f"INSERT INTO cotizacion(id_cotizacion, monto_total, ruc_proveedor, fecha, id_est_cotizacion) VALUES ('{cotizacion.id_cotizacion}', '{cotizacion.monto_total}', '{cotizacion.ruc_proveedor}', '{cotizacion.fecha}', '{cotizacion.id_est_cotizacion}')"
    conexion.cursor.execute(query)
    print("Datos Guardados")
    conexion.cerrar()

def editar2(proveedor, id_cotizacion):
    conexion = ConexionDB()

    sql = f"""UPDATE cotizacion
    SET id_est_cotizacion = '{proveedor.id_est_cotizacion}'
    WHERE id_cotizacion = {id_cotizacion}"""

    conexion.cursor.execute(sql)
    conexion.cerrar()