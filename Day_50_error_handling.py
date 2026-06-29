"""try:
   result=10/0
except ZeroDivisionError as e:
   print(f"Error Caught:{e}")
try:
    with open("nonexistent.txt","r")as f:
        content=f.read()
except FileNotFoundError as e:
        print(f"File not found:{e}")"""
import logging
logging.basicConfig(filename="devops.log", level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')
logging.info("Script Started")
logging.warning("Low disk space detected")
logging.error("connection Failed")
print("Check devops.log file!")