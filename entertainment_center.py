import media
import fresh_tomatoes

# Create an array to store the movie objects
movies = []

# Instantiate the movie objects and add them to the movies array
# A movie is instantiated as follows:
# Movie(title, synopsis, rating, box art image link, youtube video link)
movies.append(media.Movie(
    "Toy Story",
    """
    Woody (Tom Hanks), a good-hearted cowboy doll who belongs to
    a young boy named Andy (John Morris), sees his position as Andy's
    favorite toy jeopardized when his parents buy him a Buzz Lightyear
    (Tim Allen) action figure. Even worse, the arrogant Buzz thinks he's
    a real spaceman on a mission to return to his home planet. When Andy's
    family moves to a new house, Woody and Buzz must escape the clutches of
    maladjusted neighbor Sid Phillips (Erik von Detten) and reunite with
    their boy.
    """,
    4,
    "https://goo.gl/BmeuUz",
    "https://youtu.be/ZZv1vki4ou4"))

movies.append(media.Movie(
    "Howl's Moving Castle",
    """
    Sophie (Emily Mortimer) has an uneventful life at her late father's
    hat shop, but all that changes when she befriends wizard Howl
    (Christian Bale), who lives in a magical flying castle.
    However, the evil Witch of Waste (Lauren Bacall) takes issue with their
    budding relationship and casts a spell on young Sophie, which ages her
    prematurely. Now Howl must use all his magical talents to battle the
    jealous hag and return Sophie to her former youth and beauty.
    """,
    3,
    "https://goo.gl/4eG2d9",
    "https://youtu.be/iwROgK94zcM"))

movies.append(media.Movie(
    "Shawshank Redemption",
    """
    Andy Dufresne (Tim Robbins) is sentenced to two consecutive life
    terms in prison for the murders of his wife and her lover and is sentenced
    to a tough prison. However, only Andy knows he didn't commit the crimes.
    While there, he forms a friendship with Red (Morgan Freeman), experiences
    brutality of prison life, adapts, helps the warden, etc., all in 19 years.
    """,
    5,
    "https://goo.gl/pnwbSb",
    "https://youtu.be/6hB3S9bIaco"))

movies.append(media.Movie(
    "Harry Potter and the Philosopher's Stone",
    """
    Adaptation of the first of J.K. Rowling's popular children's novels
    about Harry Potter, a boy who learns on his eleventh birthday that he is
    the orphaned son of two powerful wizards and possesses unique magical
    powers of his own. He is summoned from his life as an unwanted child
    to become a student at Hogwarts, an English boarding school for wizards.
    There, he meets several friends who become his closest allies and help
    him discover the truth about his parents' mysterious deaths.
    """,
    4,
    "https://goo.gl/BnUVoM",
    "https://youtu.be/VyHV0BRtdxo"))

movies.append(media.Movie(
    "Star Wars - Return of the Jedi",
    """
    Luke Skywalker (Mark Hamill) battles horrible Jabba the Hut and cruel
    Darth Vader to save his comrades in the Rebel Alliance and triumph over the
    Galactic Empire. Han Solo (Harrison Ford) and Princess Leia (Carrie Fisher)
    reaffirm their love and team with Chewbacca, Lando Calrissian
    (Billy Dee Williams), the Ewoks and the androids C-3PO and R2-D2 to aid
    in the disruption of the Dark Side and the defeat of the evil emperor.
    """,
    4,
    "https://goo.gl/8U3ZgW",
    "https://youtu.be/MYD_xxY5wEI"))

movies.append(media.Movie(
    "Lord of the Rings - Return of the King",
    """
    The culmination of nearly 10 years' work and conclusion to Peter Jackson's
    epic trilogy based on the timeless J.R.R. Tolkien classic, "The Lord of
    the Rings: The Return of the King" presents the final confrontation
    between the forces of good and evil fighting for control of the future
    of Middle-earth. Hobbits Frodo and Sam reach Mordor in their quest to
    destroy the `one ring', while Aragorn leads the forces of good against
    Sauron's evil army at the stone city of Minas Tirith.
    """,
    5,
    "https://goo.gl/x7cqxJ",
    "https://youtu.be/WIrRJ8bCZYQ"))

# Call to open_movies_page function in fresh_tomatoes to generate HTML file
# Pass in the list of movie objects, which is the array called 'movies'
fresh_tomatoes.open_movies_page(movies)
