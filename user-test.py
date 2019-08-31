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
        self.assertEqual(len(User.user_details),0)


    # checking if user exists
    def test_user_exists(self):
        '''
        checks if user exists by password. returns a boolean if user doesn't exist
        '''
        self.new_user.save_user()
        test_user = User("Keren","Testsecondname","kayren12345")
        test_user.save_user()

        user_exists = User.user_exist("Keren")

        self.assertTrue(user_exists)

    # test that finds user by first_name
    def test_find_user_by_firstname(self):
        '''
        test to find user by first name
        '''

        self.new_user.save_user()
        test_user = User("Keren","Mungai","kayren12345")
        test_user.save_user()

        found_user = User.find_by_fname("Keren")

        self.assertEqual(found_user.first_name,test_user.first_name)
    # test that displays users
    def display_user(self):
        '''
        Test that displays users
        '''
        self.assertEqual(User.display_user(),User.user_details)
if __name__ == '__main__':
    unittest.main()