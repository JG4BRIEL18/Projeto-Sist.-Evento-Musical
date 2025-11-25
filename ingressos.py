from config.db import criar_conexao

def listar_ingressos():
    conn = criar_conexao()
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT codigo, tipo, valor FROM Ingresso ORDER BY codigo")
        ingressos = cursor.fetchall()

        print("\n=== TIPOS DE INGRESSO ===")
        for i in ingressos:
            print(f"[{i[0]}] Tipo: {i[1]} | Valor: R$ {i[2]:.2f}")

        cursor.close()
        conn.close()