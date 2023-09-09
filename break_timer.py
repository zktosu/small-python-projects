# get time
# set interval
# alarm at interval
import time
seconds = int(input("Time Interval - Seconds "))
time-to-sleep = 1
s = seconds
while True:
	s = seconds
	while s:
		time.sleep(1)
		s -= 1
	print("Time for break!!!")
	time.sleep(time-to-sleep)
