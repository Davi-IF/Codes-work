
C = input("Digite o valor de C: ")[0] 
P = int(input("Digite o valor de P: "))
S = input("Digite uma palavra: ")


if P < 0 or P >= len(S):
    print("Erro: P está fora do limite da string.")
else:
    encontrado = False  


    for i in range(P, len(S)):
        if S[i] == C:
            print(f"Caractere encontrado na posição [{i}]")
            encontrado = True
            break

  
    if not encontrado:
        print(f"Caractere '{C}' não encontrado após a posição {P}.")
