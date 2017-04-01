import webapp2
from cgi import escape
import re

pageHTML = '''
    <html>
        <head>
            <title>User Signup</title>
        </head>
        <body>
            <form>
                <label>Username <input type = "text" name = "uname" value = %s></label></br>
                <label>Password <input type = "password" name = "pword"></label><br>
                <label>Confirm  <input type = "password" name = "cfirm"></label><br>
                <label>Email    <input type = "email" name = "email" value = %s></label><br>
            </form>
        </body>
    </html>
'''

def test_password():

def test_username():

def test_email():
