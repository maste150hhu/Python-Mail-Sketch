from Account import Account
import os
import getpass
import hashlib as Hash

def register():

    blake2bHash = Hash.blake2b();
    
    name = input("Choose your username: ")

    blake2bHash.update(name.encode())

    nameAsBlake2b = blake2bHash.hexdigest()
    
    userInformationFilePath = "Users/" + nameAsBlake2b + ".db"

    try:

        userInformationProtectedDatabase = open(userInformationFilePath, 'r')
        print("Username ", name, " is already taken. Please try again!")
        userInformationProtectedDatabase.close()
        register()
        
    except FileNotFoundError:

        temporaryUserCreationFilePath = open(userInformationFilePath, "a")
        temporaryUserCreationFilePath.write(nameAsBlake2b + "=") # + os.linesep)
        temporaryUserCreationFilePath.close()

    print("Choose your password: ")
    password = getpass.getpass()

    mail = input("Choose your e-Mail-adress: ")

    forename = input("Enter your forename: ")
    famname = input("Enter your family name: ")

    userInformation = [password, mail, forename, famname]
    userInformationHash = []

    credentialsHash = Hash.blake2b()
    credentialsHash.update(nameAsBlake2b.encode())
    credentialsHash.update(password.encode())
    credentialsFilePath = "Users/" + credentialsHash.hexdigest() + ".db"

    credentials = open(credentialsFilePath, "a")
    credentialsAsString = ""

    credentialsAsString += userInformation[1]
    credentialsAsString += "=" + userInformation[2]
    credentialsAsString += "=" + userInformation[3]

    credentials.write(credentialsAsString)
    credentials.close()
    

    for iterator in range(len(userInformation)):
        userInformationHash.insert(len(userInformationHash), Hash.blake2b())
    temporaryUserCreationFilePath = open(userInformationFilePath, "a")

    for iterator in range(len(userInformation)):
        userInformationHash[iterator].update(userInformation[iterator].encode())
        userInformation[iterator] = userInformationHash[iterator].hexdigest()
        temporaryUserCreationFilePath.write(userInformation[iterator] + "=")# + os.linesep)

    print(userInformationHash[0].hexdigest())

    temporaryUserCreationFilePath.close()
    inbox = open("Users/" + nameAsBlake2b + "-inbox" + ".b2DB", 'a')
    inbox.close()

#register()
