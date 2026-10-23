import socket

print("Starting the port scanner for ssh, http & https.")
target_ip = "127.0.0.1"
ports = [22, 80, 443]

for port in ports:
  so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  so.settimeout(1.0)  
  result = so.connect_ex((target_ip, port))
  so.close()
  if result == 111:
    print(f"Port {port} is closed.")
  elif result == 11:
    print("No response. Active firewall.")
  else:
    print(f"Port {port} is open.")
  
print("Port scanner closed.")
