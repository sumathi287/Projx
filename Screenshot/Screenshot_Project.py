import ctypes
from datetime import date,timedelta
import os
import pyautogui
import sys
from datetime import datetime
import time

def stop_function():
        ctypes.windll.user32.MessageBoxW(0, "Projects folder is not exist in current folder path\nplease can you create the folder path like\n"r"C:\Users\Username\Documents\Screenshot_Image_Path", "Info", 0x00)
        ctypes.windll.user32.MessageBoxW(0, "Projects folder is not exist in current folder path", "Info", 0x00)
        sys.exit()
def stop_function_1():
        ctypes.windll.user32.MessageBoxW(0, "day.txt file is not exist in \"Screenshot_Image_Path\" folder path", "Info", 0x00)
        sys.exit()    
def date_calculation(image_dir,image_name,user_var):
        current_date = datetime.now()
        timestamp_from_saved_path = os.path.getctime(image_dir)
        date_from_saved_path = datetime.fromtimestamp(timestamp_from_saved_path)
        age_of_image = (current_date-date_from_saved_path).days
        if age_of_image >= user_var:
                response =  ctypes.windll.user32.MessageBoxW(0,"the age of {image_name} is {age_of_image}\nPress 'yes' if you want to delete it\nPress 'No' you want continue the screenshot process without deleting image","Info",0x04)
                if response == 6:
                        os.remove(image_dir)
                        ctypes.windll.user32.MessageBoxW(0,f"the {image_name} is succesfully removed" , "Info", 0x00)

if getattr(sys,'frozon',False):
        file_dir = os.path.dirname(sys.executable)
else:
        file_dir = os.path.dirname(os.path.abspath(__file__))
        
folder_list = os.listdir(file_dir)

user_var = input("Enter the minimum age (in days) of images you want to delete:\n")
user_var = int(user_var)

for i in folder_list: #logic to increae the value of 'count' variable if the image is preent in current folder
        if i.endswith('jpg'):
                image_path_var =  os.path.join(file_dir,i)
                date_calculation(image_path_var,i,user_var)
time.sleep(1)

screenshot = pyautogui.screenshot()

screenshot.show()


time_stamp = datetime.now()

formating_str = time_stamp.strftime("%d-%m-%Y-%H-%M-%S")

file_saved_path = os.path.join( file_dir,f"image_{formating_str}.jpg")


file_saved_path = os.path.join( file_dir,f"image_{formating_str}.jpg")


screenshot.save(file_saved_path)