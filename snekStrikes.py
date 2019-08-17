import slackutils as utils
import snekResponse as words
import snekAdapter as adapter
from snekUtils import Command
import presenceHandler as ph
import random

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

def ephemeralResponse(payLoad, response):
    utils.ephemeralResponse(payLoad['channel'], response, payLoad['user'])

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
        ph.checkStatus()
        ephemeralResponse(payLoad, self.response)
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
        adapter.addPet(payLoad['user'], 'help')
        threadedResponse(payLoad, self.response) # reply
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
        adapter.addPet(payLoad['user'], 'pet')
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
        adapter.addPet(payLoad['user'], 'tread')
        threadedResponse(payLoad, self.response)
        return

publishedCommands.append(TreadCommand())

#############################################################

###########################
###   Provoke Command   ###
###########################

class ProvokeCommand(Command):
    def __init__(self):
        super().__init__(
            name = ProvokeCommand, 
            response = words.textProvoke,
            actions = self.doSomething, 
            triggers = ['provoke'],
            description =\
                """
                    This is the provoke command.
                    It lets you provoke Snek.
                    Apparently some people wanted this.
                """
            )

    def doSomething(self, payLoad):
        adapter.addPet(payLoad['user'], 'provoke')
        threadedResponse(payLoad, self.response)
        return

publishedCommands.append(ProvokeCommand())

#############################################################

########################
###   Poke Command   ###
########################

class PokeCommand(Command):
    def __init__(self):
        super().__init__(
            name = PokeCommand, 
            response = words.textPoke,
            actions = self.doSomething, 
            triggers = ['poke'],
            description =\
                """
                    This is the poke command.
                    It lets you poke Snek.
                    You are hurt inside.
                """
            )

    def doSomething(self, payLoad):
        adapter.addPet(payLoad['user'], 'poke')
        threadedResponse(payLoad, self.response)
        return

publishedCommands.append(PokeCommand())

#############################################################

#######################
###   Hug Command   ###
#######################

class HugCommand(Command):
    def __init__(self):
        super().__init__(
            name = HugCommand, 
            response = words.textHug,
            actions = self.doSomething, 
            triggers = ['hug'],
            description =\
                """
                    This is the hug command.
                    It lets you give Snek a hug.
                    You will certainly have a good day!
                """
            )

    def doSomething(self, payLoad):
        adapter.addPet(payLoad['user'], 'hug')
        threadedResponse(payLoad, self.response)
        return

publishedCommands.append(HugCommand())

#############################################################

########################
###   Step Command   ###
########################

class StepCommand(Command):
    def __init__(self):
        super().__init__(
            name = StepCommand, 
            response = words.textStep,
            actions = self.doSomething, 
            triggers = ['step'],
            description =\
                """
                    This is the step command.
                    You try to step on Snek.
                    I hope that was an accident.
                """
            )

    def doSomething(self, payLoad):
        adapter.addPet(payLoad['user'], 'step')
        threadedResponse(payLoad, self.response)
        return

publishedCommands.append(StepCommand())

#############################################################

########################
###   Boop Command   ###
########################

class BoopCommand(Command):
    def __init__(self):
        super().__init__(
            name = BoopCommand, 
            response = words.textBoop,
            actions = self.doSomething, 
            triggers = ['boop'],
            description =\
                """
                    This is the boop command.
                    You boop Snek right on his snoot!
                    It's just so cute.
                """
            )

    def doSomething(self, payLoad):
        adapter.addPet(payLoad['user'], 'boop')
        threadedResponse(payLoad, self.response)
        return

publishedCommands.append(BoopCommand())

#############################################################

########################
###   Kiss Command   ###
########################

class KissCommand(Command):
    def __init__(self):
        super().__init__(
            name = KissCommand, 
            response = words.textKiss,
            actions = self.doSomething, 
            triggers = ['kiss'],
            description =\
                """
                    This is the kiss command.
                    Do you really love Snek?
                    Show him you do!
                """
            )

    def doSomething(self, payLoad):
        adapter.addPet(payLoad['user'], 'kiss')
        threadedResponse(payLoad, self.response)
        return

publishedCommands.append(KissCommand())

#############################################################

#########################
###   Dumpster Fire   ###
#########################

class DumpsterCommand(Command):
    def __init__(self):
        super().__init__(
            name = DumpsterCommand, 
            response = None,
            actions = self.doSomething, 
            triggers = None,
            description =\
                """
                    This is the Dumpster
                """
            )

    def doSomething(self, payLoad):
        sqlResults = adapter.imSorry()
        allLinks = []
        for aLink in sqlResults:
            allLinks.append(aLink[0])
            
        song = random.choice(allLinks)
        inChannelResponse(payLoad, words.textSorry)
        directResponse(payLoad, song)
        return

# publishedCommands.append(DumpsterCommand())

#############################################################