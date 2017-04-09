import webapp2
from cgi import escape
import re

pageHTML = '''
    <html>
        <head>
            <title>User Signup</title>
            <link rel = "stylesheet" href = "/css/styles.css">
            <link href="https://fonts.googleapis.com/css?family=Palanquin+Dark" rel="stylesheet">
        </head>
        <body>
            <form method = "post" class = "focus">
                <h1>Account Signup</h1>
                <label>Username<input type = "text" name = "uname" value = {}></label></br>
                <span class = "error">{}</span><br>
                <label>Password<input type = "password" name = "pword"></label><br>
                <span class = "error">{}</span><br>
                <label>Confirm<input type = "password" name = "cfirm"></label><br>
                <span class = "error">{}</span><br>
                <label>Email<input type = "email" name = "email" value = {}></label><br>
                <span class = "error">{}</span><br>
                <input type = "submit">
            </form>
        </body>
    </html>
'''

success = """
    <html>
        <head>
            <title>Welcome</title>
            <link rel = "stylesheet" href = "/css/styles.css">
        </head>
        <body>
            <h1 class = "focus">Welcome, {}!</h1>
        </body>
    </html>
"""

reuser = re.compile("^[a-zA-Z0-9_-]{3,20}$")
repass = re.compile("^.{8,20}$")
remail = re.compile("^[\S]+@[\S]+.[\S]+$")

def validuser(uname):
    return reuser.match(uname)

def validpass(pword):
    return repass.match(pword)

def validemail(email):
    return remail.match(email)

class MainHandler(webapp2.RequestHandler):
    def write_form(self, doc, usrnm = "", eml = "", usrnmerr = "", pwrderr = "", cfrmerr  = "", emerr = ""):
        usrnm = escape(usrnm, quote = True)
        eml = escape(eml, quote = True)
        self.response.write(doc.format(usrnm, usrnmerr, pwrderr, cfrmerr, eml, emerr))

    def get(self):
        self.write_form(pageHTML)

    def post(self):
        uname = self.request.get("uname")
        pword = self.request.get("pword")
        cfirm = self.request.get("cfirm")
        email = self.request.get("email")
        unameerr = ""
        pworderr = ""
        cfirmerr = ""
        emailerr = ""

        validinput = True

        if not validuser(uname):
            unameerr = "Invalid username: Must contain 3-10 letters and/or numbers"
            validinput = False

        if not validpass(pword):
            pworderr = "Invalid password: Must contain 8-20 characters"
            validinput = False

        if pword != cfirm:
            cfirmerr = "Passwords do not match"
            validinput = False
        
        if not validemail(email):
            emailerr = "Please enter a valid email address"

        if validinput == False:
            self.write_form(pageHTML, uname, email, unameerr, pworderr, cfirmerr, emailerr)

        else:
            self.write_form(success, uname)
app = webapp2.WSGIApplication([('/', MainHandler)], debug = True)
