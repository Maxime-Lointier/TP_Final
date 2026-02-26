import pytest

from app.domain.rental import Rental
from app.domain.movie import Movie

movie = Movie("Jujutsu Kaisen",0)
def test_should_succed_when_given_valid_state():
    #act
    rental = Rental(movie,5)
    #arrage
    expected = movie
    #assert
    assert rental.movie == expected