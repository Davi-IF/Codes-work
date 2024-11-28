
price = float(input("type the price of the product:"))
discount = float(input("type the discount"))

tot_discount = price * (discount/100)
final_value = price - tot_discount

print(f"the final value: {final_value}" )
