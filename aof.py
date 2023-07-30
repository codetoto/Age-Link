import pymysql

conn = pymysql.connect(host="localhost", user="root",passward="love71270^^", db='aof',charset='utf8')

cur = conn.cursor()

query = """select * from user"""
cur.execute(query)

pass

result = cur.fetchall()

print(result)