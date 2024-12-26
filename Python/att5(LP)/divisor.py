
num = int(input("tpe a number: "))

prime = True

if num <= 1:
    prime = False  
elif num == 2:
    prime = True  
else:
   
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            prime = False  
            break  

if prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} isn't a prime number.")
