import MySQLdb
import xlwt

class info:
	def __init__(self,table_name,engine,table_rows):
		self.table_name = table_name
		self.engine = engine
		self.table_rows = table_rows
	def say(self):
		print self.table_name,self.engine,self.table_rows

class MysqlInfo:
	def __init__(self,dbuser,dbpass,dbhost):
		self.dbuser = dbuser
		self.dbpass = dbpass
		self.dbhost = dbhost
		self.infos = []
		
	##
	##get info to store in infos
	##
	def get_mysql_info(self):
		dbname = 'information_schema'
		db1 = MySQLdb.connect(self.dbhost,self.dbuser,self.dbpass,dbname,unix_socket='/tmp/mysql.sock')
	    #sql = 'show processlist'
		sql = "select  TABLE_NAME,ENGINE,TABLE_ROWS from information_schema.TABLES where TABLE_SCHEMA='information_schema' " 
		#sql = "select  TABLE_NAME,ENGINE,TABLE_ROWS from information_schema.TABLES where TABLE_SCHEMA='%s' " % dbname
		cur = db1.cursor()
		cur.execute(sql)
		ret = cur.fetchone()
		t1 = info(ret[0],ret[1],ret[2])
		self.infos.append(t1)
		while True:
			ret = cur.fetchone()
			if ret != None:
				#print "table_name: %s\t engine: %s\t table_rows: %s" % (ret[0],ret[1],ret[2])
				r3 = int(ret[2])
				i1 = info(ret[0],ret[1],r3)
				self.infos.append(i1)
			else:
				break
		cur.close()
		db1.close()

	def write_to_excel( self , sheet_name ):
		wb = xlwt.Workbook()
		ws = wb.add_sheet( sheet_name )	
		j = 1
		for i in  self.infos:
			ws.write( j, 1, i.table_name )
			ws.write( j, 2, i.engine )
			ws.write( j, 3, i.table_rows )
	#		print i.table_name
		#	ws.write( j, 1, i.get_table_name() )
		#	ws.write( j, 2, i.get_engine() )
		#	ws.write( j, 3, i.get_table_rows() )
			j = j+1
		wb.save(sheet_name +'.xls')

#tables.sort(key='table_rows')
#tables.sort(key='table_rows')
#sorted(tables,key=lambda info: info.table_rows)
#tables.sort(key=lambda info: info.table_rows,reverse=True)
#sorted(tables,key=tables.


if __name__ == '__main__':
	dbuser = 'root' 
	dbpass = ''
	dbhost = '127.0.0.1' 
	new1 = MysqlInfo(dbuser,dbpass,dbhost)
	new1.get_mysql_info()
	new1.write_to_excel('test')

