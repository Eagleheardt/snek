import snekStrikes as act
import snekUtils as utils

commandList = act.publishedCommands

def isVM(someText=''):
    if someText.startswith('vm'):
        return True
    return False

def isBang(someText=''):
    if someText.startswith('!'):
        return True
    return False

def checkCommand(text, option):
    for trigger in option.triggers:
        if text == trigger:
            return True
    return False

def EVAL(payload):
    data = payload['data']
    text, channel, aUser, stamp = utils.parsePayload(data)

    if isVM(text):
        pass

    if isBang(text):
        text = text.lstrip("!")
        for option in commandList:
            if checkCommand(text, option):
                option_method = getattr(option.name, option.actions.__name__)
                if option_method:
                    option.actions(data)

    

    return