# database.py
import psycopg2

def conectar():
    conexao = psycopg2.connect(
        host="localhost",
        database="estudo",
        user="postgres",
        password=""
    )
    return conexao