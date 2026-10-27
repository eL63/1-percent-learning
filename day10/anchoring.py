import os
import logging

script_dir = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(script_dir, "anchoring.log")

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)
while True:
  print("--- Anchoring Calculator ---")
  print("For what kind of service do you want to negotiate? e.g. 'hourly rate it-automation'")
  service = input("Answer: ").strip()
  
  while True:
    try:
      print("What is your desired price?")
      desired_price = float(input())
  
      anchor_price = desired_price * 1.25
      print(f"Your ideal anchor_price is '{anchor_price:.2f}€'.")
      
      walkaway_price = desired_price * 0.75
      print(f"So your walkaway_price would be '{walkaway_price:.2f}€'.")
    
      logging.info(f"Service: {service} | Desired_Price: {desired_price:.2f} | Anchor_Price: {anchor_price:.2f} | Walkaway_Price: {walkaway_price:.2f}")
      break
  
    except ValueError as e:
      print(f"Error {e}. Please enter a valid number (e.g. 45 or 79.50).\n")
  
  while True:
    print("Do you want to add another service? 'y' = yes or 'n' = no.")
    user_decision = input().lower().strip()
    if user_decision == 'y':
      break
    elif user_decision == 'n':
      print("Thank you for using the 'Anchoring Calculator'. Good luck on your next negotiation.")
      exit()
    else:
      print("Please try again 'y' for yes or 'n' for no.")