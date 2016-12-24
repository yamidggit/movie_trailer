"""
This module contains a Python Movie class which will be used in the
entertainment_center.py module to create a list of movies objects. Each object 
has the following data: movie_title, movie_poster_image_url and 
movie_trailer_youtube_url. 

"""

class Movie():
    
    # the __init__method is the constructor of the class which constructs space 
    # and memory for the new instances of the Movie class called Objects
    
    def __init__(self, movie_title, movie_poster_image_url, movie_trailer_youtube_url):
        self.title=movie_title
        self.poster_image_url=movie_poster_image_url
        self.trailer_youtube_url=movie_trailer_youtube_url

        