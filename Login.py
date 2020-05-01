from Account import Account
import os
import getpass
import hashlib as Hash

def login(n):
    name_ = input("Username: ")
    pw_ = getpass.getpass()

    blake2bHash = Hash.blake2b();
    blake2bHash.update(name_.encode())
    nameAsBlake2b = blake2bHash.hexdigest()

    passwordBlake2bHash = Hash.blake2b();
    passwordBlake2bHash.update(pw_.encode())
    passwordAsBlake2b = passwordBlake2bHash.hexdigest()

    path = "Users/" + nameAsBlake2b + ".txt"

    try:
        fh = open(path, 'r')
        userdata = fh.readlines()
        userdataSplit = userdata[0].split("=")
        fh.close()

    except FileNotFoundError:
        print("This account does not exist. Please try again!")
        n += 1
        login(n)

    if userdataSplit[0] == nameAsBlake2b and userdataSplit[1] == passwordAsBlake2b and n < 5:
        print("You have successfully logged in!")
        return userdata
    elif n < 5:
        print("Wrong combination of username and password! ")
        print(userdataSplit[1])
        print(passwordAsBlake2b)
        n += 1
        return login(n)
    elif n == 5:
        print("Too many failed logins!")
        return

#login(0)