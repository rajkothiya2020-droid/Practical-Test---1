def calculate_bill():
    print("Welcome to the Bill Splitter App!\n")

    # 1. User Inputs & Type Casting
    try:
        bill_amount = float(input("Enter total bill amount: "))
        num_people = int(input("Enter number of people: "))
        tip_percentage = int(input("Enter tip percentage (0/5/10/15/20): "))
    except ValueError:
        print("Invalid input! Please enter numeric values.\n")
        return

    # 2. Validations using Control Structures
    if num_people <= 0:
        print("Error: Number of people must be greater than 0. Please try again.\n")
        return

    if bill_amount < 0 or tip_percentage < 0:
        print("Error: Bill amount and tip percentage cannot be negative.\n")
        return

    # 3. Calculations (Operators & Expressions)
    tip_amount = (tip_percentage / 100) * bill_amount
    final_bill = bill_amount + tip_amount
    per_person = final_bill / num_people

    # 4. Output Formatting & Display
    print(f"\nTip Amount: ₹{tip_amount:.2f}")
    print(f"Total Bill (with Tip): ₹{final_bill:.2f}")
    print(f"Each person should pay: ₹{per_person:.2f}\n")


# 5. Looping Task (Repeatable Process)
while True:
    calculate_bill()
    choice = input("Would you like to calculate another bill? (y/n): ").strip().lower()
    if choice != 'y':
        print("\nThank you for using the Bill Splitter App!")
        break
    print("-" * 40)
    