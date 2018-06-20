import cx_Oracle

conn = cx_Oracle.connect('center/123456@172.16.7.116:1521/center')  

cur = conn.cursor()

cur.execute("select sysdate from dual")

data = cursor.fetchone()
 
print('Database time:%s' % data)

cur.close()

conn.close()