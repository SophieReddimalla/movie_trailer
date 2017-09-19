"""
It creates movie list and sends it to open bowser to display it.
"""
import fresh_tomatoes
import media
# pylint: disable=invalid-name
# TODO:storyline is accepted but not displayed the screen.
toy_story = media.Movie("Toy Story",
                        "A story about a boy and his toys that came to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc&t=7s")


avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

angry_birds = media.Movie("The Angry Birds Movie",
                          "A story of flightless birds on Bird Island",
                          "https://upload.wikimedia.org/wikipedia/en/f/f9/The_Angry_Birds_Movie_poster.png",
                          "https://www.youtube.com/watch?v=QRmKa7vvct4")

madagascar = media.Movie( "Madagascar",
                          "An escape from the zoo.",
                          "https://upload.wikimedia.org/wikipedia/en/3/36/Madagascar_Theatrical_Poster.jpg",
                          "https://www.youtube.com/watch?v=dm-eiFVtRws")

ratatoullie = media.Movie("Ratatoullie",
                          "He's dying to become a chef.",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")


finding_dory = media.Movie("Finding Dory",
                           "Adventures of Dory",
                           "https://upload.wikimedia.org/wikipedia/en/3/3e/Finding_Dory.jpg",
                           "https://www.youtube.com/watch?v=0tkLUap7oGQ")

#create a list of movies.
movies = [toy_story, avatar, angry_birds, madagascar, ratatoullie, finding_dory]

# Display list of movies
fresh_tomatoes.open_movies_page(movies)
