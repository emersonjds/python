import math  # Importa a biblioteca para arredondamento


# Inicializa a lista para armazenar os números
numeros = []

# Loop para ler os números do usuário
while True:
    valor = int(input())
    if valor == -1:  # Condição de parada
        break
    numeros.append(valor)

# Verifica se a lista contém elementos antes de processar os cálculos
if numeros:
    quantidade = len(numeros)
    soma = sum(numeros)
    media = math.ceil(soma / quantidade)  # Arredonda a média para cima
    maior = max(numeros)
    menor = min(numeros)
    
    # Conta quantos números são maiores que a média
    maiores_que_media = sum(1 for num in numeros if num > media)

    # Exibe os resultados
    print(f"A quantidade de números na lista: {quantidade}")
    print(f"A soma dos números da lista: {soma}")
    print(f"A média considerando os valores na lista: {media}")
    print(f"O maior número da lista: {maior}")
    print(f"O menor número da lista: {menor}")
    print(f"Quantos números da lista são maiores que a média: {maiores_que_media}")
else:
    print("Nenhum número válido foi inserido.")
