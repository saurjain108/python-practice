import time

start = time.localtime()
#print(start)
print(f" The timer started at {time.strftime('%X', start)}")

input("To stop the timer press the ENTER key")

stop = time.localtime()

print(f" The timer stopped at {time.strftime('%X', stop)}")

difference = time.mktime(stop)-time.mktime(start)

print(f"The difference between both the time is {difference}")
