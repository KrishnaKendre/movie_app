import media
import view

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "http://vignette4.wikia.nocookie.net/disney/images/4/4c/Toy-story-movie-posters-4.jpg/revision/latest?cb=20140816182710", # NOQA
                        "https://www.youtube.com/watch?v=vwyZH85NQC4",
                        "2hr")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     "https://www.movieposter.com/posters/archive/main/98/MPW-49246", # NOQA
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8",
                     "3hr")

pokemon = media.Movie("Pokemon: The First Movie",
                     "Scientists genetically create a new Pokemon,"
                     " Mewtwo, but the results are horrific and disastrous.",
                     "http://vignette2.wikia.nocookie.net/toonami/images/9/9c/Pokemon_the_First_Movie.jpg/revision/latest?cb=20130913155508", # NOQA
                     "https://www.youtube.com/watch?v=dUaELbAqKLY",
                     "1hr")

matrix = media.Movie("The Matrix",
                     "A computer hacker learns from mysterious rebels"
                     " about the true nature of his reality and his role in the war"
                     " against its controllers.",
                     "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg", # NOQA
                     "https://www.youtube.com/watch?v=vKQi3bBA1y8",
                     "2hr")

avengers = media.Movie("Avengers: Age of Ultron",
                     "When Tony Stark and Bruce Banner try"
                     " to jump-start a dormant peacekeeping program called Ultron,"
                     " things go horribly wrong and it's up to Earth's Mightiest Heroes"
                     " to stop the villainous Ultron from enacting his terrible plans.",
                     "http://t0.gstatic.com/images?q=tbn:ANd9GcRlGeugacRkKznDOtRhUCVt0AkrOTPbaaKwF9xgGZgNViyC_Xko", # NOQA
                     "https://www.youtube.com/watch?v=QPNnSfdBhtI",
                     "2hr")

dory = media.Movie("Finding Dory",
                     "The friendly-but-forgetful blue tang fish begins"
                     " a search for her long-lost parents, and everyone"
                     " learns a few things about the real meaning of family along the way.",
                     "http://ia.media-imdb.com/images/M/MV5BNzg4MjM2NDQ4MV5BMl5BanBnXkFtZTgwMzk3MTgyODE@._V1_SY1000_CR0,0,674,1000_AL_.jpg", # NOQA
                     "https://www.youtube.com/watch?v=cxskm6dDfIY",
                     "1hr")                 

movies = [toy_story, avatar, pokemon, matrix, avengers, dory]

view.open_movies_page(movies)

