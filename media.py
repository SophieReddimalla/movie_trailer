"""
Media.py Classes for Movie Trailer Website
"""

import webbrowser
class Movie:
    """
    Basic Movie Class
    """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_link):
        self.title               = movie_title
        self.storyline           = movie_storyline
        self.poster_image_url    = poster_image
        self.trailer_youtube_url = trailer_link
    def show_trailer(self):
        """
        Open an window to display video of the trailer
        """
        webbrowser.open(self.trailer_youtube_url)


        
        
