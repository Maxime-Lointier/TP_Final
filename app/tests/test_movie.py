import pytest
from app.domain.movie import Movie

def test_should_succes_when_creat_movie():
    #act
    movie = Movie("Diddy Comming Home",99)
    #arrage & assert
    assert movie.title == "Diddy Comming Home"

def test_should_change_the_title_when_changed():
    #act
    movie = Movie("Diddy Comming Home",99)
    #arrage
    movie.title = "Spider-Man Comming Home"
    #assert
    assert movie.title == "Spider-Man Comming Home"

def test_should_change_prize():
    #act
    movie = Movie("Diddy Comming Home",99)
    #arrage
    movie.price_code = 0
    #assert
    assert movie.price_code==0