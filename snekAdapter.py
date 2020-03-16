import databaseProvider as sql
import snekUtils as utils
import sqlite3
import datetime
import random

DATABASE = utils.WORKING_PATH + utils.DATABASE_PATH + utils.DATABASE_NAME
sql.__MAIN_CONNECTION = (sqlite3.connect(DATABASE, check_same_thread=False)) # prod location

####

# CREATE TABLE IF NOT EXISTS "Issues" (
# 'ID' INTEGER PRIMARY KEY AUTOINCREMENT, 
# 'TimeStamp' DATE DEFAULT (datetime('now','localtime')), 
# 'ServerNumber' INTEGER NOT NULL, 
# 'ServerStatus' TEXT NOT NULL, 
# 'SlackID' TEXT NOT NULL DEFAULT 'NONAME'
# );

def insertIssue (server, stat, userID): # adds am Issue as a server number and status
	sql.EXEC(("""
		INSERT INTO 
			Issues (ServerNumber, ServerStatus, SlackID) 
		VALUES
			({0},'{1}', '{2}');
	""").format(server,stat, userID))
	return

def singleDayReport(aDate): # Gets a daily summary of the VM number and status reported
	cmd = (("""
			SELECT
				ServerNumber
				, ServerStatus
				, count(ServerStatus)
			FROM 
				Issues 
			WHERE 
				date(TimeStamp) IN ('{0}') 
				AND ServerNumber IN (1, 2, 3, 4, 17, 40, 46, 47, 48 , 49) 
			GROUP BY 
				ServerNumber
				, ServerStatus;
			""").format(aDate))
	results = sql.GET(cmd)
	return results

def multiDayReport (date1, date2): # Gets a range summary of the VM number and status reported
	cmd = (("""
		SELECT 
			ServerNumber
			, ServerStatus
			, count(ServerStatus) as AMT
		FROM 
			Issues
		WHERE 
			date(TimeStamp) BETWEEN '{0}' AND '{1}'
			AND ServerNumber IN (1, 2, 3, 4, 17, 40, 46, 47, 48, 49) 
		GROUP BY 
			ServerNumber
			,ServerStatus
	""").format(date1, date2))
	results = sql.GET(cmd)
	return results

def reportCount(date1, date2):
	cmd = (("""
		SELECT 
			SUM(AMT)
		FROM
			(SELECT 
				ServerNumber
				, ServerStatus
				, count(ServerStatus) as AMT
			FROM 
				Issues
			WHERE 
				date(TimeStamp) BETWEEN '{0}' AND '{1}'
				AND ServerNumber IN (1, 2, 3, 4, 17, 40, 46, 47, 48, 49)
			GROUP BY 
				ServerNumber
				,ServerStatus
			) src;
	""").format(date1, date2))
	results = sql.GET(cmd)
	return results[0][0]

def getTotalReports():
	return (reportCount('1999-12-31', '9999-12-31'))

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
			AND ServerNumber IN (1, 2, 3, 4, 17, 40, 46, 47, 48, 49) ;
	""").format(date1, date2))
	results = sql.GET(cmd)
	
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
	results = sql.GET(cmd)

	return results

def treyReport (): # Gets the monthly report. Should run on the 28th every month. I hope.
	results = []
	DAY_ZERO = "2018-11-12"
	lIssuesThisMonth = ("""
		SELECT 
			count(0) as sTotalIssues
		FROM 
			Issues 
		WHERE 
			TimeStamp BETWEEN 
				datetime('now', 'start of month') 
				AND datetime('now', 'localtime')
		AND ServerNumber IN (1, 2, 3, 4, 17, 40, 46, 47, 48, 49);
	""")
	lSQLResultsIssuesThisMonth = sql.GET(lIssuesThisMonth) # Total number of issues in the current month

	results.append(lSQLResultsIssuesThisMonth)

	lIssuesAllTime = ("""
		SELECT 
			count(0) as sTotalIssues
		FROM 
			Issues
		WHERE
			ServerNumber IN (1, 2, 3, 4, 17, 40, 46, 47, 48, 49);
	""")
	lSQLResultsIssuesAllTime = sql.GET(lIssuesAllTime) # Total number of issues

	results.append(lSQLResultsIssuesAllTime)

	lDaysSinceInception = datetime.date(datetime.datetime.now()) - utls.DAY_ZERO

	results.append(lDaysSinceInception)

	lPersonMostIssuesAllTime = ("""
		SELECT 
			u.UserName
			, count(iss.SlackID) 
		FROM 
			Issues as iss 
		JOIN 
			Users as u 
		ON 
			u.SlackID = iss.SlackID 
		WHERE 
			iss.ServerNumber IN (1, 2, 3, 4, 17, 40, 46, 47, 48, 49)
		GROUP BY 
			iss.SlackID 
		ORDER BY count(iss.SlackID) DESC 
		LIMIT 1;
	""")
	lSQLResultsPersonMostIssuesAllTime = sql.GET(lPersonMostIssuesAllTime) # Total number of issues

	results.append(lSQLResultsPersonMostIssuesAllTime)

	lPersonMostIssuesThisMonth = ("""
		SELECT 
			u.UserName
			, count(iss.SlackID) 
		FROM 
			Issues as iss 
		JOIN 
			Users as u 
		ON 
			u.SlackID = iss.SlackID 
		WHERE
			iss.TimeStamp BETWEEN 
				datetime('now', 'start of month') 
				AND datetime('now', 'localtime')
			AND iss.ServerNumber IN (1, 2, 3, 4, 17, 40, 46, 47, 48, 49)
		GROUP BY 
			iss.SlackID 
		ORDER BY count(iss.SlackID) DESC 
		LIMIT 1;
	""")
	lSQLResultsPersonMostIssuesThisMonth = sql.GET(lPersonMostIssuesThisMonth) # Total number of issues

	results.append(lSQLResultsPersonMostIssuesThisMonth)

	lErrantServerAllTime = ("""
		SELECT 
			ServerNumber
			, count(ServerNumber) as sTotalIssues
		FROM 
			Issues
		WHERE
			ServerNumber IN (1, 2, 3, 4, 17, 40, 46, 47, 48, 49)
		GROUP BY
			ServerNumber
		ORDER BY
			count(ServerNumber) DESC
		LIMIT 1;
	""")
	lSQLResultsErrantServerAllTime = sql.GET(lErrantServerAllTime) # Total number of issues

	results.append(lSQLResultsErrantServerAllTime)

	lErrantServerThisMonth = ("""
		SELECT 
			ServerNumber
			, count(ServerNumber) as sTotalIssues
		FROM 
			Issues
		WHERE
			TimeStamp BETWEEN 
				datetime('now', 'start of month') 
				AND datetime('now', 'localtime')
			AND ServerNumber IN (1, 2, 3, 4, 17, 40, 46, 47, 48, 49)
		GROUP BY
			ServerNumber
		ORDER BY
			count(ServerNumber) DESC
		LIMIT 1;
	""")
	lSQLResultsErrantServerThisMonth = sql.GET(lErrantServerThisMonth) # Total number of issues

	results.append(lSQLResultsErrantServerThisMonth)

	lMostIssuesPerDayAllTime = ("""
		SELECT
			date(TimeStamp) as sTheDay 
			, count(ServerStatus) as sTotalIssues
		FROM 
			Issues
		WHERE
			ServerNumber IN (1, 2, 3, 4, 17, 40, 46, 47, 48, 49)
		GROUP BY
			date(TimeStamp);
	""")
	lSQLResultsMostIssuesPerDayAllTime = sql.GET(lMostIssuesPerDayAllTime) # Total number of issues

	results.append(lSQLResultsMostIssuesPerDayAllTime)

	lMostIssuesPerDayThisMonth = ("""
		SELECT
			date(TimeStamp) as sTheDay 
			, count(ServerStatus) as sTotalIssues
		FROM 
			Issues
		WHERE
			TimeStamp BETWEEN 
				datetime('now', 'start of month') 
				AND datetime('now', 'localtime')
			ServerNumber IN (1, 2, 3, 4, 17, 40, 46, 47, 48, 49)
		GROUP BY
			date(TimeStamp);
	""")
	lSQLResultsMostIssuesPerDayThisMonth = sql.GET(lMostIssuesPerDayThisMonth) # Total number of issues

	results.append(lSQLResultsMostIssuesPerDayThisMonth)

	return results

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
			Interactions
		GROUP BY
			aStatus
		ORDER BY
			Amount DESC;
	"""
	results = sql.GET(cmd)
	return results

# CREATE TABLE IF NOT EXISTS "Music" (
# 'ID' INTEGER PRIMARY KEY AUTOINCREMENT, 
# 'Link' TEXT NOT NULL DEFAULT 'www.google.com', 
# 'Description' TEXT NOT NULL DEFAULT 'NOT SET'
# );

def imSorry(): # an appology for the environment in which we operate
	sqlCmd = "SELECT Link FROM Music;"
	results = sql.GET(sqlCmd)
	return results

# CREATE TABLE IF NOT EXISTS "Users" (
# 'ID' INTEGER PRIMARY KEY AUTOINCREMENT, 
# 'SlackID' TEXT NOT NULL DEFAULT 'NOID', 
# 'UserName' TEXT NOT NULL DEFAULT 'NONAME'
# );

####