from Account import Account
import os
import getpass
import hashlib as Hash

def register():

    blake2bHash = Hash.blake2b();
    
    name = input("Choose your username: ")

    blake2bHash.update(name.encode())

    nameAsBlake2b = blake2bHash.hexdigest()
    
    path = "Users/" + nameAsBlake2b + ".txt"
    print(path)
    try:
        fh = open(path, 'r')
        print("Username ", name, " is already taken. Please try again!")
        fh.close()
        register()
    except FileNotFoundError:
        f = open(path, "a")
        f.write(nameAsBlake2b) # + os.linesep)
        f.close()

    print("Choose your password: ")
    password = getpass.getpass()
    
    # add password restrictions

    mail = input("Choose your e-Mail-adress: ")

    forename = input("Enter your forename: ")
    famname = input("Enter your family name: ")

    userInformation = [password, mail, forename, famname]
    f = open(path, "a")

    for i in range(len(userInformation)):
        blake2bHash.update(userInformation[i].encode())
        userInformation[i] = blake2bHash.hexdigest()
        f.write(userInformation[i] + "=")# + os.linesep)

    f.close()
    inbox = open("Users/" + nameAsBlake2b + "-inbox" + ".txt", 'a')
    inbox.close()

#register()
