import sqlite3

# conexão com banco
conexao = sqlite3.connect("Banco de dados Fokus.db")

cursor = conexao.cursor()

print("=== SISTEMA DE CLIENTES ===")
print("1 - Cadastrar cliente")
print("2 - Listar clientes")
print("3 - Atualizar cliente")
print("4 - Deletar cliente")

opcao = input("Escolha uma opção: ")

# CREATE
if opcao == "1":

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    cursor.execute("""
    INSERT INTO clientes (nome, idade)
    VALUES (?, ?)
    """, (nome, idade))

    conexao.commit()

    print("Cliente cadastrado com sucesso!")

# READ
elif opcao == "2":

    cursor.execute("SELECT * FROM clientes")

    clientes = cursor.fetchall()

    for cliente in clientes:
        print(cliente)

# UPDATE
elif opcao == "3":

    id_cliente = int(input("Digite o ID do cliente: "))
    novo_nome = input("Novo nome: ")
    nova_idade = int(input("Nova idade: "))

    cursor.execute("""
    UPDATE clientes
    SET nome = ?, idade = ?
    WHERE id = ?
    """, (novo_nome, nova_idade, id_cliente))

    conexao.commit()

    print("Cliente atualizado com sucesso!")

# DELETE
elif opcao == "4":

    id_cliente = int(input("Digite o ID do cliente: "))

    cursor.execute("""
    DELETE FROM clientes
    WHERE id = ?
    """, (id_cliente,))

    conexao.commit()

    print("Cliente deletado com sucesso!")

else:
    print("Opção inválida!")

# fechar conexão
conexao.close()