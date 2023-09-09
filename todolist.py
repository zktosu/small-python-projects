import sqlite3
conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("create table todos(id integer primary key, todo char(300), status boolean default False)")
# get task from user.
cur.execute("insert into todos(todo) values('say hi')")
# select operation addition, status change
cur.execute("select * from todos where status=False")
for item in cur:
	print(item[0],item[1])
