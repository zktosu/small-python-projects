# mood logger will log moods 
# based on the current time.
# get mood time it as now
# record to :memory: database.
import sqlite3
conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("create table moods(time int primary key not null, mood char(100) not null)")
while True:
	mood = input("Please type your mood (happy,sad,angry etc)")
	mood_time = 12 #datetime.now() 
	cur.execute("insert into moods(time, mood) values(?,?)",(mood_time,mood))
	cur.execute("select * from moods")
	for item in cur.fetchall():
		print(item[0],item[1])
