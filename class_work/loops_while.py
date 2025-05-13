import os
import time

def is_file_exist(filename):
    if os.path.exists(filename):
        return True
    else:
        return False

a = 10
counter = 1
while not is_file_exist("C:\\Program Files\\Java\\jdk-17") and counter <= 10:
    counter += 1 # counter = counter + 1
    time.sleep(5)


