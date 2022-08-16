"""Extend Phonebook application
Functionality of Phonebook application:
Add new entries
Search by first name
Search by last name
Search by full name
Search by telephone number
Search by city or state
Delete a record for a given telephone number
Update a record for a given telephone number
An option to exit the program

The first argument to the application should be the name of the phonebook.
Application should load JSON data, if it is present in the folder with application,
else raise an error. After the user exits, all data should be saved to loaded JSON."""

import json
import os

try:
    if not os.path.isfile('phonebook.json'):
        raise OSError

    with open('phonebook.json', 'r') as file:
        data = file.read()
        data_json = json.loads(data)


    def phonebook_func():
        answer = 0
        while answer != '9':
            answer = input("""
            Functionality:
            '1' — Add new entries
            '2' — Search by first name 
            '3' — Search by last name 
            '4' — Search by full name
            '5' — Search by telephone number
            '6' — Search by city
            '7' — Delete a record
            '8' — Update a record
            '9' — Exit
            Enter number: """)

            if answer == '1':
                print('Add new entries')
                first_name = input("First name : ")
                last_name = input("Last name: ")
                city = input("City: ")
                telephone_number = input("Telephone number: ")

                data_json['phonebook'].append({
                    "first_name": first_name,
                    "last_name": last_name,
                    "city": city,
                    "telephone_number": telephone_number
                })
                print('Entries added')

            elif answer == '2':
                search_first_name = input("Enter the first name you want to find: ")
                find_first_name = 0
                for name in data_json['phonebook']:
                    if search_first_name == name['first_name']:
                        find_first_name += 1
                        print(f'Contacts with this first name:')
                        print(f'№{find_first_name} {name}')
                if find_first_name == 0:
                    print('Contacts with this first name not found')

            elif answer == '3':
                search_last_name = input("Enter the last name you want to find: ")
                find_last_name = 0
                for name in data_json['phonebook']:
                    if search_last_name == name['last_name']:
                        find_last_name += 1
                        print(f'Contacts with this last name:')
                        print(f'{find_last_name} {name}')
                if find_last_name == 0:
                    print('Contacts with this last name not found')

            elif answer == '4':
                search_full_name = input("Enter the full name you want to find: ")
                find_full_name = 0
                for name in data_json['phonebook']:
                    if search_full_name == f'{name["first_name"]} {name["last_name"]}' \
                            or search_full_name == f'{name["last_name"]} {name["first_name"]}':
                        find_full_name += 1
                        print(f"Contacts with this full name:")
                        print(f'{find_full_name} {name}')
                if find_full_name == 0:
                    print('Contacts with this full name not found')

            elif answer == '5':
                search_telephone_number = input("Enter the telephone number you want to find: ")
                find_telephone_number = 0
                for name in data_json['phonebook']:
                    if search_telephone_number == name['telephone_number']:
                        find_telephone_number += 1
                        print(f"Contacts with this telephone number:")
                        print(f'{find_telephone_number} {name}')
                if find_telephone_number == 0:
                    print('Contacts with this telephone number not found')

            elif answer == '6':
                search_city = input("Enter the city you want to find: ")
                find_city = 0
                for name in data_json['phonebook']:
                    if search_city == name['city']:
                        find_city += 1
                        print(f"Contacts with this city:")
                        print(f'{find_city} {name}')
                    if find_city == 0:
                        print('Contacts with this city not found')

            elif answer == '7':
                delete_telephone_number = input("Enter the telephone number of the contact you want to delete: ")
                for name in data_json['phonebook']:
                    if delete_telephone_number == name['telephone_number']:
                        data_json['phonebook'].remove(name)
                print('Entries deleted')

            elif answer == '8':

                search_for_change_phone = input('Enter the telephone number of the contact you want to update: ')
                change_first_name = input("First name: ")
                change_last_name = input("Last name: ")
                change_city = input("City: ")
                change_telephone_number = input("Telephone number: ")

                for name in data_json['phonebook']:
                    if search_for_change_phone == name['phone_number']:
                        name["first_name"] = change_first_name
                        name["last_name"] = change_last_name
                        name["city"] = change_city
                        name["telephone_number"] = change_telephone_number
                print('Entries updated')

            elif answer == '9':
                with open('phonebook.json', 'w') as file:
                    json.dump(data_json, file, ensure_ascii=False, indent=4)
                break

            answer_end = input('Would you like to continue? Enter a number from 1 to 8, Quite — number 9: ')
            if answer_end == '9':
                with open('phonebook.json', 'w') as file:
                    json.dump(data_json, file, ensure_ascii=False, indent=4)
                break


    phonebook_func()
    print(data_json)

except OSError as error_text:
    print('File not found')
