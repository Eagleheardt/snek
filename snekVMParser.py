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
	print(someText)
	return bool(someText.count(":") % 2)

def parseVM(text=''): # breaks up a message starting with "VM"

	if oddColons(text):
		return 99, None 
	
	# emojis are bound on either side with a colon.
	# if there is an odd number of colons in any message, 
	# perhaps it was just a maintenance announcement?

	text = text.lstrip("vm").strip() # removes the VM and whitespace from the original text

	emoji = text.split(":") # splits it apart by emoji/colons
	emoji = list(map(str.strip, emoji)) # removes the whitespace from all objects

	VMServer = emoji.pop(0) # removes and returns the first item in the list - should be our VM number

	if not emoji or len(emoji[0]) > len(" skull_and_crossbones "):
		return 99, None # This is to attempt to mitigate longer, maintenance style messages

	VMServer = checkInt(VMServer) # makes sure it's a number, else it's 99

	emoji = list(filter(None, emoji)) # removes the blanks from the list

	return VMServer, emoji