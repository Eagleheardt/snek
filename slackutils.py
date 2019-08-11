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
    print("date congert")

    try:
        print("1")
        datetimeObject = dt.strptime(someDate, '%Y-%m-%d')
        print(datetimeObject.strftime("%m/%d/%Y"))
        return datetimeObject
    except:
        pass

    try:
        print("3")
        datetimeObject = dt.strptime(someDate, '%m/%d/%Y')
        print(datetimeObject.strftime("%m/%d/%Y"))
        return datetimeObject
    except:
        pass

    return None

def sanitizeID(slackID=''):
    return slackID.replace('<', '').replace('>','').replace('@','').upper()


def reconstitueID(slackID=''):
    return '<@{}>'.format(slackID)