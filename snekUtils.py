CLIENT = None

class Command:
    def __init__(self, name, response, action, description):
        self.name = name
        self.response = response
        self.description = description
        self.action = action

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

def directResponse(channel, someUser, text):
    CLIENT.chat_postMessage(
        channel=someUser,
        text=text,
        as_user=True
        )