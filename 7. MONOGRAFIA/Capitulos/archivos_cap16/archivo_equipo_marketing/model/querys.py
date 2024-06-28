from .conexion_db import conexionDB
import psycopg2
from psycopg2 import sql

def verificar_credenciales(usuario, contrasena):
    conexion = conexionDB()
    cursor = conexion.cursor
    query = sql.SQL("""
        SELECT id_equipo_mark 
        FROM persona 
        WHERE usuario = {} AND contraseña = {};
    """).format(sql.Literal(usuario), sql.Literal(contrasena))
    cursor.execute(query)
    id_equipo_mark = cursor.fetchone()[0] if cursor.rowcount > 0 else None
    conexion.cerrar()
    return id_equipo_mark

def obtener_max_id_campaña():
    conexion = conexionDB()
    cursor = conexion.cursor
    query = "SELECT MAX(id_campaña) FROM campaña"
    cursor.execute(query)
    max_id = cursor.fetchone()[0] or 0
    conexion.cerrar()
    return max_id

def insertar_campaña(id_campaña, nom_campaña, fecha_ini, fecha_fin, dir_url, modalidad, archivo, desc_campaña, id_equipo_mark, id_gest_mark):
    conexion = conexionDB()
    cursor = conexion.cursor
    query = """
        INSERT INTO campaña (id_campaña, nom_campaña, fecha_ini, fecha_fin, dir_url, modalidad, archivo, desc_campaña, id_equipo_mark, id_gest_mark) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    cursor.execute(query, (id_campaña, nom_campaña, fecha_ini, fecha_fin, dir_url, modalidad, archivo, desc_campaña, id_equipo_mark, id_gest_mark))
    conexion.conexion.commit()  # Realizamos el commit para guardar los cambios en la base de datos
    conexion.cerrar()

def insertar_campañaxprod(id_campaña, id_producto):
    conexion = conexionDB()
    cursor = conexion.cursor
    query = sql.SQL("""
        INSERT INTO campañaxprod (id_campaña, id_producto) 
        VALUES ({}, {});
    """).format(sql.Literal(id_campaña), sql.Literal(id_producto))
    cursor.execute(query)
    conexion.conexion.commit()
    conexion.cerrar()

def insertar_campañaxcanal(id_campaña, id_canal):
    conexion = conexionDB()
    cursor = conexion.cursor
    query = sql.SQL("""
        INSERT INTO campañaxcanal (id_campaña, id_canal) 
        VALUES ({}, {});
    """).format(sql.Literal(id_campaña), sql.Literal(id_canal))
    cursor.execute(query)
    conexion.conexion.commit()
    conexion.cerrar()

def obtener_observaciones_pendientes(equipo_id):
    conexion = conexionDB()
    cursor = conexion.cursor
    query = """
            SELECT o.id_observacion, o.descripcion, o.id_campaña, o.estado_atendido
            FROM observacion o
            JOIN campaña c ON o.id_campaña = c.id_campaña
            WHERE c.id_equipo_mark = %s AND o.estado_atendido = false
            """
    cursor.execute(query, (equipo_id,))
    observaciones = cursor.fetchall()
    conexion.cerrar()
    return observaciones


def obtener_campaña_por_id(id_campaña):
    conexion = conexionDB()
    cursor = conexion.cursor
    query = """
        SELECT *
        FROM campaña
        WHERE id_campaña = %s
    """
    cursor.execute(query, (id_campaña,))
    campaña = cursor.fetchone()
    conexion.cerrar()
    return campaña

def actualizar_campaña(id_campaña, nom_campaña, fecha_ini, fecha_fin, dir_url, modalidad, archivo, desc_campaña):
    conexion = conexionDB()
    cursor = conexion.cursor
    query = """
        UPDATE campaña
        SET nom_campaña = %s, fecha_ini = %s, fecha_fin = %s, dir_url = %s, modalidad = %s, archivo = %s, desc_campaña = %s
        WHERE id_campaña = %s
    """
    cursor.execute(query, (nom_campaña, fecha_ini, fecha_fin, dir_url, modalidad, archivo, desc_campaña, id_campaña))
    conexion.conexion.commit()
    conexion.cerrar()

def actualizar_estado_observacion(id_observacion):
    conexion = conexionDB()
    cursor = conexion.cursor
    query = """
        UPDATE observacion
        SET estado_atendido = true
        WHERE id_observacion = %s
    """
    cursor.execute(query, (id_observacion,))
    conexion.conexion.commit()
    conexion.cerrar()


from .conexion_db import conexionDB

def actualizar_campaña(id_campaña, nombre, fecha_ini, fecha_fin, dir_url, modalidad, archivo, desc_campaña):
    conexion = conexionDB()
    cursor = conexion.cursor
    query = """
            UPDATE campaña
            SET nom_campaña = %s, fecha_ini = %s, fecha_fin = %s, dir_url = %s, modalidad = %s, archivo = %s, desc_campaña = %s
            WHERE id_campaña = %s
            """
    values = (nombre, fecha_ini, fecha_fin, dir_url, modalidad, archivo, desc_campaña, id_campaña)
    cursor.execute(query, values)
    conexion.conexion.commit()
    conexion.cerrar()

def actualizar_estado_observacion(id_observacion):
    conexion = conexionDB()
    cursor = conexion.cursor
    query = """
            UPDATE observacion
            SET estado_atendido = true
            WHERE id_observacion = %s
            """
    values = (id_observacion,)
    cursor.execute(query, values)
    conexion.conexion.commit()
    conexion.cerrar()










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

