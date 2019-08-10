import snekStrikes as action
import snekReports as reporting
import snekUtils as utils

__commandList = action.publishedCommands

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

def checkStart(text, option):
    for trigger in option.triggers:
        if text.startswith(trigger):
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
        print("begin bang")
        for option in __commandList:
            print(option)
            if checkCommand(text, option):
                option_method = getattr(option.name, option.actions.__name__)
                if option_method:
                    option.actions(data)
                    return

        for option in reporting.publishedCommands:
            print(option)
            if checkStart(text, option):
                option_method = getattr(option.name, option.actions.__name__)
                if option_method:
                    option.actions(data)
                    return

    return