import csv

ARQUIVO = "medicamentos.csv"


def carregar():
    lista = []

    try:
        arquivo = open(ARQUIVO, "r", encoding="utf-8")
        leitor = csv.reader(arquivo)

        for dados in leitor:
            if len(dados) == 3:
                nome = dados[0]
                categoria = dados[1]
                quantidade = int(dados[2])

                medicamento = [nome, categoria, quantidade]
                lista.append(medicamento)

        arquivo.close()

    except FileNotFoundError:
        pass

    return lista


def salvar(lista):
    arquivo = open(ARQUIVO, "w", encoding="utf-8")
    escritor = csv.writer(arquivo)

    for medicamento in lista:
        escritor.writerow([
            medicamento[0],
            medicamento[1],
            medicamento[2]
        ])

    arquivo.close()


def cadastrar(lista):
    print("\n--- CADASTRAR MEDICAMENTO ---")

    nome = input("Nome: ")
    categoria = input("Categoria: ")
    quantidade = int(input("Quantidade: "))

    medicamento = [nome, categoria, quantidade]

    lista.append(medicamento)

    salvar(lista)

    print("Medicamento cadastrado!")


def listar(lista):
    print("\n--- MEDICAMENTOS ---")

    if len(lista) == 0:
        print("Nenhum medicamento cadastrado.")
    else:
        for medicamento in lista:
            print(
                "Nome:",
                medicamento[0],
                "| Categoria:",
                medicamento[1],
                "| Quantidade:",
                medicamento[2]
            )


def buscar(lista):
    nome = input("\nDigite o nome do medicamento: ")

    encontrado = False

    for medicamento in lista:
        if medicamento[0].lower() == nome.lower():
            print("\nMedicamento encontrado!")
            print("Nome:", medicamento[0])
            print("Categoria:", medicamento[1])
            print("Quantidade:", medicamento[2])

            encontrado = True

    if encontrado == False:
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
            print("Opção inválida.")


menimport csv

ARQUIVO = "medicamentos.csv"


def carregar():
    lista = []

    try:
        arquivo = open(ARQUIVO, "r", encoding="utf-8")
        leitor = csv.reader(arquivo)

        for dados in leitor:
            if len(dados) == 3:
                nome = dados[0]
                categoria = dados[1]
                quantidade = int(dados[2])

                medicamento = [nome, categoria, quantidade]
                lista.append(medicamento)

        arquivo.close()

    except FileNotFoundError:
        pass

    return lista


def salvar(lista):
    arquivo = open(ARQUIVO, "w", encoding="utf-8")
    escritor = csv.writer(arquivo)

    for medicamento in lista:
        escritor.writerow([
            medicamento[0],
            medicamento[1],
            medicamento[2]
        ])

    arquivo.close()


def cadastrar(lista):
    print("\n--- CADASTRAR MEDICAMENTO ---")

    nome = input("Nome: ")
    categoria = input("Categoria: ")
    quantidade = int(input("Quantidade:


menu
