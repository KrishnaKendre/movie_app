import webbrowser


class Video():
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration


class Movie(Video):
    """ This class provides a way to store movie related information """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, duration):
        Video.__init__(self, movie_title, duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


# Example of Inheritance in python
class ShowRating(Movie):
    def __init__(self):
        self.VALID_RATINGS = Movie.VALID_RATINGS
