# Recebendo nome e idade do usuário
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

# Verificando se o usuário é adulto
if idade >= 18:
    print(f"{nome} é adulto")
else:
    print(f"{nome} não é adulto")