# Project
Password Locker

## Project pre-discription
An app that stores users passwords for various apps since its hard to memorize passwords

# Author
Mungai Keren

## Author details
* Email: wambukeren@gmail.com

# Description 
This project does tests for each method in the user and credentials classes. The methods tested include; saving, displaying, deleting and checking if user and app actually exist as saved.
The app continues to enable the user interact with the app as they can add apps and passwords used in their different accounts.
For one to use the app, a user has to login using their details, user name and password, then can proceed to add accounts they have passwords for or view the passwords for previously added apps.

# User stories
The user would like to.... :

* To create an account for the application or log into the application.
* Store my existing acounts login details for various accounts that i have registered for.
* Generate new password for an account that i haven't registered for and store it with the         account name.
* Delete stored account login details that i do now want anymore.
* Copy my credentials to the clipboard

# Set-up and installation instructions
 ### You need to have the following installed
  * Python3.6
  * Pip
  * Pyperclip
  * x-clip
 ### Cloning
  * Open Terminal {Ctrl+Alt+T}
  * git clone https://github.com/MungaiKeren/Password-locker.git

  * cd Password-locker

  * Open with your favourite editor code . or atom .
 ### Running the Application
  To run the application, open the cloned file in terminal and run the following commands:

    $ chmod +x run.py
    $ ./run.py
  To run test for the application $ python3 user-test.py
# Behaviour driven development
| Behaviour                          | Input                               | Output  |
| ---:                               | ---:                                | ---:    |
| Run the application in the terminal| chmod +x run.py followed by ./run.py | App runs |
| App asks for user name             | Enter user name | App asks for password |
| App prompts password or use user customized| Enter password | App displays a welcome note |
| App proceeds to list an option for user interactions| select short code | prompts generated |
| Short code NC - create new account | app name and password | user app and password displayed |
| Short code VC-view user accounts | - | Displays a list of accounts created and their passwords|| Short code DEL - delete accounts | account and password of app to be deleted| deletes app | 
| App exits anonymously| Bugs present in code | report bug |
## Known bugs
The app is not able to save the initial app details.


## Technologies used
* Python

# Development
To contribute,
* Fork the repo
* Create a new branch ```git branch contributions/improvements```
* Navigate to your the improvements branch ```git checkout improvements```
* Make appropriate changes in the files
* Add changes to reflect the changes made.
* Commit your changes ```git commit -am "improvements"```
* Push to the git branch ```git push origin improvements```
* Create a pull request

# License
MIT license