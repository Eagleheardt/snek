# import snekAdapter as adapter

###################
###   Globals   ###
###################

PATH = "/home/ubuntu/"

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

####################
###   Statuses   ###
####################

# Record of the woes faced by our environment

__RECONNECT = "Auto reconnect"
__WINDOW = "Window closes"
__LOADING = "Loading"
__RESTART = "Restart IE"

__DEFAULT_STATUS = "Non-Specific Error"

#############################
###   Status conversion   ###
#############################

# Changes our emoji into something more ... useful

__STATUS_DICTIONARY = {

	"face_vomiting":__RECONNECT,

	"fire":__WINDOW,

	"loading":__LOADING,

	"skull_and_crossbones":__RESTART,
	"angry_skeletor":__RESTART,
    "dumpster_fire":__RESTART
    
	}

##########################
###   Convert status   ###
##########################

# converts the emoji to a human-readable status

def convertStatus (stat): 
	if stat not in __STATUS_DICTIONARY:
		return __DEFAULT_STATUS
		
	return __STATUS_DICTIONARY[stat]

def howManyProblems(someText=''):
	emojis = someText.count(":") / 2
	if not(emojis % 2 == 0):
		return -1
	
	return emojis

# def parseVM(vmMsg): # breaks up a message starting with "VM"
#     try:
#         vm, stat, rest = vmMsg.split(':',2) # breaks string into 3 parts on a colon
#         del rest # 'rest' is deleted
#     except: # if there aren't at least 3 parts
#         return False, False # returns double false
#     vm = vm[2:].strip()
#     return vm, stat # returns the VM number and status

# def parseDateRange(someDates): # breaks apart dates
#     date1, date2 = someDates.split(',')
#     return date1.strip(), date2.strip()

##########################################################
# SQL formatters for reports

# EOD report:

# newStr = "Report for: " + aDate + "\n"
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

