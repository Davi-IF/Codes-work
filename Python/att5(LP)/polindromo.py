
num = int(input("Digite um número: "))

original = num
reversed_num = 0

while num != 0:
    remainder = num % 10            
    reversed_num = reversed_num * 10 + remainder  
    num = num // 10                

if original == reversed_num:
    print(f"{original} é um número palíndromo.")
else:
    print(f"{original} não é um número palíndromo.")
