def calculate_tip(bill_amount, tip_percentage):
    tip = bill_amount * ( tip_percentage / 100)
    total_bill = bill_amount + tip
    return tip, total_bill

bill_amount = float(input("Enter the bill amount: $"))
tip_percentage = float(input("Enter the tip percentage (e.g., 15, 20): "))

tip, total_bill = calculate_tip(bill_amount, tip_percentage)

print(f"Tip Amount: ${tip:-2f}")
print(f"Total Bill: ${total_bill:-2f}")