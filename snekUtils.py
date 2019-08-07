import snekAdapter as adapter

########################
###   Slack client   ###
########################

# The main client
# used to send the commands to the server

CLIENT = None

####################
###   Statuses   ###
####################

# Record of the woes faced by our environment

RECONNECT = "Auto reconnect"
WINDOW = "Window closes"
LOADING = "Loading"
RESTART = "Restart IE"

DEFAULT_STATUS = "Non-Specific Error"

#############################
###   Status conversion   ###
#############################

# Changes our emoji into something more ... useful

STATUS_DICTIONARY = {

	"face_vomiting":RECONNECT,

	"fire":WINDOW,

	"loading":LOADING,

	"skull_and_crossbones":RESTART,
	"angry_skeletor":RESTART,
    "dumpster_fire":RESTART
    
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

##########################
###   Convert status   ###
##########################

# converts the emoji to a human-readable status

def convertStatus (stat): 
	if stat not in STATUS_DICTIONARY:
		return DEFAULT_STATUS
		
	return STATUS_DICTIONARY[stat]

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