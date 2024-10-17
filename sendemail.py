'''
Project name : Automate sending emails and text messages
Created Date: Monday, January 2nd 2023, 5:12:13 pm
Author: Oussama HASSSNAOUI
        Hassan BENHAMOU
        Oumamima KARKBA

Copyright (c) 2023.
'''
#----------------------------------- libraries used : ------------------------------#

import smtplib                       #standard protocole to send and receive emails in internet
from main import *                   #import all the function from main file
import pandas as pd                  #import pandas to read from an excel file
import random                        #import random to pick a random task from task list

#--------------------------- store infos filled in 2 variables : -------------------#

boss_user, boss_pass = auth_info()

# ---------------------- establish the connetion to the SMPT server: ---------------#

smtpObj = smtplib.SMTP("smtp.gmail.com", 587)         #establishes a connection with an SMTP server at gmail domain and 587 port  
smtpObj.ehlo()
smtpObj.starttls()                                    #After calling starttls, all further communication with the server will be encrypted using TLS.
smtpObj.login(boss_user, boss_pass)                   #authenticate the client with the SMTP server
server_ver(smtpObj.login(boss_user, boss_pass)[0])    #The return code is the status of the login request

#----------------------- sending emails confirmation : -----------------------------#

confirmation = input("type 'Confirm' to send emails : ")
while confirmation.lower() != "confirm":
    print("Error! Try again")
    time.sleep(1)
    os.system("CLS")
    confirmation = input("type 'Confirm' to send emails : ")

#-------------------------- reading from excel file : ------------------------------#

email_list = pd.read_excel('Classeur1.xlsx')
task_dict = {}
name_dict = {}
names = email_list['NAME']      #[name1, name2 ,name3, ...]
emails = email_list['EMAIL']    #[email1, email2 ,email3, ...]

#-------------------------- extract task list --------------------------------------#

Tasks = tasks_list()

#-------------------------- main function  ------------------------------------------#

def assign_task():

    for i in range(len(emails)):
        email = emails[i]
        random_task = random.choice(Tasks)

        # for every record get the name and the task 
        task_dict[email] = random_task
        name_dict[email] = names[i]
        # delete the task choosen before
        Tasks.remove(random_task)

    for email in task_dict:

        # the message to be emailed
        message = str(
            "Subject: Task\n"
            + "Hi {} ,\n\n".format(name_dict[email])
            + "My name is BIGGYBOSS ,  head of the L3KES TEAM. I sent you this email to inform you that your task is :  "
            + task_dict[email]
        )
        print(
            name_dict[email]
            + " \t\tYour task is : \t\t"
            + task_dict[email],
        )
        smtpObj.sendmail(boss_user , [email], message)

#---------------------------------- rappel de fonction --------------------------------------#

for i in range(12):
    assign_task()
    time.sleep(60*60*24*30)

#---------------------------------- Disconnecting from the SMTP server ----------------------#
smtpObj.quit()