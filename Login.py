from Account import Account
import os
import getpass
import hashlib as Hash

def login(n):
    usernameRaw = input("Username: ")
    passwordRaw = getpass.getpass()

    blake2bHash = Hash.blake2b();
    blake2bHash.update(usernameRaw.encode())
    nameAsBlake2b = blake2bHash.hexdigest()

    passwordBlake2bHash = Hash.blake2b();
    passwordBlake2bHash.update(passwordRaw.encode())
    passwordAsBlake2b = passwordBlake2bHash.hexdigest()

    path = "Users/" + nameAsBlake2b + ".db"

    try:
        fh = open(path, 'r')
        userdata = fh.readlines()
        userdataSplit = userdata[0].split("=")
        fh.close()

    except FileNotFoundError:
        print("This account does not exist. Please try again!")
        n += 1
        login(n)

    # build an array containing the user-information
    
    credentialsHash = Hash.blake2b()
    credentialsHash.update(nameAsBlake2b.encode())
    credentialsHash.update(passwordRaw.encode())
    credentialsFilePath = "Users/" + credentialsHash.hexdigest() + ".db"

    credentials = open(credentialsFilePath, "r")
    userInformationRaw = credentials.readlines()
    userInformationSplit = userInformationRaw[0].split("=")

    userInformation = [usernameRaw, userInformationSplit[0], userInformationSplit[1], userInformationSplit[2]]

    if userdataSplit[0] == nameAsBlake2b and userdataSplit[1] == passwordAsBlake2b and n < 5:
        print("You have successfully logged in!")
        return userInformation
    elif n < 5:
        print("Wrong combination of username and password! ")
        print(userdataSplit[0])
        print(nameAsBlake2b)
        n += 1
        return login(n)
    elif n == 5:
        print("Too many failed logins!")
        return

#login(0)