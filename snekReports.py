import snekUtils as utils
import snekResponse as words
from snekUtils import Command

publishedCommands = []

# if command == "!snekpets":
#     addPet(aUser, "snekpets")
#     directResponse(aUser,getPets())
#     return

# if command.startswith("!report"): # if the message starts with the string "!report" this goes off
#     theDate = command[8:]
#     response = EODReport(theDate)
#     directResponse(aUser,response)
#     return

# if command.startswith("!range"):
#     theDates = command[7:]
#     date1,date2 = parseDateRange(theDates)
#     response = historicalReport(date1,date2)
#     directResponse(aUser,response)
#     return

# if command.startswith("!mike"):
#     theDates = command[6:]
#     date1,date2 = parseDateRange(theDates)
#     response = mikeReport(date1,date2)
#     directResponse(aUser,response)
#     return

# if command.startswith("!gary"):
#     theDates = command[6:]
#     date1,date2 = parseDateRange(theDates)
#     response = garyReport(date1,date2)
#     directResponse(aUser,response)
#     return

# if command == "!howmany":
#     allStat = getReports('2018-01-01', '9999-12-31')
#     directResponse(aUser,"So far I've eaten {0} problems.".format(allStat))
#     return
