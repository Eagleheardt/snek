import threading
import time
import datetime
import snekResponse as words
import random

def BethanyHealthChecker():
    d = datetime.datetime.now()
    if (d.isoweekday() in range(1, 6)):
        if (d.hour > 16): # stops the process if it'a after 5 PM
            return
        if (d.hour in range(8, 17)):
            #utils.directResponse("UBW657ERF", random.choice(words.textTreySays)) #Bethany
            utils.directResponse("UC176R92M", random.choice(words.textTreySays)) #Andre
        threading.Timer(random.randint(900, 1500), BethanyHealthChecker).start() # Starts BethanyHealthChecker() after a random time between 15 and 25 minutes
    return

threading.Timer(1500, BethanyHealthChecker).start() # Starts BethanyHealthChecker() after a 25 minute break

#######################
###   Report Test   ###
#######################

def ReportTest():
    d = datetime.datetime.now()
    if (d.day == 16):
        if (d.hour in range(6, 9)):
            utils.directResponse("UC176R92M", "This is how you're going to do timed reports.\n\n\n" + )
            return
        threading.Timer(600, ReportTest).start()
    return

threading.Timer(utils.MONITOR_START_DELAY_IN_SECONDS, ReportTest).start()