import snekUtils as utils
import snekResponse as words
from snekUtils import Command

#############################
###   Response Commands   ###
#############################

def inChannelResponse(channel, response):
    utils.inChannelResponse(channel, response)
    return

def threadedResponse(channel, response, stamp):
    utils.threadedResponse(channel, response, stamp)
    return

def directResponse(aUser, response):
    utils.directResponse(aUser, response)
    return

###########################
###   Example Command   ###
###########################

class ExampleCommand(Command):
    self.name = "ExampleCommand"
    self.response = words.textExample
    self.actions = doSomething
    self.triggers = ['test']
    self.description =\
    """
        This is the description
    """
    

    def doSomething():
        pass

#########################################################

class HelpCommand(Command):
    self.name = "HelpCommand"
    self.response = words
    self.description =\
    """
        This is the description
    """