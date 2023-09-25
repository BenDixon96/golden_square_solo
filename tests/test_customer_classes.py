from lib.customer_classes import *
from unittest.mock import Mock
import pytest

def test_dish():
    my_dish = Dish("roast chicken", 11.50)
    assert my_dish.name == "roast chicken"
    assert my_dish.price == 11.50


roast_chicken = Dish("roast chicken", 11.50)
burger = Dish('burger', 10.50)
fries = Dish('fries', 5.25)
onion_rings = Dish('onion rings', 6.00)
milk_shake = Dish('milk shake', 3.50)
menu = [roast_chicken, burger, fries, onion_rings, milk_shake]

def test_order_show_menu():
    an_order = Order(menu)
    assert an_order.show_menu() == "roast chicken 11.50 burger 10.50 fries 5.25 onion rings 6.00 milk shake 3.50"

def test_add_to_order():
    my_order = Order(menu)
    my_order.add_dish(roast_chicken)
    assert my_order.order == [roast_chicken]
    
def test_adding_not_on_menu():
    my_order = Order(menu)
    with pytest.raises(Exception) as e:
        my_order.add_dish("pork")
    error_message = str(e.value)
    assert error_message == "sorry not on the menu"    

def test_add_multiple_dishes():
    my_order = Order(menu)
    my_order.add_dish(roast_chicken, 2)
    assert my_order.order == [roast_chicken, roast_chicken]


def test_total_cost():
    my_order = Order(menu)
    my_order.add_dish(roast_chicken, 2)
    assert my_order.grand_total() == 23
    
def test_show_my_order():
    my_order = Order(menu)
    my_order.add_dish(roast_chicken, 2)
    my_order.add_dish(burger)
    assert my_order.show_my_order() == "your order: 2 roast chicken: 23.00 1 burger: 10.50 total cost: 33.50 would you like to add anything else?"
    