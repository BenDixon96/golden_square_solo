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

def test_remove_dish():
    my_order = Order(menu)
    my_order.add_dish(roast_chicken, 2)
    my_order.add_dish(burger)
    my_order.remove_dish(roast_chicken)
    assert my_order.order == [roast_chicken, burger]

def test_remove_multiple_dishes():
    my_order = Order(menu)
    my_order.add_dish(roast_chicken, 2)
    my_order.add_dish(burger)
    my_order.remove_dish(roast_chicken, 2) 
    assert my_order.order == [burger]
    
def test_clear_my_order():
    my_order = Order(menu)
    my_order.add_dish(roast_chicken, 2)
    my_order.add_dish(burger)
    my_order.clear_order()
    assert my_order.order == []



def test_order_tracker():
    my_order_tracker = Order_tracker()
    assert my_order_tracker.my_order == []

def test_order_tracker_veiw_oder():
    requester_mock = Mock()
    response_mock = Mock()
    my_order_tracker = Order_tracker(requester_mock)
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"datetime":"2023-09-26T11:09:54.412327+01:00"}
    mock_order = Mock()

    mock_order.order = [roast_chicken, burger, fries]
    my_order_tracker.make_order(mock_order)
    assert my_order_tracker.my_order == [roast_chicken, burger, fries]


def test_order_tracker_veiw_oder_with_mock():
    requester_mock = Mock()
    response_mock = Mock()
    my_order_tracker = Order_tracker(requester_mock)
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"datetime":"2023-09-26T11:09:54.412327+01:00"}
    mock_order = Mock()
    mock_order.grand_total.return_value = 27.25
    mock_order.order = [roast_chicken, burger, fries]
    my_order_tracker.make_order(mock_order)
    assert my_order_tracker.show_order() == "your most recent order was made at 11:09 on 2023-09-26: order: 1 roast chicken: 11.50 1 burger: 10.50 1 fries: 5.25 total cost: 27.25 thank you your order it should arrive by 11:39"    

def test_order_tracker_with_order():
    requester_mock = Mock()
    response_mock = Mock()
    my_order_tracker = Order_tracker(requester_mock)
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"datetime":"2023-09-26T11:09:54.412327+01:00"}
    my_order = Order(menu)
    my_order.add_dish(roast_chicken, 2)
    my_order.add_dish(burger)
    my_order_tracker.make_order(my_order)
    assert my_order_tracker.show_order() == "your most recent order was made at 11:09 on 2023-09-26: order: 2 roast chicken: 23.00 1 burger: 10.50 total cost: 33.50 thank you your order it should arrive by 11:39"

def test_get_time():
    requester_mock = Mock()
    response_mock = Mock()
    my_order_tracker = Order_tracker(requester_mock)
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"datetime":"2023-09-26T11:09:54.412327+01:00"}
    my_order_tracker._get_order_time()
    assert my_order_tracker.order_time == ["2023-09-26", "11:09"]

def test_dont_make_an_order_when_one_is_outstanding():
    my_order = Order(menu)
    my_order.add_dish(roast_chicken, 2)
    my_order.add_dish(burger)
    another_order = Order(menu)
    another_order.add_dish(burger)
    requester_mock = Mock()
    response_mock = Mock()
    my_order_tracker = Order_tracker(requester_mock)
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"datetime":"2023-09-26T11:09:54.412327+01:00"}
    my_order_tracker.make_order(my_order)
    my_order_tracker.make_order(another_order)
    assert my_order_tracker.my_order == [roast_chicken, roast_chicken, burger]

def test_eta():
    
    requester_mock = Mock()
    response_mock = Mock()
    my_order_tracker = Order_tracker(requester_mock)
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"datetime":"2023-09-26T11:09:54.412327+01:00"}
    my_order = Order(menu)
    my_order.add_dish(roast_chicken, 2)
    my_order.add_dish(burger)
    my_order_tracker.make_order(my_order)
    my_order_tracker._get_eta()

    assert str(my_order_tracker.eta) == '11:39:00'

def test_order_confermed():
    requester_mock = Mock()
    response_mock = Mock()
    my_order_tracker = Order_tracker(requester_mock)
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"datetime":"2023-09-26T11:09:54.412327+01:00"}
    my_order = Order(menu)
    my_order.add_dish(roast_chicken, 2)
    my_order.add_dish(burger)
    assert my_order_tracker.make_order(my_order) == "thank you your order it will arrive by 11:39"
    


     

