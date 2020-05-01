#!/usr/bin/python
# -*- encoding : utf8 -*-

from fbchat import Client
from fbchat.models import *
from getpass import getpass 
import sys
import os
import time

def loadMovieScript(filePath, parse_level="word"):
    with open(filePath, "r") as f:
        data = f.read()
        if parse_level == "word":
            new_data = data.split(" ")
            
            filtered_new_data = list(filter(lambda word: word != '' or word != '    ', new_data))
    return filtered_new_data

def fetchTrollingList(friendDB):
    numOfUsersToSpam = int(input("Input number of users to spam: "))
    #todo error msg if num is negative
    if numOfUsersToSpam < 0:
        sys.exit(1)
        
    trollingList = []
    while numOfUsersToSpam > 0:
        name = input("Enter user name: ")
        trollingList.append(friendDB[name])
        numOfUsersToSpam = numOfUsersToSpam - 1
    return trollingList


def main():
    print(
"""Welcome to TrollyMMSS, a Messenger Movie Script Spammer.
It was developed purely just for fun and for testing
what can you do with a fbchat module, inspired by a 
faebook video who posts Bee movie quotes. Maybe I will
turn it to an android app fully, we will see :).
Have fun using it, and if I made a mistake, dont fret
to give me feedback.""")
    username = input("Please enter your email: ")
    #connecting to Facebook
    client = Client(username, getpass())
    print("User ID: %s" %(client.uid))

    users = client.fetchAllUsers()
    
    friendUids = [user.uid for user in users]
    friendNames = [user.name for user in users]
    friendDB = dict(zip(friendNames, friendUids))
    print(friendDB)
    trollingList = fetchTrollingList(friendDB)
    print("Trolling list: %s" % str(trollingList))
    trolling_data = loadMovieScript("beemoviescript.txt")
    test = input("Do you really wish do this? You may be blocked by the selected users if you do this if they find this harassing? [y/n]")
    if test == "n":
        sys.exit(1)
    for word in trolling_data:
        for trollID in trollingList:
            print("Sending word: %s to %s user" % (word, trollID))
            client.send(Message(text=word), thread_id=trollID, thread_type=ThreadType.USER)
        #todo - sleep for 5 seconds to avoid facebook server treshold
        time.sleep(0.75)
    print("Loging out. Bye Bye!")
    client.logout()
    print("User has successfully logged out.")



if __name__ == "__main__":
    main()


