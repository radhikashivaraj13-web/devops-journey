import os
from datetime import datetime
log_file="devops-log.txt"
with open(log_file,"w")as f:
    f.write(f"========devops Log========\n")
    f.write(f"created:{datetime.now()}\n")
with open(log_file,"a") as f:
    f.write(f"Log entry added at {datetime.now()}\n")
with open(log_file,"r") as f:
    print(f.read())        