from config.db import criar_conexao
from services.evento_lista import listar_eventos

def listar_participantes():
    conn = criar_conexao()
    if conn is None:
        return

    listar_eventos()
    evento_id = input(
        "\nDigite o código do evento para ver os participantes: ")

    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT p.nome, p.cpf, p.email, i.tipo, i.valor, v.data_compra
            FROM Venda_Ingresso v
            JOIN Publico p ON v.publico_codigo = p.codigo
            JOIN Ingresso i ON v.ingresso_codigo = i.codigo
            WHERE v.evento_codigo = %s
            ORDER BY v.data_compra;
        """, (evento_id,))

        resultados = cursor.fetchall()

        print("\n=== PARTICIPANTES DO EVENTO ===")
        if resultados:
            for r in resultados:
                print(
                    f"Nome: {r[0]} | CPF: {r[1]} | E-mail: {r[2]} | Ingresso: {r[3]} | Valor: R$ {r[4]:.2f} | Compra: {r[5]}")
        else:
            print("Nenhum participante encontrado para este evento.")

    except Exception as e:
        print("Erro ao listar participantes:", e)
    finally:
        cursor.close()
        conn.close()

def editar_participante():
    conn = criar_conexao()
    if conn is None:
        return

    print("\n=== EDITAR PARTICIPANTE ===")
    cpf_atual = input("Digite o CPF do participante que deseja editar: ")

    try:
        cursor = conn.cursor()

        # Verificar se o CPF existe
        cursor.execute("SELECT codigo, nome, cpf, email FROM Publico WHERE cpf = %s", (cpf_atual,))
        participante = cursor.fetchone()

        if not participante:
            print("Nenhum participante encontrado com esse CPF.")
            return

        print(f"\nParticipante encontrado:")
        print(f"1 - Nome atual : {participante[1]}")
        print(f"2 - CPF atual  : {participante[2]}")
        print(f"3 - Email atual: {participante[3]}")

        escolha = input("\nO que deseja editar? (1-Nome / 2-CPF / 3-Email): ")

        if escolha == "1":
            novo_valor = input("Digite o novo nome: ")
            cursor.execute("UPDATE Publico SET nome = %s WHERE cpf = %s", (novo_valor, cpf_atual))

        elif escolha == "2":
            novo_valor = input("Digite o novo CPF: ")
            cursor.execute("UPDATE Publico SET cpf = %s WHERE cpf = %s", (novo_valor, cpf_atual))

        elif escolha == "3":
            novo_valor = input("Digite o novo email: ")
            cursor.execute("UPDATE Publico SET email = %s WHERE cpf = %s", (novo_valor, cpf_atual))

        else:
            print("Opção inválida.")
            return

        conn.commit()
        print("\nDados atualizados com sucesso!")

    except Exception as e:
        print("Erro ao editar participante:", e)

    finally:
        cursor.close()
        conn.close()

