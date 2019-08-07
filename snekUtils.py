# import snekAdapter as adapter

########################
###   Slack client   ###
########################

# The main client
# used to send the commands to the server

CLIENT = None

###################
###   Globals   ###
###################

PATH = "/home/ubuntu/"

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

def parsePayload(data):
    text = data['text'].lower().strip()
    channel = data['channel']
    aUser = data['user']
    stamp = data['ts']

    return text, channel, aUser, stamp

##########################
###   Convert status   ###
##########################

# converts the emoji to a human-readable status

def convertStatus (stat): 
	if stat not in __STATUS_DICTIONARY:
		return __DEFAULT_STATUS
		
	return __STATUS_DICTIONARY[stat]

#############################
###   Response Commands   ###
#############################

def inChannelResponse(channel, response):
    CLIENT.chat_postMessage(
        channel=channel,
        text=response,
        as_user=True
        )

def threadedResponse(channel, response, stamp):
    CLIENT.chat_postMessage(
        channel=channel,
        text=response,
        thread_ts=stamp,
        as_user=True
    )

def directResponse(aUser, response):
    CLIENT.chat_postMessage(
        channel=aUser,
        text=response,
        as_user=True
        )