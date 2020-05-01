import os
from Account import Account
import datetime

#class Email:

    # An email consists of sender (send)
    # recipient (rec), title, text
    #def __init__(self, send, rec, title, text):
    #    self.send = send
    #    self.rec = rec
    #    self.title = title
    #    self.text = text

    # this function will send an email to the recipient
    # while writing its content into his inbox-"table"
def send(from_):

        try:

            name = input("To: ")
            path = "Users/" + name + "-inbox" + ".txt"
            print(path)

            fh = open(path, 'a')
            
            tit = input("Title: ")
            text = input("Content: ")

            now = datetime.datetime.now()
            fh.write(now.strftime("%Y-%m-%d %H:%M") + os.linesep)
            fh.write(from_)
            fh.write(name + os.linesep)
            fh.write(tit + os.linesep)
            fh.write(text + os.linesep)

            fh.close()

            print()
            print("Your mail was sent to " + name)

        except FileNotFoundError:
            print()
            print("The username you entered does not exist")