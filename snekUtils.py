# import snekAdapter as adapter

########################
###   Slack client   ###
########################

# The main client
# used to send the commands to the server

CLIENT = None

#############################
###   Response Commands   ###
#############################

def inChannelResponse(channel, response):
    CLIENT.chat_postMessage(
        channel=channel,
        text=response,
        as_user=True
        )
    return

def threadedResponse(channel, response, stamp):
    CLIENT.chat_postMessage(
        channel=channel,
        text=response,
        thread_ts=stamp,
        as_user=True
        )
    return

def directResponse(aUser, response):
    CLIENT.chat_postMessage(
        channel=aUser,
        text=response,
        as_user=True
        )
    return

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

