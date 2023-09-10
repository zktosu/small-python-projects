# get time
# set interval
# alarm at interval
import time
seconds = int(input("Time Interval - Seconds "))
time_to_sleep = 1
s = seconds
while True:
	s = seconds
	print("Start...")
	while s:
		time.sleep(1)
		s -= 1
	print("Time for break!!!")
	time.sleep(time_to_sleep)
	print("rest time is finished")
