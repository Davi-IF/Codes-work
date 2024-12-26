
n = float(input("Digite um número para calcular a raiz quadrada: "))

b = 2.0

p = (b + (n / b)) / 2.0

while abs((b * b) - n) >= 0.0001:
    b = p  
    p = (b + (n / b)) / 2.0  

print(f"A raiz quadrada aproximada de {n:.4f} é {b:.4f}")
