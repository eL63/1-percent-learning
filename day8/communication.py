import os
import random
import logging

script_dir = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(script_dir, "communication_tracker.log")

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

communication = {
    "WIN-WIN": "Both individuals have a good feeling",
    "Be polarizing": "Stand for a clear opinion and values",
    "0 percent or 100 percent": "Radical presence and focus",
    "The Silence": "Exude sovereignty",
    "Let go": "Let go of the need to control the other person's reaction"
}

random_rule = random.choice(list(communication.keys()))

print(f"Todays random rule: {random_rule}")
print(f"Meaning: {communication[random_rule]}\n")

print("How are you going to use this rule in todays conversations?")
user_answer = input("Your answer: ").rstrip()

if user_answer:
    logging.info(f"Rule drawn: [{random_rule}] | User Plan: {user_answer}")
    print("Excellent your plan has been saved to your communication log.")
else:
    logging.warning(f"Rule drawn: [{random_rule}] | User provided no answer.")
    print("\nSkipped saving. Remember to stay mindful in your next conversation!")