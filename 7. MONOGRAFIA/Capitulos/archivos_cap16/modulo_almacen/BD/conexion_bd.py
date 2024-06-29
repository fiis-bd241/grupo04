import psycopg2

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