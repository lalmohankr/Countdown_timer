import time

hours = input("Enter hours: ")
if hours.isdigit():
    hours = int(hours)
else:
    print("Hours must be an integer value.")
    quit()

minutes = input("Enter minutes: ")
if minutes.isdigit():
    minutes = int(minutes)
else:
    print("minutes must be an integer value.")
    quit()

seconds = input("Enter seconds: ")
if seconds.isdigit():
    seconds = int(seconds)
else:
    print("Seconds must be an integer value.")
    quit()

total_seconds = hours * 3600 + minutes * 60 + seconds

def countdown(time_sec):
    while time_sec:
        hours, remainder = divmod(time_sec, 3600)
        mins, secs = divmod(remainder, 60)
        timeformat = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
    
    print("\nTimer Ended!")

countdown(total_seconds)