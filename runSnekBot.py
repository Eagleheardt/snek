import sqlite3
from sqlite3 import Error
import os
import time
import datetime
import re
import sys
import schedule
import random
import cryptography

from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from slackclient import SlackClient
from cryptography.fernet import Fernet

# Snek's birthday is October 25, 2018

#################
#   TODO LIST   #
#################

# Monthly formatted report: 
# Person who reported the most - number of reports (Snek's favorite person of the month)
# Most errant server - server number - number of issues
# Overall highest reporter - number of reports
# overall most errant server - number of reports
# Daily highest number of issues.
# Highest issues on a day in that month
# Daily average overall
# daily average on the month

############################################################################

conn = sqlite3.connect('snekbot/data/snekbot.db') # Connect to the database
serverCursor = conn.cursor() # establish cursor to enact on the DB

######################################
#####   Begin token decryption   #####
######################################

keyFile = open('snekbot/data/snek_token.key', 'rb')
key = keyFile.read()
keyFile.close()

f = Fernet(key)

encryptedTokenFile = open('snekbot/data/snek_token.encrypted', 'rb')
encryptedToken = encryptedTokenFile.read()

decryptedToken = f.decrypt(encryptedToken)

####################################
#####   End token decryption   #####
####################################

SLACK_BOT_TOKEN = decryptedToken.decode() # set slack token

slack_client = SlackClient(SLACK_BOT_TOKEN) # instantiate Slack client

snekBotID = None # Snek's user ID in Slack: value is assigned after the bot starts up

# constants
RTM_READ_DELAY = 0.5 # 0.5 second delay in reading events

def stdOut(s): # pipes data to coodinating backup file
    curDate = datetime.today().strftime('%Y-%m-%d')
    curTime = datetime.now().strftime('%H:%M:%S')
    logFile = open((("/home/ubuntu/logs/{0}.log").format(curDate)),"a")
    logFile.write(("{0}:  {1}\n").format(curTime,s))
    logFile.close()
    return

def logIt(): # writes simple string to file
    curDate = datetime.today().strftime('%Y-%m-%d')
    curTime = datetime.now().strftime('%H:%M:%S')
    logFile = open((("/home/ubuntu/logs/{0}.log").format(curDate)),"a")
    logFile.write(("{0}:  Snek 15 minute check in!\n").format(curTime))
    logFile.close()
    return

schedule.every(15).minutes.do(logIt) # calls logIt every 15 minutes

def checkInt(s): # validates input as integer; returns 999 if it isn't
	try: 
		return int(s)
	except ValueError:
		return 999

def SQLInsert(aConn,sqlCmd): # TODO: abstract out insertions to use this method
	return

def SQLReturn(aConn,sqlCmd): # fetches data from the database
	reportCur = aConn.cursor()
	reportCur.execute(sqlCmd)
	SQLResults = reportCur.fetchall()
	reportCur.close()
	return SQLResults

def convertStatus (stat): # converts the emoji to a human-readable status
	statDict = {
		"face_vomiting":"Auto reconnect",
		"fire":"Window Closes",
		"loading":"Loading",
		"skull_and_crossbones":"Restart IE",
		"angry_skeletor":"Restart IE",
        "dumpster_fire":"Restart IE"
	}
	if stat not in statDict:
		return "Non-Specific Error"
		
	return statDict[stat]
	
def insertStatus (server, stat): # adds a server number and status
	serverCursor.execute(("""
		INSERT INTO 
			Status (ServerNumber, ServerStatus) 
		VALUES
			('{0}','{1}');
	""").format(checkInt(server), convertStatus(stat.strip())))
	conn.commit()
	return

def insertHistory (server, stat): # adds a server number and status
	serverCursor.execute(("""
		INSERT INTO 
			History (ServerNumber, ServerStatus) 
		VALUES
			('{0}','{1}');
	""").format(checkInt(server), convertStatus(stat.strip())))
	conn.commit()
	return

def insertUserHistory (server, stat, user): # adds a server number and status
	serverCursor.execute(("""
		INSERT INTO 
			UseHistory (ServerNumber, ServerStatus, SlackID)
		VALUES
			('{0}','{1}','{2}');
	""").format(checkInt(server), convertStatus(stat.strip()), user))
	conn.commit()
	return
	
def EODReport (aDate): # Gets a daily summary of the VM number and status reported
	cmd = (("""
		SELECT 
			ServerNumber as [Server]
			, ServerStatus as [Status]
			, count(ServerStatus) as [Amount]
		FROM 
			Status
		WHERE 
			date(TimeStamp) IN('{0}')
			AND ServerNumber IN(1,2,3,4,17)
		GROUP BY 
			ServerNumber
			,ServerStatus;
	""").format(aDate))
	results = SQLReturn(conn,cmd)
	newStr = "Report for: " + aDate + "\n"
	for row in results:
		i = 1
		for item in row:
			if i == 1:
				newStr += "VM" + str(item) + " - "
			if i == 2:
				newStr += "Status: " + str(item) + " - "
			if i == 3:
				if item != 1:
					newStr += "Reported: " + str(item) + " times"
				else:
					newStr += "Reported: " + str(item) + " time"
			i += 1
		newStr += "\n"
	return newStr
	
def EODReportRange (date1, date2): # Gets a range summary of the VM number and status reported
	cmd = (("""
		SELECT 
			ServerNumber as [Server]
			, ServerStatus as [Status]
			, count(ServerStatus) as [Amount]
		FROM 
			Status
		WHERE 
			date(TimeStamp) BETWEEN '{0}' AND '{1}'
			AND ServerNumber IN('1','2','3','4','17')
		GROUP BY 
			ServerNumber
			,ServerStatus
	""").format(date1, date2))
	results = SQLReturn(conn,cmd)
	newStr = "Report for: " + date1 + " to " + date2 + "\n"
	for row in results:
		i = 1
		for item in row:
			if i == 1:
				newStr += "VM" + str(item) + " - "
			if i == 2:
				newStr += "Status: " + str(item) + " - "
			if i == 3:
				if item != 1:
					newStr += "Reported: " + str(item) + " times"
				else:
					newStr += "Reported: " + str(item) + " time"
			i += 1
		newStr += "\n"
	return newStr

def addPet(aUser,aStat):  #adds a 'pet' to the database
	newCur = conn.cursor()
	newCur.execute(("""
		INSERT INTO 
			SnekStats (User, aStatus)
		VALUES
			('{0}','{1}');
	""").format(aUser,aStat))
	newCur.close()
	conn.commit()
	return

def getReports (date1, date2): # get reports on a date range
	cmd = (("""
		SELECT 
			SUM(AMT)
		FROM
			(SELECT 
				ServerNumber
				, ServerStatus
				, count(ServerStatus) as AMT
			FROM 
				History
			WHERE 
				date(TimeStamp) BETWEEN '{0}' AND '{1}'
				AND ServerNumber IN(1,2,3,4,17)
			GROUP BY 
				ServerNumber
				,ServerStatus
			) src;
	""").format(date1, date2))
	results = SQLReturn(conn, cmd)
	return results[0][0]

def historicalReport (date1, date2): # Gets a range summary of the VM number and status reported
	cmd = (("""
		SELECT 
			ServerNumber as [Server]
			, ServerStatus as [Status]
			, count(ServerStatus) as [Amount]
		FROM 
			History
		WHERE 
			date(TimeStamp) BETWEEN '{0}' AND '{1}'
			AND ServerNumber IN('1','2','3','4','17')
		GROUP BY 
			ServerNumber
			,ServerStatus
	""").format(date1, date2))
	results = SQLReturn(conn,cmd)
	newStr = "Report for: " + date1 + " to " + date2 + "\n"
	for row in results:
		i = 1
		for item in row:
			if i == 1:
				newStr += "VM" + str(item) + " - "
			if i == 2:
				newStr += "Status: " + str(item) + " - "
			if i == 3:
				if item != 1:
					newStr += "Reported: " + str(item) + " times"
				else:
					newStr += "Reported: " + str(item) + " time"
			i += 1
		newStr += "\n"

	newStr += ("\nTotal reports: {0}").format(getReports(date1, date2))
	return newStr

### SELECT UseHistory.TimeStamp, UseHistory.ServerNumber, UseHistory.ServerStatus, User.UserName FROM UseHistory JOIN User ON User.SlackID = UseHistory.SlackID WHERE UseHistory.SlackID NOT LIKE 'NOID' AND UseHistory.ServerNumber IN(1,2,3,4,17);
#### New comprehensive query

def getPets(): # returns the amount of love Snek gets
	cmd = """
		SELECT 
			aStatus, COUNT(*) as Amount
		FROM
			SnekStats
		GROUP BY
			aStatus
		ORDER BY
			Amount DESC;
	"""
	rawResults = SQLReturn(conn, cmd)
	newStr = "People do lots of things to me! I love pets most of all, though!\nI have been:\n"
	for row in rawResults:
		i = 1
		for item in row:
			if i == 1:
				newStr += str(item) + ": "
			if i == 2:
				newStr += str(item) + " times"
			i += 1
		newStr += "\n"
	return newStr

def imSorry(aConn): # an appology for the environment in which we live
        sqlCmd = "SELECT Link FROM Sorry;"
        results = SQLReturn(aConn,sqlCmd)
        allLinks = []
        for aLink in results:
                allLinks.append(aLink)
        return (random.choice(allLinks))

def celebrate(aNum): # returns a gif and an inspirational message
    gif = """
    https://media1.giphy.com/media/jKYU63SjCLCKkTmtml/giphy-downsized.gif?cid=6104955e5c06a4d74e61555a51acae3e
    """
    info = ("""
    I have just received report number {0}!

    Everyone, please keep your heads up!
    I'm listening to your problems, and they are being recorded!
	:rsi: :rsi: :rsi: :rsi: :rsi: :rsi: :rsi: :rsi: :rsi: :rsi: :rsi: :rsi: :rsi: 
	As long as you keep reporting issues, we will fight for a more stable environment!
    """.format(aNum))
    return gif, info

def parseSlackInput(aText): # breaks apart a message
	if aText and len(aText) > 0:
		item = aText[0]
		if 'text' in item:
			msg = item['text'].strip(' ')
			chn = item['channel']
			usr = item['user']
			stp = item['ts']
                        return [str(msg),str(chn),str(usr),str(stp)]
		else:
			return [None,None,None,None]

def inChannelResponse(channel,response): # respond in channel
	slack_client.api_call(
		"chat.postMessage",
		channel=channel,
		text=response,
		as_user=True
		)
	return

def threadedResponse(channel,response,stamp): # respond in a thread
	slack_client.api_call(
		"chat.postMessage",
		channel=channel,
		text=response,
		thread_ts=stamp,
		as_user=True
		)
	return

def directResponse(someUser,text): # respond directly
	slack_client.api_call(
		"chat.postMessage",
		channel=someUser,
		text=text,
		as_user=True
		)
	return

def parseVM(vmMsg): # breaks up a message starting with "VM"
	try:
		vm, stat, rest = vmMsg.split(':',2) # breaks string into 3 parts on a colon
		del rest # 'rest' is deleted
	except: # if there aren't at least 3 parts
		return False, False # returns double false
	vm = vm[2:].strip()
	return vm, stat # returns the VM number and status

def parseDateRange(someDates): # breaks apart dates
	date1, date2 = someDates.split(',')
	return date1.strip(), date2.strip()

#######################################################
#######################################################
##############  Evaluate the commands    ##############
#######################################################
#######################################################

def handle_command(command, channel,aUser,tStamp):
	command = command.lower()
	response = None
		
	# This is where you start to implement more commands!

	if command == "!help": # !help can be the only thing they type
		response = """I'm Snek! Here's how I can help!
				
				If you just report VM issues, I will eat and store them!
				Vm[#] [status] to report! That's it!
				Don't bother editing your response, just say it again, if I don't eat it.
				:face_vomiting: = Auto reconnect
				:fire: = Window Closes
				:skull_and_crossbones: = Restart IE completely
				:loading: = Loading
				
				!help - display this message.
				!pet - I love the pets!

				!report[SPACE][YYYY-MM-DD] - gives a breakdown of all the server statuses reported for that day.
				!range[SPACE][YYYY-MM-DD],[YYYY-MM-DD]- gives a breakdown of all the server statuses reported for that date range.
				"""
		threadedResponse(channel,response,tStamp)
		addPet(aUser, "help")
		return

	if command == "!pet":
		addPet(aUser, "pet")
		threadedResponse(channel,"You pet Snek. Snek is happy.",tStamp)
		return

	if command == "!tread":
		addPet(aUser, "tread")
		threadedResponse(channel,"No tread on Snek. Snek is friend.",tStamp)
		return

	if command == "!provoke":
		addPet(aUser, "provoke")
		threadedResponse(channel,"Feed Snek. No provoke.",tStamp)
		return

	if command == "!poke":
		addPet(aUser, "poke")
		threadedResponse(channel,"You poke Snek. Why poke Snek?",tStamp)
		return

	if command == "!hug":
		addPet(aUser, "hug")
		threadedResponse(channel,"You hug Snek. Snek is love. Snek is life.",tStamp)
		return

	if command == "!step":
		addPet(aUser, "step")
		threadedResponse(channel,"Watch for Snek. Snek helps!",tStamp)
		return

	if command == "!boop":
		addPet(aUser, "boop")
		threadedResponse(channel,"Boop Snek snoot. Doot doot.",tStamp)	
		return

	if command == "!snekpets":
		addPet(aUser, "snekpets")
		directResponse(aUser,getPets())
		return

	if command.startswith("!report"): # if the message starts with the string "!report" this goes off
		theDate = command[8:]
		response = EODReport(theDate)
		directResponse(aUser,response)
		return

	if command.startswith("!range"):
		theDates = command[7:]
		date1,date2 = parseDateRange(theDates)
		response = historicalReport(date1,date2)
		directResponse(aUser,response)
		return

	if command == "!howmany":
		allStat = getReports('2018-01-01', '9999-12-31')
		directResponse(aUser,"So far I've eaten {0} problems.".format(allStat))
		return

	if command == "f5 :dumpster_fire:":
		aLink = imSorry(conn)
                sryMsg = "I'm sorry for the unstable environment. Let me send you something to brighten your mood!"
                inChannelResponse(channel,sryMsg)
                directResponse(aUser,aLink)
		return

	if command.startswith("vm"):
		vm, stat = parseVM(command)
		if not stat:
			if len(command) > 10: # if the message is longer than 10 characters, it probably wasn't meant to be viewed
				return
			inChannelResponse(channel,"I can't eat that!") # goes off to remind folks that you need the emoji status
			return
		insertStatus(vm, stat)
		insertHistory(vm, stat)
                insertUserHistory(vm, stat, aUser)
		inChannelResponse(channel,"You have fed Snek.")

		currentDT = datetime.now()
		currentDT = currentDT.strftime("%Y-%m-%d %H:%M:%S")

		stdOut(("Snek|{0}|{1}|{2}|{3}").format(currentDT, checkInt(vm), convertStatus(stat), aUser))
		allStat = getReports('2018-01-01', '9999-12-31')
		if (allStat % 1000) == 0: # shoots off every 1k issues logged
			gif, info = celebrate(allStat)
			inChannelResponse('CC568PC3X',gif)
			inChannelResponse('CC568PC3X',info)
		return
	
	return # ends handle_command method

########################################################
########################################################
##############   End command evaluation   ##############
########################################################
########################################################

	####################
	# Example commands #
	####################

	# if command == "!history":
	# 	theDates = command[9:]
	# 	date1,date2 = parseDateRange(theDates)
	# 	response = historicalReport(date1,date2)
	# 	directResponse(aUser,response)
	# 	return
    
	# if command.startswith("!test"):
	# 	response = (("""Text:{0}
	# 			Channel:{1}
	# 			TS:{2}
	# 			User:{3}
	# 			""").format(command,channel,tStamp,aUser))
	# 	inChannelResponse(channel,response)
	# 	return

	# ADMIN command
	# if command == "!farewell":
	# 	if aUser == "UC176R92M":
	# 		inChannelResponse(channel,"Good bye eveyone!")
	# 	return
	
###########################################################
###########################################################
##############   Start of scheduled events   ##############
###########################################################
###########################################################

#############################
# testing channel GDJEY6HJN #
#############################

def mos3():
        # Jan 25 2019
        gif = """http://bestanimations.com/Holidays/Birthday/birthdaygifs/birthday-candles-happy-bday-wishes-animated-gif.gif"""
        res = """
        Hey everyone!
        I'm 3 months old, today!
        With your help, I've recorded a LOT different incidents with the VM environments!
        Please keep up the good work!
        """

        inChannelResponse('CC568PC3X',gif)
        inChannelResponse('CC568PC3X',res)
        return

def mos6():
        # Apr 25 2019
        gif = """http://bestanimations.com/Holidays/Birthday/birthdaygifs/birthday-candles-happy-bday-wishes-animated-gif.gif"""
        res = """
        Hey everyone!
        I'm 6 months old, today!
        With your help, I've recorded a LOT different incidents with the VM environments!
        Please keep up the good work!
        """

        inChannelResponse('CC568PC3X',gif)
        inChannelResponse('CC568PC3X',res)
        return

def mos9():
        # Jul 25 2019
        gif = """http://bestanimations.com/Holidays/Birthday/birthdaygifs/birthday-candles-happy-bday-wishes-animated-gif.gif"""
        res = """
        Hey everyone!
        I'm 9 months old, today!
        With your help, I've recorded a LOT different incidents with the VM environments!
        Please keep up the good work!
        """

        inChannelResponse('CC568PC3X',gif)
        inChannelResponse('CC568PC3X',res)
        return

def year1():
        # Oct 25 2019
        gif = """http://bestanimations.com/Holidays/Birthday/birthdaygifs/birthday-candles-happy-bday-wishes-animated-gif.gif"""
        res = """
        Hey everyone!
        I'm a year old, today!
        With your help, I've recorded a LOT different incidents with the VM environments!
        Please keep up the good work!
        """

        inChannelResponse('CC568PC3X',gif)
        inChannelResponse('CC568PC3X',res)
        return

def year2():
        # Oct 25 2019
        gif = """http://bestanimations.com/Holidays/Birthday/birthdaygifs/birthday-candles-happy-bday-wishes-animated-gif.gif"""
        res = """
        Hey everyone!
        I'm two years old, today!
        With your help, I've recorded a LOT different incidents with the VM environments!
        Please keep up the good work!
        """

        inChannelResponse('CC568PC3X',gif)
        inChannelResponse('CC568PC3X',res)
        return

def year3():
        # Oct 25 2019
        gif = """http://bestanimations.com/Holidays/Birthday/birthdaygifs/birthday-candles-happy-bday-wishes-animated-gif.gif"""
        res = """
        Hey everyone!
        I'm three years old, today!
        With your help, I've recorded a LOT different incidents with the VM environments!
        Please keep up the good work!
        """

        inChannelResponse('CC568PC3X',gif)
        inChannelResponse('CC568PC3X',res)
        return

def year4():
        # Oct 25 2019
        gif = """http://bestanimations.com/Holidays/Birthday/birthdaygifs/birthday-candles-happy-bday-wishes-animated-gif.gif"""
        res = """
        Hey everyone!
        I'm four years old, today!
        With your help, I've recorded a LOT different incidents with the VM environments!
        Please keep up the good work!
        """

        inChannelResponse('CC568PC3X',gif)
        inChannelResponse('CC568PC3X',res)
        return

def year5():
        # Oct 25 2019
        gif = """http://bestanimations.com/Holidays/Birthday/birthdaygifs/birthday-candles-happy-bday-wishes-animated-gif.gif"""
        res = """
        Hey everyone!
        I'm five years old, today!
        With your help, I've recorded a LOT different incidents with the VM environments!
        Please keep up the good work!
        """

        inChannelResponse('CC568PC3X',gif)
        inChannelResponse('CC568PC3X',res)
        return


def testJOBPast():
    gif = """http://bestanimations.com/Holidays/Birthday/birthdaygifs/birthday-candles-happy-bday-wishes-animated-gif.gif"""
    res = """
    PAST PAST
    """

    inChannelResponse('GDJEY6HJN',gif)
    inChannelResponse('GDJEY6HJN',res)
    return

def testJOBFuture():
    gif = """http://bestanimations.com/Holidays/Birthday/birthdaygifs/birthday-candles-happy-bday-wishes-animated-gif.gif"""
    res = """
    Current Current Current Current Current
    """

    inChannelResponse('GDJEY6HJN',gif)
    inChannelResponse('GDJEY6HJN',res)
    return

def checkDate(scheduler, someDateTime, jobName):
    currentTime = datetime.now()
    if someDateTime > currentTime:
        scheduler.add_job(jobName, 'date',run_date=someDateTime)
    return

bDay = BackgroundScheduler()

checkDate(bDay,datetime(2019,2,7,2,15,30),testJOBFuture)

checkDate(bDay,datetime(2019,1,25,12,35,30),mos3)
checkDate(bDay,datetime(2019,4,25,12,15,30),mos6)
checkDate(bDay,datetime(2019,7,25,12,35,30),mos9)
checkDate(bDay,datetime(2019,10,25,12,15,30),year1)
checkDate(bDay,datetime(2020,10,25,12,15,30),year2)
checkDate(bDay,datetime(2021,10,25,12,15,30),year3)
checkDate(bDay,datetime(2022,10,25,12,15,30),year4)
checkDate(bDay,datetime(2023,10,25,12,15,30),year5)

bDay.start()

#########################################################
#########################################################
##############   End of scheduled events   ##############
#########################################################
#########################################################

if __name__ == "__main__":
	if slack_client.rtm_connect(with_team_state=False):
		stdOut("Snek Bot connected and running!")
		# Read bot's user ID by calling Web API method `auth.test`
		snekBotID = slack_client.api_call("auth.test")["user_id"]
		while True:
			try:
				command, channel,usr,stp = parseSlackInput(slack_client.rtm_read())
				schedule.run_pending()
				if command:
					handle_command(command, channel,usr,stp)
			except:
				pass

			time.sleep(RTM_READ_DELAY)
	else:
		pass
		stdOut("Connection failed. Exception traceback above.")
