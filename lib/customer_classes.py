



#As a customer
#  So that I can check if I want to order something
#  
#  I would like to see a list of dishes with prices.
#
#   class menu 
#   class dish
#     
#
#   As a customer
#
#
#   So that I can order the meal I want
#
#   I would like to be able to select some number of several available dishes.

#   As a customer
#   So that I can verify that my order is correct
#   I would like to see an itemised receipt with a grand total.

#   Use the twilio-python package to implement this next one. You will need to use mocks too.
#
#   As a customer
#   So that I am reassured that my order will be delivered on time
#   I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.
#  
#
#
#
#    class dish- this will include the name and price of the dish
#
class Dish():
    def __init__(self, name, price):
        self.name = name
        self.price = price
#
#  class order: this will have a list dishes it could also have the  function 
#
#   has function, show menu contains a list of dishes
#
#   has function make add to order takes 2 arguments a dish and a number(to show quantity)
#   if the order is not on the menu it will return an error message 
#   
#   has a function show me my order; 
# #returns a list of added items, there price and the total price 
#  
#   has a function make order 
#    this will change a bool value order_made from false to true and will recored the time of  
#   the order
#
#   class order tracker will contain a log of previous orders and when they where made
#   
#
# 
#      
roast_chicken = Dish("roast chicken", 11.50)
burger = Dish('burger', 10.50)
fries = Dish('fries', 5.25)
onion_rings = Dish('onion rings', 6.00)
milk_shake = Dish('milk shake', 3.50)
my_menu = [roast_chicken, burger, fries, onion_rings, milk_shake]





class Order():
    def __init__(self, menu):
        self.menu = menu
        self.order = []
        self.order_placed = False    
    def show_menu(self):
        res = ""
        for i in self.menu:
            res += i.name
            res += " "
            res += '{:.2f}'.format(i.price)
            res += ' '
        return res[:-1]   
    def add_dish(self, dish, amount=1):
        if dish not in self.menu:
            raise Exception("sorry not on the menu")
        else:
            for i in range(0, amount):
                self.order.append(dish)
    def grand_total(self):
        total = 0
        for i in self.order:
            total += i.price
        return total                
    def show_my_order(self):
        check = []
        result = {}
        total_cost = self.grand_total()
        string_cost = "{:.2f}".format(total_cost)
        res = "your order: "
        for i in self.order:
            if i not in check:
                check.append(i)
                num_of_dish = self.order.count(i)
                item_cost = num_of_dish * i.price
                name_of_dish = i.name
                res += str(num_of_dish) 
                res += " "
                res += name_of_dish
                res += ": "
                res += "{:.2f}".format(item_cost)
                res += " "
        return res + f'total cost: {string_cost} would you like to add anything else?'
    

                
        
        







    

