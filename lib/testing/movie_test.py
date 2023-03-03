import pytest

from lib.Movie import Movie

class TestMovie:
    '''Movie in movie.py'''

    def test_has_title(self):
        '''has the title passed into __init__.'''
        movie = Movie(title="Avatar: The Way of Water")
        assert movie.title == "Avatar: The Way of Water"

    def test_requires_nonzero_string_title(self):
        '''requires titles to be strings of >0 characters.'''
        with pytest.raises(Exception):
            Movie(title=1)
        with pytest.raises(Exception):
            Movie(title="")
    
    def test_has_reviews(self):
        '''contains an instance attribute, reviews, a list of its reviews.'''
        movie = Movie(title="Scarface")
        assert hasattr(movie, "reviews")
        assert isinstance(movie.reviews, list)

    def test_has_reviewers(self):
        '''contains an instance attribute, reviewers, a list of its viewers who left reviews.'''
        movie = Movie(title="Rashomon")
        assert hasattr(movie, "reviewers")
        assert isinstance(movie.reviewers, list)

    def test_calculates_average_rating(self):
        '''has a method "average_rating" that returns the average of self.reviews.'''
        movie = Movie(title="My Neighbor Totoro")
        movie.reviews = [1, 3, 2, 4, 5, 4, 2]
        assert movie.average_rating() == 3

    def test_shows_highest_rated(self):
        '''has a method "highest_rated" that returns the highest rated movie.'''
        Movie.all = []
        movie_1 = Movie(title="Avatar: The Way of Water")
        movie_1.reviews = [1, 1, 1, 2, 3, 4, 4, 5]
        movie_2 = Movie(title="Scarface")
        movie_2.reviews = [1, 1, 1, 1, 1, 1]
        movie_3 = Movie(title="Rashomon")
        movie_3.reviews = [5, 5, 5, 5, 5, 5, 5]
        movie_4 = Movie(title="My Neighbor Totoro")
        movie_4.reviews = [4, 3, 4, 3, 2, 5, 4]
        assert Movie.highest_rated().title == "Rashomon"
