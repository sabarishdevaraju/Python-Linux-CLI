import os
import subprocess

#date = os.popen("date").read()
#print(date)

#longlist = os.popen("whoami").read()
#print(longlist)
# Important: Avoid inserting untrusted user input directly into os.popen() 
# commands because it uses a shell and can lead to command injection.

ll = subprocess.run(['ls','-l'], capture_output=True, text=True)
print("output : "+ ll.stdout) # stdout — normal command output.
print(f"Error : {ll.stderr}") # stderr — error output.
print(f"Exit status : {ll.returncode}") # returncode — command exit status (0 generally means success).









