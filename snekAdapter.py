import databaseProvider as sql
import snekUtils as utils
import datetime
import random

DATABASE = utils.PATH + "snekBotTest/data/snekbot.db" # prod location
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
	
	return results
	
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
	return results

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
	
	return results

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
	
	return results

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

	return results

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
	
	return newStr

