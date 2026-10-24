import os

def scan_file(filename, keywords):
    try:
      with open(filename, 'r') as file:
          for line_number, line in enumerate(file, 1):
            for keyword in keywords:
              if keyword in line:
                  print(f"[!] Found keyword: '{keyword}' in line: {line_number}")
    except Exception as e:
        print(f"Error: {e}")


script_dir = os.path.dirname(os.path.abspath(__file__))
abs_filename = os.path.join(script_dir, "file_to_proof.txt")
keywords = ['malware', 'exploit']
filename = 'file_to_proof.txt'
scan_file(abs_filename, keywords)