def main():
    name = input("Digite seu nome completo: ")

    
    name = name.strip()


    last_name = name.rsplit(' ', 1)

    if len(last_name) == 2:
       
        surname = last_name[1]
        first_name = last_name[0]
    else:
      
        surname = ""
        first_name = last_name[0]

  
    print(f"Nome: {first_name}")
    print(f"Sobrenome: {surname}")

if __name__ == "__main__":
    main()
