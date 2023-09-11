import sqlite3
conn = sqlite3.connect(":memory:")
conn.execute("""
create table contacts(id integer primary key autoincrement,name char(100),address char(100),phone char(100));
""")
cur = conn.cursor()
# cur.execute("insert into contacts(name,address,phone) values(?,?,?)",("name","address","23040324"))
# cur.execute("select * from contacts")

while True:
	option = input("Please select operation: (a)dd, (r)emove")
	if option == "a":
		name = input("please enter name")
		address = input("please enter an address")
		phone = input("please enter phone number")
		cur.execute("insert into contacts(name,address,phone) values(?,?,?)",(name, address, phone))
	if option == "r":
		name = input("Please enter a name to remove")
		cur.execute("delete from contacts where name = ?",(name,))
	for item in cur.fetchall():
		print(item[0],item[1],item[2],item[3])

