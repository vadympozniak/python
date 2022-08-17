"""Custom exception
Create your custom exception named `CustomException`, you can inherit from base Exception class,
but extend its functionality to log every error message to a file named `logs.txt`.
Tips: Use __init__ method to extend functionality for saving messages to file"""


class CustomException(Exception):
    def __init__(self, message):
        self.message = message

        try:
            if int(message) > 0:
                print('The entered number is greater than zero')
            elif int(message) < 0:
                print('The entered number is less than zero')
            elif int(message) == 0:
                print('The entered number is zero')
            else:
                raise Exception('Enter the number.')

        except Exception as err_message:
            try:
                with open('logs.txt', 'a') as file:
                    file.write(f'{str(err_message)} \n')
            except PermissionError:
                print('The file is write-protected.')


if __name__ == '__main__':
    my_file = CustomException(1)