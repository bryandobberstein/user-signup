import webapp2
from cgi import escape
import re

pageHTML = '''
    <html>
        <head>
            <title>User Signup</title>
            <link rel = "stylesheet" href = "/css/styles.css">
        </head>
        <body>
            <form method = "post">
                <label>Username <input type = "text" name = "uname" value = {}></label>{}</br>
                <label>Password <input type = "password" name = "pword"></label>{}<br>
                <label>Confirm  <input type = "password" name = "cfirm"></label>{}<br>
                <label>Email    <input type = "email" name = "email" value = {}></label>{}<br>
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
            <h1>Welcome, {}!</h1>
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

def validcfirm(cfirm, pword):
    if len(cfirm) != len(pword):
        return False
    for i in range(len(cfirm)):
        if cfirm[i] != pword[i]:
            return False
    return True

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
            pworderr = "Invalid password: Must be between 8 and 20 characters"
            validinput = False

        if not validcfirm(cfirm, pword):
            cfirmerr = "Passwords do not match"
            validinput = False
        
        if not validemail(email):
            emailerr = "Please enter a valid email address"

        if validinput == False:
            self.write_form(pageHTML, uname, email, unameerr, pworderr, cfirmerr, emailerr)

        else:
            self.write_form(success, uname)
app = webapp2.WSGIApplication([('/', MainHandler)], debug = True)
