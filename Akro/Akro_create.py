import random
import os
import argparse
import tweepy
from keys import *
vers_number = "1.5"
debug = True
kafiye = False


#-----------------------------------------------------------------------------
def analyzer(poem):
	siir = open(poem, "r")
	siirf = siir.readlines()
	siir.close()
	
	#print(siirf)
	for i in akro_word:
		random.shuffle(siirf)
		for line in siirf:
			if kafiye == False:
				if i == line[0]:
					linef = line[0].upper()
					lineother = line[1:]
					endline = linef + lineother
					print(endline[:-1])
					break
			else:
				if i == line[0] and kafword == line[-2]:
					linef = line[0].upper()
					lineother = line[1:]
					endline = linef + lineother
					print(endline[:-1])
					break
#----------------------------------------------------------------------------
def greet(akro):
	global siir_file
	global akro_word
	global kafword
	print("welcome to akro creator V" + vers_number)
	print(" ")
	akro_word = akro
	if debug == False:
		akro_word = input("please enter the holy world")
		siir_file = input("please enter the poem file name ")
	else:
		print("debug mode holy word using")
		print("debug mode file using\n")
		#akro_word ="dalyarak"
		siir_file = "real_poem"
		kafword = "e"
	analyzer(siir_file)
#---------------------------------------------------------------------------

#greet()

#print(siir_file)

parser = argparse.ArgumentParser()
parser.add_argument("akro", help="holy world")
parser.add_argument("--k", help="kafiye 'kelimenin son harfine kafiye harfi yazın'")

args = parser.parse_args()
wordi = args.akro

print("patates")
kafiye = True
worda = input("please enter holy world")
worda = worda[:-1]
greet(worda)















