bill = float(input("What was the total bill? £"))
people = int(input("How many people are splitting the bill"))
tip = int(input("What percentage tip would you like to give? "))

total_bill = bill*(1 + tip/100)
per_person = total_bill / people
print(f"Each person should pay: £{per_person:.2f}")