from model.conexion_db import ConexionDB

class Proveedor:
    def __init__(self, ruc_proveedor, razon_social, web_proveedor, rubro, direccion, telefono, id_est_proveedor):
        self.ruc_proveedor = ruc_proveedor
        self.razon_social = razon_social
        self.web_proveedor = web_proveedor
        self.rubro = rubro
        self.direccion = direccion
        self.telefono = telefono
        self.id_est_proveedor = id_est_proveedor
    def __str__(self):
        return f'proveedor[{self.ruc_proveedor},{self.razon_social},{self.web_proveedor},{self.rubro},{self.direccion},{self.telefono},{self.est_prov}]'

def guardar(proveedor):
    conexion = ConexionDB()
    query = f"INSERT INTO proveedor(ruc_proveedor, razon_social, web_proveedor, rubro, direccion, telefono, id_est_proveedor) VALUES ('{proveedor.ruc_proveedor}', '{proveedor.razon_social}', '{proveedor.web_proveedor}', '{proveedor.rubro}', '{proveedor.direccion}', '{proveedor.telefono}', '{proveedor.id_est_proveedor}')"
    conexion.cursor.execute(query)
    print("Datos Guardados")
    conexion.cerrar()

def listar():
    conexion = ConexionDB()
    lista_proveedores = []
    query = 'SELECT * FROM proveedor'
    conexion.cursor.execute(query)
    lista_proveedores = conexion.cursor.fetchall()
    conexion.cerrar()

    return lista_proveedores
def editar(proveedor, ruc_proveedor):
    conexion = ConexionDB()

    sql = f"""UPDATE proveedor
    SET razon_social = '{proveedor.razon_social}', web_proveedor = '{proveedor.web_proveedor}',rubro = '{proveedor.rubro}',direccion = '{proveedor.direccion}',telefono = {proveedor.telefono}, id_est_proveedor = '{proveedor.id_est_proveedor}'
    WHERE ruc_proveedor = '{ruc_proveedor}'"""

    conexion.cursor.execute(sql)
    conexion.cerrar()