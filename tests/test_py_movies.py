"""
Tests the Movie class
"""

from py_movies.py_movies import PyMovies


def test_instantiation():
    # This is just an example, please feel free to remove this test to fit your
    # needs
    pm = PyMovies("API_KEY_HERE")
    assert pm.api_key == "API_KEY_HERE"
