"""
Video
Create classes following this UML: see picture in github

Note that the method info() should be different in the different classes where it should be implemented.

Use the following code to test your program:
pokemon = TV_serie("Pokemon", "Cartoon", 4.5, 550)
titanic = Movie("Titanic", "Romance", 4.7, 194)
code = Documentary("The Code", "Math", 4)

for video in tuple((pokemon, titanic, code)):
    print(video.info())

An example output could be:
TV series with title Pokemon, genre Cartoon, rating 4.5 and episodes 550
Movie with title Titanic, genre Romance, rating 4.7, duration 194 minutes
Video with title The Code, genre Math and rating 4
"""


class Video:
    def __init__(self, title: str, genre: str, rating: float) -> None:
        self.title = title
        self.genre = genre # changed from gender to genre to be able to work
        self.rating = rating

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception(f"Please use string and not{type(value)}")
        self._title = value

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        if not isinstance(value, str):
            raise Exception(f"Please use string and not {type(value)}")
        self._genre = value

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if not isinstance(value, (int, float)):
            raise Exception(f"Pleas use int or float and not {type(value)}")
        self._rating = value

    def info(self) -> str:
        return f"Video with title {self.title}, genre {self.genre} and rating {self.rating}"


class TvSerie(Video):  # changed to TvSerie to follow convention
    def __init__(self, title: str, genre: str, rating: float, num_episodes: int) -> None:
        super().__init__(title, genre, rating)
        self.num_episodes = num_episodes

    def info(self) -> str:
        return f"TV series with title {self.title}, genre {self.genre}, rating {self.rating} and episodes {self.num_episodes}"


class Movie(Video):
    def __init__(self, title: str, genre: str, rating: float, duration: float) -> None:
        super().__init__(title, genre, rating)
        self.duration = duration

    def info(self) -> str:
        return f"Movies with title {self.title}, genre {self.genre}, rating {self.rating} and duration {self.duration}"


class Documentary(Video):
    def __init__(self, title: str, genre: str, rating: float) -> None:
        super().__init__(title, genre, rating)


# Use this code for test the program
pokemon = TvSerie("Pokemon", "Cartoon", 4.5, 550)  # change to follow convention for TvSerie
titanic = Movie("Titanic", "Romance", 4.7, 194)
code = Documentary("The Code", "Math", 4)


for video in tuple((pokemon, titanic, code)):
    print(video.info())  # remove print to get rid of None if print is already in methods but if return print is needed here
