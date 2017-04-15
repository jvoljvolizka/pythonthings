import tweepy 
import time
import sys
import random 
import basecon
from keys import * 
def spambot():
	baselist = [2,
				   3,
				   4,
				   5,
				   6,
				   7,
				   8,
				   9,
				   10,
				   11,
				   12,
				   13,
				   14,
				   15,
				   16,
				   17,
				   18,
				   19,
				   20,
				   21,
				   22,
				   23,
				   24,
				   25,
				   26,
				   27,
				   28,
				   29,
				   30,
				   31,
				   32,
				   33,
				   34,
				   35,
				   36,
				   37,
				   38,
				   39,
				   40,
				   41,
				   42,
				   43,
				   44,
				   45,
				   46,
				   47,
				   48,
				   49,
				   50,
				   51,
				   52,
				   53,
				   54,
				   55,
				   56,
				   57,
				   58,
				   59,
				   60,
				   61,
				   62,
				   63,
				   64,
				   65,
				   66,
				   67,
				   68,
				   69,
				   70,
				   71,
				   72,
				   73,
				   74,
				   75,
				   76,
				   77,
				   78,
				   79,
				   80,
				   81,
				   82,
				   83,
				   84,
				   85,
				   86,
				   87,
				   88,
				   89,
				   90,
				   91,
				   92,
				   93,
				   94,
				   95,
				   96,
				   97,
				   98,
				   99,
				   100]
	#basesel = basecon.randombase(baselist)
	basesel = baselist
	basecount = 0
	sleeptime = 3600

	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)

	message_list = []
	message = "key test success!"
	dest = "@Dorukcakiir "
	while True:
		#print(baselist)
		basecount += 1
		if basecount == 98:
			print("FJHRUSHTIOSHDIDHGODSH")
			spambot()
			#print(baselist)
			basesel = baselist
			#basesel = basecon.randombase(baselist)
			basecount = 0
			#print(basesel)
			#print(baselist)
		random.shuffle(basesel)
		randbase = basesel.pop()

		message_list = []
		brainfuck = [1100010,1100101,1111001,1101110,1101001,1101110,1101001,100000,1110011,1101001,1101011,1100101,1111001,1101001,1101101]
		for num in brainfuck:
			new = basecon.converter(num,2,randbase)
			message_list.append(new)
		message_list_end = ' '.join(message_list)
		api.update_status(dest + message_list_end)
		print(message_list_end)
		print(randbase)
		#print(basecount)
		time.sleep(sleeptime)
spambot()
#test = open("attempt_counter" , "w")
#test.write(countstr)
#test.close()