#!/usr/bin/python3
import os
import logging

script_dir = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(script_dir, "myapp.log")

logger = logging.getLogger(__name__)

def main():
  # Logger configuration. Format adds a timestamp
  logging.basicConfig(filename=log_path, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
  
  logger.info('Started')
  print("Did you do 2 Minutes of exercises today? y/n")
  
  while True:
    user_input = input().lower().strip()
    if user_input == 'y':
        print("Congratulation you are on your best way to improve your life!")
        logger.info('Habit completed: User did exercises! +1%')
        break
    elif user_input == 'n':
        print("You can do it! Use the knowledge from the 1% method!")
        logger.info('Habit missed: User did not exercise.')
        break
    else:
        print("Proof your input please. :-) Try again 'y' or 'n'.")
        logger.warning(f'Invalid user input attempted: "{user_input}"')
        
  logger.info('Finished')

if __name__ == '__main__':
   main()
