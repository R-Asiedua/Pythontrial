#This is a calculator for a shop. It calculates the total and average prices and also compares prices.
print("AZUBI STORE")
products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]
prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]
#the variable last_week represents the number of customers that purchased products last week.
mean = round(sum(prices)/len(prices),2)
print("The Total Price Average for all Products in the Store is: $",mean)
#reduced each price by $5 and created a new price list
new_pricelist = [ price - 5 for price in prices ]
print("The New Price List (reduced by $5) is: ",new_pricelist)
#total average revenue generated from the products
total_revenue = sum(price * customers for price, customers in zip(prices, last_week))
print("Total Revenue Generated from the Products (using new prices) is: $", total_revenue)
# assuming the revenue was generated over 7 days
days = 7
average_daily_revenue = total_revenue / days
print("Average Daily Revenue Generated from the Products is: $", average_daily_revenue)
# Created an empty list to store products with prices less than $30
products_less_than_30 = []
for i in range(len(products)):
    if new_pricelist[i] < 30:
        products_less_than_30.append(products[i])
print("Products with Prices Less than $30 based on New Prices:")
print(products_less_than_30)