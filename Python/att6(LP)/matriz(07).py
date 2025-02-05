
linhas = 4
colunas = 5


matriz = []


print("Digite 20 elementos para a matriz (4 linhas e 5 colunas):")
for i in range(linhas):
    linha = []  
    for j in range(colunas):
        elemento = int(input(f"Elemento [{i+1}][{j+1}]: "))  
        linha.append(elemento)  
    matriz.append(linha)  


print("\nMatriz 4x5 inserida:")
for linha in matriz:
    print(" ".join(map(str, linha)))  
