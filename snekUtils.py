import slackutils as utils
import datetime
import re

###################
###   Globals   ###
###################

# Snek's birthday is October 25, 2018
SNEK_BIRTHDAY = datetime.date(2018, 10, 25)
# First day of record keeping is November 11, 2018
DAY_ZERO = datetime.date(2018, 11, 12)
WORKING_PATH = "/home/ubuntu/"
DATABASE_NAME = "newSnek.db"
DATABASE_PATH = "snekbot/data/" # prod
# DATABASE_PATH = "snekTest/data/" # test
KEY_PATH = "snekbot/data/snek_token" # prod
# KEY_PATH = "snekTest/data/snekTest" # test
VM_CHANNEL = "CC568PC3X" # #ppl_vm channel
TEST_CHANNEL = "GDJEY6HJN" # #testing channel
MAX_RETURN = 250
MAX_REPORTS = 3

SNEK_TEST_ID = "UM4CZP7TP"
SNEK_ID = "UDKKZD7DG"

MONITOR_START_DELAY_IN_SECONDS = 7500.0 # 125 minutes
MONITOR_RUN_DELAY_IN_SECONDS = 30.0

#################
###   ReGeX   ###
#################

ONE_DATE = "20[1-2][0-9]-(0[1-9]|1[0-2])-([0-2][0-9]|3[0-1])$"
DATE_RANGE = "20[1-2][0-9]-(0[1-9]|1[0-2])-([0-2][0-9]|3[0-1]),\s?20[1-2][0-9]-(0[1-9]|1[0-2])-([0-2][0-9]|3[0-1])$"

#########################
###   Command Class   ###
#########################

# Holds the basics of a command for Snek

class Command:
    def __init__(self, name, response, actions, triggers, description):
        self.name = name
        self.response = response
        self.actions = actions
        self.triggers = triggers
        self.description = description

# End Command Class

##########################################################

#############################
###   Response Commands   ###
#############################

def inChannelResponse(channel, response):
    utils.inChannelResponse(channel, response)
    return

def threadedResponse(channel, response, stamp):
    utils.threadedResponse(channel, response, stamp)
    return

def directResponse(aUser, response):
    utils.directResponse(aUser, response)
    return

def ephemeralResponse(channel, response, aUser):
	utils.ephemeralResponse(channel, response, aUser)

def sanitizeID(slackID=''):
	utils.sanitizeID(slackID)
	return

def reconstitueID(slackID=''):
	utils.reconstitueID(slackID)
	return

def dateConverter(someText=''):
	return utils.dateConverter(someText)

def linkFormatter(someURL='',someText=''):
    return utils.linkFormatter(someURL, someText)

# extract the date
def dateExtractor(pattern='',someText=''):
	extractedDate = re.search(pattern, someText)
	if extractedDate:
		return extractedDate.group(0)
	else:
		return None

def dateSplitter(dateGroup=''):
	d1, d2 = dateGroup.split(',')
	d1 = d1.strip()
	d2 = d2.strip()

	return d1, d2

def validPayload(sqlPayload):
	if sqlPayload:
		return True
	return False

def snekLogger(someText=''):
	curDate = datetime.datetime.today().strftime('%Y-%m-%d')
	curTime = datetime.datetime.now().strftime('%H:%M:%S')
	logFile = open((("/home/ubuntu/logs/snekErr-{0}.log").format(curDate)),"a")
	logFile.write("{} - {}".format(curTime, someText))
	logFile.close()
	return

# SQL formatters for reports

def parseStandardReport(sqlPayload):
	report = ""
	for tupple in sqlPayload:
		tServerNumber = tupple[0]
		tStatus = tupple[1]
		tAmount = tupple[2]
		amt = "time" if int(tAmount) == 1 else "times"

		report += "VM{} - Status: {} - {} {}\n".format(tServerNumber, tStatus, tAmount, amt)
	
	return report

def parseSingleDayReport(sqlPayload, aDate, totalReports):
	report = "Report for: {}\n".format(aDate)
	report += parseStandardReport(sqlPayload)	
	report += "Total reports: {}".format(totalReports)

	return report

def parseMultiDayReport(sqlPayload, aDate1, aDate2, totalReports):
	report = "Report for: {} to {}\n".format(aDate1, aDate2)
	report += parseStandardReport(sqlPayload)	
	report += "Total reports: {}".format(totalReports)

	return report

def parseMikeReport(sqlPayload, aDate1, aDate2, totalReports):
	report = "MikeReport for: {} to {}\n".format(aDate1, aDate2)
	for tupple in sqlPayload:
		tTimeStamp = tupple[0]
		tServer = tupple[1]
		tStatus = tupple[2]

		report += "TimeStamp: {} - VM: {} - Status: {}\n".format(tTimeStamp, tServer, tStatus)

	report += "Total reports: {}".format(totalReports)

	return report

def parseGaryReport(sqlPayload, aDate1, aDate2, totalReports):
	report = "GaryReport for: {} to {}\n".format(aDate1, aDate2)
	for tupple in sqlPayload:
		tWeek = tupple[0]
		tStatus = tupple[1]
		tAmount = tupple[2]
		amt = "time" if int(tAmount) == 1 else "times"

		report += "Week start: {} - Status: {} - {} {}\n".format(tWeek, tStatus, tAmount, amt)

	report += "Total reports: {}".format(totalReports)

	return report

def parsePets(sqlPayload):
	report = "People do lots of things to me! I love pets most of all, though!\nI have been:\n"
	for tupple in sqlPayload:
		tAct = tupple[0]
		tAmount = tupple[1]
		amt = "time" if int(tAmount) == 1 else "times"

		report += "{}: {} {}\n".format(tAct, tAmount, amt)

	return report

def parseTreyReport(listOfInformation):
	snekBorder = (":snek:" * 15)
	snekOverallDecor =\
	"""
	***   Overall Statistics   ***
	"""
	report = ""

	report += snekBorder
	report += "\n\nHere is your monthly Snek status report:\n\n"
	for tupple in sqlPayload:
		tFavePersonMonth = tupple[0]
		tFavePersonMonthReports = tupple[1]

		report += "My favorite person this month was {} who fed me {} times\n".format(tFavePersonMonth, tFavePersonMonthReports)

		tErrantServerMonth = tupple[2]
		tErrantServerMonthReports = tupple[3]

		report += "The most server with the most issues this month was {} who gave me {} problems\n".format(tErrantServerMonth, tErrantServerMonthReports)

		tDayOfMostIssues = tupple[4]
		tDayOfMostIssuesAmount = tupple[5]

		tDayEnding = "th"
		if tDayOfMostIssues.endswith('1'):
			tDayEnding = "st"
			if tDayOfMostIssues.endswith('11'):
				tDayEnding = "th"
		elif tDayOfMostIssues.endswith('2'):
			tDayEnding = "nd"
			if tDayOfMostIssues.endswith('12'):
				tDayEnding = "th"
		elif tDayOfMostIssues.endswith('3'):
			tDayEnding = "rd"
			if tDayOfMostIssues.endswith('13'):
				tDayEnding = "th"
		else:
			tDayEnding = "th"

		report += "The most difficult day this month was the {}{} when I had to eat {} problems\n".format(tDayOfMostIssues, tDayEnding, tDayOfMostIssuesAmount)

		tAverageErrorsPerDayLastMonth = tupple[6]

		report += "This month I ate an average of {} problems each day".format(tDayOfMostIssues, tDayOfMostIssuesAmount)

		tOverallPerson = tupple[7]
		tOverallPersonReports = tupple[8]

		report += snekOverallDecor

		report += "Overall, I've eaten the most from {} who sent me {} problems\n".format(tOverallPerson, tOverallPersonReports)
		
		tOverallErrantServer = tupple[9]
		tOverallErrantServerReports = tupple[10]

		report += "Overall, I've been fed the most from server number {} which has had {} problems\n".format(tOverallErrantServer, tOverallErrantServerReports)

		tAverageErrorsPerDayOverall = tupple[11]

		report += "On average, I eat {} problems per day. Every day.\n\n".format(tAverageErrorsPerDayOverall)

	report += snekBorder
	
	return report

def parseTestTimerReport(sqlPayload):
	report = ""
	for tupple in sqlPayload:
		tAct = tupple[0]
		tAmount = tupple[1]
		amt = "time" if int(tAmount) == 1 else "times"

		report += "{}: {} {}\n".format(tAct, tAmount, amt)

	return report