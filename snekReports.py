import snekUtils as utils
import snekAdapter as adapter
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
            response = None,
            actions = self.doSomething, 
            triggers = None,
            description =\
                """
                    This is the description
                """
            )

    def doSomething(self, payLoad):
        inChannelResponse(payLoad, self.response)
        return

# publishedCommands.append(ExampleCommand())

#############################################################

############################
###   Snekpets Command   ###
############################

class SnekpetsCommand(Command):
    def __init__(self):
        super().__init__(
            name = SnekpetsCommand, 
            response = None,
            actions = self.doSomething, 
            triggers = ['snekpets','getpets','allpets','sneksnek'],
            description =\
                """
                    This is the snekpets command.
                    It will return a list of all the interactions with Snek.
                    Hopefully there is more good than bad.
                    If someone is abusing Snek, they will be reported to HR.
                """
            )

    def doSomething(self, payLoad):
        # sql.get snek pets
        # utils. parse snek pets
        # response = parsed pets
        directResponse(payLoad, response)
        return

# publishedCommands.append(SnekpetsCommand())

#############################################################

##########################
###   Report Command   ###
##########################

class ReportCommand(Command):
    def __init__(self):
        super().__init__(
            name = ReportCommand, 
            response = None,
            actions = self.doSomething, 
            triggers = ['report'],
            description =\
                """
                    This is the report command.
                    It will return a list of the issues on a single day.
                """
            )

    def doSomething(self, payLoad):
        text = payLoad['text']
        try:
            date = utils.dateExtractor(utils.ONE_DATE, text)
            if date is None:
                return
            sqlResults = adapter.singleDayReport(date)
            totalReports = adapter.reportCount(date, date)
            response = utils.parseSingleDayReport(sqlResults, date, totalReports) # parse the payload
        except:
            return

        directResponse(payLoad, response)
        return

publishedCommands.append(ReportCommand())

#############################################################

#########################
###   Range Command   ###
#########################

class RangeCommand(Command):
    def __init__(self):
        super().__init__(
            name = RangeCommand, 
            response = None,
            actions = self.doSomething, 
            triggers = ['range', 'multiple', 'multi', 'many'],
            description =\
                """
                    This is the range command.
                    It will return a list of the issues on a single day.
                """
            )

    def doSomething(self, payLoad):
        text = payLoad['text']
        try:
            dateBlock = utils.dateExtractor(utils.DATE_RANGE, text)
            if dateBlock is None:
                return

            date1, date2 = utils.dateSplitter(dateBlock)

            sqlResults = adapter.multiDayReport(date1, date2)
            totalReports = adapter.reportCount(date1, date2)
            response = utils.parseMultiDayReport(sqlResults, date1, date2, totalReports) # parse the payload
        except Exception as e:
            print(e)
            return

        directResponse(payLoad, response)
        return

publishedCommands.append(RangeCommand())

#############################################################

###########################
###   Howmany Command   ###
###########################

class HowmanyCommand(Command):
    def __init__(self):
        super().__init__(
            name = HowmanyCommand, 
            response = words.textTotalProblems,
            actions = self.doSomething, 
            triggers = ['howmany'],
            description =\
                """
                    This is the howmany command.
                    It will return a simple message of how many issues have been reported
                    in a direct message.
                """
            )

    def doSomething(self, payLoad):
        totalReports = adapter.getTotalReports()
        inChannelResponse(payLoad, self.response.format(totalReports))
        return

publishedCommands.append(HowmanyCommand())

#############################################################

##############################
###   MikeReport Command   ###
##############################

class MikeReportCommand(Command):
    def __init__(self):
        super().__init__(
            name = MikeReportCommand, 
            response = None,
            actions = self.doSomething, 
            triggers = ['mike'],
            description =\
                """
                    This is the MikeReport command.
                    It will return a report of ...
                """
            )

    def doSomething(self, payLoad):
        text = payLoad['text']
        try:
            dateBlock = utils.dateExtractor(utils.DATE_RANGE, text)
            if dateBlock is None:
                return

            date1, date2 = utils.dateSplitter(dateBlock)
            totalReports = adapter.reportCount(date1, date2)
            if totalReports > utils.MAX_RETURN:
                directResponse(payLoad, utils.textTooMuchInfo)
                return
            
            sqlResults = adapter.mikeReport(date1, date2)
            
            response = utils.parseMultiDayReport(sqlResults, date1, date2, totalReports) # parse the payload
        except Exception as e:
            print(e)
            return

        directResponse(payLoad, response)
        return

publishedCommands.append(MikeReportCommand())

#############################################################

##############################
###   GaryReport Command   ###
##############################

class GaryReportCommand(Command):
    def __init__(self):
        super().__init__(
            name = GaryReportCommand, 
            response = None,
            actions = self.doSomething, 
            triggers = ['gary'],
            description =\
                """
                    This is the GaryReport command.
                    It will return a report of ...
                """
            )

    def doSomething(self, payLoad):
        text = payLoad['text']
        try:
            dateBlock = utils.dateExtractor(utils.DATE_RANGE, text)
            if dateBlock is None:
                return

            date1, date2 = utils.dateSplitter(dateBlock)
            totalReports = adapter.reportCount(date1, date2)
            if totalReports > utils.MAX_RETURN:
                directResponse(payLoad, utils.textTooMuchInfo)
                return
            
            sqlResults = adapter.garyReport(date1, date2)
            
            response = utils.parseMultiDayReport(sqlResults, date1, date2, totalReports) # parse the payload
        except Exception as e:
            print(e)
            return

        directResponse(payLoad, response)
        return

publishedCommands.append(GaryReportCommand())

#############################################################