print("Welcome to the tip calculator!")
bill = float(input("what is the total of the bill? $"))
tip = int(input("How much would you like to tip? 15, 18, or 20?"))
people = int(input("How many people to split the bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
total = round(bill_per_person, 2)
total = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${total} Dollars!")

