from Account import Account
import os
import getpass

def login(n):
    name_ = input("Username: ")
    pw_ = getpass.getpass()

    path = "Users/" + name_ + ".txt"

    try:
        fh = open(path, 'r')
        userdata = fh.readlines()
        fh.close()

    except FileNotFoundError:
        print("This account does not exist. Please try again!")
        n += 1
        login(n)

    if userdata[0] == name_ + os.linesep and userdata[1] == pw_ + os.linesep and n < 5:
        print("You have successfully logged in!")
        return userdata
    elif n < 5:
        print("Wrong combination of username and password! ")
        n += 1
        return login(n)
    elif n == 5:
        print("Too many failed logins!")
        return

#login(0)