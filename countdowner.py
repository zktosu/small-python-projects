# countdown application
import time
time_to = input("please type time to count down \n{mm:ss} ")
minutes, seconds = time_to.split(":")
minutes, seconds = int(minutes), int(seconds)
seconds += minutes * 60
while seconds:
	time.sleep(1)
	print("%02d:%02d"%divmod(seconds,60))
	seconds -= 1
print("Beep Beep Beep")
