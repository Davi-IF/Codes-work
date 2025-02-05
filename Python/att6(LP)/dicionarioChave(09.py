def gerar_dicionario_indices(frase):
    dicionario = {}
    for i, char in enumerate(frase):
        if char not in dicionario:  
            dicionario[char] = i
    return dicionario


frase = "O rato"
resultado = gerar_dicionario_indices(frase)
print(resultado)
