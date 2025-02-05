def main():
    A = input("Type first phrase: ")
    B = input("Type second phrase: ")

  
    A = ''.join(['*' if char.lower() == 'a' else char for char in A])

  
    B = ''.join(['*' if char.lower() == 'a' else char for char in B])

   
    print("Reversed first phrase:", A[::-1])

    
    print("Reversed second phrase:", B[::-1])

if __name__ == "__main__":
    main()
