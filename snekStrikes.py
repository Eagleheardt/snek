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
            triggers = ['test'],
            description =\
                """
                    This is the description
                """
            )

    def doSomething(self, payLoad):
        print("Example Command!!!!")
        print(payLoad)
        print(self.response)
        return

publishedCommands.append(ExampleCommand())

#########################################################

class HelpCommand(Command):
    self.name = "HelpCommand"
    self.response = words
    self.description =\
    """
        This is the description
    """