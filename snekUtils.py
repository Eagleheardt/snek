# import snekAdapter as adapter

###################
###   Globals   ###
###################

# Snek's birthday is October 25, 2018

PATH = "/home/ubuntu/"
VM_CHANNEL = "CC568PC3X"

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

# the woes faced by our environment

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
	"dumpster_fire":__WINDOW,
	"fireball":__WINDOW,

	"loading":__LOADING,
	"slow_bro":__LOADING,
	"sloth":__LOADING,
	"slow_parrot":__LOADING,

	"skull_and_crossbones":__RESTART,
	"angry_skeletor":__RESTART,
    "dumpster_fire":__RESTART
    
	}

##########################
###   Convert status   ###
##########################

# converts the emoji to a human-readable status

def convertStatus(stat=''): 
	if stat not in __STATUS_DICTIONARY:
		return __DEFAULT_STATUS
		
	return __STATUS_DICTIONARY[stat]

####################
###   Checkint   ###
####################

# validates input as integer; returns 99 if it isn't

def checkInt(someText=''): 
	try: 
		return int(someText)
	except ValueError:
		return 99

def oddColons(someText=''):
	return bool(someText.count(":") % 2)

def parseVM(text=''): # breaks up a message starting with "VM"

	if oddColons(text):
		return 99, None

	text = text.lstrip("vm").strip() # removes the VM and whitespace from the original text

	emoji = text.split(":") # splits it apart by emoji
	emoji = list(map(str.strip, emoji)) # removes the whitespace from all objects

	VMServer = emoji.pop(0) # removes and returns the first item in the list - should be our VM number

	if len(emoji[0]) > len(" skull_and_crossbones "):
		return 99, None # This is to attempt to mitigate longer, maintenance style messages

	VMServer = checkInt(VMServer) # makes sure it's a number

	emoji = list(filter(None, emoji)) # removes the blanks from the list

	return VMServer, emoji

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

