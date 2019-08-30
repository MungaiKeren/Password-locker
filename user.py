class User:
    '''
    class that generates new instaces of users
    '''
    user_details = []

    def __init__(self,first_name,second_name,password):
        self.first_name = first_name
        self.second_name = second_name
        self.password = password

    # saving the user 
    def save_user(self):
        '''
        save method that adds stores our user
        '''
        User.user_details.append(self)