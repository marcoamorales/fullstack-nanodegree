import fresh_tomatoes
import media

# Instantiate the objects which will be sent to fresh_tomatoes.py
toy_story = media.Movie('Toy Story',
                        'A story of a boy and his toys that come to life',
                        'https://upload.wikimedia.org/wikipedia/en/1/13/'
                        'Toy_Story.jpg',
                        'https://www.youtube.com/watch?v=KYz2wyBy3kc')

avatar = media.Movie('Avatar',
                     'Modern Pocahontas',
                     'https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/'
                     'Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg',
                     'https://www.youtube.com/watch?v=5PSNL1qE6VY')

lion_king = media.Movie('Lion King',
                        'A story about maturing and growing in Africa',
                        'https://upload.wikimedia.org/wikipedia/en/thumb/3/'
                        '3d/The_Lion_King_poster.jpg/'
                        '220px-The_Lion_King_poster.jpg',
                        'https://www.youtube.com/watch?v=4sj1MT05lAA')

movies = [toy_story, avatar, lion_king]
fresh_tomatoes.open_movies_page(movies)
