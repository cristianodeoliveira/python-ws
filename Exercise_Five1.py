birthday_is_today = True
number_of_items = 10
price = 10.00

if birthday_is_today:
    price = price * 0.85
if number_of_items > 5:
    price = price * 0.95

print(price)