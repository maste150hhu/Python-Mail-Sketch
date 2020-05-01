from Account import Account
import os
import getpass
import hashlib as Hash

def register():

    blake2bHash = Hash.blake2b();
    
    name = input("Choose your username: ")
    
    path = "Users/" + name + ".txt"
    print(path)
    try:
        fh = open(path, 'r')
        print("Username ", name, " is already taken. Please try again!")
        fh.close()
        register()
    except FileNotFoundError:
        f = open(path, "a")
        f.write(name + os.linesep)
        f.close()

    print("Choose your password: ")
    password = getpass.getpass()
    
    # add password restrictions

    mail = input("Choose your e-Mail-adress: ")

    forename = input("Enter your forename: ")
    famname = input("Enter your family name: ")

    f = open(path, "a")
    f.write(password + os.linesep)
    f.write(mail + os.linesep)
    f.write(forename + os.linesep)
    f.write(famname + os.linesep)
    f.close()
    inbox = open("Users/" + name + "-inbox" + ".txt", 'a')
    inbox.close()

#register()
