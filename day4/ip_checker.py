import os

print("Insert a valid IP-Address to check")

while True:
  user_input = input().strip()

  if user_input.startswith("192.168.") or user_input.startswith("10.0.") or user_input.startswith("172.16."):
      print("Thats your locale IPv4-Adress.")
      break
  else:
      print("Not a private locale IP. Please try again")

print(f"Starting Ping-Check for {user_input}...")

response = os.system(f"ping -c 1 {user_input} > /dev/null 2>&1")
if response == 0:
   print(f"SUCCESS: Device {user_input} is ONLINE!")
else:
   print(f"FAILED: Device {user_input} is OFFLINE or blocking pings!")
