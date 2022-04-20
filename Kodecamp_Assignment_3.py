print("Welcome to Oyebi's Groceries Store")
# Initializing an empty dictionary to hold the available products and price in the Store
product_list = dict()
#Setting the dictionary functions. Use 'product' as key and 'price' as value
print("\nSet key as Product and value as Price")
product_key= input("Enter the 'Product' as key:  ")
price_value = input("Enter the 'Price' as value:   ")
# requesting for user input to generate products and price for the products
print("\nFor Staff only: Welcome to your portal")
print('\nEnter a product and price at a time separated by space')
product_list[product_key] = [price_value]
store_products=dict(input().split() for i in range(20))
#generate the content of the store_products
print('These are the available products in the store and their prices: \n\t', store_products)
#confirm the data type of the item in the variable store_products if same is a dictionary.
print(type(store_products))

print("\nWelcome to Oyebi's Groceries Store Customer Booking Lot")
#allow user to access the groceries available in the stall.
#Requesting for customer's name
customer = input('Enter your name:   ')
#for name in range(len(customer)):
print(customer,  "you are welcome to Oyebi's Groceries Store")
for product, price in store_products.items():
    product =input('Enter a product of your choice:    ')
    print("\nEnter 'quit' to end your order")
    if product == 'quit':
        break
    elif product in store_products:
        print(product, 'is available and the price is:', store_products[product], 'naira')
    else:
        print(product, 'is not available, please make a new order')
        
#products and prices used for testing
  #GoldenMorn 500
#St.Luis 300
#GoldenPenny 350
#Ariel 100
#Pepsodent 400
#SupremeIceCream 400
#Dano 500
#Milo 500
#Alwayspad 300
#Kiss Kid 500
#Snickers 400
#Digestive 300
#Ever Fresh:350
#Chicken 1000
#Carrot 150
#Veleta 1000
#SoulMate 200
#OralB 400
#Dabur 400
