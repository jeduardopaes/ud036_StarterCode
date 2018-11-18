""" Script to produce a movies website
this code will create a website displaying the movies created below.

Modules used:
    media - contains the class Movie,
    fresh_tomatoes - contains the code that builds the HTML page
"""

import media
import fresh_tomatoes


# Creating Homefront movie
homefront = media.Movie("Homefront",
                        "Cop moves with his kid to a new city to get a" +
                        "fresh start, but things get complicated once a" +
                        "local drugs dealer finds out.",
                        "https://images-na.ssl-images-amazon.com/images/I/91RPYFInHqL._SL1500_.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=uLz2nTYjCFg")

# Creating Willy Wonka & the chocolate factory movie
willy_wonka = media.Movie("Willy Wonka & the chocolate factory",
                          "Fantasy factory and beautiful movie.",
                          "https://secure.img2-fg.wfcdn.com/im/56351951/compr-r85/4026/40261677/willy-wonka-willy-wonka-framed-graphic-art-print-poster.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=2cBja3AbahY")

# Creating The Internship movie
the_internship = media.Movie("The Internship",
                             "Internship at google is never easy," +
                             "but always fun.",
                             "https://motionpictureart.com/wp-content/uploads/2018/02/InternshipMovieBannerPosterDutch.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=jir62_ptloI")

# Creating Dr. Strange movie
dr_strange = media.Movie("Dr. Strange",
                         "Marvel movie, Cumberbach, what else do you need?",
                         "https://vignette.wikia.nocookie.net/marvelcinematicuniverse/images/5/5e/Doctor_Strange_IMAX_poster.jpg/revision/latest?cb=20161013190301",  # NOQA
                         "https://www.youtube.com/watch?v=HSzx-zryEgM")

# Creating The Killing Joke movie
the_killing_joke = media.Movie("The Killing Joke",
                               "Batman, Joker, DC at it's finest.",
                               "https://vignette.wikia.nocookie.net/batman/images/2/2f/KillingJokeCartoon.jpg/revision/latest?cb=20160602154448",  # NOQA
                               "https://www.youtube.com/watch?v=ZQTqu1_iQkw")

# Creating Batman: Under the red hood movie
batman_under_the_red_hood = media.Movie("Batman: Under the red hood",
                                        "Joker kills robin, there is no way" +
                                        "it's gonna end there.",
                                        "https://m.media-amazon.com/images/M/MV5BYTdlODI0YTYtNjk5ZS00YzZjLTllZjktYmYzNWM4NmI5MmMxXkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_.jpg",  # NOQA
                                        "https://www.youtube.com/watch?v=A2c9MsP3OVs")  # NOQA

# Creating the list with all the movies
movies = [the_killing_joke, dr_strange, willy_wonka, the_internship, homefront,
          batman_under_the_red_hood]

# Calling the method from fresh_tomatoes wich creates web page
fresh_tomatoes.open_movies_page(movies)
