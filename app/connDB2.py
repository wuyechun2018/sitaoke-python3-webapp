import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='wuyechun',db='db_employessleave')

cur = conn.cursor()

cur.execute("SELECT * FROM act_id_user")

for r in cur.fetchall():

           print(r)

cur.close()

conn.close()