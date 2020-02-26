import snekStrikes as action
import snekReports as reporting
import snekUtils as utils
import snekVMHandler as vmh

__commandList = action.publishedCommands + reporting.publishedCommands

def dumpsterFire(someText=''):
    if someText == "f5 :dumpster_fire:" or someText == "f5 :cute_dumpster_fire:":
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
        fire = action.DumpsterCommand()
        fire.actions(data)
        return

    if isVM(text):
        vmh.insertStatus(data, utils.MAX_REPORTS)
        return

    if isBang(text):
        text = text.lstrip("!")
        for option in __commandList:
            if checkCommand(text, option):
                option_method = getattr(option.name, option.actions.__name__)
                if option_method:
                    option.actions(data)
                    return

            if checkStart(text, option):
                option_method = getattr(option.name, option.actions.__name__)
                if option_method:
                    option.actions(data)
                    return
    return