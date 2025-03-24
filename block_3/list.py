palestra1 = {
    "Marley Beltran",
    "Allen Black",
    "Flynn Adams",
    "Ajay Copeland",
    "Keziah Shaw",
    "Junaid Hogan",
    "Leanne Fields",
}

palestra2 = {
    "Tara Blackwell",
    "Jared Salas",
    "Samira Sykes",
    "Junaid Hogan",
    "Leanne Fields",
}

palestra3 = {
    "Flynn Adams",
    "Ajay Copeland",
    "Keziah Shaw",
    "Leanne Fields",
    "Junaid Hogan",
}

# Conjunto de pessoas que participaram de todas as palestras (interseção)
participantesAssiduos = palestra1 & palestra2 & palestra3

# Conjunto de todas as pessoas que participaram de pelo menos uma palestra (união)
participacaoGeral = palestra1 | palestra2 | palestra3

# Convertendo para lista e ordenando os nomes
participantesAssiduos = sorted(list(participantesAssiduos))
participacaoGeral = sorted(list(participacaoGeral))

# Exibindo os resultados
print("Pessoas que participaram de todas as palestras:")
for pessoa in participantesAssiduos:
    print(pessoa)

print("\nPresenca geral:")
for pessoa in participacaoGeral:
    print(pessoa)