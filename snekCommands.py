import snekStrikes as action
import snekReports as reporting
import snekUtils as utils
import snekVMParser as vmp

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
        VMServer, emoji = vmp.parseVM(text)

        if emoji is None or len(emoji) is 0:
            return # if no emojis, do nothing
        
        for i in emoji:
            testInsert = "This will be inserted: "
            testInsert += "VM: {} Status: {}".format(VMServer, vmp.convertStatus(i))
            print(testInsert)

            # CC568PC3X
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