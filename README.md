Sistema de Cadastro de Medicamentos
Este projeto é um sistema simples em Python para cadastrar, listar e buscar medicamentos. Os dados são armazenados em um arquivo medicamentos.csv, permitindo que as informações continuem salvas mesmo depois que o programa seja encerrado.

Funcionamento
O programa utiliza um menu com quatro opções:

Cadastrar medicamento – permite informar o nome, a categoria e a quantidade do medicamento.

Listar medicamentos – mostra todos os medicamentos cadastrados.

Buscar medicamento – procura um medicamento pelo nome, sem diferenciar letras maiúsculas e minúsculas.

Sair – salva os dados e encerra o programa.

Principais funções
carregar() – lê os medicamentos do arquivo CSV e coloca os dados em uma lista.

salvar(lista) – grava os medicamentos da lista no arquivo medicamentos.csv.

cadastrar(lista) – recebe os dados de um novo medicamento e adiciona à lista.

listar(lista) – exibe todos os medicamentos cadastrados.

buscar(lista) – procura um medicamento pelo nome e exibe suas informações.

menu() – controla o funcionamento do sistema e apresenta as opções ao usuário.

Armazenamento dos dados
Os medicamentos são armazenados como listas contendo três informações:

[Nome, Categoria, Quantidade]

Por exemplo:

[Dipirona, Analgésico, 20]

Esses dados são gravados no arquivo CSV no seguinte formato:

Dipirona,Analgésico,20

O programa também trata a situação em que o arquivo ainda não existe. Nesse caso, ele inicia com uma lista vazia.

Tecnologias utilizadas
Python

Biblioteca csv

Arquivo CSV para armazenamento dos dados