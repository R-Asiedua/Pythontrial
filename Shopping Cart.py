#This is a simple shopping cart. The user will be able to add and remove items to their cart, view the contents of their cart,and calculate the total cost of their items
shopping_cart=[]
while True:
    print('Options')
    print('1. Add Items to Cart')
    print('2. Remove Item from Cart') 
    print('3. View Cart')
    print('4. Calculate Total Cost')
    print('5. Quit')

    choice= input('Enter the option you want: ')
    if choice== "1":
        item_name= input('Please enter the name of the product: ')
        item_price= input('Please enter the price of the product: ')
        shopping_cart.append({"name":item_name, "price":item_price})
    elif choice== "2":
        item_name= input('Please enter the name of the item you want to remove: ')
        for item in shopping_cart:
            if item["name"]== item_name:
                shopping_cart.remove(item)
                print(f"{item_name} was removed")
                break
    elif choice== "3":
        print(shopping_cart)
    elif choice== "4":
        total_cost= sum(int(item["price"]) for item in shopping_cart)
        print(total_cost)
    elif choice== "5":
        print('Exiting the shopping cart application')
        break