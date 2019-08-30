import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours.
    '''    
    new_user = User("Keren","Mungai","kayren12345")

    def setUp(self):
        '''
        setup method that runs before each test cases
        '''
        self.new_user = User("Keren","Mungai","kayren12345")
    def tearDown(self):
        '''
        teardown method that lean up after each test case has run
        '''
        User.user_details = []
    # test to check whether user is initialized correctly
    def test_init(self):
        '''
        test to check whether user is initialized correctly
        '''
        self.assertEqual(self.new_user.first_name,"Keren")
        self.assertEqual(self.new_user.second_name,"Mungai")
        self.assertEqual(self.new_user.password,"kayren12345")
    # test to check whether our user details have been saved
    def test_save_user(self):
        '''
        test that checks whether our user details have been saved
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_details),1)
    # deleting user
    def test_delete_user(self):
        '''
        test to check whether a user can delete account
        '''
        self.new_user.save_user()
        test_user = User("Keren","Mungai","kayren12345")
        test_user.save_user

        self.new_user.delete_account()
        self.assertEqual(len(User.user_details),1)
    # checking if user exists
    def test_user_exists(self):
        '''
        checks if user exists by password. returns a boolean if user doesn't exist
        '''
        self.new_user.save_user()
        test_user = User("Testname","Testsecondname","kayren12345")
        test_user.save_user()

        user_exists = User.user_exist("kayren12345")

        self.assertTrue(user_exists)


if __name__ == '__main__':
    unittest.main()

#    def test_contact_exists(self):
        # '''
        # test to check if we can return a Boolean  if we cannot find the contact.
        # '''

        # self.new_contact.save_contact()
        # test_contact = Contact("Test","user","0711223344","test@user.com") # new contact
        # test_contact.save_contact()

        # contact_exists = Contact.contact_exist("0711223344")

        # self.assertTrue(contact_exists)