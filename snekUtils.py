import slackutils as utils
import datetime
import re

###################
###   Globals   ###
###################

# Snek's birthday is October 25, 2018
SNEK_BIRTHDAY = datetime.datetime(2018, 10, 25)
WORKING_PATH = "/home/ubuntu/"
DATABASE_PATH = "snekTest/data/newSnek.db"
KEY_PATH = "snekTest/data/snekTest"
VM_CHANNEL = "CC568PC3X"
MAX_REPORTS = 3

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
	report += "Total reports: {}".format(totalReports[0][0])

	return report

def parseMultiDayReport(sqlPayload, aDate1, aDate2, totalReports):
	report = "Report for: {} to {}\n".format(aDate1, aDate2)
	report += parseStandardReport(sqlPayload)	
	report += "Total reports: {}".format(totalReports[0][0])

	return report

# mike report

# newStr = "Report for: " + date1 + " to " + date2 + "\n"
# 	for row in results:
# 		i = 1
# 		for item in row:
# 			if i == 1:
# 				newStr += "TimeStamp: " + str(item) + " - "
# 			if i == 2:
# 				newStr += "VM: " + str(item) + " - "
# 			if i == 3:
# 				newStr += "Status: " + str(item)
# 			i += 1
# 		newStr += "\n"

# 	newStr += ("\nTotal reports: {0}").format(getReports(date1, date2))


# gary report

# newStr = "Report for: " + date1 + " to " + date2 + "\n"
# 	for row in results:
# 		i = 1
# 		for item in row:
# 			if i == 1:
# 				newStr += "Week Start: " + str(item) + " - "
# 			if i == 2:
# 				newStr += "Status: " + str(item)
# 			if i == 3:
# 				if int(item) > 1:
# 					newStr += " - " + str(item) + " times"
# 				else:
# 					newStr += " - " + str(item) + " time"
# 			i += 1
# 		newStr += "\n"
#   return newStr

# get pets

# newStr = "People do lots of things to me! I love pets most of all, though!\nI have been:\n"
# 	for row in rawResults:
# 		i = 1
# 		for item in row:
# 			if i == 1:
# 				newStr += str(item) + ": "
# 			if i == 2:
# 				newStr += str(item) + " times"
# 			i += 1
# 		newStr += "\n"
        # return newStr


#I'm sorry

# allLinks = []
# for aLink in results:
# 		allLinks.append(aLink)
# return (random.choice(allLinks))