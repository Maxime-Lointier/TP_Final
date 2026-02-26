import pytest
from app.domain.customer import Customer
from app.domain.rental import Rental

def test_should_succed_when_create():
    #act
    customer = Customer("Maxrani")

    #arrage & assert
    assert customer.name == "Maxrani"

def test_should_return_list_when_ask():
    #act
    customer = Customer("Maxrani")
    #arrage & assert
    assert type(customer.rentals) == list

def test_should_return_length_of_list_when_add():
    #act
    customer = Customer("Maxrani")
