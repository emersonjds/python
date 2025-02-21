def validaSenha(password):
    # Verifica se a senha tem entre 5 e 15 caracteres
    if len(password) < 5 or len(password) > 15:
        return False

    # Conta a quantidade de números na senha
    num_count = sum(1 for char in password if char.isdigit())

    # Conta a quantidade de letras maiúsculas na senha
    upper_count = sum(1 for char in password if char.isupper())

    # Verifica se há pelo menos 2 números e 2 caracteres maiúsculos
    if num_count < 2 or upper_count < 2:
        return False

    return True

# Não alterar o código abaixo
myPass = input()

if validaSenha(myPass):
    print("Senha válida")
else:
    print("Senha inválida")