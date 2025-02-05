TAMANHO = 15

def main():
    A = []
    soma = 0
    
    print(f"Digite os elementos da matriz {TAMANHO}x{TAMANHO}:")
    for i in range(TAMANHO):
        linha = list(map(int, input().split()))
        if len(linha) != TAMANHO:
            raise ValueError(f"Cada linha deve conter exatamente {TAMANHO} elementos.")
        A.append(linha)
    
    for i in range(TAMANHO):
        if isinstance(A[i][i], int) and A[i][i] % 2 == 0:
            soma += A[i][i]
    
    print(f"Soma dos elementos pares na diagonal principal: {soma}")

if __name__ == "__main__":
    main()
