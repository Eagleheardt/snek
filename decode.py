from cryptography.fernet import Fernet

MAIN_KEY = None

def getToken():
    keyFile = open('{}.key'.format(MAIN_KEY), 'rb')
    key = keyFile.read()
    keyFile.close()

    f = Fernet(key)

    encryptedTokenFile = open('{}.encrypted'.format(MAIN_KEY), 'rb')
    encryptedToken = encryptedTokenFile.read()

    decryptedToken = f.decrypt(encryptedToken)

    SLACK_BOT_TOKEN = decryptedToken.decode()

    return SLACK_BOT_TOKEN