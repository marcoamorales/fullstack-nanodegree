class Movie(object):
    """This class provides a way to save movie information
    """

    VALID_RATINGS = ['PG', 'PG-13', 'M']

    def __init__(self, movie_title, movie_summary, poster_url, trailer_url):
        self.title = movie_title
        self.summary = movie_summary
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url
