import databaseProvider as sql
import snekUtils as utils
import sqlite3
import datetime
import random

DATABASE = utils.WORKING_PATH + utils.DATABASE_PATH
sql.__MAIN_CONNECTION = (sqlite3.connect(DATABASE, check_same_thread=False)) # prod location

print("SDFLKJ")

####

# CREATE TABLE IF NOT EXISTS "Issues" (
# 'ID' INTEGER PRIMARY KEY AUTOINCREMENT, 
# 'TimeStamp' DATE DEFAULT (datetime('now','localtime')), 
# 'ServerNumber' INTEGER NOT NULL, 
# 'ServerStatus' TEXT NOT NULL, 
# 'SlackID' TEXT NOT NULL DEFAULT 'NONAME'
# );

def insertIssue (server, stat): # adds am Issue as a server number and status
	sql.EXEC(("""
		INSERT INTO 
			Issues (ServerNumber, ServerStatus) 
		VALUES
			({0},'{1}');
	""").format(server,stat))
	return

def singleDayReport(aDate): # Gets a daily summary of the VM number and status reported
	print("singleDayReport")
	cmd = (("""
			SELECT 	
				ServerNumber as [Server]
				, ServerStatus as [Status]
				, count(ServerStatus) as [Amount] 
			FROM 
				Issues 
			WHERE 
				date(TimeStamp) IN ('{0}') 
				AND ServerNumber IN (1, 2, 3, 4, 17) 
			GROUP BY 
				ServerNumber
				, ServerStatus;
			""").format(aDate))
	print(cmd)
	results = sql.GET(cmd)
	print("after")
	print(results)
	return results

def rangeReport (date1, date2): # Gets a range summary of the VM number and status reported
	cmd = (("""
		SELECT 
			ServerNumber as [Server]
			, ServerStatus as [Status]
			, count(ServerStatus) as [Amount]
		FROM 
			Issues
		WHERE 
			date(TimeStamp) BETWEEN '{0}' AND '{1}'
			AND ServerNumber IN (1, 2, 3, 4, 17)
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
			Issues 
		WHERE
			date(TimeStamp) BETWEEN '{0}' AND '{1}' 
			AND ServerNumber IN(1, 2, 3, 4, 17);
	""").format(date1, date2))
	results = SQLReturn(conn,cmd)
	
	return results

def garyReport (date1, date2): # Gets the time, VM number, and status reported across a date range

	cmd = (("""
		SELECT 
			date(Week)
			, ServerStatus
			, count(0) as probs
		FROM (
			SELECT datetime([TimeStamp], 'start of day', 'weekday 1', '-7 day') as Week
				, ServerStatus
			FROM Issues
		) as t
		WHERE 
			Week BETWEEN '{0}' AND '{1}' 
		GROUP BY 
			Week, ServerStatus
		ORDER BY 
			Week, ServerStatus;
	""").format(date1, date2))

	return results

def allIssues():
	return (rangeReport('1999-12-31', '9999-12-31'))

# CREATE TABLE IF NOT EXISTS "Interactions" (
# 'ID' INTEGER PRIMARY KEY AUTOINCREMENT, 
# 'TimeStamp' DATE DEFAULT (datetime('now','localtime')),
# 'User' TEXT NOT NULL DEFAULT 'NONE',
# 'aStatus' TEXT NOT NULL DEFAULT 'NONE'
# );

def addPet(aUser,aStat):  # adds a 'pet' to the database
	sql.EXEC(("""
		INSERT INTO 
			Interactions (User, aStatus)
		VALUES
			('{0}','{1}');
	""").format(aUser,aStat))
	return

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

# CREATE TABLE IF NOT EXISTS "Music" (
# 'ID' INTEGER PRIMARY KEY AUTOINCREMENT, 
# 'Link' TEXT NOT NULL DEFAULT 'www.google.com', 
# 'Description' TEXT NOT NULL DEFAULT 'NOT SET'
# );

def imSorry(aConn): # an appology for the environment in which we live
	sqlCmd = "SELECT Link FROM Music;"
	results = sql.GET(sqlCmd)
	return results

# CREATE TABLE IF NOT EXISTS "Users" (
# 'ID' INTEGER PRIMARY KEY AUTOINCREMENT, 
# 'SlackID' TEXT NOT NULL DEFAULT 'NOID', 
# 'UserName' TEXT NOT NULL DEFAULT 'NONAME'
# );

####