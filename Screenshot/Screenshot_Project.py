import ctypes
from datetime import date,timedelta
import os
import pyautogui
import sys
import time
def stop_function():
        '''show prompt message box'''
        ctypes.windll.user32.MessageBoxW(0, "Projects folder is not exist in current folder path", "Info", 0x00)
        sys.exit()
def stop_function_1():
        ctypes.windll.user32.MessageBoxW(0, "day_1.txt file is not exist in current folder path", "Info", 0x00)
        sys.exit()

try:

        files = os.listdir(os.path.join(os.path.expanduser("~"),"Documents","Projects"))
except FileNotFoundError:
        stop_function()

count = 0

date =  date.today()

days_to_add = timedelta(days=15)

future_date = date + days_to_add 


date = str(date)

file = "day_1.txt"

try:
        path = os.path.join(os.path.expanduser("~"),"Documents","Projects")
except FileNotFoundError:
        stop_function()
        
file_path = os.path.join(path,file)


try:

        f = open(file_path ,"r")

        ver = f.read()

        f.close()

except FileNotFoundError:
        stop_function_1()

if ver == date:
    f = open(file_path ,"w")
    f.write(f"{future_date}")
    f.close()
    for i in files:
        if i.endswith((".jpeg",".jpg")):
            os.remove(os.path.join(path,i))

files = os.listdir(os.path.join(os.path.expanduser("~"),"Documents","Projects"))
print(type(files))
for i in files:
    if i.endswith((".jpeg",".jpg")):
        count += 1

screenshot = pyautogui.screenshot() #take screenshot

screenshot.show() #to view the screenshot image on the screen

screenshot.save(os.path.join(os.path.expanduser("~"),"Documents","Projects",f"image_{count}.jpg")) #save the image in current path location