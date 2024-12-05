def main():
   
    v_house = float(input("Type the value of the house: "))
    salary = float(input("Type the salary: "))
    yearsp = int(input("Type the payment period in years: "))

    
    months = yearsp * 12
    prest = v_house / months
    max_prest = salary * 0.30

    
    if prest <= max_prest:
        print("Loan allowed!")
    else:
        print("Loan not allowed!")


if __name__ == "__main__":
    main()
