
dividend = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))
 
 
 
if divisor == 0:
        print("Erro: Divisão por zero não é permitida.")
else:
        quotient = 0
        remainder = dividend

        while remainder >= divisor:
            remainder -= divisor  
            quotient += 1          


        print(f"O quociente é: {quotient}")
        print(f"O resto da divisão é: {remainder}")
