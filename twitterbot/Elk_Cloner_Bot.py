import tweepy 
import time
import sys
from keys import * 

sleeptime = 20

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

siir = open("bla", "r")
siirf = siir.readlines()
siir.close()

for line in siirf:
	api.update_status(line)
	print(line)
	time.sleep(sleeptime)
	