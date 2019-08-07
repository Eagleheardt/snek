import snekUtils as utils
import snekResponse as words
from snekUtils import Command

publishedCommands = []

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
    def __init__(self):
        super().__init__(
            name = ExampleCommand, 
            response = words.textExample,
            actions = self.doSomething, 
            triggers = ['test', 'example'],
            description =\
                """
                    This is the description
                """
            )

    def doSomething(self, payLoad):
        inChannelResponse(payLoad['data']['channel'],self.response)
        return

publishedCommands.append(ExampleCommand())

#########################################################
