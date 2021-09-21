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
    def __init__(self, title: str, gender: str, rating: float) -> None:
        self.title = title
        self.gender = gender
        self.rating = rating
    
    def info(self) -> str:
        pass


class TV_serie:
    #def __super__()
    def __init__(self, title: str, genre: str, rating: float, num_episodes: int) -> None:
        self.title = title
        self.genre = genre
        self.rating = rating
        self.num_episodes = num_episodes

    def info(self) -> str:
        pass


class Movie:
    def __init__(self, title: str, genre: str, rating: float, duration: float) -> None:
        self.title = title
        self.genre = genre
        self.rating = rating
        self.duration = duration

    def info(self) -> str:
        pass


class Documentary:
    def __init__(self, title: str, genre: str, rating: float) -> None:
        self.title = title
        self.genre = genre
        self.rating = rating


"""
Use this code for test the program
pokemon = TV_serie("Pokemon", "Cartoon", 4.5, 550)
titanic = Movie("Titanic", "Romance", 4.7, 194)
code = Documentary("The Code", "Math", 4)

for video in tuple((pokemon, titanic, code)):
    print(video.info())
"""