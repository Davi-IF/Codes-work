a = int(input("type the number a:"))
b = int(input("type the number b:"))
op = (input("select option (+) (-) (*) (/)"))

if op == '+':
    sum = a + b
    print(f"result: {sum}")

elif op == '-':
    sub = a - b
    print(f"result: {sub}")

elif op == '*':
    mult = a * b
    print(f"result: {mult}")

elif op == '/':
    if a != 0:
        div = a / b
        print(f"result: {div}")
    else:
        print("division isn't allowed!")
else:
    print("invalid")


