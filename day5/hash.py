import hashlib

print("Password Hash system.")

while True:
  user_input = input("Please insert a password with at least 8 chars: ")
  if len(user_input) < 8:
    print("Your password is too short. Please try again.")
  else:
    print("Perfect your password is going to be hashed.")
    break

try: 
  hash_objekt = hashlib.sha256(user_input.encode())
  hashed_password = hash_objekt.hexdigest()
  print(f"Your SHA-256 Hash is: {hashed_password}")
except Exception as e:
  print(f"Error: {e}")