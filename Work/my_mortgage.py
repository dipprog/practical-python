
principal = 165000.0
rate = 0.069
payment = 7990
total_paid = 0

month_number = 0

while principal > 0:
    month_number = month_number + 1
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment
    print(month_number, round(total_paid, 2), round(principal, 2))

if principal < 0:
    total_paid = total_paid - abs(principal)

print('Total paid', round(total_paid, 1))
print('Months', month_number)
