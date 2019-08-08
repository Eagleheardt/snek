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
        inChannelResponse(payLoad['channel'],self.response)
        return

publishedCommands.append(ExampleCommand())

#############################################################

###########################
###   Example Command   ###
###########################

class HelpCommand(Command):
    def __init__(self):
        super().__init__(
            name = HelpCommand, 
            response = words.textHelp,
            actions = self.doSomething, 
            triggers = ['help'],
            description =\
                """
                    This is the help command.
                    It gives a list of all the ways the public can interact with Snek.
                    There are a few commands left off, both for brevity and to keep spam down.
                """
            )

    def doSomething(self, payLoad):
        inChannelResponse(payLoad['channel'],self.response)
        return

publishedCommands.append(HelpCommand())

#############################################################
