# coding: utf-8 

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
for i in range(20):
    print(data_list[i])

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]
input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
for i in range(1,21): #coloquei 21 para incluir a 20 linha com dados 
    print(f'linha{i}:',data_list[i][6])


# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem

"""
    Extrai uma coluna específica de uma lista de listas.

    Argumentos:
        data: Lista de listas, onde cada sublista representa uma linha de dados.
        index: Índice da coluna que deve ser extraída.

    Retorna:
        Uma lista contendo os valores da coluna especificada, extraída de cada linha dos dados.
"""

def column_to_list(data, index):
    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    for linha in data: # a data é uma lista de lista, o index é a posicao da coluna 
        column_list.append(linha[index]) #insere cada coluna 
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1048575, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
male = 0
female = 0

for linha in data_list:
    if linha[6] == 'Male':
       male = male + 1
    if linha[6] == 'Female':
        female = female + 1
        
        
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 665437 and female == 198247, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)

"""
    Conta a quantidade de usuários do sexo masculino e feminino na base de dados.

    Argumentos:
        data_list: Lista de listas, onde cada sublista representa uma linha da base de dados.
                   A informação de gênero é esperada na posição de índice 6.

    Retorna:
        Uma lista com dois valores inteiros:
            - O número total de usuários do sexo masculino (índice 0).
            - O número total de usuários do sexo feminino (índice 1).
"""

def count_gender(data_list):
    male = 0
    female = 0
    for linha in data_list:
        if linha[6] == 'Male':
            male = male + 1
        if linha[6] == 'Female':
            female = female + 1
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 665437 and count_gender(data_list)[1] == 198247, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.

"""
    Determina qual gênero é mais comum na base de dados.

    Argumentos:
        data_list: Lista de listas, onde cada sublista representa uma linha da base de dados.
                   A informação de gênero deve estar na posição de índice 6.

    Retorna:
        Uma string indicando o gênero mais frequente:
            - "Male" se houver mais usuários do sexo masculino,
            - "Female" se houver mais usuários do sexo feminino,
            - "Equal" se ambos os gêneros tiverem a mesma quantidade.
"""


def most_popular_gender(data_list):
    male, female = count_gender(data_list)
            
    if male > female: 
        answer = "Male"
    elif female > male:
        answer = "Female"
    else: 
        answer = "Equal"
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
"""
    Conta a quantidade de usuários por tipo de assinatura na base de dados.

    Argumentos:
        data_list: Lista de listas, onde cada sublista representa uma linha da base de dados.
                   A informação do tipo de usuário (Customer ou Subscriber) está no índice 5.

    Retorna:
        Uma lista com dois valores inteiros:
            - O número total de usuários do tipo "Customer" (índice 0).
            - O número total de usuários do tipo "Subscriber" (índice 1).
"""


def count_usertype(data_list):
    customer = 0
    subscribe = 0
    dependent = 0
    for linha in data_list:
        if linha[5] == 'Customer':
            customer = customer + 1
        elif linha[5] == 'Subscriber':
            subscribe = subscribe + 1
        elif linha[5] == 'Dependent':
            dependent = dependent+ 1 
    return [customer, subscribe, dependent]

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Customer", "Subscriber", "Dependent"]
quantity = count_usertype(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo de Usuário')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo de Usuário')
plt.show(block=True)


input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque algumas linhas estão com a coluna gênero vazia"
print("resposta:", answer)

nulo = 0

for linha in data_list:
    if linha[6] == '':
       nulo = nulo + 1

        
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Nulos: ", nulo)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)

min_trip = converted_trip_duration_list[0]
max_trip = converted_trip_duration_list[0]
mean_trip = 0.
median_trip = 0.

converted_trip_duration_list = []
for trip in trip_duration_list:
    converted_trip_duration_list.append(float(trip))

#Média
mean_trip = sum(converted_trip_duration_list)/len(converted_trip_duration_list)

#Minimo
for trip in converted_trip_duration_list:
    if trip < min_trip:
        min_trip = trip

#Máximo
for trip in converted_trip_duration_list:
    if trip > max_trip:
        max_trip = trip

#Mediana
lista_ordenada = sorted(converted_trip_duration_list)
tamanho_lista = len(converted_trip_duration_list)
    
if tamanho_lista % 2 == 0:  # Par
    meio1 = lista_ordenada[tamanho_lista // 2 - 1]
    meio2 = lista_ordenada[tamanho_lista // 2]
    median_trip = (meio1 + meio2) / 2
else:  # Impar
    meio = lista_ordenada[tamanho_lista // 2]
    median_trip = meio


print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min:", min_trip, "Max: ", max_trip, f"Média: {mean_trip:.2f}", "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 885, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 624, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_statitons_list = []

for lista in range(len(data_list)):
    start_statitons_list.append(data_list[lista][3])
    

start_stations = set(start_statitons_list)

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 578, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
"""
      Função de exemplo com anotações.
      Argumentos:
          param1: O primeiro parâmetro.
          param2: O segundo parâmetro.
      Retorna:
          Uma lista de valores x.

"""

input("Aperte Enter para continuar...")
# TAREFA 12
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
### FIZ COM A AJUDA DO CHATGPT
def count_items(data_list, index):
    """
    Conta a frequência de cada item único presente em uma coluna específica da base de dados.

    Argumentos:
        data_list: Lista contendo as entradas dos dados. Cada entrada é uma sublista.
        index: O índice da coluna na qual você deseja contar os itens únicos.

    Retorna:
        Uma tupla contendo duas listas:
            - A primeira com os itens únicos encontrados na coluna.
            - A segunda com o número de ocorrências de cada item.
    """
    # Extraímos a coluna desejada com base no índice
    column_list = [linha[index] for linha in data_list]
    
    item_types = list(set(column_list))  # Encontra os itens únicos
    count_items = []

    # Conta quantas vezes cada item aparece na coluna
    for item in item_types:
        count = column_list.count(item)
        count_items.append(count)

    return item_types, count_items

# Verificação para continuar com a tarefa
if answer == "yes":
    # Testando a função com o tipo de usuário (coluna 5)
    types, counts = count_items(data_list, 5)  # Alterar o índice para o que você quiser contar

    # Exibindo o resultado
    print("Tipos encontrados:", types)
    print("Contagem de itens:", counts)


    
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1048575, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------
