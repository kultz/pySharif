#!/usr/bin/python
# Coded by Sina Sabouni xcode21@icloud.com
import sys
import json
import os.path
import re
from random import randint

theBox={}
def main():
	print (30 * '-')
	print ("Enter \"help\" to find possible commands")
	print (30 * '-')
	###########################
	## error handling 		 ##
	## only accept as defined##
	###########################
	## Wait for valid input in while...not ###
	is_valid=""
	valid_commands=['add','remove','quiz','cards','empty','quit','help','save','load']
	while True :
		choice = str(raw_input('>> Enter a Command : ') )
		#if choice in valid_commands:
			### Take action as per selected menu-option ###
		if choice == "add":
		        addCard()
		elif choice == "cards":
		        fetchCards()
		elif choice == "empty":
				emptyBox()
		elif choice == "remove":
				removeFromBox()
		elif choice == "save":
				saveTheBox()
		elif choice =="load":
				loadTheBox()
		elif bool(re.search(r'quiz', choice)) == True:
				quiz(choice)
		elif choice == "help":
		        help()
		elif choice == "quit":
		        quit()
		else:
		        print ("Not a valid command! Type \"help\" to find out the possible commands")
		        pass
		#else:
			#print("Not a valid command! Type help to find out the possible commands")
			#pass

def addCard():

	question = raw_input('Enter a Question : ')
	answer = raw_input('Enter a Answer : ')
	if question.lower() in theBox:
		print ("Question already exist")
	else:
		theBox.update({question.lower():answer.lower()})
		print("Q/A added successfuly")
		pass

def fetchCards():
	if len(theBox.keys()) > 0:
		for key in theBox:
			print 30*"-"
			print "Q: ", key
			print "A: ", theBox[key]
	else:
		print "There is no cards added yet!"


def emptyBox():
	print len(theBox.keys()), "Cards removed successfuly!"
	theBox.clear()
def removeFromBox():
	input = raw_input('Enter a Question to remove : ')
	if input.lower() in theBox:
		keyToDelete = input.lower()
		del theBox[keyToDelete]
		print "Card removed successfuly!"
	else:
		print "Question does not exist!"
def saveTheBox():
	input = raw_input('Enter a file name to save : ')
	filename = str(input+".box")
	json.dump(theBox, open(filename,'w'))
	print "Cards save in", filename
def loadTheBox():
	global theBox
	filename = str( raw_input('Enter a file name to load from (eg: file.box): ') )
	if os.path.isfile(filename):
		theBox = json.load(open(filename))
	else:
		print "File does not exist!"
def quiz(n):
	if len(theBox.keys()) > 0:
		n = n.split()
		corrects = 0
		incorrects = 0
		for i in range(int(n[1])):
			rq = randint(0,len(theBox.keys())-1)
			raorq = theBox.values()[rq]
			print i+1 , "-" , theBox.keys()[rq]," >>"
			getAnswer = raw_input()
			if getAnswer == raorq:
				corrects += 1
				print "[+] Correct!"
			else:
				incorrects += 1
				print "[-] Incorrect!"
		print corrects, "correct, ", incorrects," incorrect", " total score: ", (100/int(n[1]))*corrects,"%"
	else:
		print "There is no Cards!"
def quit():
	try:
	    sys.exit(1)
	except SystemExit as e:
	    sys.exit(e)
	except Exception:
	    raise
def help():
	print (30 * '-')
	print ("1. add: to add a card to list")
	print ("2. remove: to remove a card from list")
	print ("3. cards: to show cards")
	print ("4. quiz x: to holding a quiz, x should be numeric")
	print ("5. empty: to empty the cards box")
	print ("6. save: to save the cards box into a file")
	print ("7. load: to load cards from a file")
	print ("8. quit: to exit the app")
	print (30 * '-')


if __name__ == '__main__':
    main()
