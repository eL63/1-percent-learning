#!/usr/bin/env python3
from datetime import datetime

now = datetime.now().strftime("%A %d-%B-%Y %H:%M:%S")
print(f"This is the date where everything changes: {now}")

print('''
Here are 4 principles to improve in your life:
- "A daily improvement of just 1% adds up to a 37-fold increase over the course of a year."
- "Focus on systems rather than on goals."
- "Progress often feels like a straight line; in reality, it follows an exponential path."
- "True behavioral change does not begin with what you want to achieve (results), but with who you want to be (identity)."
''')
