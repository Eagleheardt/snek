import databaseProvider as sql
import datetime
import random

DATABASE = "snekBotTest/data/snekbot.db" # prod location
sql.setConnection(DATABASE) # set DB connection


####

# CREATE TABLE IF NOT EXISTS "Status" (
# 'ID' INTEGER PRIMARY KEY AUTOINCREMENT, 
# 'TimeStamp' DATE DEFAULT (datetime('now','localtime')),
# ServerNumber INTEGER NOT NULL, 
# ServerStatus TEXT NOT NULL);

# CREATE TABLE IF NOT EXISTS "SnekStats" (
# ID INTEGER PRIMARY KEY AUTOINCREMENT, 
# TimeStamp DATE DEFAULT (datetime('now','localtime')),
# User TEXT NOT NULL DEFAULT 'NONE',
# aStatus TEXT NOT NULL DEFAULT 'NONE');

# CREATE TABLE History (
# 'ID' INTEGER PRIMARY KEY AUTOINCREMENT, 
# 'TimeStamp' DATE DEFAULT (datetime('now','localtime')), 
# 'ServerNumber' INTEGER NOT NULL, 
# 'ServerStatus' TEXT NOT NULL);

# CREATE TABLE IF NOT EXISTS "Sorry"(
# 'ID' INTEGER PRIMARY KEY AUTOINCREMENT,
# 'Link' TEXT NOT NULL DEFAULT 'www.google.com');

# CREATE TABLE IF NOT EXISTS "User" (
# 'ID' INTEGER PRIMARY KEY AUTOINCREMENT, 
# 'SlackID' TEXT NOT NULL DEFAULT 'NOID', 
# 'UserName' TEXT NOT NULL DEFAULT 'NONAME');

# CREATE TABLE UseHistory (
# 'ID' INTEGER PRIMARY KEY AUTOINCREMENT, 
# 'TimeStamp' DATE DEFAULT (datetime('now','localtime')), 
# 'ServerNumber' INTEGER NOT NULL, 
# 'ServerStatus' TEXT NOT NULL, 
# 'SlackID' TEXT NOT NULL DEFAULT 'NONAME');

####

def insertStatus (server, stat): # adds a server number and status
	serverCursor.execute(("""
		INSERT INTO 
			Status (ServerNumber, ServerStatus) 
		VALUES
			('{0}','{1}');
	""").format(checkInt(server), convertStatus(stat.strip())))
	conn.commit()
	return

def insertHistory (server, stat): # adds a server number and status
	serverCursor.execute(("""
		INSERT INTO 
			History (ServerNumber, ServerStatus) 
		VALUES
			('{0}','{1}');
	""").format(checkInt(server), convertStatus(stat.strip())))
	conn.commit()
	return

def insertUserHistory (server, stat, user): # adds a server number and status
	serverCursor.execute(("""
		INSERT INTO 
			UseHistory (ServerNumber, ServerStatus, SlackID)
		VALUES
			('{0}','{1}','{2}');
	""").format(checkInt(server), convertStatus(stat.strip()), user))
	conn.commit()
	return
	
def EODReport (aDate): # Gets a daily summary of the VM number and status reported
	cmd = (("""
		SELECT 
			ServerNumber as [Server]
			, ServerStatus as [Status]
			, count(ServerStatus) as [Amount]
		FROM 
			Status
		WHERE 
			date(TimeStamp) IN('{0}')
			AND ServerNumber IN(1,2,3,4,17)
		GROUP BY 
			ServerNumber
			,ServerStatus;
	""").format(aDate))
	results = SQLReturn(conn,cmd)
	newStr = "Report for: " + aDate + "\n"
	for row in results:
		i = 1
		for item in row:
			if i == 1:
				newStr += "VM" + str(item) + " - "
			if i == 2:
				newStr += "Status: " + str(item) + " - "
			if i == 3:
				if item != 1:
					newStr += "Reported: " + str(item) + " times"
				else:
					newStr += "Reported: " + str(item) + " time"
			i += 1
		newStr += "\n"
	return newStr
	
def EODReportRange (date1, date2): # Gets a range summary of the VM number and status reported
	cmd = (("""
		SELECT 
			ServerNumber as [Server]
			, ServerStatus as [Status]
			, count(ServerStatus) as [Amount]
		FROM 
			Status
		WHERE 
			date(TimeStamp) BETWEEN '{0}' AND '{1}'
			AND ServerNumber IN('1','2','3','4','17')
		GROUP BY 
			ServerNumber
			,ServerStatus
	""").format(date1, date2))
	results = SQLReturn(conn,cmd)
	newStr = "Report for: " + date1 + " to " + date2 + "\n"
	for row in results:
		i = 1
		for item in row:
			if i == 1:
				newStr += "VM" + str(item) + " - "
			if i == 2:
				newStr += "Status: " + str(item) + " - "
			if i == 3:
				if item != 1:
					newStr += "Reported: " + str(item) + " times"
				else:
					newStr += "Reported: " + str(item) + " time"
			i += 1
		newStr += "\n"
	return newStr

def addPet(aUser,aStat):  #adds a 'pet' to the database
	newCur = conn.cursor()
	newCur.execute(("""
		INSERT INTO 
			SnekStats (User, aStatus)
		VALUES
			('{0}','{1}');
	""").format(aUser,aStat))
	newCur.close()
	conn.commit()
	return

def getReports (date1, date2): # get reports on a date range
	cmd = (("""
		SELECT 
			SUM(AMT)
		FROM
			(SELECT 
				ServerNumber
				, ServerStatus
				, count(ServerStatus) as AMT
			FROM 
				History
			WHERE 
				date(TimeStamp) BETWEEN '{0}' AND '{1}'
				AND ServerNumber IN(1,2,3,4,17)
			GROUP BY 
				ServerNumber
				,ServerStatus
			) src;
	""").format(date1, date2))
	results = SQLReturn(conn, cmd)
	return results[0][0]

def historicalReport (date1, date2): # Gets a range summary of the VM number and status reported
	cmd = (("""
		SELECT 
			ServerNumber as [Server]
			, ServerStatus as [Status]
			, count(ServerStatus) as [Amount]
		FROM 
			History
		WHERE 
			date(TimeStamp) BETWEEN '{0}' AND '{1}'
			AND ServerNumber IN('1','2','3','4','17')
		GROUP BY 
			ServerNumber
			,ServerStatus
	""").format(date1, date2))
	results = SQLReturn(conn,cmd)
	newStr = "Report for: " + date1 + " to " + date2 + "\n"
	for row in results:
		i = 1
		for item in row:
			if i == 1:
				newStr += "VM" + str(item) + " - "
			if i == 2:
				newStr += "Status: " + str(item) + " - "
			if i == 3:
				if item != 1:
					newStr += "Reported: " + str(item) + " times"
				else:
					newStr += "Reported: " + str(item) + " time"
			i += 1
		newStr += "\n"

	newStr += ("\nTotal reports: {0}").format(getReports(date1, date2))
	return newStr

def mikeReport (date1, date2): # Gets the time, VM number, and status reported across a date range
	cmd = (("""
		SELECT 
			TimeStamp
			, ServerNumber
			, ServerStatus
		FROM
			UseHistory 
		WHERE
			date(TimeStamp) BETWEEN '{0}' AND '{1}' 
			AND ServerNumber IN('1','2','3','4','17');
	""").format(date1, date2))
	results = SQLReturn(conn,cmd)
	newStr = "Report for: " + date1 + " to " + date2 + "\n"
	for row in results:
		i = 1
		for item in row:
			if i == 1:
				newStr += "TimeStamp: " + str(item) + " - "
			if i == 2:
				newStr += "VM: " + str(item) + " - "
			if i == 3:
				newStr += "Status: " + str(item)
			i += 1
		newStr += "\n"

	newStr += ("\nTotal reports: {0}").format(getReports(date1, date2))
	return newStr

def garyReport (date1, date2): # Gets the time, VM number, and status reported across a date range
	
	cmd = (("""
		SELECT 
			date(Week)
			, ServerStatus
			, count(0) as Issues
		FROM (
			SELECT datetime([TimeStamp], 'start of day', 'weekday 1', '-7 day') as Week
				, ServerStatus
			FROM UseHistory
		) as t
		WHERE 
			Week BETWEEN '{0}' AND '{1}' 
		GROUP BY 
			Week, ServerStatus
		ORDER BY 
			Week, ServerStatus;
	""").format(date1, date2))
	results = SQLReturn(conn,cmd)
	newStr = "Report for: " + date1 + " to " + date2 + "\n"
	for row in results:
		i = 1
		for item in row:
			if i == 1:
				newStr += "Week Start: " + str(item) + " - "
			if i == 2:
				newStr += "Status: " + str(item)
			if i == 3:
				if int(item) > 1:
					newStr += " - " + str(item) + " times"
				else:
					newStr += " - " + str(item) + " time"
			i += 1
		newStr += "\n"

	return newStr

def getPets(): # returns the amount of love Snek gets
	cmd = """
		SELECT 
			aStatus, COUNT(*) as Amount
		FROM
			SnekStats
		GROUP BY
			aStatus
		ORDER BY
			Amount DESC;
	"""
	rawResults = SQLReturn(conn, cmd)
	newStr = "People do lots of things to me! I love pets most of all, though!\nI have been:\n"
	for row in rawResults:
		i = 1
		for item in row:
			if i == 1:
				newStr += str(item) + ": "
			if i == 2:
				newStr += str(item) + " times"
			i += 1
		newStr += "\n"
	return newStr

def imSorry(aConn): # an appology for the environment in which we live
        sqlCmd = "SELECT Link FROM Sorry;"
        results = SQLReturn(aConn,sqlCmd)
        allLinks = []
        for aLink in results:
                allLinks.append(aLink)
        return (random.choice(allLinks))

def celebrate(aNum): # returns a gif and an inspirational message
    gif = """
    https://media1.giphy.com/media/jKYU63SjCLCKkTmtml/giphy-downsized.gif?cid=6104955e5c06a4d74e61555a51acae3e
    """
    info = ("""
    I have just received report number {0}!
    Everyone, please keep your heads up!
    I'm listening to your problems, and they are being recorded!
	:rsi: :rsi: :rsi: :rsi: :rsi: :rsi: :rsi: :rsi: :rsi: :rsi: :rsi: :rsi: :rsi: 
	As long as you keep reporting issues, we will fight for a more stable environment!
    """.format(aNum))
    return gif, info