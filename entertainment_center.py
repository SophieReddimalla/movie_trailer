"""
It creates movie list and sends it to open bowser to display it.
"""
import fresh_tomatoes
import media
# pylint: disable=invalid-name
# TODO:storyline is accepted but not displayed the screen.
# Use image_base_url to reduce the size of the url
image_base_url = "https://upload.wikimedia.org/wikipedia/en"
# Toy Story : movie title, storyline, poster image, toy story trailer
mv_toy_story = media.Movie(
    "Toy Story",
    "A story about a boy and his toys that came to life",
    image_base_url + "/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc&t=7s")

# Avatar : movie title, storyline, poster image, avatar trailer
mv_avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    image_base_url + "/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=d1_JBMrrYw8")

# Angry birds : movie title, storyline, poster image, angry birds trailer
mv_angry_birds = media.Movie(
    "The Angry Birds Movie",
    "A story of flightless birds on Bird Island",
    image_base_url + "/f/f9/The_Angry_Birds_Movie_poster.png",
    "https://www.youtube.com/watch?v=QRmKa7vvct4")

# Madagascar : movie title, storyline, poster image, madagascar trailer
mv_madagascar = media.Movie(
    "Madagascar"
    "An escape from the zoo.",
    image_base_url + "/3/36/Madagascar_Theatrical_Poster.jpg",
    "https://www.youtube.com/watch?v=dm-eiFVtRws")

# Ratatoullie : movie title, storyline, poster image, ratatoullie trailer
mv_ratatoullie = media.Movie(
    "Ratatoullie",
    "He's dying to become a chef.",
    image_base_url + "/5/50/RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=c3sBBRxDAqk")

# Finding Dory : movie title, storyline, poster image, finding dory trailer
mv_finding_dory = media.Movie(
    "Finding Dory",
    "Adventures of Dory",
    image_base_url + "/3/3e/Finding_Dory.jpg",
    "https://www.youtube.com/watch?v=0tkLUap7oGQ")

# Create a list of movies.
movies = [mv_toy_story,
          mv_avatar,
          mv_angry_birds,
          mv_madagascar,
          mv_ratatoullie,
          mv_finding_dory]

# Display list of movies
fresh_tomatoes.open_movies_page(movies)
