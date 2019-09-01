class Credentials:
    '''
    class that generates instances of new credentials
    '''
    app_details = []
    
    def __init__(self,app,app_password):
        self.app = app
        self.app_password = app_password
    
    def save_app(self):
        '''
        function that stores our accounts
        '''
        Credentials.app_details.append(self)