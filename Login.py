from Account import Account
import os
import getpass
import hashlib as Hash

def login(iterator):
    usernameRaw = input("Username: ")
    passwordRaw = getpass.getpass()

    blake2bHash = Hash.blake2b();
    blake2bHash.update(usernameRaw.encode())
    nameAsBlake2b = blake2bHash.hexdigest()

    passwordBlake2bHash = Hash.blake2b();
    passwordBlake2bHash.update(passwordRaw.encode())
    passwordAsBlake2b = passwordBlake2bHash.hexdigest()

    userDatabase = "Users/" + nameAsBlake2b + ".db"

    try:
        UserDatabaseConnection = open(userDatabase, 'r')
        userdata = UserDatabaseConnection.readlines()
        userdataSplit = userdata[0].split("=")
        UserDatabaseConnection.close()

    except FileNotFoundError:
        print("This account does not exist. Please try again!")
        iterator += 1
        login(iterator)

    # build an array containing the user-information
    
    credentialsHash = Hash.blake2b()
    credentialsHash.update(nameAsBlake2b.encode())
    credentialsHash.update(passwordRaw.encode())
    credentialsFilePath = "Users/" + credentialsHash.hexdigest() + ".db"

    credentials = open(credentialsFilePath, "r")
    userInformationRaw = credentials.readlines()
    userInformationSplit = userInformationRaw[0].split("=")

    userInformation = [usernameRaw, userInformationSplit[0], userInformationSplit[1], userInformationSplit[2]]

    if userdataSplit[0] == nameAsBlake2b and userdataSplit[1] == passwordAsBlake2b and iterator < 5:
        print("You have successfully logged in!")
        return userInformation

    elif iterator < 5:
        print("Wrong combination of username and password! ")
        print(userdataSplit[0])
        print(nameAsBlake2b)
        iterator += 1
        return login(iterator)
        
    elif iterator == 5:
        print("Too many failed logins!")
        return

#login(0)