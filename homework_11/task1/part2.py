if __name__ == '__main__':
    try:
        with open('myfile.txt') as file:
            text = file.read()
    except FileNotFoundError:
        print('File not found')
    else:
        print(text)