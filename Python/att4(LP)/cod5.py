def main():
  
    kwh = float(input("Enter the amount of kWh consumed: "))
    type = input("Enter the type of installation (R for Residential, C for Commercial, I for Industrial): ").upper()

    if type == 'R':  # Residencial
        if kwh <= 500:
            price = kwh * 0.40
        else:
            price = kwh * 0.65
    elif type == 'C':  # Comercial
        if kwh <= 1000:
            price = kwh * 0.55
        else:
            price = kwh * 0.60
    elif type == 'I':  # Industrial
        if kwh <= 5000:
            price = kwh * 0.55
        else:
            price = kwh * 0.60
    else:
        print("Invalid installation type!")
        return  

    # Saída do resultado
    print(f"The total amount to pay is: R$ {price:.2f}")

# Chamada da função principal
if __name__ == "__main__":
    main()
