# media contains the Class definition for Movie
# fresh_tomatoes renders the html page for the movies care of udacity
# could also use from media import Movie to avoid long path - ie Movie vs media.Movie
import media
import fresh_tomatoes

# create movie instances
star_wars = media.Movie(
    "Star Wars",
    "Young Skywalker lived a long time ago in a galaxy far, far away...but is making a comeback",
    "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
    "https://youtu.be/sGbxmsDFVnE")
                        
braveheart = media.Movie(
    "Braveheart",
    "An epic adventure about a great Scottish warrior leader",
    "https://upload.wikimedia.org/wikipedia/en/5/55/Braveheart_imp.jpg",
    "https://youtu.be/nMft5QDOHek")

bourne_identity = media.Movie(
    "The Bourne Identity",
    "An unwitting assassin tries to reclaim his identity in this spy thriller",
    "https://upload.wikimedia.org/wikipedia/en/a/ae/BourneIdentityfilm.jpg",
    "https://youtu.be/cD-uQreIwEk")

hangover = media.Movie(
    "The Hangover",
    "A cheeky comedy about a Vegas bachelor party gone wrong",
    "https://upload.wikimedia.org/wikipedia/en/b/b9/Hangoverposter09.jpg",
    "https://youtu.be/tcdUhdOlz9M")

something_about_mary = media.Movie(
    "There's Something About Mary",
    "A man attempts to win his high school obsession with hilarious results",
    "https://upload.wikimedia.org/wikipedia/en/d/df/There%27s_Something_About_Mary_POSTER.jpg",
    "https://youtu.be/eGjXwDYpOLE")

beverly_hills_cop = media.Movie(
    "Beverly Hills Cop",
    "A detroit cop takes on Beverly Hills in this action comedy",
    "https://upload.wikimedia.org/wikipedia/en/a/a2/Beverly_Hills_Cop.jpg",
    "https://youtu.be/7aYmBrXyISA")

# Create a movies list for input to fresh_tomatoes.py
movies = [star_wars, braveheart, bourne_identity, hangover, something_about_mary, 
          beverly_hills_cop]

# Use fresh_tomatoes.py to create the html page with the movies
fresh_tomatoes.open_movies_page(movies)

