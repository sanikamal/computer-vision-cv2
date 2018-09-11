import MySQLdb
# Open database connection
db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
# prepare a cursor object using cursor() m ethod
cursor = db.cursor()
# execute SQL query using execute() m ethod.
cursor.execute("SELECT VERSION()")
# Fetch a single row using fetchone() m ethod.
data = cursor.fetchone()
print "Database version : %s " % data
# disconnect from server
db.close()
