import sqlite3
from pathlib import Path

DB_NAME = "chamados.db"
SQL_FILE = "chamados.sql"

CHAMADOS = [
    {"id": 1, "titulo": "Erro no login", "prioridade": "Alta", "status": "Aberto", "usuario": "Ana Silva"},
    {"id": 2, "titulo": "Tela branca no app", "prioridade": "Crítica", "status": "Aberto", "usuario": "Bruno Costa"},
    {"id": 3, "titulo": "Atualizar cadastro", "prioridade": "Baixa", "status": "Em progresso", "usuario": "Carlos Souza"},
    {"id": 4, "titulo": "Boleto não gerado", "prioridade": "Média", "status": "Aberto", "usuario": "Daniela Lima"},
    {"id": 5, "titulo": "Botão quebrado", "prioridade": "Baixa", "status": "Aberto", "usuario": "Eduardo Rocha"},
    {"id": 6, "titulo": "Lentidão na busca", "prioridade": "Média", "status": "Em progresso", "usuario": "Fernanda Alves"},
    {"id": 7, "titulo": "Recuperar senha", "prioridade": "Alta", "status": "Aberto", "usuario": "Gabriel Santos"},
    {"id": 8, "titulo": "Erro no Pix", "prioridade": "Crítica", "status": "Aberto", "usuario": "Amanda Melo"},
    {"id": 9, "titulo": "Mudar foto de perfil", "prioridade": "Baixa", "status": "Fechado", "usuario": "Igor Ribeiro"},
    {"id": 10, "titulo": "Exportar PDF falhou", "prioridade": "Média", "status": "Aberto", "usuario": "Juliana Vieira"},
    {"id": 11, "titulo": "Carrinho esvaziando", "prioridade": "Alta", "status": "Em progresso", "usuario": "Lucas Martins"},
    {"id": 12, "titulo": "Cupom inválido", "prioridade": "Média", "status": "Aberto", "usuario": "Mariana Dias"},
    {"id": 13, "titulo": "Página 404 no FAQ", "prioridade": "Baixa", "status": "Aberto", "usuario": "Nicolas Ferreira"},
    {"id": 14, "titulo": "Atraso na entrega", "prioridade": "Alta", "status": "Aberto", "usuario": "Patricia Gomes"},
    {"id": 15, "titulo": "Email de boas-vindas", "prioridade": "Baixa", "status": "Fechado", "usuario": "Rodrigo Ramos"},
    {"id": 16, "titulo": "Estorno pendente", "prioridade": "Alta", "status": "Em progresso", "usuario": "Sabrina Oliveira"},
    {"id": 17, "titulo": "Alerta de segurança", "prioridade": "Crítica", "status": "Aberto", "usuario": "Thiago Barbosa"},
    {"id": 18, "titulo": "Link quebrado no menu", "prioridade": "Baixa", "status": "Aberto", "usuario": "Vanessa Cunha"},
    {"id": 19, "titulo": "Nota fiscal sumiu", "prioridade": "Média", "status": "Aberto", "usuario": "Willian Cardoso"},
    {"id": 20, "titulo": "Modo escuro travando", "prioridade": "Baixa", "status": "Em progresso", "usuario": "Yasmim Lopes"},
    {"id": 21, "titulo": "Erro na API de CEP", "prioridade": "Alta", "status": "Aberto", "usuario": "Arthur Antunes"},
    {"id": 22, "titulo": "Notificação duplicada", "prioridade": "Baixa", "status": "Aberto", "usuario": "Beatriz Mendes"},
    {"id": 23, "titulo": "Sessão expirando rápido", "prioridade": "Média", "status": "Em progresso", "usuario": "Caio Nogueira"},
    {"id": 24, "titulo": "Erro no cartão de crédito", "prioridade": "Crítica", "status": "Aberto", "usuario": "Diana Prince"},
    {"id": 25, "titulo": "Traduzir termo em inglês", "prioridade": "Baixa", "status": "Fechado", "usuario": "Elton John"},
    {"id": 26, "titulo": "Chat de suporte offline", "prioridade": "Alta", "status": "Aberto", "usuario": "Fábio Assunção"},
    {"id": 27, "titulo": "Upload de comprovante", "prioridade": "Média", "status": "Aberto", "usuario": "Gisele Bündchen"},
    {"id": 28, "titulo": "Histórico sumiu", "prioridade": "Alta", "status": "Em progresso", "usuario": "Heitor Villa"},
    {"id": 29, "titulo": "Termos de uso desatualizados", "prioridade": "Baixa", "status": "Aberto", "usuario": "Isabela Garcia"},
    {"id": 30, "titulo": "Erro 500 no checkout", "prioridade": "Crítica", "status": "Aberto", "usuario": "Jorge Ben"},
    {"id": 31, "titulo": "Ajustar margem do header", "prioridade": "Baixa", "status": "Em progresso", "usuario": "Karina Bacchi"},
    {"id": 32, "titulo": "Filtro por data quebrado", "prioridade": "Média", "status": "Aberto", "usuario": "Leonardo Dicaprio"},
    {"id": 33, "titulo": "Assinatura não renovada", "prioridade": "Alta", "status": "Aberto", "usuario": "Marta Vieira"},
    {"id": 34, "titulo": "Áudio do vídeo não funciona", "prioridade": "Média", "status": "Aberto", "usuario": "Neymar Junior"},
    {"id": 35, "titulo": "Atualizar política de privacidade", "prioridade": "Baixa", "status": "Fechado", "usuario": "Otávio Mesquita"},
    {"id": 36, "titulo": "Queda do servidor interno", "prioridade": "Crítica", "status": "Em progresso", "usuario": "Paula Toller"},
    {"id": 37, "titulo": "Convite por email falhou", "prioridade": "Baixa", "status": "Aberto", "usuario": "Quintino Aires"},
    {"id": 38, "titulo": "Extrato em branco", "prioridade": "Alta", "status": "Aberto", "usuario": "Renata Vasconcellos"},
    {"id": 39, "titulo": "Ícone errado no painel", "prioridade": "Baixa", "status": "Aberto", "usuario": "Samuel Rosa"},
    {"id": 40, "titulo": "Duplicidade de cobrança", "prioridade": "Crítica", "status": "Aberto", "usuario": "Tais Araújo"},
    {"id": 41, "titulo": "Validação de CNPJ", "prioridade": "Média", "status": "Em progresso", "usuario": "Umberto Eco"},
    {"id": 42, "titulo": "Mensagem de erro confusa", "prioridade": "Baixa", "status": "Aberto", "usuario": "Valéria Valenssa"},
    {"id": 43, "titulo": "Problema com fonte negrito", "prioridade": "Baixa", "status": "Aberto", "usuario": "Wagner Moura"},
    {"id": 44, "titulo": "Links de redes sociais fora do ar", "prioridade": "Média", "status": "Aberto", "usuario": "Xuxa Meneghel"},
    {"id": 45, "titulo": "Sem sinal de geolocalização", "prioridade": "Alta", "status": "Em progresso", "usuario": "Yuri Gagarin"},
    {"id": 46, "titulo": "Página recarregando sozinha", "prioridade": "Alta", "status": "Aberto", "usuario": "Zeca Pagodinho"},
    {"id": 47, "titulo": "Gráfico de vendas travado", "prioridade": "Média", "status": "Aberto", "usuario": "Alinne Moraes"},
    {"id": 48, "titulo": "Impossível remover endereço", "prioridade": "Média", "status": "Em progresso", "usuario": "Beto Jamaica"},
    {"id": 49, "titulo": "Vazamento de memória na aba", "prioridade": "Crítica", "status": "Aberto", "usuario": "Cláudia Raia"},
    {"id": 50, "titulo": "Ajustar alinhamento do rodapé", "prioridade": "Baixa", "status": "Fechado", "usuario": "Dado Dolabella"},
]


def conectar():
    return sqlite3.connect(DB_NAME)


def escapar_sql(valor):
    return "'" + str(valor).replace("'", "''") + "'"


def exportar_sql(caminho=SQL_FILE):
    linhas = [
        "DROP TABLE IF EXISTS chamados;",
        "CREATE TABLE chamados (",
        "    id INTEGER PRIMARY KEY,",
        "    titulo TEXT NOT NULL,",
        "    prioridade TEXT NOT NULL,",
        "    status TEXT NOT NULL,",
        "    usuario TEXT NOT NULL",
        ");",
        "",
        "INSERT INTO chamados (id, titulo, prioridade, status, usuario) VALUES",
    ]

    valores = []
    for chamado in CHAMADOS:
        valores.append(
            "(" + ", ".join(
                [
                    str(chamado["id"]),
                    escapar_sql(chamado["titulo"]),
                    escapar_sql(chamado["prioridade"]),
                    escapar_sql(chamado["status"]),
                    escapar_sql(chamado["usuario"]),
                ]
            ) + ")"
        )

    linhas.append(",\n".join(valores) + ";")
    Path(caminho).write_text("\n".join(linhas), encoding="utf-8")
    print(f"Arquivo SQL gerado em {caminho}")


def inicializar_banco():
    conn = conectar()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS chamados (
            id INTEGER PRIMARY KEY,
            titulo TEXT NOT NULL,
            prioridade TEXT NOT NULL,
            status TEXT NOT NULL,
            usuario TEXT NOT NULL
        )
        """
    )

    total = conn.execute("SELECT COUNT(*) FROM chamados").fetchone()[0]
    if total == 0:
        conn.executemany(
            "INSERT INTO chamados (id, titulo, prioridade, status, usuario) VALUES (?, ?, ?, ?, ?)",
            [
                (chamado["id"], chamado["titulo"], chamado["prioridade"], chamado["status"], chamado["usuario"])
                for chamado in CHAMADOS
            ],
        )

    conn.commit()
    conn.close()


def formatar_tabela(rows):
    if not rows:
        print("Nenhum chamado encontrado.")
        return

    headers = ["ID", "Título", "Prioridade", "Status", "Usuário"]
    tabela = [headers] + [[str(value) for value in row] for row in rows]
    widths = [
        max(len(str(tabela[i][j])) for i in range(len(tabela)))
        for j in range(len(headers))
    ]

    def linha(valores):
        return " | ".join(str(valor).ljust(widths[idx]) for idx, valor in enumerate(valores))

    separador = "-+-".join("-" * width for width in widths)
    print(linha(headers))
    print(separador)
    for row in tabela[1:]:
        print(linha(row))


def listar_chamados(sql, parametros=()):
    conn = conectar()
    rows = conn.execute(sql, parametros).fetchall()
    conn.close()
    formatar_tabela(rows)


def pesquisa_usuario():
    usuario = input("Qual o usuário? ").strip()
    print(f"\nResultados para: {usuario}\n")
    listar_chamados(
        "SELECT id, titulo, prioridade, status, usuario FROM chamados WHERE usuario LIKE ? ORDER BY id",
        (f"%{usuario}%",),
    )


def pesquisa_prioridade():
    print("Essas são as prioridades existentes: Baixa; Crítica; Média; Alta")
    prioridade = input("Qual a prioridade? ").strip()
    print(f"\nResultados para: {prioridade}\n")
    listar_chamados(
        "SELECT id, titulo, prioridade, status, usuario FROM chamados WHERE prioridade = ? ORDER BY id",
        (prioridade,),
    )


def pesquisa_status():
    print("Essas são os status existentes: Aberto; Em progresso; Fechado")
    status = input("Qual o status? ").strip()
    print(f"\nResultados para: {status}\n")
    listar_chamados(
        "SELECT id, titulo, prioridade, status, usuario FROM chamados WHERE status LIKE ? ORDER BY id",
        (f"%{status}%",),
    )


def mostrar_urgentes():
    print("\nChamados urgentes (Crítica e Abertos)\n")
    listar_chamados(
        "SELECT id, titulo, prioridade, status, usuario FROM chamados WHERE status = 'Aberto' AND prioridade = 'Crítica' ORDER BY id"
    )


def abrir_chamado():
    usuario = input("Qual o nome do usuário? ").strip()
    titulo = input("De um título para o chamado: ").strip()
    print("Essas são as prioridades existentes: Baixa; Crítica; Média; Alta")
    prioridade = input("Qual a prioridade? ").strip()
    print("Essas são os status existentes: Aberto; Em progresso; Fechado")
    status = input("Qual o status? ").strip()

    conn = conectar()
    proximo_id = conn.execute("SELECT COALESCE(MAX(id), 0) + 1 FROM chamados").fetchone()[0]
    conn.execute(
        "INSERT INTO chamados (id, titulo, prioridade, status, usuario) VALUES (?, ?, ?, ?, ?)",
        (proximo_id, titulo, prioridade, status, usuario),
    )
    conn.commit()
    conn.close()
    print(f"\nChamado criado com sucesso: ID {proximo_id}\n")


def resolver_chamado():
    identificador = input("Qual o id? ").strip()
    conn = conectar()
    conn.execute("UPDATE chamados SET status = 'Em progresso' WHERE id = ?", (identificador,))
    conn.commit()
    conn.close()
    print(f"\nChamado {identificador} atualizado para 'Em progresso'.\n")


def fechar_chamado():
    identificador = input("Qual o id? ").strip()
    conn = conectar()
    conn.execute("UPDATE chamados SET status = 'Fechado' WHERE id = ?", (identificador,))
    conn.commit()
    conn.close()
    print(f"\nChamado {identificador} atualizado para 'Fechado'.\n")


def menu():
    while True:
        print("\n---\nLista de Chamados\n---")
        print("1 - Pesquisa por usuário")
        print("2 - Pesquisa por prioridade")
        print("3 - Pesquisa por status")
        print("4 - Chamados urgentes (Crítica e Abertos)")
        print("5 - Abrir chamado")
        print("6 - Resolver chamado")
        print("7 - Fechar chamado")
        print("8 - Exibir todos os chamados em tabela")
        print("9 - Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            pesquisa_usuario()
        elif opcao == "2":
            pesquisa_prioridade()
        elif opcao == "3":
            pesquisa_status()
        elif opcao == "4":
            mostrar_urgentes()
        elif opcao == "5":
            abrir_chamado()
        elif opcao == "6":
            resolver_chamado()
        elif opcao == "7":
            fechar_chamado()
        elif opcao == "8":
            print("\nTodos os chamados\n")
            listar_chamados("SELECT id, titulo, prioridade, status, usuario FROM chamados ORDER BY id")
        elif opcao == "9":
            print("\nSaindo do sistema...")
            break
        else:
            print("Opção não se encontra na lista")


if __name__ == "__main__":
    exportar_sql(SQL_FILE)
    inicializar_banco()
    menu()
