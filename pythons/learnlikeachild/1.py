#pizzasolutions
no_of_pizza = int(input("eneter the number of pizza you wanted"))
cost_per_pizza =int(256)
total_cost_of_pizza = no_of_pizza*cost_per_pizza
tax = int(0.08)
print(f"the total price of the pizza is :{total_cost_of_pizza} and \n")
print("the total price of the pizza including vat", total_cost_of_pizza + tax)
