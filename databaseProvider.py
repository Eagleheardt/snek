import sqlite3
import numpy as np

DATABASE = ''
__MAIN_CONNECTION = sqlite3.connect(DATABASE, check_same_thread=False)

def EXEC(sqlCmd): # fetches data from the database
	try:
		__someCursor = __MAIN_CONNECTION.cursor()
		__someCursor.execute(sqlCmd)
		if __someCursor.rowcount == 0:
			return 3
		__MAIN_CONNECTION.commit() 

		return 0

	except TypeError:
		return 7

	except ValueError:
		return 8

	except:
		return 9

	finally:
		__someCursor.close()

def GET(sqlCmd):
	try:
		__someCursor = __MAIN_CONNECTION.cursor()
		print("cursor set")
		print(__someCursor)
		__someCursor.execute(sqlCmd)
		print('do it')
		result = __someCursor.fetchall()
		print("result")
		print(result)

	except Exception as e:
		print('why???')
		print(e)
		return -1

	finally:
		__someCursor.close()

	return result

def SELECT_ALL(tableName): # returns a list of lists
	cmd = """
		SELECT * 
		FROM {0};
	""".format(tableName)

	return GET(cmd)

def SIMPLE_SELECT(tableName, whereColumn, whereCondition): # returns a list of lists
	cmd = """
		SELECT * 
			FROM {0}
		WHERE
			{1} = {2};
	""".format(tableName, whereColumn, whereCondition)

	return GET(cmd)

def SIMPLE_INSERT(tableName, column, value):
	cmd = """
		INSERT INTO 
			{0} ({1})
		VALUES
			({2});
	""".format(tableName, column, value)

	return EXEC(cmd)

def VARIABLE_INSERT(tableName, amtOfColumns, vArgs): 
	if len(vArgs) % amtOfColumns != 0:
		return 2

	comma =","
	argList = np.reshape(vArgs, (-1, amtOfColumns))

	columnsToUse = ""
	valuesToUse = []
	
	for x, i in enumerate(argList):
		i = np.array2string(i, separator=',').replace('[','').replace(']','')
		if x == 0:
			columnsToUse = i
			continue
		valuesToUse.append(i)

	code = 0

	for i in valuesToUse:
		code = SIMPLE_INSERT(tableName, columnsToUse, i)
		if code != 0:
			return code

	return code

# def SIMPLE_UPDATE(tableName, updateColumn, updateValue, whereColumn, whereCondition):
# 	cmd = """
# 		UPDATE {0}
# 		SET {1} = {2}
# 		WHERE {3} = {4};
# 	""".format(tableName, updateColumn, updateValue, whereColumn, whereCondition)

# 	return EXEC(cmd)

# def SIMPLE_DELETE(tableName, whereColumn, whereCondition):
# 	cmd = """
# 		DELETE FROM {0}
#         WHERE {1} = {2};
# 	""".format(tableName, whereColumn, whereCondition)

# 	return EXEC(cmd)
