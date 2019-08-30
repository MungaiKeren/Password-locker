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
if __name__ == '__main__':
    unittest.main()

