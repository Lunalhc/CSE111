from datetime import datetime

#subtotal = float (input('Please enter the subtotal:'))

date = datetime.now()
day_of_week =datetime. weekday(date)
discount = 0 
run = True
while run:
    

if day_of_week == 1 or day_of_week == 2:
    if subtotal >= 50:
        discount = subtotal / 10

        subtotal = subtotal - discount


sales_tax = subtotal * .06

total = sales_tax + subtotal - discount

print (f"Sales tax is {sales_tax:.2f}.")

print (f"Your discount for today is {discount:.2f}")

print (f"The total for today is {total:.2f}")

input ()
