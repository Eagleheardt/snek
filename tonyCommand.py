import publicCommands
import adminCommands
commandList = []
commandList = publicCommands.published + adminCommands.published

def checkCommand(text, option):
    for name in option.name:
        if text.lower().startswith(name.lower()):
            return True
    return False

def runCommand(payload):
    if 'text' in payload['data']:
        data = payload['data']
        text = data['text'].strip(' ')   
        text = text[1:]
        for option in commandList:
            if checkCommand(text, option):
                option_method = getattr(option.source, option.method.__name__)
                if option_method:
                    option.method(payload)


