import snekStrikes as action
import snekReports as reporting
import snekUtils as utils

__commandList = action.publishedCommands + reporting.publishedCommands

def dumpsterFire(someText=''):
    if someText == "f5 :dumpster_fire:":
        return True
    return False

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

def EVAL(data):
    text = data['text'].lower().strip()
    userID = data['user']

    if dumpsterFire(text):
        # TODO send I'm sorry
        pass

    if isVM(text):
        # Call VM command
        # TODO evaluate VM issues
        
        return

    if isBang(text):
        text = text.lstrip("!")
        for option in __commandList:
            if checkCommand(text, option):
                option_method = getattr(option.name, option.actions.__name__)
                if option_method:
                    option.actions(data)
                    return

    return