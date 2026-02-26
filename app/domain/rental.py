from __future__ import annotations

from app.domain.movie import Movie


class Rental:
    def __init__(self, movie: Movie, days_rented: int):
        self._movie = movie
        self._days_rented = days_rented

    @property
    def days_rented(self):
        return self._days_rented

    @property
    def movie(self):
        return self._movie

    @movie.setter
    def movie(self, movie: Movie):
        self._movie = movie

    @days_rented.setter
    def days_rented(self, value):
        self._days_rented = value

    def get_charge(self):
        this_amount = 0
        if self.movie.price_code == Movie.REGULAR:
            this_amount += 2
            if self.days_rented >2:
                this_amount += (self.days_rented - 2) *1.5

        elif self.movie.price_code == Movie.NEW_RELEASE:
            this_amount += self.days_rented * 3
        elif self.movie.price_code == Movie.CHILDRENS:
            this_amount += 1.5
            if self.days_rented > 3:
                this_amount += (self.days_rented -3) *1.5
        return this_amount
