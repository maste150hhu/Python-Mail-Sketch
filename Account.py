import sys

class Account:
    def __init__(self, accname, passw, email):
        self.accname = accname
        self.passw = passw
        self.email = email
        print("You have successfully registered ", accname)

    def printData(self):
        print("Account-name: ", self.accname)
        print("e-Mail-adress: ", self.email)


#user = Account("mastre99", "12345678", "mastremolten@gmail.com")
#user.printData()