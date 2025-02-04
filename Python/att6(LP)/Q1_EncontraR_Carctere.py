# Solicita os inputs do usuário
C = input("Digite o valor de C: ")[0]  # Pega apenas o primeiro caractere
P = int(input("Digite o valor de P: "))
S = input("Digite uma palavra: ")

# Verifica se P está dentro dos limites da string
if P < 0 or P >= len(S):
    print("Erro: P está fora do limite da string.")
else:
    encontrado = False  # Variável para indicar se encontramos o caractere

    # Percorre a string a partir da posição P
    for i in range(P, len(S)):
        if S[i] == C:
            print(f"Caractere encontrado na posição [{i}]")
            encontrado = True
            break

    # Se o caractere não for encontrado
    if not encontrado:
        print(f"Caractere '{C}' não encontrado após a posição {P}.")
