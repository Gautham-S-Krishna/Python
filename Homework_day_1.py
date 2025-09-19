products = ['rice','sugar','oil']
price_of_rice = 45
price_of_sugar = 40
price_of_oil = 130
quantity_of_rice = 3
quantity_of_sugar = 2.5
quantity_of_oil = 1.8
total_price = (price_of_rice * quantity_of_rice) + (price_of_sugar * quantity_of_sugar) + (price_of_oil * quantity_of_oil)
print("The total price of your grocery is:", total_price)
# To show the total bill as an integer
print("The total price of your grocery as an integer is:", int(total_price))

# To show total bill as a string
print("The total price of your grocery as a string is:",str(total_price))
import random
delivery_charge = total_price +random.randrange(5,10)
print(f"final bill = {delivery_charge}")



