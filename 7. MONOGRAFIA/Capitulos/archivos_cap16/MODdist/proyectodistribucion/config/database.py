import psycopg2
from psycopg2 import sql

def get_db_connection():
    return psycopg2.connect(
        dbname = "nueva_migni",
        user = "postgres",
        password = "kenedy428",
        host = "localhost",
        port = "5432"
    )
