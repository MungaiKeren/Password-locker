#!/usr/bin/env python3.6
from user import User
from credentials import Credentials


# creating an acount
def create_user(fname,sname,password):
    '''
    function to create a new user account
    '''
    new_user = User(fname,sname,password)
    return new_user

# saving user
def save_user(user):
    '''
    Function to save our user details
    '''
    user.save_user()

# delete user
def del_account(user):
    '''
    Function that deletes a user acoount
    '''
    user.delete_account()

# finding a user by first name
def find_user(first_name):
    '''
    Function that finds user by their first name and returns their first name
    '''
    return User.find_by_fname(first_name)

# checking if a user exists
def user_existance(first_name):
    '''
    Function that checks if a user exist and returns a boolean
    '''
    return User.user_exist(first_name)

# displaying users
def display_users():
    '''
    Function that does actual display of users
    '''
    return User.display_user()

## main function
def main():
    print("Welcome to passlock, to login please enter your name and password")

    user_name = input()
    password = str(input())

    print(f"Welcome {user_name}!")

    while True:
        print("Use this short codes: VC - to view users NC - to name a new account and store its password AC - to see a list of your accounts")

        short_code = input().upper()

        if short_code == 'NC'
            print("New app:")

            print("App name:")
            app = input()
            
            print("App password")
            app_password = input()

            
     

#             save_contacts(create_contact(first_name,last_name,phone_number,email_address)) # create and save new contact
#             print('/n')
#             print(f"New Contact {first_name} {last_name} created")
#             print('/n')

#         elif short_code == 'dc':
#             if display_contacts():
#                 print("Here is a list of all your contacts")
#                 print('/n')

#                 for contact in display_contacts():
#                     print(f"{contact.first_name}{contact.last_name} .....{contact.phone_number}")
                    
#                     print('/n')
#             else:
#                     print('/n')
#                     print("You don't seem to have any ontacts saved yet")
#                     print('/n')
#         elif short_code == 'fc':
#                 print("Enter the number you want to search for")
#                 search_number  = input()

#                 if checking_if_contact_exists(search_number):
#                     search_contact = find_contact(search_number)
#                     print(f"{search_contact.first_name}{search_contact.last_name}")
#                     print("-"*20)

#                     print(f"Phone number.....{search_contact.phone_number}")
#                     print(f"Email address....{search_contact.email}")
#                 else :
#                     print("That contact does not exist")
#         elif short_code == 'ex':
#             print("Bye....")
#             break
#         else :
#             print("I really didn't get that contact.Please use shortcodes")
