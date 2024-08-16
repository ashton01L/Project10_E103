# Author: Ashton Lee
# Github User: ashton01L
# Date: 8/14/2024
# Description: First, define a class named 'Movie' that has four data members:
# '_title', '_genre', '_director', and '_year'.
# Next define a class named 'StreamingService' that has two data members:
# '_name' and '_catalog'.
# Lastly, define a class named 'StreamingGuide' that has one data member,
# '_streaming_services', which will be a list of 'StreamingService' objects.
class Movie:
    def __init__(self, title, genre, director, year):
        """
        Initialize a Movie object with title, genre, director, and year.
        """
        self._title = title
        self._genre = genre
        self._director = director
        self._year = year

    def get_title(self):
        """
        Return the title of the movie.
        """
        return self._title

    def get_genre(self):
        """
        Return the genre of the movie.
        """
        return self._genre

    def get_director(self):
        """
        Return the director of the movie.
        """
        return self._director

    def get_year(self):
        """
        Return the release year of the movie.
        """
        return self._year


class StreamingService:
    def __init__(self, name):
        """
        Initialize a StreamingService object with a name and an empty catalog.
        """
        self._name = name
        self._catalog = {}

    def get_name(self):
        """
        Return the name of the streaming service.
        """
        return self._name

    def get_catalog(self):
        """
        Return the catalog of movies.
        """
        return self._catalog

    def add_movie(self, movie):
        """
        Adds a Movie object to the catalog.
        The movie title is used as the key in the catalog dictionary.
        """
        self._catalog[movie.get_title()] = movie

    def delete_movie(self, title):
        """
        Removes a Movie from the catalog by title.
        """
        if title in self._catalog:
            del self._catalog[title]


class StreamingGuide:
    def __init__(self):
        """
        Initialize a StreamingGuide object with an empty list of streaming services.
        """
        self._streaming_services = []

    def add_streaming_service(self, service):
        """
        Add a StreamingService object to the list of streaming services.
        """
        self._streaming_services.append(service)

    def delete_streaming_service(self, service_name):
        """
        Remove a StreamingService from the list by name.
        """
        self._streaming_services = [
            service for service in self._streaming_services if service.get_name() != service_name
        ]

    def where_to_watch(self, title):
        """
        Find which streaming services have the movie with the given title.
        Returns a list where the first element is a string of the movie title
        concatenated with its year in parentheses, and the rest are the names of
        streaming services that have the movie. If the movie is not available on
        any service, return None.
        """
        result = None
        for service in self._streaming_services:
            catalog = service.get_catalog()
            if title in catalog:
                movie = catalog[title]
                if result is None:
                    result = [f"{movie.get_title()} ({movie.get_year()})"]
                result.append(service.get_name())

        return result if result else None

# Example data
movie_1 = Movie('The Seventh Seal', 'comedy', 'Ingmar Bergman', 1957)
movie_2 = Movie('Home Alone', 'tragedy', 'Chris Columbus', 1990)
movie_3 = Movie('Little Women', 'action thriller', 'Greta Gerwig', 2019)
movie_4 = Movie('Galaxy Quest', 'historical documents', 'Dean Parisot', 1999)

stream_serv_1 = StreamingService('Netflick')
stream_serv_1.add_movie(movie_2)

stream_serv_2 = StreamingService('Hula')
stream_serv_2.add_movie(movie_1)
stream_serv_2.add_movie(movie_4)
stream_serv_2.delete_movie('The Seventh Seal')
stream_serv_2.add_movie(movie_2)

stream_serv_3 = StreamingService('Dizzy+')
stream_serv_3.add_movie(movie_4)
stream_serv_3.add_movie(movie_3)
stream_serv_3.add_movie(movie_1)

stream_guide = StreamingGuide()
stream_guide.add_streaming_service(stream_serv_1)
stream_guide.add_streaming_service(stream_serv_2)
stream_guide.add_streaming_service(stream_serv_3)
stream_guide.delete_streaming_service('Hula')

search_results = stream_guide.where_to_watch('Little Women')
print(search_results)  # Output: ['Little Women (2019)', 'Dizzy+']