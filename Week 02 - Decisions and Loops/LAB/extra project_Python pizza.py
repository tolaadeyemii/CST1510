size = input("What size pizza do you want? Small, Medium, or Large: ")
pepperoni = input("Do you want pepperoni? Yes or No: ")
extra_cheese = input("Do you want extra cheese? Yes or No: ")
if size == "Small":
    bill = 15

elif size == "Medium":
    bill = 20

else:
    bill = 25

if pepperoni == "Yes":
    if size == "Small":
        bill = bill + 2
    else:
        bill = bill + 3
if extra_cheese == "Yes":
    bill = bill + 1

print(f"Your final bill is: ${bill}.")