def gerar_dicionario_indices(frase):
    dicionario = {}
    for indice, caractere in enumerate(frase):
        if caractere not in dicionario:
            dicionario[caractere] = indice
    return dicionario


def main():
    frase = input("Digite uma frase: ")
    resultado = gerar_dicionario_indices(frase)
    print(resultado)


if __name__ == "__main__":
    main()
