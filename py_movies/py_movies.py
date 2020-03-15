""" Python Movies Library

"""

from .movie import Movie


class PyMovies():
    """ A library class with some helpful movie functions.

    """

    def __init__(self, api_key):
        """
        Instantiate the PyMovies library with the OMDB API key
        """
        self.api_key = api_key

    def lookup_movie(self, movie_id):
        """ NOT IMPLEMENTED: Lookup and returns movie object if found
        """

        # hint: use the api key to make an http call to the OMDB API
        # then instantiate a movie object with the results and return a Movie
        return Movie("random title")
