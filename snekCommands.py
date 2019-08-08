import snekStrikes as act
import snekUtils as utils

__commandList = act.publishedCommands

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

def EVAL(payload):
    data = payload['data']
    text = data['text'].lower().strip()

    if dumpsterFire(text):
        # TODO send I'm sorry
        pass

    if isVM(text):
        # TODO evaluate VM issues
        pass

    if isBang(text):
        text = text.lstrip("!")
        for option in __commandList:
            if checkCommand(text, option):
                option_method = getattr(option.name, option.actions.__name__)
                if option_method:
                    option.actions(data)

    return