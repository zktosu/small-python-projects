import sqlite3
conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("create table todos(id integer primary key, todo char(300))")

cur.execute("insert into todos(todo) values('say hi')")
cur.execute("select * from todos")
for item in cur:
	print(item[0],item[1])
