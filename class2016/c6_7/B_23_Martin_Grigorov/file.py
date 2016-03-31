import os
import MySQLdb

#os.system("mysql -u root -p");


def db_connect():
	uname = raw_input("Enter uname:")
	password = raw_input("Enter password:")
	print "\n"

	db = MySQLdb.connect("localhost",uname, password)
	global cursor
	cursor = db.cursor()

def read_tasks(filename):
	f = open(filename,'r').read()
	print f
	print "\n"


def execute_file(file_):
	#for line in open(file_):
	#	cursor.execute(line)
	print cursor.fetchall()
	print "\n"

	
#select db
def use_db():
	dbname = raw_input("Select database:")
	#cursor.execute("DROP DATABASE " +dbname)
	#cursor.execute("CREATE DATABASE " +dbname)
	cursor.execute("USE " + dbname + ";")

#show all databases
def show_databases():
	print "Databases:"
	cursor.execute("SHOW DATABASES;")
	result = cursor.fetchall()
	print result
	print "\n"

db_connect()
show_databases()
use_db()
execute_file("creates.sql")
read_tasks("task1.txt")
