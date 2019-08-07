import snekStrikes as act

commandList = act.publishedCommands

def isVM(someText=''):
    if someText.startswith('vm'):
        return True
    return False

def isBang(someText=''):
    if someText.startswith('!'):
        return True
    return False
 

def EVAL(payload):
    if 'text' not in payload['data']:
        return

    data = payload['data']
    print(data)

    text = data['text'].lower().strip()

    if isVM(text):
        print("VM")
        pass

    if isBang(text):
        print("bang bang")
        text = text.lstrip("!")
        pass

    

    return