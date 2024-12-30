def tabuada(option, number):
    
    for i in range(1,11):
        match option:
            case 1:
                print(f"{number} + {i} = {number + i}")
            case 2:
                print(f"{number} - {i} = {number - i}")
            case 3:
                print(f"{number} x {i} = {number * i}")
            case 4:
                if i != 0:
                     print(f"{number} x {i} = {number / i:.2f}")
                else:
                    print("impossible")
            case _:
                 print("invalid")

def main ():
    op = 0

    while op != 5:
        print("MENU:\n")
        print("1 - addition\n")
        print("2 - subtraction\n")
        print("3 - multiplication\n")
        print("4 - division\n")
        print("5 - exit\n")

        op = int(input(" type the option:"))

        if op == 5:
              print("exiting...")
        elif op >= 1 and op<=4:
            num = int(input("type number to see the table:"))

            tabuada(op, num)
        else:
            print("invalid, try again...")
        
if __name__ == "__main__":
    main()
        
              