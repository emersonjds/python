import numpy as np # type: ignore

# Implemente uma função que retorne os valores das chaves de um dicionário em uma lista
def DictToList(dict):
    valores = list()  # Inicializa uma lista vazia

    for v in dict:
        valores.append(dict.get(v))  # Obtém o valor da chave v e adiciona à lista

    return valores

faturamento = {
    "01/01/2023": 5500,
    "02/01/2023": 8850,
    "03/01/2023": 10500,
    "04/01/2023": 6010,
    "05/01/2023": 4500,
    "06/01/2023": 11000,
    "07/01/2023": 1260
}

lista_faturamento = DictToList(faturamento)

# Imprima a soma dos valores contidos em lista_faturamento usando uma função do NumPy
print(np.sum(lista_faturamento))