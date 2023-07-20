# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0

month_number = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    month_number = month_number + 1

    if (month_number >= extra_payment_start_month) and (month_number <= extra_payment_end_month):
        ep = extra_payment
    else:
        ep = 0

    principal = principal * (1 + rate / 12) - payment - ep
    total_paid = total_paid + payment + ep
    print(f'{month_number:>4d} {total_paid:10.2f} {principal: 10.2f}')

if principal < 0:
    total_paid = total_paid - abs(principal)

print('Total paid', round(total_paid, 1))
print('Months', month_number)
