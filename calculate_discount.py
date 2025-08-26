def calculate_discount(price, disc):
    if disc >= 20:
        Discount = price * disc / 100
        finalprice = price - Discount
        return finalprice 
    else:
     return price 
    #getting the input 
price = float(input("Enter your price "))
disc = float(input("Enter the discount "))
final_price = calculate_discount(price,disc)   

if final_price == price:
    print("No discount.Price:",price)
else:
    print ("Final price and discount is:",final_price)