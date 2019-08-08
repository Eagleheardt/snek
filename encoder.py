###################################################################
#                                                                 #
#   This will create a key and encrypt a string against that key  #
#                                                                 #
###################################################################

from cryptography.fernet import Fernet

key = Fernet.generate_key()

# Python3 syntax:
keyName = input("Enter the name of the key file:\n")

# Python 2.7 syntax:
# keyName = raw_input("Enter the name of the key file:\n")

keyFileName =  (('{0}.key').format(keyName))

keyFile = open(keyFileName, 'wb')
keyFile.write(key)
keyFile.close()

# Python3 syntax:
token = input("Paste slack token:\n")

# Python 2.7 syntax:
# token = raw_input("Paste slack token:\n")

message = token.encode()
f = Fernet(key)
encrypted = f.encrypt(message)

encryptedFileName = (('{0}.encrypted').format(keyName))

encodedTokenFile = open(encryptedFileName,'wb')

encodedTokenFile.write(encrypted)
encodedTokenFile.close()
