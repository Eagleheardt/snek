textExample =\
"""
This is the sample text for Snek.
In the code, it shows an example of 3 quotation notation. 
It also shows how to declare a variable on one 
line and put the value on the next line.
"""

textHelp =\
"""
I'm Snek! Here's how I can help!
				
If you just report VM issues, I will eat and store them!
Vm[#] [status] to report! That's it!
Don't bother editing your response, just say it again, if I don't eat it.
:face_vomiting: = Auto reconnect
:fire: = Window Closes
:skull_and_crossbones: = Restart IE completely
:loading: = Loading
	
!help - display this message.
!pet - I love the pets!
!report[SPACE][YYYY-MM-DD] - gives a breakdown of all the server statuses reported for that day.
!range[SPACE][YYYY-MM-DD],[YYYY-MM-DD] - gives a breakdown of all the server statuses reported for that date range.
!mike[SPACE][YYYY-MM-DD],[YYYY-MM-DD] - WARNING: huge report! Gives a breakdown of the time, the server, and the status for that date range.
!gary[SPACE][YYYY-MM-DD],[YYYY-MM-DD] - WARNING: huge report! Gives a breakdown of the the week, the status, and the number of times occurred.
"""

textCantEat = "I can't eat that!"

textEat = "You have fed Snek."

textTotalProblems = "So far I've eaten {} problems."

textSorry = "I'm sorry for the unstable environment. Let me send you something to brighten your mood!"

textPet = "You pet Snek. Snek is happy."

textTread = "No tread on Snek. Snek is friend."

textProvoke = "Feed Snek. No provoke."

textPoke = "You poke Snek. Why poke Snek?"

textHug = "You hug Snek. Snek is love. Snek is life."

textStep = "Watch for Snek. Snek helps!"

textBoop = "Boop Snek snoot. Doot doot."

textKiss = "You lean in close and kiss Snek. Snek blushes!"

textThousandGif = "<http://gph.is/28NyLmU|{}th issue!>"
textThousandFlags = ":rsi: " * 16
textThousandInfo =\
"""
I have just received report number {0}!
Everyone, please keep your heads up!
I'm listening to your problems, and they are being recorded!
As long as you keep reporting issues, we will fight for a more stable environment!
"""

textYearGif = "http://gph.is/2fVdfmI"

	# if command == "!snekpets":
	# 	addPet(aUser, "snekpets")
	# 	directResponse(aUser,getPets())
	# 	return

	# if command.startswith("!report"): # if the message starts with the string "!report" this goes off
	# 	theDate = command[8:]
	# 	response = EODReport(theDate)
	# 	directResponse(aUser,response)
	# 	return

	# if command.startswith("!range"):
	# 	theDates = command[7:]
	# 	date1,date2 = parseDateRange(theDates)
	# 	response = historicalReport(date1,date2)
	# 	directResponse(aUser,response)
	# 	return

	# if command.startswith("!mike"):
	# 	theDates = command[6:]
	# 	date1,date2 = parseDateRange(theDates)
	# 	response = mikeReport(date1,date2)
	# 	directResponse(aUser,response)
	# 	return

	# if command.startswith("!gary"):
	# 	theDates = command[6:]
	# 	date1,date2 = parseDateRange(theDates)
	# 	response = garyReport(date1,date2)
	# 	directResponse(aUser,response)
	# 	return

	# if command == "!howmany":
	# 	allStat = getReports('2018-01-01', '9999-12-31')
	# 	directResponse(aUser,"So far I've eaten {0} problems.".format(allStat))
	# 	return

	# if command == "f5 :dumpster_fire:":
	# 	aLink = imSorry(conn)
    #             sryMsg = "I'm sorry for the unstable environment. Let me send you something to brighten your mood!"
    #             inChannelResponse(channel,sryMsg)
    #             directResponse(aUser,aLink)
	# 	return

	# if command.startswith("vm"):
	# 	vm, stat = parseVM(command)
	# 	if not stat:
	# 		if len(command) > 10: # if the message is longer than 10 characters, it probably wasn't meant to be viewed
	# 			return
	# 		inChannelResponse(channel,"I can't eat that!") # goes off to remind folks that you need the emoji status
	# 		return
	# 	insertStatus(vm, stat)
	# 	insertHistory(vm, stat)
    #     insertUserHistory(vm, stat, aUser)
	# 	inChannelResponse(channel,"You have fed Snek.")

	# 	currentDT = datetime.now()
	# 	currentDT = currentDT.strftime("%Y-%m-%d %H:%M:%S")

	# 	stdOut(("Snek|{0}|{1}|{2}|{3}").format(currentDT, checkInt(vm), convertStatus(stat), aUser))
	# 	allStat = getReports('2018-01-01', '9999-12-31')
	# 	if (allStat % 1000) == 0: # shoots off every 1k issues logged
	# 		gif, info = celebrate(allStat)
	# 		inChannelResponse('CC568PC3X',gif)
	# 		inChannelResponse('CC568PC3X',info)
	# 	return