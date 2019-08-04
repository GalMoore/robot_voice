#!/usr/bin/python3
import sys
from ohbot import ohbot
# import ohbot
# import os
import time
import csv

path_to_csv = "/home/gal/catkin_ws/src/robot_chatbot/chatbot.csv"

# number arrives from sys.argv[i] it is a string
def get_csv_text(number):
	with open(path_to_csv) as csvfile:
	    readCSV = csv.reader(csvfile, delimiter=',')
	    counter = 0
	    for row in readCSV:

	    	if number==0:
	    		return("there is no zero")

	    	# elif number==1 and counter==1:
	    	# 	return(row[1])

	    	if counter == number-1:
	    		return(row[1])
	    	counter = counter + 1

# sentence = get_csv_text(0)

# sys.argv[1] means any number passed here as a string
sentence = get_csv_text(int(sys.argv[1]))
print("what is sys.argv? " + str(sys.argv[1]) + " " +  str(type(sys.argv[1])))
print(sentence)
# print("saying:", sys.argv[1])


# sys.argv[1] is the number of the sentence to say
# grab the sentence from csv file here: 

# ohbot.setVoice("-ven+croak")

# ohbot.setVoice("-vfr+f1 -p99 -s180")	
# https://github.com/ohbot/ohbot-python
# ohbot.setVoice("-ven-us -a200 ")
# ohbot.say(sentence)


ohbot.setVoice("-ven-us+f2")
# ohbot.say(sentence)


# # say the sentence
ohbot.say(sentence)

