def main():
  
    kwh = float(input("Enter the amount of kWh consumed: "))
    type = input("Enter the type of installation (R for Residential, C for Commercial, I for Industrial): ").upper()

    if type == 'R': 
        if kwh <= 500:
            price = kwh * 0.40
        else:
            price = kwh * 0.65
    elif type == 'C': 
        if kwh <= 1000:
            price = kwh * 0.55
        else:
            price = kwh * 0.60
    elif type == 'I':  
        if kwh <= 5000:
            price = kwh * 0.55
        else:
            price = kwh * 0.60
    else:
        print("Invalid installation type!")
        return  

    
    print(f"The total amount to pay is: R$ {price:.2f}")

if __name__ == "__main__":
    main()
