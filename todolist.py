import sqlite3
conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("create table todos(id integer primary key, todo char(300), status boolean default False)")
# get task from user.
while True:
	operation = input("Select Operation {a:add,d:done} ")
	if operation == 'a':
		input_val = input("please type the task ")
		cur.execute("insert into todos(todo) values(?)",(input_val,))
	if operation == 'd':
		input_id = input("please give id of task done ")
		cur.execute("delete from todos where id=?",(input_id,))
# select operation addition, status change
	cur.execute("select * from todos where status=False")
	for item in cur:
		print(item[0],item[1])
	if operation=='q':
		break
