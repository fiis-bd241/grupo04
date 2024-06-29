from .conexion_db import conexionDB
from datetime import date

def obtener_campaña_por_id(campaña_id):
    conexion = conexionDB()
    conexion.cursor.execute("SELECT * FROM campaña WHERE Id_campaña = %s", (campaña_id,))
    campaña = conexion.cursor.fetchone()
    conexion.cerrar()
    return campaña

def actualizar_campaña(campaña_id, datos):
    conexion = conexionDB()
    set_clause = ', '.join([f"{key} = %s" for key in datos.keys()])
    values = list(datos.values())
    values.append(campaña_id)
    sql = f"UPDATE campaña SET {set_clause} WHERE Id_campaña = %s"
    conexion.cursor.execute(sql, values)
    conexion.cerrar()

def borrar_campaña(campaña_id):
    conexion = conexionDB()
    try:
        conexion.cursor.execute("START TRANSACTION")
        conexion.cursor.execute("DELETE FROM observacion WHERE Id_campaña = %s", (campaña_id,))
        conexion.cursor.execute("DELETE FROM campañaxprod WHERE Id_campaña = %s", (campaña_id,))
        conexion.cursor.execute("DELETE FROM campañaxcanal WHERE Id_campaña = %s", (campaña_id,))
        conexion.cursor.execute("DELETE FROM campaña WHERE Id_campaña = %s", (campaña_id,))
        conexion.conexion.commit()
    except Exception as e:
        print(f"Error al borrar campaña: {e}")
        conexion.conexion.rollback()
    finally:
        conexion.cerrar()


def obtener_campañas_vigentes(hoy):
    conexion = conexionDB()
    conexion.cursor.execute("SELECT * FROM campaña WHERE fecha_ini <= %s AND fecha_fin >= %s", (hoy, hoy))
    campañas = conexion.cursor.fetchall()
    conexion.cerrar()
    return campañas

def obtener_campañas_propuestas(hoy):
    conexion = conexionDB()
    conexion.cursor.execute("SELECT * FROM campaña WHERE fecha_ini > %s", (hoy,))
    campañas = conexion.cursor.fetchall()
    conexion.cerrar()
    return campañas


def obtener_ultimo_id_observacion():
    conexion = conexionDB()
    conexion.cursor.execute("SELECT MAX(Id_observacion) FROM observacion")
    ultimo_id = conexion.cursor.fetchone()[0]
    conexion.cerrar()
    return ultimo_id if ultimo_id is not None else 0

def agregar_observacion(id_campaña, descripcion):
    conexion = conexionDB()
    estado_atendido = False
    id_observacion = obtener_ultimo_id_observacion() + 1
    conexion.cursor.execute("INSERT INTO observacion (Id_observacion, descripcion, Id_campaña, estado_atendido) VALUES (%s, %s, %s, %s)",
                            (id_observacion, descripcion, id_campaña, estado_atendido))
    conexion.cerrar()
    return True  # Indicar éxito al agregar la observación

def obtener_productos_por_campaña(campaña_id):
    conexion = conexionDB()
    conexion.cursor.execute("SELECT id_producto FROM campañaxprod WHERE id_campaña = %s", (campaña_id,))
    productos = conexion.cursor.fetchall()
    conexion.cerrar()
    return [producto[0] for producto in productos]

def actualizar_productos_por_campaña(campaña_id, productos):
    conexion = conexionDB()
    try:
        conexion.cursor.execute("START TRANSACTION")
        conexion.cursor.execute("DELETE FROM campañaxprod WHERE id_campaña = %s", (campaña_id,))
        for producto_id in productos:
            conexion.cursor.execute("INSERT INTO campañaxprod (id_campaña, id_producto) VALUES (%s, %s)", (campaña_id, producto_id))
        conexion.conexion.commit()
    except Exception as e:
        print(f"Error al actualizar productos: {e}")
        conexion.conexion.rollback()
    finally:
        conexion.cerrar()


def obtener_canales_por_campaña(campaña_id):
    conexion = conexionDB()
    conexion.cursor.execute("SELECT id_canal FROM campañaxcanal WHERE id_campaña = %s", (campaña_id,))
    canales = conexion.cursor.fetchall()
    conexion.cerrar()
    return [canal[0] for canal in canales]


def actualizar_canales_por_campaña(campaña_id, canales):
    conexion = conexionDB()
    try:
        conexion.cursor.execute("START TRANSACTION")
        conexion.cursor.execute("DELETE FROM campañaxcanal WHERE id_campaña = %s", (campaña_id,))
        for canal_id in canales:
            conexion.cursor.execute("INSERT INTO campañaxcanal (id_campaña, id_canal) VALUES (%s, %s)", (campaña_id, canal_id))
        conexion.conexion.commit()
    except Exception as e:
        print(f"Error al actualizar canales: {e}")
        conexion.conexion.rollback()
    finally:
        conexion.cerrar()

