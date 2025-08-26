def calculate_discount(price, discount_percent):
    if discount_percent >=20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price
    
price = input("Enter the price: ")
discount_percent = input("Enter the discount percentage: ")
final_price = calculate_discount(float(price), float(discount_percent))
print(f"The final price after discount is: {final_price}")