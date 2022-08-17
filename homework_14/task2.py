"""Write a decorator that takes a list of stop words and replaces them with * inside the decorated function"""


def stop_words(words: list):
    def wrapper(func):
        def string(name):
            string_example = str(func(name))
            for word in words:
                if word.lower() in string_example.lower():
                    string_example = string_example.replace(word, '*')
            return string_example
        return string
    return wrapper


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f'{name} drinks pepsi in his brand new BMW!'


if __name__ == '__main__':
    print(create_slogan('Vadym'))