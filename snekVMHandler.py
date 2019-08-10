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

######################
###   Odd colons   ###
######################

# does the message contain an odd number of colons?

def oddColons(someText=''):
	return bool(someText.count(":") % 2)

########################
###   Parse status   ###
########################

# Breaks up a message starting with "VM"
# This is the main purpose of Snek!

def parseStatus(text=''): 

	if oddColons(text):
		return 99, None 
	
	# emojis are bound on either side with a colon.
	# if there is an odd number of colons in any message, 
	# perhaps it was just a maintenance announcement?

	text = text.lstrip("vm").strip() # removes the VM and whitespace from the original text

	emojiList = text.split(":") # splits it apart by emoji/colons
	emojiList = list(map(str.strip, emojiList)) # removes the whitespace from all objects

	VMServerPart = emojiList.pop(0) # removes and returns the first item in the list 
	VMServer, rest = VMServerPart.split(" ", 1) # should be our VM number
	del rest # garbage collection

	if not emojiList:
		return 99, None # if there's nothing left, get out

	VMServer = checkInt(VMServer) # makes sure it's a number, else it's 99

	emojiList = list(filter(None, emojiList)) # removes the blanks from the list

	return VMServer, emojiList