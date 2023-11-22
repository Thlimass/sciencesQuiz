import psycopg2
from config import DATABASE

try:
    conn = psycopg2.connect(
        dbname=DATABASE.database,
        user=DATABASE.user,
        password=DATABASE.password,
        host=DATABASE.host,
        port=DATABASE.port
    )
    print("Conexão bem-sucedida!")
    conn.close()  # Não se esqueça de fechar a conexão após o teste
except psycopg2.Error as e:
    print("Erro de conexão:", e)
