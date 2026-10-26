import os
import logging

script_dir = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(script_dir, "bias_detector.log")

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

print("On which project are you working currently?")
project_name = input().strip()

print("How much time or money did you already invest?")
investment = input().strip()

while True:
  print("If you would start from scratch again, would you do this project again? 'y' or 'n'")
  restart_choice = input().lower().strip()
  
  if restart_choice == 'y':
      logging.info(f"Project: [{project_name}] | Investment: [{investment}] | Restart_Choice: [{restart_choice}] | Decision: Keep going!")
      print("Logged successfully your decision!")
      break
  elif restart_choice == 'n':
      logging.info(f"Project: [{project_name}] | Investment: [{investment}] | Restart_Choice: [{restart_choice}] | Decision: Let go!")
      print("Logged successfully your decision!")
      break
  else:
      print("Invalid input. Please enter 'y' for yes or 'n' for no.")