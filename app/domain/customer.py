from __future__ import annotations

from .movie import Movie
from .rental import Rental


class Customer:
    def __init__(self, name: str):
        self._name = name
        self._rentals: list[Rental] = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def rentals(self) -> list[Rental]:
        return self._rentals

    @name.setter
    def name(self, name: str):
        self._name = name

    @rentals.setter
    def rentals(self, rentals: list[Rental]):
        self._rentals = rentals

    def add_rental(self, arg: Rental):
        self._rentals.append(arg)

    def statement(self) -> str:
        total_amount = 0.0
        frequent_renter_points = 0

        rentals = iter(self._rentals)

        result = "Record for " + self._name + "\n"
        for each in rentals:
            this_amount = 0.0

            this_amount = each.get_charge()

            frequent_renter_points +=1

            if (each.movie.price_code == Movie.NEW_RELEASE) and each.days_rented > 1 :
                frequent_renter_points += 1
            result += "\t" + each.movie.title + "\t" + str(this_amount) + "\n"

            total_amount += this_amount
        result += "Amount owed is " + str(total_amount) + "\n"
        result += "you earned" + str(frequent_renter_points) +"frequent renter point "

        return  result

    def amont_for_current_rental(self, aRental: Rental):
        return  aRental.get_charge()
