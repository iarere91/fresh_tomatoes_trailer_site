class Movie:

    """ The Movie class represents a movie and information about
    that movie, such as its title, synopsis, a user defined rating,
    a URL pointing to an image of the movie's box art, and a URL
    to the a trailer of the movie on YouTube. """

    def __init__(self, title, synopsis, rating, poster_image_url,
                 trailer_youtube_url):

        """
        __init__ is responsible for initialising the movie
        object and setting the object's attributes.

        Below is a description of each attribute and the information it
        should contain:

        'title' is the movie's title, such as "Finding Dory".
        'synopsis' is a short description of the movie's plot.
        'rating' is an integer that is between 0 and 5 (out of 5 stars)
        'poster_image_url' should be a URL to the image of the movie's box art.
        'trailer_youtube_url' is a link to a trailer of the movie on YouTube.
        """

        self.title = title
        self.synopsis = synopsis
        self.rating = rating
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
