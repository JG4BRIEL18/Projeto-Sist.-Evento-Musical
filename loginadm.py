import getpass
from config.db import criar_conexao


def login_admin():
    print("=== LOGIN DO ADMINISTRADOR ===")
    usuario = input("Usuário: ")
    senha = getpass.getpass("Senha: ")

    # conecta ao banco de dados
    conn = criar_conexao()
    if not conn:
        print("Erro: não foi possível conectar ao banco.")
        return False

    try:
        cur = conn.cursor()

        # Consulta o usuário no banco
        query = """
            SELECT codigo 
            FROM LOGINBD
            WHERE usuario = %s AND senha = %s;
        """
        cur.execute(query, (usuario, senha))
        resultado = cur.fetchone()

        if resultado:
            print("Login realizado com sucesso!\n")
            cur.close()
            conn.close()
            return True
        else:
            print("Credenciais inválidas. Acesso negado.\n")
            cur.close()
            conn.close()
            return False

    except Exception as e:
        print(f"Erro ao validar login: {e}")
        return False
