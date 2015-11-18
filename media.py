import webbrowser

class Movie(object):
    """ This class provides a way to store movie related information
    
        Attributes:
            title: The movie's title.
            storyline: The movie's storyline.
            poster_image_url: The movie's poster_image_url.
            trailer_youtube_url: The movie's trailer_youtube_url.
    """
    # this is an example of a class variable - it's available to all instances
    # the google style guide recommends all caps for these
    VALID_MOVIE_RATINGS = ["G", "PG", "PG 13", "R"]
    
    # this is the constructor for class Movie()...it runs every time an object
    # is instantiated
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        # these are the attributes of the class or instance variables
        # self refers to whatever object is instantiated
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    
    # this is an example of a class method accessed via object.showtrailer()
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)