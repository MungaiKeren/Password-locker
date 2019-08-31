#!/usr/bin/env python3.6
from user import User

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

# # displaying all contacts
# def display_contacts():
#     '''
#     function that returns all saved contacts
#     '''
#     return Contact.display_contacts()