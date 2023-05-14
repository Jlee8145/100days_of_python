age = input("What is your current age? ")

weeks = 52 * (90 - int(age))
days = 365 * (90 - int(age))
months = 12 * (90 - int(age))

print(f"You have {days} days, {weeks} weeks and {months} months left.")
