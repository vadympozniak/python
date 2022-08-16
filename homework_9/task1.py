"""A simple function.
Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie.
The function should then print “My favorite movie is named {name}”."""


def favorite_movie(name):
    string = f'My favorite movie is named {name}'
    return string


if __name__ == '__main__':
    print(favorite_movie('The Color of Pomegranates'))
