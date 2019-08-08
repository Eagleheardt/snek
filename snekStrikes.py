import snekUtils as utils
import snekResponse as words
from snekUtils import Command

publishedCommands = []

#############################
###   Response Commands   ###
#############################

def inChannelResponse(payLoad, response):
    utils.inChannelResponse(payLoad['channel'], response)
    return

def threadedResponse(payLoad, response):
    utils.threadedResponse(payLoad['channel'], response, payLoad['ts'])
    return

def directResponse(payLoad, response):
    utils.directResponse(payLoad['user'], response)
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
        inChannelResponse(payLoad, self.response)
        return

publishedCommands.append(ExampleCommand())

#############################################################

########################
###   Help Command   ###
########################

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
        threadedResponse(payLoad, self.response)
        return

publishedCommands.append(HelpCommand())

#############################################################

########################
###   Pet Command   ###
########################

class PetCommand(Command):
    def __init__(self):
        super().__init__(
            name = PetCommand, 
            response = words.textPet,
            actions = self.doSomething, 
            triggers = ['pet'],
            description =\
                """
                    This is the pet command.
                    It lets you give Snek a pet.
                    It also records this action.
                """
            )

    def doSomething(self, payLoad):
        threadedResponse(payLoad, self.response)
        return

publishedCommands.append(PetCommand())

#############################################################

#########################
###   Tread Command   ###
#########################

class TreadCommand(Command):
    def __init__(self):
        super().__init__(
            name = TreadCommand, 
            response = words.textTread,
            actions = self.doSomething, 
            triggers = ['tread'],
            description =\
                """
                    This is the tread command.
                    It lets you tread on Snek.
                    Why would you do this?
                """
            )

    def doSomething(self, payLoad):
        threadedResponse(payLoad, self.response)
        return

publishedCommands.append(PetCommand())

#############################################################