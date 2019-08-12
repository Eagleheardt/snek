import datetime
import re
import slackutils as utils

###################
###   Globals   ###
###################

# Snek's birthday is October 25, 2018
SNEK_BIRTHDAY = datetime.datetime(2018, 10, 25)
PATH = "/home/ubuntu/"
VM_CHANNEL = "CC568PC3X"
MAX_REPORTS = 1

#################
###   ReGeX   ###
#################

ONE_DATE = "\d{4}-\d{2}-\d{2}"
DATE_RANGE = "\d{4}-\d{2}-\d{2}, \d{4}-\d{2}-\d{2}"

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

# SQL formatters for reports

def parseSingleDayReport(sqlPayload):
	print(sqlPayload)
	return(sqlPayload)
	# newStr = "Report for: " + aDate + "\n"
	# for row in sqlPayload:
	# 	i = 1
	# 	for item in row:
	# 		if i == 1:
	# 			newStr += "VM" + str(item) + " - "
	# 		if i == 2:
	# 			newStr += "Status: " + str(item) + " - "
	# 		if i == 3:
	# 			if item != 1:
	# 				newStr += "Reported: " + str(item) + " times"
	# 			else:
	# 				newStr += "Reported: " + str(item) + " time"
	# 		i += 1
	# newStr += "\n"
	# return newStr

# EODReport range

# newStr = "Report for: " + date1 + " to " + date2 + "\n"
# 	for row in results:
# 		i = 1
# 		for item in row:
# 			if i == 1:
# 				newStr += "VM" + str(item) + " - "
# 			if i == 2:
# 				newStr += "Status: " + str(item) + " - "
# 			if i == 3:
# 				if item != 1:
# 					newStr += "Reported: " + str(item) + " times"
# 				else:
# 					newStr += "Reported: " + str(item) + " time"
# 			i += 1
# 		newStr += "\n"
# 	return newStr

# historical report

# newStr = "Report for: " + date1 + " to " + date2 + "\n"
# 	for row in results:
# 		i = 1
# 		for item in row:
# 			if i == 1:
# 				newStr += "VM" + str(item) + " - "
# 			if i == 2:
# 				newStr += "Status: " + str(item) + " - "
# 			if i == 3:
# 				if item != 1:
# 					newStr += "Reported: " + str(item) + " times"
# 				else:
# 					newStr += "Reported: " + str(item) + " time"
# 			i += 1
# 		newStr += "\n"

#     newStr += ("\nTotal reports: {0}").format(getReports(date1, date2))
#     return newStr

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

