from config.db import criar_conexao


def listar_eventos():
    conn = criar_conexao()
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT '[' || e.codigo || '] Data: ' || e.data || "
            " ' | Horário: ' || e.horario || "
            " ' | Local: ' || e.local || "
            " ' | Banda: ' || STRING_AGG(a.nome, ' e Banda: ') AS descricao_evento "
            "FROM evento e "
            "INNER JOIN evento_artista ea ON e.codigo = ea.evento_codigo "
            "INNER JOIN artista a ON ea.artista_codigo = a.codigo "
            "GROUP BY e.codigo, e.data, e.horario, e.local "
            "ORDER BY e.codigo"
        )
        eventos = cursor.fetchall()

        print("\n=== EVENTOS DISPONÍVEIS ===")
        for e in eventos:
            print(e[0])  

        cursor.close()
        conn.close()



