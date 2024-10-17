'''
Project name : Automate sending emails and text messages
Created Date: Monday, January 2nd 2023, 5:12:13 pm
Author: Oussama HASSNAOUI
        Hassan BENHAMOU
        Oumamima KARKBA

Copyright (c) 2023.
'''

#----------------------------------- libraries used : ------------------------------#

import time                     #used for the display style
import smtplib                  #standard protocole to send emails in internet
import os                       #used for the display style(CLS)
from getpass import getpass     #hide password while typing it
from sys import stdout          #for the display
import random                   #import random to pick a random task from task list


#---------------------------information verfication function : ---------------------#

def afiichage():
    print("\n\n")
    print("#######################################################################\n")
    print("#\t\tWelcome! to our messaging application                 #\n")
    print("#\t\tFill the information's bellow please :                #\n")
    print("#######################################################################\n")

def auth_info():
    pin = "1234"
    afiichage()
    x = str(input("\t\t\t email :  "))
    y = getpass("\t\t\t password :  ")
    z = getpass("\t\t\t Pin to continue :  ")
    while z != pin:
        print("\t\t\tIncorrect PIN ! Try again...")
        time.sleep(1)
        os.system("CLS")
        afiichage()
        x = str(input("\t\t\t email :  "))
        y = getpass("\t\t\t password :  ")
        z = getpass("\t\t\t Pin to continue :  ")
    else:
        print("login successful !")
        print("please wait", end="")

    for i in range(0, 15):
        print(". ", end="")
        stdout.flush()
        if i >= 5:
            time.sleep(0.2)
        else:
            time.sleep(0.1)

    os.system("CLS")
    return x, y

#--------------------------- verfication to the server function : ---------------------#

def server_ver(a):
    if a == 503:
        print("login successfully to the server!")

#--------------------------------------- Tasks list -----------------------------------#

def tasks_list():
    L = [
        "Chapter 7 : Pattern Matching with Regular Expressions",
        "Chapter 8: Reading and Writing Files",
        "Chapter 9: Organizing Files",
        "Chapter 10: Debugging",
        "Chapter 11: Web Scraping",
        "Chapter 12: Working with Excel Spreadsheets ",
        "Chapter 13: Working with PDF and Word Documents",
        "Chapter 14: Working with CSV Files and JSON Data",
        "Chapter 15: Keeping Time, Scheduling Tasks, and Launching Programs ",
    ]
    return L