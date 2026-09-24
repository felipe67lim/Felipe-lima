import csv

ARQUIVO = "medicamentos.csv"


def carregar():
    lista = []

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)

            for dados in leitor:
                # Verifica se a linha possui 3 informações
                if len(dados) != 3:
                    continue

                nome = dados[0]
                categoria = dados[1]

                # Ignora o cabeçalho do arquivo CSV
                if dados[2].lower() == "quantidade":
                    continue

                # Tenta transformar a quantidade em número
                try:
                    quantidade = int(dados[2])
                except ValueError:
                    continue

                medicamento = [nome, categoria, quantidade]
                lista.append(medicamento)

    except FileNotFoundError:
        pass

    return lista


def salvar(lista):
    with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        # Cabeçalho
        escritor.writerow(["nome", "categoria", "quantidade"])

        for medicamento in lista:
            escritor.writerow([
                medicamento[0],
                medicamento[1],
                medicamento[2]
            ])


def cadastrar(lista):
    print("\n--- CADASTRAR MEDICAMENTO ---")

    nome = input("Nome: ")
    categoria = input("Categoria: ")

    try:
        quantidade = int(input("Quantidade: "))
    except ValueError:
        print("Quantidade inválida. Digite apenas números.")
        return

    medicamento = [nome, categoria, quantidade]

    lista.append(medicamento)

    salvar(lista)

    print("Medicamento cadastrado com sucesso!")


def listar(lista):
    print("\n--- MEDICAMENTOS ---")

    if len(lista) == 0:
        print("Nenhum medicamento cadastrado.")
        return

    for medicamento in lista:
        print(
            "Nome:", medicamento[0],
            "| Categoria:", medicamento[1],
            "| Quantidade:", medicamento[2]
        )


def buscar(lista):
    print("\n--- BUSCAR MEDICAMENTO ---")

    nome = input("Digite o nome do medicamento: ")

    encontrado = False

    for medicamento in lista:
        if medicamento[0].lower() == nome.lower():
            print("\nMedicamento encontrado!")
            print("Nome:", medicamento[0])
            print("Categoria:", medicamento[1])
            print("Quantidade:", medicamento[2])

            encontrado = True
            break

    if not encontrado:
        print("Medicamento não encontrado.")


def menu():
    lista = carregar()

    while True:
        print("\n===== MENU =====")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Buscar")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar(lista)

        elif opcao == "2":
            listar(lista)

        elif opcao == "3":
            buscar(lista)

        elif opcao == "4":
            salvar(lista)
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida. Escolha uma opção de 1 a 4.")


menu()

