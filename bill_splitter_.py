print("Welcome to Bill Splitter App")

while True:
    bill_amount = float(input("Enter total bill: "))
    num_people = int(input("Enter number of people: "))
    tip_percentage = int(input("Enter tip percentage (0/5/10/15/20): "))

    if num_people <= 0:
        print("Error: Number of people must be greater than 0. Please try again.")
        print()

    elif bill_amount < 0 or tip_percentage < 0:
        print("Error: Bill amount and tip percentage cannot be negative.")
        print()

    else:
       
        tip_amount = (tip_percentage / 100) * bill_amount
        total_bill = bill_amount + tip_amount
        per_person = total_bill / num_people

        print("Tip Amount:", tip_amount)
        print("Total Bill (with Tip):", total_bill)
        print("Each person should pay:", per_person)

        again = input("Would you like to calculate another bill? (y/n): ")
        if again != 'y':
            print("\nThank you for using the Bill Splitter App!")
            break
            
    print("-" * 40)
    