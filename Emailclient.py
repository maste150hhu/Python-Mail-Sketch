import os
import sys
from Account import Account
import Login
import Register
import Email
import datetime
import getpass

# set some important globals
loggedIn = False
currentUser = None

# function to update user-information
def update(usernameRaw, passwordRaw, emailAdress, forename, familyName):

    # path to the account-information
    path = "Users/" + usernameRaw + ".db"

    # override the information
    try:
        userDatabase = open(path, "w")
        userDatabase.write(usernameRaw + os.linesep)
        userDatabase.write(passwordRaw + os.linesep)
        userDatabase.write(emailAdress + os.linesep)
        userDatabase.write(forename + os.linesep)
        userDatabase.write(familyName + os.linesep)
        userDatabase.close()
        print()

        try:
            userDatabaseTemporary = open(path, 'r')
            global currentUser
            currentUser = userDatabaseTemporary.readlines()
            userDatabaseTemporary.close()

        except FileNotFoundError:
            return
        print("Your account-information has been updated!")

    except FileNotFoundError:
        return

# function to display all available AMT commands
def showAccountHelp():
    print()
    print("Here you will find a list of all available AMT commands")
    print()
    print("?          - show this window")
    print("changepw   - utility to change your password")
    print("changemail - utility to change your email")
    print("exit       - return to the normal terminal")

# function to display all available commands
def showHelp():
    # selection of available commands before login
    if not loggedIn:
        print(os.linesep)
        print("Here you will find a list of all available commands:")
        print(os.linesep)
        print("?        - shows this window")
        print("login    - opens the login-panel")
        print("register - launches the registration routine")
        print("exit     - closes the application")
        print(os.linesep + "More commands available when logged in.")
    # added commands when logged in
    elif loggedIn:
        print(os.linesep)
        print("Here you will find a list of all available commands:")
        print(os.linesep)
        print("?        - shows this window")
        print("send     - calls the email-editor")
        print("inbox    - enter your inbox and show all emails")
        print("exit     - closes the application")
        print("info     - returns information about your account")
        print("account  - manage your account")    

    print(os.linesep)

# here the program will start
print(os.linesep)
print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -")
print("     Emailclient - Version 1.0 - 06.04.2019 - Marco Steinke")
print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -")
print(os.linesep)
print("Type \"?\""" to find a list of all available commands or enter your command directly"+ os.linesep)

# terminal is implemented in a while-loop
while True:
    # fetch the command from the terminal
    userInputCommand = input("> ")
    
    # case 1: call showHelp
    if userInputCommand == "?":
        showHelp()

    # case 2: user-login
    elif userInputCommand == "login":
        if not loggedIn:
            currentUser = Login.login(0)
            if not currentUser == None:
                loggedIn = True
                
                # set important variables
                username = currentUser[0]
                email    = currentUser[1]
                forename = currentUser[2]
                famname  = currentUser[3]

                print(os.linesep + "Welcome " + currentUser[2] + "!")

        else:
            print()
            print("You are already logged in!")

    # case 3: registration
    elif userInputCommand == "register":
        if not loggedIn:
            Register.register()
        else:
            print()
            print("You are already logged in!")

    # case 4: exit the program
    elif userInputCommand == "exit":
        sys.exit()

    # case 5: show account-information
    elif userInputCommand == "info":
        if not loggedIn:
            print()
            print("You need to be logged in to use this command" + os.linesep)

        else:
            print()
            print("Username: " + currentUser[0])
            print("Email: " + currentUser[1])
            print("Forename: " + currentUser[2])
            print("Name: " + currentUser[3])

    # cae 6: show account-management-terminal
    elif userInputCommand == "account":
        if not loggedIn:
            print()
            print("You need to be logged in to use this command" + os.linesep)

        # if logged in, start the AMT
        else:
            print()
            print("You have now entered the AMT (AccountManagementTerminal). Type ? to learn about the commands!")

            # while-loop which implements the AMT
            while True:
                accountcmd = input("account> ")

                # case 6.1: exit the AMT
                if accountcmd == "?":
                    showAccountHelp()

                elif accountcmd == "exit":
                    break

                # case 6.2: Call change-password-routine
                elif accountcmd == "changepw":
                    print()
                    print("Please enter your current password to use this function!")
                    oldpw = getpass.getpass()

                    if password == oldpw:
                        print()
                        print("Please enter your new password!")
                        newpw = getpass.getpass()
                        update(username, newpw, email, forename, famname)

                    else:
                        print()
                        print("The password you entered is not correct!")

                # case 6.3: Call change-email-routine
                elif accountcmd == "changemail":
                    print()
                    print("Please enter your current password to use this function!")
                    oldpw = getpass.getpass()

                    if password == oldpw:
                        print()
                        newmail = input("Please enter your new Email: ")
                        update(username, password, newmail, forename, famname)

                    else:
                        print()
                        print("The password you entered is not correct!")

                # case 6.4: unknown command used
                else:
                    print(os.linesep + "Command not found. Please try again!")
   
    # case 7: sending emails to another user
    elif userInputCommand == "send":
        if not loggedIn:
            print()
            print("You need to be logged in to use this command")

        else:
            Email.send(currentUser[0])

    # case 8: reading the inbox
    elif userInputCommand == "inbox":
        if not loggedIn:
            print()
            print("You need to be logged in to use this command")
            
        else:
            count = 0
            path = "Users/" + currentUser[0].replace(os.linesep, "") + "-inbox.b2DB"
            f = open(path, 'r')

            # generates an array with cardinality 5*n 
            # where n is the amount of emails
            # 0: Date
            # 1: From
            # 2: To
            # 3: Title
            # 4: Content
            inboxData = f.readlines()
            x = 0
            while x < len(inboxData):
                term = x/5 + 1
                print(str(term).replace(".0", ""))
                print("-  -  -  -  -  -  -  -  -  -  -")
                print("Date: " + inboxData[x])
                print("From: " + inboxData[x+1].replace(os.linesep, ""))
                print("-  -  -  -  -  -  -  -  -  -  -")
                print(inboxData[x+3].replace(os.linesep, ""))
                print("-  -  -  -  -  -  -  -  -  -  -")
                print(inboxData[x+4])
                print("-  -  -  -  -  -  -  -  -  -  -")
                print()
                print()
                x += 5 
            print("There are " + str(term).replace(".0", "") + " Mails in your inbox!")           
            print()
            print("Type 'exit' to leave the inbox-terminal or 'delete' to delete an Email with a certain ID")

            mailcmd = input("inbox> ")
            
            # case 8.1: delete an email
            if mailcmd == "delete":
                ID = input("inbox:delete> Enter the ID: ")

                # calculate the mail's index (location)
                index = (int(ID) - 1) * 5

                # move all following elements to the front by 5 steps
                for i in range(index, len(inboxData) - 5):
                    inboxData[i] = inboxData[i+5]
                    print(i)
                
                path = "Users/" + currentUser[0].replace(os.linesep, "") + "-inbox.db"
                fp = open(path, 'w')
                for x in inboxData:
                    fp.write(inboxData[x])

    # case X: command not found
    else:
        print(os.linesep + "Command not found. Please try again!")
    