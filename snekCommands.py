import snekStrikes as action
import snekReports as reporting
import snekUtils as utils

__commandList = action.publishedCommands# + reporting.publishedCommands

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
        text = text.lstrip("vm").strip() # removes the VM and whitespace from the original text

        emoji = text.split(":") # splits it apart by emoji
        VMServer = emoji.pop(0) # removes and returns the first item in the list - should be our VM number

        emoji = list(filter(None, emoji)) # removes the blanks from the list
        emoji = map(str.strip, emoji) # removes the whitespace from all objects


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