from beers_movies import beers
from beers_movies import movies

while True:
    read = int(input('Welcome to the bar. Your age:\n'))
    if read >= 18:
        print('You have come to the right place. Here are our brands:')
        for element in beers:
            print(element)
    elif read < 18:
        print('This is no place for a', read, 'year old. How about seeing a movie?')
        for element in movies:
            print(element)


