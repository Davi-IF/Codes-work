salary = float(input("type the salary:"))

if salary > 1250:
    increase = salary + (salary * 0.10)
    new_salary = increase
else:
    increase = salary + (salary * 0.15)
    new_salary = increase

print(f"new salary: {new_salary}")

