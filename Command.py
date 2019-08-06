import snekStrikes as act

def isVM(someText=''):
    if someText.startswith('vm'):
        return True
    return False

def isBang(someText=''):
    if someText.startswith('!'):
        return True
    return False
 

def EVAL(payload):
    if 'text' in payload['data']:
        data = payload['data']
        print(data)

    return