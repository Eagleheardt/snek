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

###########################
###   General parsers   ###
###########################

# removes all decoration from a user ID
# use when needing to get ID from inside a message

def sanitizeID(slackID=''):
    return slackID.replace('<', '').replace('>','').replace('@','').upper()

# adds the decoration back to an ID
# use when calling out a person by name in a channel

def reconstitueID(slackID=''):
    return '<@{}>'.format(slackID)

# renames a link to something more readable
# use when you want to hide ugly URLs

def linkFormatter(someURL='',someText=''):
    return "<{}|{}>".format(someURL, someText)
