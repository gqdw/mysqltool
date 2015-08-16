import MySQLdb
import xlwt

dbuser = 'root'
dbpass = ''
dbname = 'information_schema'
tables= []
class info:
	#table_name = ''
	#engine = ''
	#table_rows = ''
	
	def __init__(self,table_name,engine,table_rows):
		self.table_name = table_name
		self.engine = engine
		self.table_rows = table_rows
	def get_table_name( self ):
		return  self.table_name
	def get_engine( self ):
		return self.engine
	def get_table_rows( self ):
		return self.table_rows
#	def get_table_name()
#	def __getitem__(self,key): return self.[key]
	def say(self):
		print self.table_name,self.engine,self.table_rows
	#def ret(self):
	#	return 

def get_mysql_info():
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

##
def write_to_excel( sheet_name ):
	wb = xlwt.Workbook()
	ws = wb.add_sheet( sheet_name )	
	j = 1
	for i in  tables:
		#ws.write( j, 1, i['table_name'] )
		#ws.write( j, 2, i['engine'] )
		#ws.write( j, 3, i['table_rows'] )
		ws.write( j, 1, i.get_table_name() )
		ws.write( j, 2, i.get_engine() )
		ws.write( j, 3, i.get_table_rows() )
		j = j+1
	wb.save(sheet_name +'.xls')

##end write_to_excel
def main():
	get_mysql_info()
	write_to_excel( 'shengchan')
#	for i in tables:
#	#	print i['table_name'],i['engine'],i['table_rows']
#		i.say()


main()
