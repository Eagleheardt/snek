import databaseProvider as sql
import datetime

DATABASE = "lenderBot/data/lendingLibrary.db" # prod location
sql.setConnection(DATABASE) # set DB connection


####
# CREATE TABLE IF NOT EXISTS "Status" ('ID' INTEGER PRIMARY KEY AUTOINCREMENT, 'TimeStamp' DATE DEFAULT (datetime('now','localtime')),ServerNumber INTEGER NOT NULL, ServerStatus TEXT NOT NULL);
# CREATE TABLE IF NOT EXISTS "SnekStats" (ID INTEGER PRIMARY KEY AUTOINCREMENT, TimeStamp DATE DEFAULT (datetime('now','localtime')),User TEXT NOT NULL DEFAULT 'NONE',aStatus TEXT NOT NULL DEFAULT 'NONE');
# CREATE TABLE History ('ID' INTEGER PRIMARY KEY AUTOINCREMENT, 'TimeStamp' DATE DEFAULT (datetime('now','localtime')), 'ServerNumber' INTEGER NOT NULL, 'ServerStatus' TEXT NOT NULL);
# CREATE TABLE IF NOT EXISTS "Sorry"('ID' INTEGER PRIMARY KEY AUTOINCREMENT,'Link' TEXT NOT NULL DEFAULT 'www.google.com');
# CREATE TABLE IF NOT EXISTS "User" ('ID' INTEGER PRIMARY KEY AUTOINCREMENT, 'SlackID' TEXT NOT NULL DEFAULT 'NOID', 'UserName' TEXT NOT NULL DEFAULT 'NONAME');
# CREATE TABLE UseHistory ('ID' INTEGER PRIMARY KEY AUTOINCREMENT, 'TimeStamp' DATE DEFAULT (datetime('now','localtime')), 'ServerNumber' INTEGER NOT NULL, 'ServerStatus' TEXT NOT NULL, 'SlackID' TEXT NOT NULL DEFAULT 'NONAME');
###

#######################
###   Users Table   ###
#######################

# CREATE TABLE `Users` (
# 	`ID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
# 	`userName`	TEXT NOT NULL,
# 	`slackID`	TEXT NOT NULL UNIQUE,
# 	`directID`	TEXT NOT NULL,
# 	`IsAdmin`	BIT NOT NULL DEFAULT 0
# );

def isAdmin(slackID):
    result = """
    SELECT
        IsAdmin
    FROM
        Users
    WHERE
        slackID = '{0}';
    """.format(slackID)
    
    try:
        fin = sql.GET(result)[0][0]
    except:
        fin = 0

    return fin

def isDirect(channelID):
    result = """
    SELECT
        *
    FROM
        Users
    WHERE
        directID = '{0}';
    """.format(channelID)

    try:
        fin = sql.GET(result)[0][0]
    except:
        fin = 0

    return fin

def getSlackID(name):
    cmd = """
        SELECT 
            slackID
        FROM 
            Users 
        WHERE 
            userName LIKE '{0}'
    """.format(name)

    try:
        fin = sql.GET(cmd)[0][0]
    except:
        fin = 'No ID'

    return fin

#######################
###   Facts Table   ###
#######################

# CREATE TABLE `Facts` (
# `ID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
# `Line` TEXT NOT NULL UNIQUE 
# );

def insert_Fact(newType):
    return sql.SIMPLE_INSERT("Facts", "Line", "'{}'".format(newType))

def selectAll_Facts():
    return sql.SELECT_ALL("Facts")

def remove_Facts(ID):
    return sql.SIMPLE_DELETE("Facts", "ID", ID)

def getFactByID(ID):
    result = """
    SELECT
        Line
    FROM
        Facts
    WHERE
        ID = {0};
    """.format(ID)

    try:
        fin = sql.GET(result)[0][0]
    except:
        fin = 0

    return fin

#########################
###   Insults Table   ###
#########################

# CREATE TABLE `Insults` (
# `ID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
# `Line` TEXT NOT NULL UNIQUE 
# );

def insert_Insult(newType):
    return sql.SIMPLE_INSERT("Insults", "Line", "'{}'".format(newType))

def selectAll_Insults():
    return sql.SELECT_ALL("Insults")

def remove_Insults(ID):
    return sql.SIMPLE_DELETE("Insults", "ID", ID)

def getInsultByID(ID):
    result = """
    SELECT
        Line
    FROM
        Insults
    WHERE
        ID = {0};
    """.format(ID)

    try:
        fin = sql.GET(result)[0][0]
    except:
        fin = 0

    return fin

###########################
###   MediaType Table   ###
###########################

# CREATE TABLE MediaType (
# ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
# Description TEXT NOT NULL UNIQUE
# );

# Video games, board games, cards, etc

def insert_MediaType(newType):
    return sql.SIMPLE_INSERT("MediaType", "Description", "'{}'".format(newType))

def remove_MediaType(ID):
    return sql.SIMPLE_DELETE("MediaType", "ID", ID)

def selectAll_MediaType():
    return sql.SELECT_ALL("MediaType")

def getMediaTypeByID(ID):
    result = """
    SELECT
        Description
    FROM
        MediaType
    WHERE
        ID = {0};
    """.format(ID)

    try:
        fin = sql.GET(result)[0][0]
    except:
        fin = 0

    return fin

def get_MediaTypeID(mediaType):
    cmd = """
    SELECT
        ID
    FROM
        MediaType
    WHERE
        Description LIKE '{}';
    """.format(mediaType)
    
    try:
        result = sql.GET(cmd)[0][0]
    except:
        result = 1 # defaults to 1, undefined

    return result

###############################
###   MediaCategory Table   ###
###############################

# CREATE TABLE MediaCategory (
# ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
# Name TEXT NOT NULL UNIQUE
# );

# family, Comedy, Horror, etc.

def insert_MediaCategory(newCategory):
    return sql.SIMPLE_INSERT("MediaCategory", "Name", "'{}'".format(newCategory))

def remove_MediaCategory(ID):
    return sql.SIMPLE_DELETE("MediaCategory", "ID", ID)

def selectAll_MediaCategory():
    return sql.SELECT_ALL("MediaCategory")

def getMediaCategoryByID(ID):
    result = """
    SELECT
        Name
    FROM
        MediaCategory
    WHERE
        ID = {0};
    """.format(ID)

    try:
        fin = sql.GET(result)[0][0]
    except:
        fin = 0

    return fin

def get_MediaCategoryID(mediaType):
    cmd = """
    SELECT
        ID
    FROM
        MediaCategory
    WHERE
        Name LIKE '{}';
    """.format(mediaType)

    try:
        result = sql.GET(cmd)[0][0]
    except:
        result = 1 # defaults to 1, undefined

    return result

#######################
###   Media Table   ###
#######################

# CREATE TABLE Media (
# ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
# MediaType INTEGER NOT NULL DEFAULT 1, 
# MediaCategory INTEGER NOT NULL DEFAULT 1, 
# OwnerID TEXT NOT NULL, 
# FullName TEXT NOT NULL, 
# LongGame BIT NOT NULL DEFAULT 1, 

# FOREIGN KEY (MediaType) REFERENCES MediaType(ID), 
# FOREIGN KEY (MediaCategory) REFERENCES MediaCategory(ID), 
# FOREIGN KEY (OwnerID) REFERENCES Users(SlackID)
# );

def insert_Media(mediaInfo):
    return sql.SIMPLE_INSERT("Media", "MediaType, MediaCategory, OwnerID, FullName, LongGame", mediaInfo)

def remove_Media(ID):
    return sql.SIMPLE_DELETE("Media", "ID", ID)

def select_MediaID(ID):
    return sql.SIMPLE_SELECT("Media", "ID", ID)

def selectAll_Media():
    return sql.SELECT_ALL("Media")

def update_MediaCategory(mediaID, categoryID):
    cmd = """
    UPDATE Media
    SET MediaCategory = {}
    WHERE ID = {};
    """.format(categoryID, mediaID)

    return sql.EXEC(cmd)

def update_MediaType(mediaID, typeID):
    cmd = """
    UPDATE Media
    SET MediaType = {}
    WHERE ID = {};
    """.format(typeID, mediaID)

    return sql.EXEC(cmd)

def getMediaNameByID(ID):
    result = """
    SELECT
        FullName
    FROM
        Media
    WHERE
        ID = {0};
    """.format(ID)

    try:
        fin = sql.GET(result)[0][0]
    except:
        fin = 0

    return fin

def format_Media():
    cmd = """
    SELECT 
    m.ID
    , m.FullName
    , mc.Name
    , mt.Description
    , CASE m.LongGame 
        WHEN 1
            THEN 'Long'
            ELSE 'Short'
        END as Length
	, CASE (
        SELECT COUNT(0) as numberOut
        FROM Transactions as t
            WHERE 
                t.MediaID = m.ID
                AND t.CheckIN is null
            )
        WHEN 0
            THEN 'Available'
            ELSE 'Checked Out'
        END	as Available
    FROM Media as m
    JOIN 
    MediaCategory as mc 
        ON m.MediaCategory = mc.ID
    , MediaType as mt 
	    ON m.MediaType = mt.ID;
    """

    return sql.GET(cmd)

def format_Media_Available():
    cmd = """
    SELECT 
    m.ID
    , m.FullName
    , mc.Name
    , mt.Description
    , CASE m.LongGame 
        WHEN 1
            THEN 'Long'
            ELSE 'Short'
        END as Length
	, CASE (
        SELECT COUNT(0) as numberOut
        FROM Transactions as t
            WHERE 
                t.MediaID = m.ID
                AND t.CheckIN is null
            )
        WHEN 0
            THEN 'Available'
            ELSE 'Checked Out'
        END	as Available
    FROM Media as m
    JOIN 
    MediaCategory as mc 
        ON m.MediaCategory = mc.ID
    , MediaType as mt 
	    ON m.MediaType = mt.ID
	WHERE (
        SELECT COUNT(0) as numberOut
        FROM Transactions as t
            WHERE 
                t.MediaID = m.ID
                AND t.CheckIN is null
            ) = 0;
    """

    return sql.GET(cmd)

def format_Media_CheckedOut():
    cmd = """
    SELECT 
    m.ID
    , m.FullName
    , mc.Name
    , mt.Description
    , CASE m.LongGame 
        WHEN 1
            THEN 'Long'
            ELSE 'Short'
        END as Length
	, CASE (
        SELECT COUNT(0) as numberOut
        FROM Transactions as t
            WHERE 
                t.MediaID = m.ID
                AND t.CheckIN is null
            )
        WHEN 0
            THEN 'Available'
            ELSE 'Checked Out'
        END	as Available
    FROM Media as m
    JOIN 
    MediaCategory as mc 
        ON m.MediaCategory = mc.ID
    , MediaType as mt 
	    ON m.MediaType = mt.ID
	WHERE (
        SELECT COUNT(0) as numberOut
        FROM Transactions as t
        WHERE 
            t.MediaID = m.ID
            AND t.CheckIN is null
        ) > 0;
    """

    return sql.GET(cmd)

def format_Media_WhosGotIt():
    cmd = """
    SELECT 
    m.ID
    , m.FullName
    , t.slackID
	, t.checkOUT
    FROM Media as m JOIN
        (SELECT t.mediaID
        , t.checkout
        , t.slackID
            FROM Transactions as t
            WHERE 
            t.CheckIN is null
            ) as t
		ON m.ID = t.mediaID
    JOIN 
    Users as u
		ON u.slackID = t.slackID
    ORDER BY m.ID ASC;
    """

    return sql.GET(cmd)

def getAvalableByCategory(mediaCategory):
    pass
    cmd = """
    SELECT 
    m.ID
    , m.FullName
    , mc.Name
    , mt.Description
    , CASE m.LongGame 
        WHEN 1
            THEN 'Long'
            ELSE 'Short'
        END as Length
    FROM Media as m
    JOIN 
    MediaCategory as mc 
        ON m.MediaCategory = mc.ID
    , MediaType as mt 
	    ON m.MediaType = mt.ID
	WHERE (
        SELECT COUNT(0) as numberOut
        FROM Transactions as t
            WHERE 
                t.MediaID = m.ID
                AND t.CheckIN is null
            ) = 0
			AND mc.Name like '{}';
    """.format(mediaCategory)

    try:
        fin = sql.GET(cmd)
    except:
        fin = False

    return fin

def getAvalableByType(mediaType):
    pass
    cmd = """
    SELECT 
    m.ID
    , m.FullName
    , mc.Name
    , mt.Description
    , CASE m.LongGame 
        WHEN 1
            THEN 'Long'
            ELSE 'Short'
        END as Length
    FROM Media as m
    JOIN 
    MediaCategory as mc 
        ON m.MediaCategory = mc.ID
    , MediaType as mt 
	    ON m.MediaType = mt.ID
	WHERE (
        SELECT COUNT(0) as numberOut
        FROM Transactions as t
            WHERE 
                t.MediaID = m.ID
                AND t.CheckIN is null
            ) = 0
			AND mt.Description like '{}';
    """.format(mediaType)

    try:
        fin = sql.GET(cmd)
    except:
        fin = False

    return fin

def getMyStuff(SlackID):
    cmd = """
    SELECT t.MediaID
    ,m.fullName
    , t.checkOUT
    FROM Transactions as t
    JOIN Media as m
        ON m.ID = t.mediaID
    WHERE 
        t. SlackID = '{}'
        AND t.checkIN is null;
    """.format(SlackID)

    try:
        fin = sql.GET(cmd)
    except:
        fin = "You haven't checked anything out!"

    return fin

##############################
###   Transactions Table   ###
##############################

# CREATE TABLE Transactions (
# 'ID' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
# 'MediaID' INTEGER NOT NULL, 
# 'SlackID' TEXT NOT NULL, 
# 'CheckIN' DATE, 
# 'CheckOUT' DATE, 

# FOREIGN KEY (MediaID) REFERENCES Media(ID), 
# FOREIGN KEY (SlackID) REFERENCES Users(SlackID) 
# );

def tooManyOut(slackID):
    cmd = """
    SELECT COUNT(0) as numberOut
    FROM Transactions as t
    WHERE 
        t.SlackID = '{0}'
        AND t.CheckIN is null;
    """.format(slackID)

    numOut = sql.GET(cmd)[0][0]
    
    if numOut >= 2: # if they have 2 or more items out, they'll need to talk to an admin
        return True
        
    return False

def isItemCheckedOut(mediaID):
    cmd = """
    SELECT COUNT(0) as numberOut
    FROM Transactions as t
    WHERE 
        t.MediaID = {0}
        AND t.CheckIN is null;
    """.format(mediaID)

    numOut = sql.GET(cmd)[0][0]
    
    if int(numOut) >= 1: # can't check ou an item twice... I hope
        return True
        
    return False

def Media_CheckIN(mediaID, slackID):
    if not isItemCheckedOut(mediaID): # if this doesn't work, you'll need an admin
        return 7

    cmd = """
    UPDATE 
    Transactions
    SET
    CheckIN = datetime('now','localtime')
    WHERE
    MediaID = {0}
    AND SlackID = '{1}'
    AND CheckIN is null;
    """.format(mediaID, slackID)

    return sql.EXEC(cmd)

def Media_CheckOUT(mediaID, slackID):
    if isItemCheckedOut(mediaID): # can't check out something twice
        return 5

    if tooManyOut(slackID): # can only check out a cuople of items
        return 4

    cmd = """
    INSERT INTO 
    Transactions
    (MediaID, SlackID, CheckOUT)
    VALUES
    ({0},'{1}', datetime('now','localtime'));
    """.format(mediaID, slackID)

    return sql.EXEC(cmd)

def Media_adminCheckIN(mediaID):
    cmd = """
    UPDATE 
    Transactions
    SET
    CheckIN = datetime('now','localtime')
    WHERE
    MediaID = {0}
    AND CheckIN is null;
    """.format(mediaID)

    return sql.EXEC(cmd)

def Media_adminCheckOUT(mediaID, slackID):
    if isItemCheckedOut(mediaID): # can't check out something twice ... I hope
        return 5

    cmd = """
    INSERT INTO 
    Transactions
    (MediaID, SlackID, CheckOUT)
    VALUES
    ({0},'{1}', datetime('now','localtime'));
    """.format(mediaID, slackID)

    return sql.EXEC(cmd)

def returnAll(slackID):
    cmd = """
    UPDATE 
    Transactions
    SET
    CheckIN = datetime('now','localtime')
    WHERE
    SlackID = '{0}'
    AND CheckIN is null;
    """.format(slackID)

    return sql.EXEC(cmd)

def popularity():
    """
    SELECT t.mediaID, COUNT(0) as HOWMANY
    FROM Transactions as t
    WHERE 
    t.checkOUT IS NOT NULL
    GROUP BY t.mediaID
    ORDER BY COUNT(0) desc;
    """
    return