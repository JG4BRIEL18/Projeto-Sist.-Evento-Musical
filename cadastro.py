from config.db import criar_conexao
from datetime import date
from services.evento_lista import listar_eventos
from services.ingressos import listar_ingressos

def cadastrar_participante():
    print("\n=== CADASTRO DE PARTICIPANTE ===")
    nome = input("Nome: ")
    cpf = input("CPF (xxx.xxx.xxx-xx): ")
    email = input("E-mail: ")

    listar_eventos()
    evento_codigo = int(input("\nDigite o código do evento: "))

    listar_ingressos()
    ingresso_codigo = int(input("\nDigite o código do ingresso: "))

    conn = criar_conexao()
    if conn is None:
        return

    try:
        cursor = conn.cursor()

        # Verificar se a pessoa já existe
        cursor.execute(
            "SELECT codigo FROM Publico WHERE cpf = %s OR email = %s", (cpf, email))
        resultado = cursor.fetchone()

        if resultado:
            publico_codigo = resultado[0]
            print("Pessoa já cadastrada no sistema.")
        else:
            cursor.execute(
                "INSERT INTO Publico (nome, cpf, email) VALUES (%s, %s, %s) RETURNING codigo",
                (nome, cpf, email)
            )
            publico_codigo = cursor.fetchone()[0]
            print("Pessoa cadastrada com sucesso.")

        # Verificar se já comprou ingresso para este evento
        cursor.execute("""
            SELECT COUNT(*) FROM Venda_Ingresso
            WHERE evento_codigo = %s AND publico_codigo = %s AND ingresso_codigo = %s;
        """, (evento_codigo, publico_codigo, ingresso_codigo))
        ja_comprou = cursor.fetchone()[0]

        if ja_comprou > 0:
            print("Esta pessoa já comprou este tipo de ingresso para este evento.")
        else:
            # Registrar nova compra
            data_compra = date.today()
            cursor.execute(
                """INSERT INTO Venda_Ingresso (ingresso_codigo, evento_codigo, publico_codigo, data_compra)
                    VALUES (%s, %s, %s, %s)""",
                (ingresso_codigo, evento_codigo, publico_codigo, data_compra)
            )
            conn.commit()
            print("Ingresso registrado com sucesso.")

    except Exception as e:
        print("Erro ao cadastrar:", e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()