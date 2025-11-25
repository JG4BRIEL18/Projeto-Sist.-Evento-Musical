import psycopg2


def criar_conexao():
    try:
        conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='peteca22',
            host='localhost',
            port='5432'
        )
        print(
            "Conexão realizada com sucesso!")
        return conn
    except Exception as e:
        print(f"Erro ao conectar com o banco de dados: {e}")
        return None
