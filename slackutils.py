import datetime as dt

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

def dateConverter(someDate=''):
    datetimeObject = ''

    try:
        datetimeObject = dt.strptime(someDate, '%m/%d/%y')
        datetimeObject = dt.strptime(someDate, '%Y-%m-%d')
    except:
        pass

    return datetimeObject

def sanitizeID(slackID=''):
    return slackID.replace('<', '').replace('>','').replace('@','').upper()


def reconstitueID(slackID=''):
    return '<@{}>'.format(slackID)