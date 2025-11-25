from config.db import criar_conexao

def excluir_participante_por_email(email):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    cursor.execute("SELECT codigo, nome FROM Publico WHERE email = %s", (email,))
    resultado = cursor.fetchone()

    if resultado:
        codigo, nome = resultado
        cursor.execute("DELETE FROM Venda_Ingresso WHERE publico_codigo = %s", (codigo,))
        cursor.execute("DELETE FROM Publico WHERE codigo = %s", (codigo,))
        conexao.commit()
        print(f"Participante '{nome}' excluído com sucesso.")
    else:
        print("Email não encontrado.")

    cursor.close()
    conexao.close()



def excluir_participante_por_cpf(cpf):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    cursor.execute("SELECT codigo, nome FROM Publico WHERE cpf = %s", (cpf,))
    resultado = cursor.fetchone()

    if resultado:
        codigo, nome = resultado
        cursor.execute("DELETE FROM Venda_Ingresso WHERE publico_codigo = %s", (codigo,))
        cursor.execute("DELETE FROM Publico WHERE codigo = %s", (codigo,))
        conexao.commit()
        print(f"Participante '{nome}' excluído com sucesso.")
    else:
        print("CPF não encontrado.")

    cursor.close()
    conexao.close()