#Python Password Manager Project
'''
Author: Azaz Ahmad Swapnil
B.Sc in Computer Science and Engineering 
Daffodil International University

'''
#------------------------------------------------------------------

import os.path


def checkExistence():
    if os.path.exists():
        pass
    else:
        file = open("info.txt",'w')
        file.close()
#Write to File

def appendNew():
    #This Function is for append new password in the txt file given;

    file = open("info.txt",'a')

print()
print()

userName = input("Please enter the user name: ")
password = input("Please enter the password here : ")
website = input("Please enter the website address here :")

print()
print()

usrnm = "UserName:" + userName + "\n"
pwd = "Password:" + password + "\n"
web = "website:" + website + "\n"

open("---------------------------------\n")
open(usrnm)
open(pwd)
open(web)
open("--------------------\n")
open("\n")
open.close()

#Output the Password;

def readPasswords():
    file = open('info.txt','r')
    content = file.read()
    file.close()
    print(content)
