# Recebendo a idade como entrada
idade = int(input("Digite a idade: "))

# Classificando a idade
if idade <= 10:
    print('Criança')
elif idade >= 18:  # No need to check idade > 10 since we already know it's not <= 10
    print('Adulto')
else:
    print('Adolescente')