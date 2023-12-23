#This is a tip calculator for Asanka Hotel
print("Asanka Hotel")
#Get the charge for the food from the user
price = int(input("Please enter the price of the food: $"))
#Converting the price variable to an integer variable.
tip = 0.18
salestax = 0.07
tip_calc = float(tip) * float(price)
#Since the calculated tip may have more than two decimal places, the value will be rounded to two decimal places
rounded_tip = round(tip_calc,2)
print("Tip = $",rounded_tip)
salestax_calc = float(salestax) * float(price)
#Since the calculated sales tax may have more than two decimal places, the value will be rounded to two decimal places
rounded_salestax_calc = round(salestax_calc,2)
print("Sales Tax = $",rounded_salestax_calc)
#To make all the necessary variables easily identifiable and reduce confusion, a list will be created.
variables = [price, rounded_tip, rounded_salestax_calc]
#In order to find the total price the cutomer will need to pay, all the variables in the list were added together.
total= sum(variables)
print("Grand Total = $", total)

