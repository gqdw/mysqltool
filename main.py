import MySQLdb
import xlwt

dbuser = 'root'
dbpass = ''
dbname = 'information_schema'
tables= []
class info:
	def __init__(self,table_name,engine,table_rows):
		self.table_name = table_name
		self.engine = engine
		self.table_rows = table_rows
	def say(self):
		print self.table_name,self.engine,self.table_rows

def connect_mysql():
	db1 = MySQLdb.connect('localhost',dbuser,dbpass,dbname,unix_socket='/tmp/mysql.sock')
	#sql = 'show processlist'
	sql = "select  TABLE_NAME,ENGINE,TABLE_ROWS from TABLES where TABLE_SCHEMA='shengchan' "
	cur = db1.cursor()

	cur.execute(sql)
	ret = cur.fetchone()
	t1 = info(ret[0],ret[1],ret[2])
	tables.append(t1)
	#print ret
	while True:
	#while ret !=  None :
		ret = cur.fetchone()
		if ( ret != None):
			#print "table_name: %s\t engine: %s\t table_rows: %s" % (ret[0],ret[1],ret[2])
			r3 = int(ret[2])
			i1 = info(ret[0],ret[1],ret[2])
			tables.append(i1)
	#		tables.append({'table_name':ret[0],'engine':ret[1],'table_rows':r3})
			#tables.append({'table_name':ret[0],'engine':ret[1],'table_rows':int(ret[2])})
		else:
			break

	cur.close()
	db1.close()
#tables.sort(key='table_rows')
#tables.sort(key='table_rows')
#sorted(tables,key=lambda info: info.table_rows)
tables.sort(key=lambda info: info.table_rows,reverse=True)
#sorted(tables,key=tables.

def main():
	connect_mysql()
	for i in tables:
	#	print i['table_name'],i['engine'],i['table_rows']
		i.say()


main()
