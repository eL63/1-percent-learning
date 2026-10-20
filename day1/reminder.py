from datetime import datetime
import time

REMINDER_TIME = "06:00"

print("Hey little programmer welcome to todays coding session.")

while True:
    now = datetime.now().strftime("%H:%M")

    if now == REMINDER_TIME:
        print(f"Good Morning! It is {now}. Time to code!")
        time.sleep(61)

    time.sleep(10)
    