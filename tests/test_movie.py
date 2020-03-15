"""
Tests the Movie class
"""

from py_movies.movie import Movie


def test_title():
    # This is just an example, please feel free to remove this test to fit your
    # needs
    m = Movie("test")
    assert m.title == "test"
