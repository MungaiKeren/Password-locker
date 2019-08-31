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







# # saving contacts
# def save_contacts(contact):
#     '''
#     Function to save contact
#     '''
#     contact.save_contact()
# # delete contact
# def del_contact(contact):
#     '''
#     function to delete contact
#     '''
#     contact.delete_contact()
# # finding a contact
# def find_contact(number):
#     '''
#     Function that finds a contact by number and returns the 
#     contact
#     '''
#     return Contact.find_by_number(number)
# # check if a contact exists
# def checking_if_contact_exists(number):
#     '''
#     function to check if a contact exists with the number and 
#     return a boolean
#     '''
#     return Contact.contact_exist(number)
# # displaying all contacts
# def display_contacts():
#     '''
#     function that returns all saved contacts
#     '''
#     return Contact.display_contacts()