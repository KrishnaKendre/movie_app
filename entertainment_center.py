import media
import view

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "http://vignette4.wikia.nocookie.net/disney/images/4/4c/Toy-story-movie-posters-4.jpg/revision/latest?cb=20140816182710",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4"
                        "2hr")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     "https://www.movieposter.com/posters/archive/main/98/MPW-49246",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8"
                     "3hr")

movies = [toy_story, avatar]

view.open_movies_page(movies)

