import time
import requests
from twilio.rest import Client

from datetime import datetime

import datetime
a = datetime.datetime(100,1,1,11,34,59)
from datetime import datetime
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
#   has function clear order
#
#   has a function place oder this will 
#    
#     class customer, keeps a phomne number
#   
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



########### these are obviously not my details but it does work ################################
account_sid = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token  = "XXxxxxxxxXXXXXXXXXXXXXXXXXXXXXXXXX" 





class Order():
    def __init__(self, menu):
        self.menu = menu
        self.order = []

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
    def remove_dish(self, dish, amount=1):
            for i in range(0, amount):
                self.order.remove(dish)
    def clear_order(self):
        self.order = []            
        
        


class Order_tracker():
    def __init__(self, request=None, my_phone_number="+44##########", rest_phone_number="44###########"):
        self.my_order = []
        self.total_for_order = 0
        eta = 0
        self.order_time = []
        self.receipts = {}
        self.request = request
        self.eta = 0
        self.oustanding_order = False
        self.my_phone_number = my_phone_number
        self.rest_phone_number = rest_phone_number
    def make_order(self, order, deliverytime=30):
        if self.my_order != []:
            self.receipts[f'order made on {self.order_time[0]} was made at {self.order_time[1]}'] = [self.show_order()[63:-47], f'should arrive at {self.eta}'[:-3]]
            self.order_time = []
            self.eta = 0
            self.my_order = []
        self.my_order = order.order
        self.total_for_order = order.grand_total()
        self._get_order_time()
        self._get_eta(deliverytime)
        self.oustanding_order = False
        result = f'thank you your order it will arrive by {str(self.eta)[0:5]}'
        this_client = Client(account_sid, auth_token)
        message = this_client.messages.create(
        to=self.my_phone_number,
        from_=self.rest_phone_number,
        body=result)
        print(message.sid)
        return result 

    def show_order(self):
        res = f'your most recent order was made at {self.order_time[1]} on {self.order_time[0]}: order: '
        total_cost = self.total_for_order
        string_cost = "{:.2f}".format(total_cost)
        check = []
        for i in self.my_order:
            if i not in check:
                check.append(i)
                num_of_dish = self.my_order.count(i)
                item_cost = num_of_dish * i.price
                name_of_dish = i.name
                res += str(num_of_dish) 
                res += " "
                res += name_of_dish
                res += ": "
                res += "{:.2f}".format(item_cost)
                res += " "
        return res + f'total cost: {string_cost} thank you your order it should arrive by {str(self.eta)[0:5]}'
    def _get_order_time(self):
        response = self.request.get("https://worldtimeapi.org/api/ip")
        json = response.json()
        time = json["datetime"]
        order_date = time[:10]
        order_time = time[11:16]
        self.order_time.extend([order_date, order_time])
    def _get_eta(self, deliverytime):
        import datetime
        time_change = datetime.timedelta(minutes=deliverytime)
        mins = self.order_time[1]
        from datetime import datetime
        time_of_ord = datetime.strptime(mins, "%H:%M")
        eta = time_of_ord + time_change
        self.eta = eta.time()
    def show_receipts(self):
        res = ''
        for i, x in self.receipts.items():
            res += i 
            res += ": "
            res += x[0]
            res += ' '
            res += x[1]
        return res    










    

