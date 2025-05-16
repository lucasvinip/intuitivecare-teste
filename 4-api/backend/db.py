import MySQLdb
from MySQLdb.cursors import DictCursor

def get_db_connection():
    try:
        conn = MySQLdb.connect(
            host="127.0.0.1",
            user="root",
            passwd="",
            db="dados_ans",
            cursorclass=DictCursor
        )
        print("✅ Conexão bem-sucedida!")
        return conn

    except MySQLdb.Error as err:
        print(f"Erro ao conectar: {err}")
        return None

    except Exception as e:
        import traceback
        print("Erro inesperado:")
        traceback.print_exc()
        return None
